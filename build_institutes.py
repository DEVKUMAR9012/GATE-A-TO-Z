"""
Fetches real institute images using Wikipedia's REST v1 Summary API
(much more reliable, rarely rate-limited), downloads them locally,
and generates institutes.html
"""
import urllib.request
import urllib.parse
import json
import os
import time

INST_DIR = "img/institutes"
os.makedirs(INST_DIR, exist_ok=True)

institutes = [
    # --- IITs ---
    {"name": "IIT Kharagpur",       "type": "iit", "wiki": "Indian_Institute_of_Technology_Kharagpur", "website": "http://www.iitkgp.ac.in",      "cutoff": 720},
    {"name": "IIT Bombay",          "type": "iit", "wiki": "Indian_Institute_of_Technology_Bombay",    "website": "http://www.iitb.ac.in",         "cutoff": 780},
    {"name": "IIT Madras",          "type": "iit", "wiki": "Indian_Institute_of_Technology_Madras",    "website": "https://www.iitm.ac.in",        "cutoff": 770},
    {"name": "IIT Kanpur",          "type": "iit", "wiki": "Indian_Institute_of_Technology_Kanpur",    "website": "https://www.iitk.ac.in",        "cutoff": 750},
    {"name": "IIT Delhi",           "type": "iit", "wiki": "Indian_Institute_of_Technology_Delhi",     "website": "https://home.iitd.ac.in",       "cutoff": 780},
    {"name": "IIT Guwahati",        "type": "iit", "wiki": "Indian_Institute_of_Technology_Guwahati",  "website": "https://www.iitg.ac.in",        "cutoff": 700},
    {"name": "IIT Roorkee",         "type": "iit", "wiki": "Indian_Institute_of_Technology_Roorkee",   "website": "https://www.iitr.ac.in",        "cutoff": 720},
    {"name": "IIT Ropar",           "type": "iit", "wiki": "Indian_Institute_of_Technology_Ropar",     "website": "https://www.iitrpr.ac.in",      "cutoff": 640},
    {"name": "IIT Bhubaneswar",     "type": "iit", "wiki": "Indian_Institute_of_Technology_Bhubaneswar","website": "https://www.iitbbs.ac.in",     "cutoff": 640},
    {"name": "IIT Gandhinagar",     "type": "iit", "wiki": "Indian_Institute_of_Technology_Gandhinagar","website": "https://www.iitgn.ac.in",      "cutoff": 660},
    {"name": "IIT Hyderabad",       "type": "iit", "wiki": "Indian_Institute_of_Technology_Hyderabad", "website": "https://www.iith.ac.in",        "cutoff": 670},
    {"name": "IIT Jodhpur",         "type": "iit", "wiki": "Indian_Institute_of_Technology_Jodhpur",   "website": "https://www.iitj.ac.in",        "cutoff": 640},
    {"name": "IIT Patna",           "type": "iit", "wiki": "Indian_Institute_of_Technology_Patna",     "website": "https://www.iitp.ac.in",        "cutoff": 630},
    {"name": "IIT Indore",          "type": "iit", "wiki": "Indian_Institute_of_Technology_Indore",    "website": "https://www.iiti.ac.in",        "cutoff": 650},
    {"name": "IIT Mandi",           "type": "iit", "wiki": "Indian_Institute_of_Technology_Mandi",     "website": "https://www.iitmandi.ac.in",    "cutoff": 620},
    {"name": "IIT (BHU) Varanasi",  "type": "iit", "wiki": "Indian_Institute_of_Technology_(BHU)_Varanasi","website": "https://www.iitbhu.ac.in", "cutoff": 660},
    {"name": "IIT Palakkad",        "type": "iit", "wiki": "Indian_Institute_of_Technology_Palakkad",  "website": "https://www.iitpkd.ac.in",      "cutoff": 620},
    {"name": "IIT Tirupati",        "type": "iit", "wiki": "Indian_Institute_of_Technology_Tirupati",  "website": "https://www.iittp.ac.in",       "cutoff": 600},
    {"name": "IIT (ISM) Dhanbad",   "type": "iit", "wiki": "Indian_Institute_of_Technology_(ISM)_Dhanbad","website": "https://www.iitism.ac.in",  "cutoff": 640},
    {"name": "IIT Bhilai",          "type": "iit", "wiki": "Indian_Institute_of_Technology_Bhilai",    "website": "https://www.iitbhilai.ac.in",   "cutoff": 590},
    {"name": "IIT Goa",             "type": "iit", "wiki": "Indian_Institute_of_Technology_Goa",       "website": "https://www.iitgoa.ac.in",      "cutoff": 580},
    {"name": "IIT Jammu",           "type": "iit", "wiki": "Indian_Institute_of_Technology_Jammu",     "website": "https://www.iitjammu.ac.in",    "cutoff": 570},
    {"name": "IIT Dharwad",         "type": "iit", "wiki": "Indian_Institute_of_Technology_Dharwad",   "website": "https://www.iitdh.ac.in",       "cutoff": 570},
    # --- NITs ---
    {"name": "NIT Tiruchirappalli", "type": "nit", "wiki": "National_Institute_of_Technology,_Tiruchirappalli", "website": "https://www.nitt.edu",       "cutoff": 680},
    {"name": "NIT Karnataka (Surathkal)","type": "nit","wiki": "National_Institute_of_Technology_Karnataka","website": "https://www.nitk.ac.in",    "cutoff": 660},
    {"name": "NIT Rourkela",        "type": "nit", "wiki": "National_Institute_of_Technology_Rourkela","website": "https://www.nitrkl.ac.in",      "cutoff": 650},
    {"name": "NIT Warangal",        "type": "nit", "wiki": "National_Institute_of_Technology_Warangal","website": "https://www.nitw.ac.in",        "cutoff": 650},
    {"name": "NIT Calicut",         "type": "nit", "wiki": "National_Institute_of_Technology_Calicut", "website": "https://www.nitc.ac.in",        "cutoff": 640},
    {"name": "VNIT Nagpur",         "type": "nit", "wiki": "Visvesvaraya_National_Institute_of_Technology","website": "https://www.vnit.ac.in",   "cutoff": 620},
    {"name": "MNIT Jaipur",         "type": "nit", "wiki": "Malaviya_National_Institute_of_Technology_Jaipur","website": "https://www.mnit.ac.in","cutoff": 610},
    {"name": "NIT Kurukshetra",     "type": "nit", "wiki": "National_Institute_of_Technology_Kurukshetra","website": "https://www.nitkkr.ac.in", "cutoff": 600},
    {"name": "NIT Silchar",         "type": "nit", "wiki": "National_Institute_of_Technology_Silchar", "website": "https://www.nits.ac.in",        "cutoff": 560},
    {"name": "NIT Durgapur",        "type": "nit", "wiki": "National_Institute_of_Technology_Durgapur","website": "https://nitdgp.ac.in",         "cutoff": 560},
    {"name": "MNNIT Allahabad",     "type": "nit", "wiki": "Motilal_Nehru_National_Institute_of_Technology_Allahabad","website": "https://www.mnnit.ac.in","cutoff": 610},
    {"name": "NIT Jalandhar",       "type": "nit", "wiki": "Dr._B._R._Ambedkar_National_Institute_of_Technology_Jalandhar","website": "https://www.nitj.ac.in","cutoff": 550},
    {"name": "NIT Meghalaya",       "type": "nit", "wiki": "National_Institute_of_Technology_Meghalaya","website": "https://www.nitm.ac.in",      "cutoff": 450},
    {"name": "MANIT Bhopal",        "type": "nit", "wiki": "Maulana_Azad_National_Institute_of_Technology","website": "https://www.manit.ac.in", "cutoff": 580},
    {"name": "NIT Raipur",          "type": "nit", "wiki": "National_Institute_of_Technology_Raipur", "website": "https://www.nitrr.ac.in",        "cutoff": 520},
    {"name": "NIT Agartala",        "type": "nit", "wiki": "National_Institute_of_Technology_Agartala","website": "https://www.nita.ac.in",       "cutoff": 430},
    {"name": "NIT Goa",             "type": "nit", "wiki": "National_Institute_of_Technology_Goa",    "website": "https://www.nitgoa.ac.in",       "cutoff": 440},
    {"name": "NIT Jamshedpur",      "type": "nit", "wiki": "National_Institute_of_Technology_Jamshedpur","website": "https://www.nitjsr.ac.in",  "cutoff": 520},
    {"name": "NIT Patna",           "type": "nit", "wiki": "National_Institute_of_Technology_Patna",  "website": "https://www.nitp.ac.in",         "cutoff": 500},
    {"name": "NIT Hamirpur",        "type": "nit", "wiki": "National_Institute_of_Technology_Hamirpur","website": "https://www.nith.ac.in",       "cutoff": 490},
    {"name": "NIT Puducherry",      "type": "nit", "wiki": "National_Institute_of_Technology_Puducherry","website": "https://www.nitpy.ac.in",   "cutoff": 440},
    {"name": "NIT Manipur",         "type": "nit", "wiki": "National_Institute_of_Technology_Manipur","website": "https://www.nitmanipur.ac.in",  "cutoff": 400},
    {"name": "NIT Arunachal Pradesh","type":"nit", "wiki": "National_Institute_of_Technology_Arunachal_Pradesh","website": "https://www.nitap.ac.in","cutoff": 380},
    {"name": "NIT Srinagar",        "type": "nit", "wiki": "National_Institute_of_Technology_Srinagar","website": "https://www.nitsri.ac.in",    "cutoff": 430},
    {"name": "NIT Delhi",           "type": "nit", "wiki": "National_Institute_of_Technology_Delhi",  "website": "https://www.nitdelhi.ac.in",     "cutoff": 490},
    {"name": "NIT Mizoram",         "type": "nit", "wiki": "National_Institute_of_Technology_Mizoram","website": "https://www.nitmz.ac.in",       "cutoff": 380},
    {"name": "NIT Nagaland",        "type": "nit", "wiki": "National_Institute_of_Technology_Nagaland","website": "https://www.nitnagaland.ac.in","cutoff": 380},
    {"name": "NIT Sikkim",          "type": "nit", "wiki": "National_Institute_of_Technology_Sikkim", "website": "https://www.nitsikkim.ac.in",    "cutoff": 380},
    {"name": "NIT Uttarakhand",     "type": "nit", "wiki": "National_Institute_of_Technology_Uttarakhand","website": "https://www.nituk.ac.in", "cutoff": 400},
    {"name": "NIT Andhra Pradesh",  "type": "nit", "wiki": "National_Institute_of_Technology_Andhra_Pradesh","website": "https://www.nitandhra.ac.in","cutoff": 400},
    {"name": "IIEST Shibpur",       "type": "nit", "wiki": "Indian_Institute_of_Engineering_Science_and_Technology,_Shibpur","website": "https://www.iiest.ac.in","cutoff": 520},
]

FALLBACK = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/640px-No_image_available.svg.png"

def fetch_thumbnail(wiki_title):
    """Use Wikipedia REST v1 API - returns verified thumbnail URL."""
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{wiki_title}"
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'GATE-A-TO-Z-Bot/1.0 (educational project)'
        })
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode())
            if 'thumbnail' in data:
                return data['thumbnail']['source']
    except Exception as e:
        print(f"  Error: {e}")
    return None

def download_image(url, filename):
    """Download image to local file."""
    filepath = os.path.join(INST_DIR, filename)
    if os.path.exists(filepath):
        print(f"  Already exists: {filename}")
        return filepath
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as r:
            with open(filepath, 'wb') as f:
                f.write(r.read())
        print(f"  Downloaded: {filename}")
        return filepath
    except Exception as e:
        print(f"  Download failed: {e}")
        return None

def main():
    # Step 1: Fetch thumbnail URLs and download locally
    for inst in institutes:
        slug = inst['wiki'].replace(' ', '_')
        ext = ".jpg"
        filename = f"{slug}{ext}"
        local_path = os.path.join(INST_DIR, filename)
        
        print(f"Processing: {inst['name']}")
        
        if os.path.exists(local_path):
            inst['local_img'] = f"{INST_DIR}/{filename}"
        else:
            thumb_url = fetch_thumbnail(inst['wiki'])
            time.sleep(0.5)  # polite delay
            if thumb_url:
                # Detect extension
                ext = ".jpg" if "jpg" in thumb_url.lower() or "jpeg" in thumb_url.lower() else ".png"
                filename = f"{slug}{ext}"
                local_path = os.path.join(INST_DIR, filename)
                dl = download_image(thumb_url, filename)
                inst['local_img'] = f"{INST_DIR}/{filename}" if dl else None
            else:
                inst['local_img'] = None
    
    # Step 2: Generate HTML
    print("\nGenerating institutes.html...")
    generate_html()
    print("Done!")

SIDEBAR = """      <div class="sidebar-header"><div class="logo">GATE A TO Z</div></div>
      <div class="search-container mb-4">
        <i class="fas fa-search search-icon"></i>
        <input type="text" class="search-input" id="global-search" placeholder="Search topics...">
        <div class="search-results-container" id="search-results"></div>
      </div>
      <ul class="nav-list">
        <li class="nav-item"><a href="index.html" class="nav-link"><i class="fas fa-home"></i> Overview</a></li>
        <li class="nav-item"><a href="basics.html" class="nav-link"><i class="fas fa-book"></i> GATE Basics</a></li>
        <li class="nav-item"><a href="papers.html" class="nav-link"><i class="fas fa-file-alt"></i> GATE Papers</a></li>
        <li class="nav-item"><a href="syllabus.html" class="nav-link"><i class="fas fa-laptop-code"></i> GATE CS</a></li>
        <li class="nav-item"><a href="opportunities.html" class="nav-link"><i class="fas fa-bullseye"></i> Opportunities</a></li>
        <li class="nav-item"><a href="admissions.html" class="nav-link"><i class="fas fa-university"></i> IIT / NIT Admissions</a></li>
        <li class="nav-item"><a href="institutes.html" class="nav-link active"><i class="fas fa-landmark"></i> Institute Explorer</a></li>
        <li class="nav-item"><a href="psu.html" class="nav-link"><i class="fas fa-building"></i> PSU Recruitment</a></li>
        <li class="nav-item"><a href="scholarship.html" class="nav-link"><i class="fas fa-money-bill-wave"></i> Scholarship</a></li>
        <li class="nav-item"><a href="abroad.html" class="nav-link"><i class="fas fa-globe"></i> Abroad</a></li>
        <li class="nav-item"><a href="roadmap.html" class="nav-link"><i class="fas fa-map-signs"></i> Roadmap & Plan</a></li>
        <li class="nav-item"><a href="decision-tree.html" class="nav-link"><i class="fas fa-code-branch"></i> Decision Tree</a></li>
        <li class="nav-item"><a href="targets.html" class="nav-link"><i class="fas fa-crosshairs"></i> Targets</a></li>
        <li class="nav-item"><a href="resources.html" class="nav-link"><i class="fas fa-link"></i> Official Sources</a></li>
        <li class="nav-item mt-4">
            <a href="login.html" class="nav-link" style="border:1px solid var(--accent-primary);border-radius:var(--border-radius-sm);">
                <i class="fas fa-sign-in-alt"></i> Join GAZ (Optional)
            </a>
        </li>
      </ul>"""

def generate_html():
    cards = ""
    for inst in institutes:
        img_src = inst.get('local_img') or FALLBACK
        cutoff = inst.get('cutoff', 0)
        badge = "IIT" if inst['type'] == "iit" else "NIT"
        badge_cls = "high" if inst['type'] == "iit" else "medium"
        wiki_url = f"https://en.wikipedia.org/wiki/{inst['wiki']}"
        search_url = f"https://google.com/search?q={urllib.parse.quote(inst['name'] + ' MTech CSE GATE cutoff 2024')}"
        cutoff_html = f'<span class="cutoff-tag">GATE: {cutoff}+</span>' if cutoff else ''
        cards += f"""
          <div class="institute-card {inst['type']}">
            <div class="inst-img-wrapper">
              <img src="{img_src}" alt="{inst['name']} campus" loading="lazy">
              <span class="inst-badge badge {badge_cls}">{badge}</span>
              {cutoff_html}
            </div>
            <div class="inst-content">
              <h4 class="inst-name">{inst['name']}</h4>
              <div class="inst-links">
                <a href="{inst['website']}" target="_blank" class="inst-link">Official <i class="fas fa-external-link-alt"></i></a>
                <a href="{wiki_url}" target="_blank" class="inst-link">Wiki <i class="fas fa-external-link-alt"></i></a>
                <a href="{search_url}" target="_blank" class="inst-link">Cutoffs <i class="fas fa-search"></i></a>
              </div>
            </div>
          </div>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Institute Explorer | GATE A TO Z</title>
  <meta name="description" content="All 23 IITs and 31 NITs with real campus photos, GATE CS cutoffs, and official websites.">
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
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
      <section id="explorer" class="section searchable">
        <span class="section-tag">Directory</span>
        <h2 class="section-title">Institute Explorer</h2>
        <p class="text-secondary mb-4">All <strong>23 IITs</strong> and <strong>31 NITs</strong> offering M.Tech via GATE — with real campus photos, official websites, and approximate GATE CSE cutoff scores.</p>
        <div class="filters mb-4">
          <button class="filter-btn active" onclick="filterInst('all',this)">All (54)</button>
          <button class="filter-btn" onclick="filterInst('iit',this)">IITs (23)</button>
          <button class="filter-btn" onclick="filterInst('nit',this)">NITs / Others (31)</button>
        </div>
        <div class="institute-grid" id="inst-grid">
{cards}
        </div>
      </section>
    </main>
  </div>
  <script>
    function filterInst(type, btn) {{
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('.institute-card').forEach(c => {{
        c.style.display = (type === 'all' || c.classList.contains(type)) ? 'flex' : 'none';
      }});
    }}
  </script>
  <script src="js/app.js"></script>
</body>
</html>"""

    with open("institutes.html", "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    main()
