"""
Build the PSU page with company logos downloaded from Wikimedia.
"""
import urllib.request
import urllib.parse
import json
import os
import time

PSU_DIR = "img/psu"
os.makedirs(PSU_DIR, exist_ok=True)

psus = [
    {
        "name": "ONGC",
        "full": "Oil and Natural Gas Corporation",
        "wiki": "Oil_and_Natural_Gas_Corporation",
        "website": "https://www.ongcindia.com",
        "role": "Programming Officer / E1",
        "sector": "Oil & Gas",
        "safe_air": "< 100",
        "air_num": 100,
        "ctc": "~₹ 17–20 LPA",
        "selection": "GATE Score → GD → Personal Interview (85% GATE + 15% PI)",
        "eligibility": "B.Tech CSE/IT. Min 60% (55% for SC/ST/PH). Age ≤ 30 yrs.",
        "notes": "One of the biggest PSU recruiters for CS. Excellent perks including HRA, quarters, and medical for entire family.",
        "status": "active"
    },
    {
        "name": "IOCL",
        "full": "Indian Oil Corporation Limited",
        "wiki": "Indian_Oil_Corporation",
        "website": "https://www.iocl.com",
        "role": "Information Systems Officer (Grade A)",
        "sector": "Oil & Gas",
        "safe_air": "< 150",
        "air_num": 150,
        "ctc": "~₹ 16–19 LPA",
        "selection": "GATE Score → GD → Personal Interview",
        "eligibility": "B.Tech CSE/IT/ECE. Min 65%. Age ≤ 26 yrs.",
        "notes": "Huge company. One of the Maharatna PSUs. Job security is outstanding. Postings can be anywhere in India.",
        "status": "active"
    },
    {
        "name": "POSOCO / Grid-India",
        "full": "Power System Operation Corporation",
        "wiki": "Power_System_Operation_Corporation",
        "website": "https://www.posoco.in",
        "role": "Executive Trainee (CS/IT)",
        "sector": "Power",
        "safe_air": "< 150",
        "air_num": 150,
        "ctc": "~₹ 18–22 LPA",
        "selection": "GATE Score only (No Interview). Direct merit list.",
        "eligibility": "B.Tech CSE/IT. Min 65%. Age ≤ 28 yrs.",
        "notes": "Extremely competitive for CS. No interview makes GATE score the only deciding factor. Excellent work-life balance.",
        "status": "active"
    },
    {
        "name": "DRDO",
        "full": "Defence Research and Development Organisation",
        "wiki": "Defence_Research_and_Development_Organisation",
        "website": "https://www.drdo.gov.in",
        "role": "Scientist 'B'",
        "sector": "Defence & Research",
        "safe_air": "< 250",
        "air_num": 250,
        "ctc": "~₹ 15.5 LPA + allowances",
        "selection": "GATE Score → Personal Interview (Technical + HR)",
        "eligibility": "B.Tech CSE/IT. Min 60%. Age ≤ 28 yrs.",
        "notes": "Prestige is unmatched. You work on cutting-edge defense technology. Gazetted Officer status. Government housing available.",
        "status": "active"
    },
    {
        "name": "BARC",
        "full": "Bhabha Atomic Research Centre",
        "wiki": "Bhabha_Atomic_Research_Centre",
        "website": "https://www.barc.gov.in",
        "role": "Scientific Officer (OCES/DGFS)",
        "sector": "Nuclear / Research",
        "safe_air": "< 300",
        "air_num": 300,
        "ctc": "~₹ 14–16 LPA + allowances",
        "selection": "GATE Score → Interview (Shortlisted candidates attend a 1-year training at Mumbai before final placement)",
        "eligibility": "B.Tech CSE/IT. Min 60%. Age ≤ 26 yrs.",
        "notes": "Very prestigious. Includes 1-year OCES/DGFS training program in Mumbai or Mysuru. Classified work on nuclear R&D systems.",
        "status": "active"
    },
    {
        "name": "CRIS",
        "full": "Centre for Railway Information Systems",
        "wiki": "Centre_for_Railway_Information_Systems",
        "website": "https://www.cris.org.in",
        "role": "Assistant Software Engineer / Junior Software Engineer",
        "sector": "Railways / IT",
        "safe_air": "< 400",
        "air_num": 400,
        "ctc": "~₹ 12–15 LPA",
        "selection": "GATE Score → Technical Interview",
        "eligibility": "B.Tech CSE/IT. Min 60%. Age ≤ 30 yrs.",
        "notes": "The IT arm of Indian Railways. Great for CSE students since the work is pure software development (PNR system, ticketing etc).",
        "status": "active"
    },
    {
        "name": "ISRO",
        "full": "Indian Space Research Organisation",
        "wiki": "Indian_Space_Research_Organisation",
        "website": "https://www.isro.gov.in",
        "role": "Scientist/Engineer 'SC'",
        "sector": "Space Research",
        "safe_air": "< 200",
        "air_num": 200,
        "ctc": "~₹ 15.6 LPA + allowances",
        "selection": "GATE Score → Written Test (Centralised Recruitment Board) → Interview",
        "eligibility": "B.Tech CSE/IT/ECE. Min 65%. Age ≤ 35 yrs.",
        "notes": "Dream job for engineers. Uses GATE scores for initial shortlisting but has its own CRB exam and interview. Incredible prestige and interesting work.",
        "status": "active"
    },
    {
        "name": "BHEL",
        "full": "Bharat Heavy Electricals Limited",
        "wiki": "Bharat_Heavy_Electricals_Limited",
        "website": "https://www.bhel.com",
        "role": "Engineer Trainee (IT/CS)",
        "sector": "Manufacturing / Power",
        "safe_air": "< 500",
        "air_num": 500,
        "ctc": "~₹ 12–14 LPA",
        "selection": "GATE Score → GD → Personal Interview",
        "eligibility": "B.Tech CSE/IT. Min 60%. Age ≤ 27 yrs.",
        "notes": "Navratna PSU. CS vacancies are limited but available. Good for those wanting a stable government job with moderate technical work.",
        "status": "active"
    },
    {
        "name": "NTPC",
        "full": "National Thermal Power Corporation",
        "wiki": "NTPC_Limited",
        "website": "https://www.ntpc.co.in",
        "role": "Executive Trainee (IT)",
        "sector": "Power",
        "safe_air": "Varies",
        "air_num": 0,
        "ctc": "~₹ 18–22 LPA",
        "selection": "GATE Score → Group Discussion → Interview",
        "eligibility": "B.Tech CSE/IT. Min 65%. Age ≤ 27 yrs.",
        "notes": "Maharatna PSU. CS vacancies are irregular and uncommon. When they do recruit, competition is fierce. Check notifications yearly.",
        "status": "irregular"
    },
    {
        "name": "GAIL",
        "full": "Gas Authority of India Limited",
        "wiki": "GAIL_(India)",
        "website": "https://www.gail.nic.in",
        "role": "Executive Trainee (Telecommunication/IT)",
        "sector": "Oil & Gas",
        "safe_air": "< 300",
        "air_num": 300,
        "ctc": "~₹ 18–22 LPA",
        "selection": "GATE Score → GD → Personal Interview",
        "eligibility": "B.Tech CSE/IT/ECE for Telecom branch. Age ≤ 28 yrs.",
        "notes": "CS candidates typically apply under the 'Telecommunication' discipline. Maharatna company with excellent salary and facilities.",
        "status": "active"
    },
    {
        "name": "HPCL",
        "full": "Hindustan Petroleum Corporation Limited",
        "wiki": "Hindustan_Petroleum",
        "website": "https://www.hindustanpetroleum.com",
        "role": "Officer (IT)",
        "sector": "Oil & Gas",
        "safe_air": "< 200",
        "air_num": 200,
        "ctc": "~₹ 16–19 LPA",
        "selection": "GATE Score → Group Task → Personal Interview",
        "eligibility": "B.Tech CSE/IT. Min 60%. Age ≤ 25 yrs.",
        "notes": "Navratna Maharatna PSU. Less frequent CS recruitment than ONGC/IOCL but good pay when available.",
        "status": "active"
    },
    {
        "name": "BPCL",
        "full": "Bharat Petroleum Corporation Limited",
        "wiki": "Bharat_Petroleum",
        "website": "https://www.bharatpetroleum.in",
        "role": "Engineer (IT)",
        "sector": "Oil & Gas",
        "safe_air": "< 200",
        "air_num": 200,
        "ctc": "~₹ 16–18 LPA",
        "selection": "GATE Score → Interview",
        "eligibility": "B.Tech CSE/IT. Min 60%. Age ≤ 25 yrs.",
        "notes": "Navratna PSU. Good company culture. CS recruitment is limited but salary and perks are excellent.",
        "status": "active"
    },
]

FALLBACK_LOGO = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/320px-No_image_available.svg.png"

def fetch_thumbnail(wiki_title):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{wiki_title}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'GATE-A-TO-Z-Bot/1.0 (educational)'})
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode())
            if 'thumbnail' in data:
                return data['thumbnail']['source']
    except Exception as e:
        print(f"  Error: {e}")
    return None

def download_image(url, filename):
    filepath = os.path.join(PSU_DIR, filename)
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
        <li class="nav-item"><a href="institutes.html" class="nav-link"><i class="fas fa-landmark"></i> Institute Explorer</a></li>
        <li class="nav-item"><a href="psu.html" class="nav-link active"><i class="fas fa-building"></i> PSU Recruitment</a></li>
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

def status_badge(s):
    if s == "active": return '<span class="badge high">Active</span>'
    if s == "irregular": return '<span class="badge medium">Irregular</span>'
    return '<span class="badge notverified">Rare</span>'

def generate_html():
    cards = ""
    for p in psus:
        img_src = p.get('local_img') or FALLBACK_LOGO
        air_badge = f'<div class="psu-air-badge">AIR {p["safe_air"]}</div>' if p["air_num"] else '<div class="psu-air-badge psu-air-varies">Varies</div>'
        cards += f"""
        <div class="psu-card">
          <div class="psu-card-header">
            <div class="psu-logo-wrap">
              <img src="{img_src}" alt="{p['name']} logo" loading="lazy"
                   onerror="this.onerror=null;this.src='{FALLBACK_LOGO}'">
            </div>
            <div class="psu-header-info">
              <h3 class="psu-name">{p['name']}</h3>
              <p class="psu-full-name">{p['full']}</p>
              <div class="psu-tags">
                <span class="section-tag" style="font-size:0.7rem;padding:2px 8px;">{p['sector']}</span>
                {status_badge(p['status'])}
              </div>
            </div>
            {air_badge}
          </div>
          <div class="psu-card-body">
            <div class="psu-detail-grid">
              <div class="psu-detail-item">
                <i class="fas fa-briefcase"></i>
                <div>
                  <span class="psu-label">Role</span>
                  <span class="psu-value">{p['role']}</span>
                </div>
              </div>
              <div class="psu-detail-item">
                <i class="fas fa-rupee-sign"></i>
                <div>
                  <span class="psu-label">CTC / Package</span>
                  <span class="psu-value text-cyan">{p['ctc']}</span>
                </div>
              </div>
              <div class="psu-detail-item">
                <i class="fas fa-list-ol"></i>
                <div>
                  <span class="psu-label">Safe AIR (General)</span>
                  <span class="psu-value text-cyan">{p['safe_air']}</span>
                </div>
              </div>
              <div class="psu-detail-item">
                <i class="fas fa-user-check"></i>
                <div>
                  <span class="psu-label">Eligibility</span>
                  <span class="psu-value">{p['eligibility']}</span>
                </div>
              </div>
            </div>
            <div class="psu-selection">
              <i class="fas fa-route"></i>
              <div>
                <span class="psu-label">Selection Process</span>
                <span class="psu-value">{p['selection']}</span>
              </div>
            </div>
            <div class="psu-notes">
              <i class="fas fa-lightbulb" style="color:var(--accent-primary);margin-right:0.5rem;"></i>
              {p['notes']}
            </div>
            <a href="{p['website']}" target="_blank" class="psu-website-btn">
              Visit Official Website <i class="fas fa-external-link-alt"></i>
            </a>
          </div>
        </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PSU Recruitment for GATE CSE | GATE A TO Z</title>
  <meta name="description" content="Complete PSU recruitment guide for GATE CSE students with AIR cutoffs, salaries, eligibility, and selection process for ONGC, IOCL, DRDO, BARC, ISRO and more.">
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
      <section id="psu" class="section searchable">
        <span class="section-tag">Careers</span>
        <h2 class="section-title">PSU Recruitment for CS/IT</h2>

        <div class="callout warning mb-4">
          <span class="callout-title">⚠️ The Reality of PSUs for CSE</span>
          Unlike Core branches (Mechanical/Electrical), CSE has significantly fewer PSU vacancies. A "Qualified" GATE status is NOT enough. To secure a PSU job through GATE CSE, you generally need an <strong>All India Rank (AIR) under 200</strong> for General Category. Treat PSU preparation as a bonus, not a primary goal.
        </div>

        <div class="psu-filter-bar mb-4">
          <button class="filter-btn active" onclick="filterPSU('all',this)">All PSUs</button>
          <button class="filter-btn" onclick="filterPSU('active',this)">Active Recruiters</button>
          <button class="filter-btn" onclick="filterPSU('irregular',this)">Irregular</button>
        </div>

        <div class="psu-grid" id="psu-grid">
{cards}
        </div>

        <h3 class="mt-5 mb-3" style="color:var(--text-primary);font-family:var(--font-display);text-transform:uppercase;">General Selection Process</h3>
        <div class="table-container mb-4">
          <table>
            <thead><tr><th>Step</th><th>Stage</th><th>Weightage</th><th>Tip</th></tr></thead>
            <tbody>
              <tr><td><strong>1</strong></td><td>GATE Score (Shortlisting)</td><td class="text-cyan font-bold">~85%</td><td>This is the only thing you can control right now. Maximize your score.</td></tr>
              <tr><td><strong>2</strong></td><td>Apply on PSU Website</td><td>—</td><td>PSUs release their own notifications. Monitor their websites and job portals (like NaukriGovt) from Feb-April after GATE results.</td></tr>
              <tr><td><strong>3</strong></td><td>Group Discussion (GD)</td><td>~5%</td><td>Practice speaking on tech and current affairs for 2 minutes. Be the first to speak or summarize.</td></tr>
              <tr><td><strong>4</strong></td><td>Personal Interview (PI)</td><td>~10-15%</td><td>Review your B.Tech subjects deeply. Expect questions on OS, DBMS, Networks, and your Final Year Project.</td></tr>
            </tbody>
          </table>
        </div>

      </section>
    </main>
  </div>
  <script>
    function filterPSU(type, btn) {{
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('.psu-card').forEach(c => {{
        if (type === 'all') {{ c.style.display = 'flex'; return; }}
        c.style.display = c.dataset.status === type ? 'flex' : 'none';
      }});
    }}
  </script>
  <script src="js/app.js"></script>
</body>
</html>"""

def main():
    print("Fetching PSU logos from Wikipedia...")
    for p in psus:
        fname_base = p['wiki'].replace('/', '_')
        ext = ".jpg"
        print(f"Processing: {p['name']}")
        local_path = os.path.join(PSU_DIR, fname_base + ext)
        if os.path.exists(local_path):
            p['local_img'] = f"{PSU_DIR}/{fname_base}{ext}"
            print(f"  Already exists.")
            continue
        thumb = fetch_thumbnail(p['wiki'])
        time.sleep(0.8)
        if thumb:
            ext = ".png" if "png" in thumb.lower() else ".jpg"
            fname = fname_base + ext
            dl = download_image(thumb, fname)
            p['local_img'] = f"{PSU_DIR}/{fname}" if dl else None
        else:
            p['local_img'] = None

    print("\nGenerating psu.html...")
    html = generate_html()
    with open("psu.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Done!")

if __name__ == "__main__":
    main()
