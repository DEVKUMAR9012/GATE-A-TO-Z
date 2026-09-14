"""
Downloads real book cover images from Open Library API
and generates books.html with real covers + ratings.
"""
import urllib.request
import urllib.parse
import json
import os
import time

BOOKS_DIR = "img/books"
os.makedirs(BOOKS_DIR, exist_ok=True)

# Known ISBNs for each book — Open Library cover API uses ISBNs
books = [
    {
        "subject": "Algorithms",
        "marks": "10–13 Marks",
        "title": "Introduction to Algorithms",
        "short": "CLRS",
        "authors": "Thomas H. Cormen, Charles Leiserson, Ronald Rivest, Clifford Stein",
        "isbn": "0262033844",
        "edition": "3rd Edition",
        "rating": 4.4,
        "votes": "28,000+",
        "priority": "Must Have 🔥",
        "priority_cls": "high",
        "chapters": "Ch. 2–4 (Sorting), Ch. 6 (Heaps), Ch. 15 (DP), Ch. 16 (Greedy), Ch. 22–24 (Graph Algorithms)",
        "tip": "Don't read proofs — understand the algorithms and time complexity derivations. Solve end-of-chapter problems.",
        "amazon": "https://www.amazon.in/s?k=Introduction+to+Algorithms+CLRS"
    },
    {
        "subject": "Data Structures",
        "marks": "8–10 Marks",
        "title": "Fundamentals of Data Structures in C",
        "short": "Horowitz & Sahni",
        "authors": "Ellis Horowitz, Sartaj Sahni, Susan Anderson-Freed",
        "isbn": "0929306406",
        "edition": "2nd Edition",
        "rating": 4.1,
        "votes": "5,200+",
        "priority": "Recommended",
        "priority_cls": "high",
        "chapters": "Ch. 3 (Stacks/Queues), Ch. 4 (Linked Lists), Ch. 5 (Trees), Ch. 6 (Graphs), Ch. 7 (Sorting)",
        "tip": "Also supplement with Mark Allen Weiss for AVL trees and hashing. Both together cover all DS GATE questions.",
        "amazon": "https://www.amazon.in/s?k=Fundamentals+of+Data+Structures+in+C+Horowitz"
    },
    {
        "subject": "Discrete Mathematics",
        "marks": "8–10 Marks",
        "title": "Discrete Mathematics and Its Applications",
        "short": "Rosen",
        "authors": "Kenneth H. Rosen",
        "isbn": "0072899050",
        "edition": "7th Edition",
        "rating": 3.9,
        "votes": "9,800+",
        "priority": "Recommended",
        "priority_cls": "high",
        "chapters": "Ch. 1 (Logic/Propositions), Ch. 5 (Induction), Ch. 8 (Relations), Ch. 10–11 (Graph Theory), Ch. 6 (Combinatorics)",
        "tip": "For probability, use Sheldon Ross 'Introduction to Probability Models' Ch. 1–4 as a supplement.",
        "amazon": "https://www.amazon.in/s?k=Discrete+Mathematics+Rosen"
    },
    {
        "subject": "Theory of Computation",
        "marks": "6–8 Marks",
        "title": "An Introduction to Formal Languages and Automata",
        "short": "Peter Linz",
        "authors": "Peter Linz",
        "isbn": "0763774952",
        "edition": "5th Edition",
        "rating": 4.0,
        "votes": "3,400+",
        "priority": "Best for GATE",
        "priority_cls": "high",
        "chapters": "Ch. 2–3 (DFA, NFA, Regex), Ch. 4–5 (CFG, PDA), Ch. 8–9 (TM, Undecidability)",
        "tip": "Linz is easier to understand than Hopcroft/Ullman for GATE purposes. Use Hopcroft only for very specific proofs.",
        "amazon": "https://www.amazon.in/s?k=Formal+Languages+Automata+Peter+Linz"
    },
    {
        "subject": "Compiler Design",
        "marks": "5–7 Marks",
        "title": "Compilers: Principles, Techniques, and Tools",
        "short": "Dragon Book",
        "authors": "Alfred V. Aho, Monica S. Lam, Ravi Sethi, Jeffrey D. Ullman",
        "isbn": "0321486811",
        "edition": "2nd Edition",
        "rating": 4.0,
        "votes": "11,500+",
        "priority": "Selective Chapters",
        "priority_cls": "medium",
        "chapters": "Ch. 2 (Lexical Analysis), Ch. 4 (Parsing — LL, LR, SLR, LALR), Ch. 5 (Syntax Directed Translation)",
        "tip": "This book is very dense. For GATE, focus only on parsing sections. Lecture slides from Ullman are simpler and freely available online.",
        "amazon": "https://www.amazon.in/s?k=Compilers+Principles+Techniques+Dragon+Book"
    },
    {
        "subject": "Digital Logic",
        "marks": "5–6 Marks",
        "title": "Digital Design",
        "short": "Morris Mano",
        "authors": "M. Morris Mano",
        "isbn": "0131989243",
        "edition": "4th Edition",
        "rating": 4.2,
        "votes": "7,600+",
        "priority": "Must Have 🔥",
        "priority_cls": "high",
        "chapters": "Ch. 1 (Number Systems), Ch. 2 (Boolean Algebra), Ch. 3 (K-Maps), Ch. 4 (Combinational Circuits), Ch. 6 (Sequential Circuits), Ch. 8 (Registers)",
        "tip": "Solve ALL the K-map problems at end of chapters. Combinational and Sequential circuit questions repeat heavily in GATE.",
        "amazon": "https://www.amazon.in/s?k=Digital+Design+Morris+Mano"
    },
    {
        "subject": "Computer Organization (COA)",
        "marks": "5–7 Marks",
        "title": "Computer Organization and Embedded Systems",
        "short": "Carl Hamacher",
        "authors": "Carl Hamacher, Zvonko Vranesic, Safwat Zaky, Naraig Manjikian",
        "isbn": "0073380482",
        "edition": "6th Edition",
        "rating": 3.9,
        "votes": "4,100+",
        "priority": "Recommended",
        "priority_cls": "high",
        "chapters": "Ch. 5 (CPU Design), Ch. 6 (Pipelining), Ch. 8 (Memory Hierarchy/Cache), Ch. 9 (I/O — DMA, Interrupts)",
        "tip": "Cache memory questions (mapping, replacement policies, hit ratio) are numerical-heavy. Practice at least 30 cache problems.",
        "amazon": "https://www.amazon.in/s?k=Computer+Organization+Hamacher"
    },
    {
        "subject": "Operating Systems",
        "marks": "8–10 Marks",
        "title": "Operating System Concepts",
        "short": "Dinosaur Book",
        "authors": "Abraham Silberschatz, Peter B. Galvin, Greg Gagne",
        "isbn": "1118063333",
        "edition": "9th Edition",
        "rating": 4.1,
        "votes": "16,200+",
        "priority": "Must Have 🔥",
        "priority_cls": "high",
        "chapters": "Ch. 5 (CPU Scheduling), Ch. 6 (Process Synchronization), Ch. 7 (Deadlocks), Ch. 8–9 (Memory: Paging, Segmentation, Virtual Memory), Ch. 12 (I/O)",
        "tip": "Every CPU scheduling algorithm (FCFS, SJF, Round Robin, Priority) has been asked in GATE multiple times. Practice Gantt charts until they're effortless.",
        "amazon": "https://www.amazon.in/s?k=Operating+System+Concepts+Silberschatz+Galvin"
    },
    {
        "subject": "Databases (DBMS)",
        "marks": "8–10 Marks",
        "title": "Database System Concepts",
        "short": "Korth & Sudarshan",
        "authors": "Abraham Silberschatz, Henry F. Korth, S. Sudarshan",
        "isbn": "0073523321",
        "edition": "6th Edition",
        "rating": 4.0,
        "votes": "8,900+",
        "priority": "Must Have 🔥",
        "priority_cls": "high",
        "chapters": "Ch. 2–4 (Relational Model, SQL), Ch. 7 (Normalization 1NF–BCNF), Ch. 11 (Indexing, B/B+ Trees), Ch. 14–15 (Transactions, Concurrency)",
        "tip": "Normalization (finding candidate keys, decomposition) is a guaranteed 2-mark question every year. Master functional dependencies inside out.",
        "amazon": "https://www.amazon.in/s?k=Database+System+Concepts+Silberschatz+Korth"
    },
    {
        "subject": "Computer Networks",
        "marks": "8–10 Marks",
        "title": "Data Communications and Networking",
        "short": "Forouzan",
        "authors": "Behrouz A. Forouzan",
        "isbn": "0073376221",
        "edition": "5th Edition",
        "rating": 4.0,
        "votes": "12,400+",
        "priority": "Must Have 🔥",
        "priority_cls": "high",
        "chapters": "Ch. 3 (Data Link: Error Detection), Ch. 5 (Network/IP/Subnetting), Ch. 6 (Transport/TCP/UDP), Ch. 7 (Application: DNS, HTTP, FTP), Ch. 12 (Routing Protocols)",
        "tip": "Subnetting and IP addressing is mandatory. Also Kurose & Ross 'Top-Down Approach' is a great alternate — many prefer it for TCP/congestion control.",
        "amazon": "https://www.amazon.in/s?k=Data+Communications+Networking+Forouzan"
    },
    {
        "subject": "Engineering Mathematics",
        "marks": "12–15 Marks",
        "title": "Higher Engineering Mathematics",
        "short": "B.S. Grewal",
        "authors": "B.S. Grewal",
        "isbn": "8174091955",
        "edition": "44th Edition",
        "rating": 4.3,
        "votes": "14,700+",
        "priority": "India's Favourite",
        "priority_cls": "high",
        "chapters": "Unit 4 (Probability & Statistics), Unit 5 (Complex Variables — skip for GATE usually), Ch. on Matrices and Linear Algebra (very important for GATE)",
        "tip": "Grewal is a supplementary reference. For GATE Engg. Math (Discrete Math focus), Rosen's Discrete Math is more targeted. Use Grewal for Calculus, Probability, and Linear Algebra only.",
        "amazon": "https://www.amazon.in/s?k=Higher+Engineering+Mathematics+Grewal"
    },
]

def download_cover(isbn, filename):
    filepath = os.path.join(BOOKS_DIR, filename)
    if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
        print(f"  Already exists: {filename}")
        return True
    # Open Library Covers API
    url = f"https://covers.openlibrary.org/b/isbn/{isbn}-L.jpg"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as r:
            data = r.read()
            if len(data) < 1000:  # too small = "no cover" image
                return False
            with open(filepath, 'wb') as f:
                f.write(data)
        print(f"  Downloaded: {filename} ({len(data)//1024}KB)")
        return True
    except Exception as e:
        print(f"  Failed {filename}: {e}")
        return False

def stars_html(rating):
    full = int(rating)
    half = 1 if (rating - full) >= 0.3 else 0
    empty = 5 - full - half
    s = '<span class="stars">'
    s += '<i class="fas fa-star"></i>' * full
    if half: s += '<i class="fas fa-star-half-alt"></i>'
    s += '<i class="far fa-star"></i>' * empty
    s += '</span>'
    return s

SIDEBAR = """      <div class="sidebar-header"><div class="logo">GATE A TO Z</div></div>
      <div class="search-container mb-4">
        <i class="fas fa-search search-icon"></i>
        <input type="text" class="search-input" id="global-search" placeholder="Search topics...">
        <div class="search-results-container" id="search-results"></div>
      </div>
      <ul class="nav-list">
        <li class="nav-item"><a href="index.html" class="nav-link"><i class="fas fa-home"></i> Overview</a></li>
        <li class="nav-item"><a href="basics.html" class="nav-link"><i class="fas fa-book"></i> GATE Basics</a></li>
        <li class="nav-item"><a href="syllabus.html" class="nav-link"><i class="fas fa-laptop-code"></i> GATE CS</a></li>
        <li class="nav-item"><a href="predictor.html" class="nav-link"><i class="fas fa-magic"></i> College Predictor</a></li>
        <li class="nav-item"><a href="calculator.html" class="nav-link"><i class="fas fa-calculator"></i> Score Calculator</a></li>
        <li class="nav-item"><a href="tracker.html" class="nav-link"><i class="fas fa-tasks"></i> Progress Tracker</a></li>
        <li class="nav-item"><a href="stats.html" class="nav-link"><i class="fas fa-chart-bar"></i> GATE Stats</a></li>
        <li class="nav-item"><a href="pyq.html" class="nav-link"><i class="fas fa-question-circle"></i> PYQ Explorer</a></li>
        <li class="nav-item"><a href="books.html" class="nav-link active"><i class="fas fa-book-open"></i> Book Guide</a></li>
        <li class="nav-item"><a href="toppers.html" class="nav-link"><i class="fas fa-trophy"></i> Topper Stories</a></li>
        <li class="nav-item"><a href="faq.html" class="nav-link"><i class="fas fa-question"></i> FAQ</a></li>
        <li class="nav-item"><a href="institutes.html" class="nav-link"><i class="fas fa-landmark"></i> Institute Explorer</a></li>
        <li class="nav-item"><a href="psu.html" class="nav-link"><i class="fas fa-building"></i> PSU Recruitment</a></li>
        <li class="nav-item"><a href="admissions.html" class="nav-link"><i class="fas fa-university"></i> IIT / NIT Admissions</a></li>
        <li class="nav-item"><a href="roadmap.html" class="nav-link"><i class="fas fa-map-signs"></i> Roadmap</a></li>
        <li class="nav-item mt-4"><a href="login.html" class="nav-link" style="border:1px solid var(--accent-primary);border-radius:var(--border-radius-sm);"><i class="fas fa-sign-in-alt"></i> Join GAZ</a></li>
      </ul>"""

def generate_html():
    cards_html = ""
    for b in books:
        img_path = b.get('local_img') or ''
        img_html = f'<img src="{img_path}" alt="{b["title"]} cover" loading="lazy" onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\'">' if img_path else ''
        fallback_style = 'display:flex' if not img_path else 'display:none'
        stars = stars_html(b['rating'])
        cards_html += f"""
        <div class="book-card-v2">
          <div class="book-cover-wrap">
            {img_html}
            <div class="book-cover-fallback" style="{fallback_style}">
              <i class="fas fa-book"></i>
              <span>{b['short']}</span>
            </div>
          </div>
          <div class="book-info">
            <div class="book-subject-tag">{b['subject']} &bull; {b['marks']}</div>
            <h3 class="book-title-v2">{b['title']}</h3>
            <p class="book-authors-v2">{b['authors']}</p>
            <p class="book-edition">{b['edition']}</p>
            <div class="book-rating-row">
              {stars}
              <span class="book-rating-num">{b['rating']}/5</span>
              <span class="book-votes">({b['votes']} ratings)</span>
            </div>
            <div class="book-priority-row">
              <span class="badge {b['priority_cls']}">{b['priority']}</span>
            </div>
            <div class="book-chapters">
              <div class="book-chapters-label"><i class="fas fa-bookmark"></i> Key Chapters for GATE</div>
              <p>{b['chapters']}</p>
            </div>
            <div class="book-tip">
              <i class="fas fa-lightbulb"></i> {b['tip']}
            </div>
            <a href="{b['amazon']}" target="_blank" class="book-buy-btn">
              <i class="fab fa-amazon"></i> Find on Amazon
            </a>
          </div>
        </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Best Books for GATE CS | GATE A TO Z</title>
  <meta name="description" content="The definitive book guide for GATE CS — real covers, Goodreads ratings, and exact chapters to study for every subject.">
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    .books-table {{ width:100%; border-collapse: collapse; margin-bottom: 2rem; }}
    .books-table th, .books-table td {{ padding: 0.8rem 1rem; text-align:left; border-bottom: 1px solid var(--border); font-size:0.9rem; }}
    .books-table th {{ color:var(--accent-primary); font-family:var(--font-display); text-transform:uppercase; font-size:0.75rem; letter-spacing:0.08em; }}
    .books-table tr:hover td {{ background: rgba(110,231,183,0.03); }}

    .book-cards-grid {{ display:flex; flex-direction:column; gap:1.5rem; }}
    .book-card-v2 {{ display:flex; gap:1.75rem; background:var(--surface); border:1px solid var(--border); border-radius:var(--border-radius-md); padding:1.5rem; transition: all 0.3s; }}
    .book-card-v2:hover {{ border-color:var(--accent-primary); box-shadow: 0 8px 24px rgba(110,231,183,0.08); }}
    @media(max-width:640px){{ .book-card-v2 {{ flex-direction:column; }} }}

    .book-cover-wrap {{ width:130px; flex-shrink:0; height:180px; border-radius:8px; overflow:hidden; box-shadow: 4px 4px 16px rgba(0,0,0,0.4); position:relative; }}
    .book-cover-wrap img {{ width:100%; height:100%; object-fit:cover; }}
    .book-cover-fallback {{ width:100%; height:100%; background:linear-gradient(135deg,var(--accent-primary),#3b82f6); flex-direction:column; align-items:center; justify-content:center; color:var(--bg-primary); font-size:0.8rem; font-weight:700; text-align:center; padding:0.5rem; gap:0.5rem; }}
    .book-cover-fallback i {{ font-size:2rem; }}

    .book-info {{ flex:1; display:flex; flex-direction:column; gap:0.5rem; }}
    .book-subject-tag {{ font-size:0.72rem; color:var(--accent-primary); text-transform:uppercase; letter-spacing:0.1em; font-weight:700; }}
    .book-title-v2 {{ font-size:1.2rem; color:var(--text-primary); font-weight:700; line-height:1.3; margin:0; }}
    .book-authors-v2 {{ color:var(--text-secondary); font-size:0.85rem; margin:0; }}
    .book-edition {{ color:var(--text-muted); font-size:0.78rem; margin:0; }}
    .book-rating-row {{ display:flex; align-items:center; gap:0.5rem; flex-wrap:wrap; }}
    .stars {{ color:#f59e0b; font-size:0.9rem; }}
    .book-rating-num {{ font-weight:700; color:#f59e0b; font-size:0.9rem; }}
    .book-votes {{ color:var(--text-muted); font-size:0.78rem; }}
    .book-priority-row {{ display:flex; gap:0.5rem; }}
    .book-chapters {{ background:rgba(110,231,183,0.04); border:1px solid rgba(110,231,183,0.12); border-radius:6px; padding:0.75rem 1rem; font-size:0.83rem; color:var(--text-secondary); }}
    .book-chapters-label {{ color:var(--accent-primary); font-size:0.72rem; text-transform:uppercase; letter-spacing:0.08em; font-weight:700; margin-bottom:0.3rem; }}
    .book-chapters p {{ margin:0; line-height:1.5; }}
    .book-tip {{ font-size:0.82rem; color:var(--text-muted); font-style:italic; line-height:1.5; }}
    .book-tip i {{ color:var(--accent-primary); margin-right:0.3rem; }}
    .book-buy-btn {{ display:inline-flex; align-items:center; gap:0.5rem; padding:0.45rem 1rem; background:#ff9900; color:#111; border-radius:6px; text-decoration:none; font-size:0.82rem; font-weight:700; transition:all 0.2s; width:fit-content; margin-top:0.25rem; }}
    .book-buy-btn:hover {{ background:#ffac31; transform:translateY(-1px); }}
  </style>
</head>
<body>
  <header class="mobile-header">
    <div class="logo">GATE A TO Z</div>
    <button class="menu-toggle" id="menu-btn"><i class="fas fa-bars"></i></button>
  </header>
  <div class="app-container">
    <nav class="sidebar" id="sidebar">
{SIDEBAR}
    </nav>
    <main class="main-content">
      <section class="section">
        <span class="section-tag">Resources</span>
        <h2 class="section-title">GATE CS Book Arsenal</h2>
        <p class="text-secondary mb-4">The only books you need for GATE CS, with real covers, community ratings, and the exact chapters that matter. Don't read cover-to-cover — use the chapter guides below.</p>

        <div class="callout warning mb-4">
          <span class="callout-title">⚠️ Golden Rule</span>
          No GATE topper reads books cover-to-cover. Identify the high-yield chapters, study them deeply, then immediately practice PYQs on that topic. Repeat. Books are a reference, not a syllabus.
        </div>

        <div class="table-container mb-4">
          <table class="books-table">
            <thead><tr><th>Subject</th><th>Recommended Book</th><th>Author(s)</th><th>Rating</th><th>Priority</th></tr></thead>
            <tbody>
              {"".join(f'<tr><td><strong>{b["subject"]}</strong></td><td>{b["title"]}</td><td>{b["authors"]}</td><td style="color:#f59e0b;font-weight:700">⭐ {b["rating"]}</td><td><span class="badge {b["priority_cls"]}" style="font-size:0.7rem">{b["priority"]}</span></td></tr>' for b in books)}
            </tbody>
          </table>
        </div>

        <h3 style="font-family:var(--font-display);text-transform:uppercase;color:var(--text-primary);margin-bottom:1.25rem;">Detailed Book Cards</h3>
        <div class="book-cards-grid">
{cards_html}
        </div>
      </section>
    </main>
  </div>
  <script src="js/app.js"></script>
</body>
</html>"""

def main():
    print("Downloading book covers from Open Library...")
    for b in books:
        slug = b['isbn']
        filename = f"{slug}.jpg"
        print(f"Processing: {b['title']}")
        success = download_cover(b['isbn'], filename)
        if success:
            b['local_img'] = f"{BOOKS_DIR}/{filename}"
        else:
            b['local_img'] = None
        time.sleep(0.4)

    print("\nGenerating books.html...")
    html = generate_html()
    with open("books.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Done! {sum(1 for b in books if b.get('local_img'))} covers downloaded.")

if __name__ == "__main__":
    main()
