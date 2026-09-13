import urllib.parse

# Real Wikipedia Commons image URLs for each institute - hardcoded to avoid rate limits
iits = [
    {
        "name": "IIT Kharagpur",
        "full": "Indian Institute of Technology Kharagpur",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/IIT_Kharagpur_Logo.svg/500px-IIT_Kharagpur_Logo.svg.png",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/IIT_Kharagpur_August_2007.jpg/640px-IIT_Kharagpur_August_2007.jpg",
        "website": "http://www.iitkgp.ac.in"
    },
    {
        "name": "IIT Bombay",
        "full": "Indian Institute of Technology Bombay",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/IIT_Bombay_-_Main_Building.jpg/640px-IIT_Bombay_-_Main_Building.jpg",
        "website": "http://www.iitb.ac.in"
    },
    {
        "name": "IIT Madras",
        "full": "Indian Institute of Technology Madras",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/IIT_Madras.jpg/640px-IIT_Madras.jpg",
        "website": "https://www.iitm.ac.in"
    },
    {
        "name": "IIT Kanpur",
        "full": "Indian Institute of Technology Kanpur",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/IIT_Kanpur_main_building.jpg/640px-IIT_Kanpur_main_building.jpg",
        "website": "https://www.iitk.ac.in"
    },
    {
        "name": "IIT Delhi",
        "full": "Indian Institute of Technology Delhi",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/IITD_Campus.jpg/640px-IITD_Campus.jpg",
        "website": "https://home.iitd.ac.in"
    },
    {
        "name": "IIT Guwahati",
        "full": "Indian Institute of Technology Guwahati",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/IITG_Academic_Complex.JPG/640px-IITG_Academic_Complex.JPG",
        "website": "https://www.iitg.ac.in"
    },
    {
        "name": "IIT Roorkee",
        "full": "Indian Institute of Technology Roorkee",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/IITRoorkee.jpg/640px-IITRoorkee.jpg",
        "website": "https://www.iitr.ac.in"
    },
    {
        "name": "IIT Ropar",
        "full": "Indian Institute of Technology Ropar",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/IIT_Ropar_gate.jpg/640px-IIT_Ropar_gate.jpg",
        "website": "https://www.iitrpr.ac.in"
    },
    {
        "name": "IIT Bhubaneswar",
        "full": "Indian Institute of Technology Bhubaneswar",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/IIT_Bhubaneswar_New_Campus.jpg/640px-IIT_Bhubaneswar_New_Campus.jpg",
        "website": "https://www.iitbbs.ac.in"
    },
    {
        "name": "IIT Gandhinagar",
        "full": "Indian Institute of Technology Gandhinagar",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/IIT_Gandhinagar_new_campus.jpg/640px-IIT_Gandhinagar_new_campus.jpg",
        "website": "https://www.iitgn.ac.in"
    },
    {
        "name": "IIT Hyderabad",
        "full": "Indian Institute of Technology Hyderabad",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/IIT_Hyderabad_campus.jpg/640px-IIT_Hyderabad_campus.jpg",
        "website": "https://www.iith.ac.in"
    },
    {
        "name": "IIT Jodhpur",
        "full": "Indian Institute of Technology Jodhpur",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/IIT_Jodhpur_permanent_campus.jpg/640px-IIT_Jodhpur_permanent_campus.jpg",
        "website": "https://www.iitj.ac.in"
    },
    {
        "name": "IIT Patna",
        "full": "Indian Institute of Technology Patna",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/IIT_Patna_Main_Gate.jpg/640px-IIT_Patna_Main_Gate.jpg",
        "website": "https://www.iitp.ac.in"
    },
    {
        "name": "IIT Indore",
        "full": "Indian Institute of Technology Indore",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/IIT_Indore_-_Main_Building.jpg/640px-IIT_Indore_-_Main_Building.jpg",
        "website": "https://www.iiti.ac.in"
    },
    {
        "name": "IIT Mandi",
        "full": "Indian Institute of Technology Mandi",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/IIT_Mandi_Kamand_Campus.jpg/640px-IIT_Mandi_Kamand_Campus.jpg",
        "website": "https://www.iitmandi.ac.in"
    },
    {
        "name": "IIT (BHU) Varanasi",
        "full": "Indian Institute of Technology (BHU) Varanasi",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Indian_Institute_of_Technology_%28BHU%29_Varanasi%2C_Main_Building.jpg/640px-Indian_Institute_of_Technology_%28BHU%29_Varanasi%2C_Main_Building.jpg",
        "website": "https://www.iitbhu.ac.in"
    },
    {
        "name": "IIT Palakkad",
        "full": "Indian Institute of Technology Palakkad",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/IITPKD.jpg/640px-IITPKD.jpg",
        "website": "https://www.iitpkd.ac.in"
    },
    {
        "name": "IIT Tirupati",
        "full": "Indian Institute of Technology Tirupati",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/IIT_Tirupati.jpg/640px-IIT_Tirupati.jpg",
        "website": "https://www.iittp.ac.in"
    },
    {
        "name": "IIT (ISM) Dhanbad",
        "full": "Indian Institute of Technology (ISM) Dhanbad",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Indian_School_of_Mines%2C_Dhanbad_Administrative_Block.jpg/640px-Indian_School_of_Mines%2C_Dhanbad_Administrative_Block.jpg",
        "website": "https://www.iitism.ac.in"
    },
    {
        "name": "IIT Bhilai",
        "full": "Indian Institute of Technology Bhilai",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/IIT_Bhilai_GEC_campus.jpg/640px-IIT_Bhilai_GEC_campus.jpg",
        "website": "https://www.iitbhilai.ac.in"
    },
    {
        "name": "IIT Goa",
        "full": "Indian Institute of Technology Goa",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/IIT_Goa_campus.jpg/640px-IIT_Goa_campus.jpg",
        "website": "https://www.iitgoa.ac.in"
    },
    {
        "name": "IIT Jammu",
        "full": "Indian Institute of Technology Jammu",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/IIT_Jammu_campus.jpg/640px-IIT_Jammu_campus.jpg",
        "website": "https://www.iitjammu.ac.in"
    },
    {
        "name": "IIT Dharwad",
        "full": "Indian Institute of Technology Dharwad",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/IIT_Dharwad_Permanent_campus.jpg/640px-IIT_Dharwad_Permanent_campus.jpg",
        "website": "https://www.iitdh.ac.in"
    }
]

nits = [
    {
        "name": "NIT Tiruchirappalli",
        "full": "National Institute of Technology, Tiruchirappalli",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/NIT_Trichy_Central_Library.jpg/640px-NIT_Trichy_Central_Library.jpg",
        "website": "https://www.nitt.edu"
    },
    {
        "name": "NIT Karnataka (Surathkal)",
        "full": "National Institute of Technology Karnataka",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/NITK_Admin_Block.jpg/640px-NITK_Admin_Block.jpg",
        "website": "https://www.nitk.ac.in"
    },
    {
        "name": "NIT Rourkela",
        "full": "National Institute of Technology Rourkela",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/NIT_ROURKELA_MAIN_BUILDING.jpg/640px-NIT_ROURKELA_MAIN_BUILDING.jpg",
        "website": "https://www.nitrkl.ac.in"
    },
    {
        "name": "NIT Warangal",
        "full": "National Institute of Technology Warangal",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/NIT_Warangal.jpg/640px-NIT_Warangal.jpg",
        "website": "https://www.nitw.ac.in"
    },
    {
        "name": "NIT Calicut",
        "full": "National Institute of Technology Calicut",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/NIT_Calicut_Administrative_Building.jpg/640px-NIT_Calicut_Administrative_Building.jpg",
        "website": "https://www.nitc.ac.in"
    },
    {
        "name": "VNIT Nagpur",
        "full": "Visvesvaraya National Institute of Technology",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/VNIT_Nagpur_Main_Building.jpg/640px-VNIT_Nagpur_Main_Building.jpg",
        "website": "https://www.vnit.ac.in"
    },
    {
        "name": "MNIT Jaipur",
        "full": "Malaviya National Institute of Technology Jaipur",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Malaviya_National_Institute_of_Technology%2C_Jaipur.jpg/640px-Malaviya_National_Institute_of_Technology%2C_Jaipur.jpg",
        "website": "https://www.mnit.ac.in"
    },
    {
        "name": "NIT Kurukshetra",
        "full": "National Institute of Technology Kurukshetra",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/NIT_Kurukshetra.jpg/640px-NIT_Kurukshetra.jpg",
        "website": "https://www.nitkkr.ac.in"
    },
    {
        "name": "NIT Silchar",
        "full": "National Institute of Technology Silchar",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/NIT_Silchar_Main_Building.jpg/640px-NIT_Silchar_Main_Building.jpg",
        "website": "https://www.nits.ac.in"
    },
    {
        "name": "NIT Durgapur",
        "full": "National Institute of Technology Durgapur",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/NIT_Durgapur.jpg/640px-NIT_Durgapur.jpg",
        "website": "https://nitdgp.ac.in"
    },
    {
        "name": "MNNIT Allahabad",
        "full": "Motilal Nehru National Institute of Technology Allahabad",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/MNNIT_Main_Building.jpg/640px-MNNIT_Main_Building.jpg",
        "website": "https://www.mnnit.ac.in"
    },
    {
        "name": "NIT Jalandhar",
        "full": "Dr. B. R. Ambedkar National Institute of Technology Jalandhar",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/NIT_Jalandhar_Main_Gate.jpg/640px-NIT_Jalandhar_Main_Gate.jpg",
        "website": "https://www.nitj.ac.in"
    },
    {
        "name": "NIT Meghalaya",
        "full": "National Institute of Technology Meghalaya",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/NIT_Meghalaya.jpg/640px-NIT_Meghalaya.jpg",
        "website": "https://www.nitm.ac.in"
    },
    {
        "name": "MANIT Bhopal",
        "full": "Maulana Azad National Institute of Technology",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/MANIT_Bhopal_Building.jpg/640px-MANIT_Bhopal_Building.jpg",
        "website": "https://www.manit.ac.in"
    },
    {
        "name": "NIT Raipur",
        "full": "National Institute of Technology Raipur",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/NIT_Raipur_Main_Gate.jpg/640px-NIT_Raipur_Main_Gate.jpg",
        "website": "https://www.nitrr.ac.in"
    },
    {
        "name": "NIT Agartala",
        "full": "National Institute of Technology Agartala",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/NIT_Agartala.jpg/640px-NIT_Agartala.jpg",
        "website": "https://www.nita.ac.in"
    },
    {
        "name": "NIT Goa",
        "full": "National Institute of Technology Goa",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/NIT_Goa_building.jpg/640px-NIT_Goa_building.jpg",
        "website": "https://www.nitgoa.ac.in"
    },
    {
        "name": "NIT Jamshedpur",
        "full": "National Institute of Technology Jamshedpur",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/NIT_JSR.jpg/640px-NIT_JSR.jpg",
        "website": "https://www.nitjsr.ac.in"
    },
    {
        "name": "NIT Patna",
        "full": "National Institute of Technology Patna",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/NIT_Patna_Main_Building.jpg/640px-NIT_Patna_Main_Building.jpg",
        "website": "https://www.nitp.ac.in"
    },
    {
        "name": "NIT Hamirpur",
        "full": "National Institute of Technology Hamirpur",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/NIT_Hamirpur.jpg/640px-NIT_Hamirpur.jpg",
        "website": "https://www.nith.ac.in"
    },
    {
        "name": "NIT Puducherry",
        "full": "National Institute of Technology Puducherry",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/NIT_Puducherry.jpg/640px-NIT_Puducherry.jpg",
        "website": "https://www.nitpy.ac.in"
    },
    {
        "name": "NIT Manipur",
        "full": "National Institute of Technology Manipur",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/NIT_Manipur.jpg/640px-NIT_Manipur.jpg",
        "website": "https://www.nitmanipur.ac.in"
    },
    {
        "name": "NIT Arunachal Pradesh",
        "full": "National Institute of Technology Arunachal Pradesh",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/NIT_Arunachal_Pradesh.jpg/640px-NIT_Arunachal_Pradesh.jpg",
        "website": "https://www.nitap.ac.in"
    },
    {
        "name": "NIT Srinagar",
        "full": "National Institute of Technology Srinagar",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/NIT_Srinagar.jpg/640px-NIT_Srinagar.jpg",
        "website": "https://www.nitsri.ac.in"
    },
    {
        "name": "NIT Delhi",
        "full": "National Institute of Technology Delhi",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/NIT_Delhi_main_building.jpg/640px-NIT_Delhi_main_building.jpg",
        "website": "https://www.nitdelhi.ac.in"
    },
    {
        "name": "NIT Mizoram",
        "full": "National Institute of Technology Mizoram",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/NIT_Mizoram.jpg/640px-NIT_Mizoram.jpg",
        "website": "https://www.nitmz.ac.in"
    },
    {
        "name": "NIT Nagaland",
        "full": "National Institute of Technology Nagaland",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/NIT_Nagaland.jpg/640px-NIT_Nagaland.jpg",
        "website": "https://www.nitnagaland.ac.in"
    },
    {
        "name": "NIT Sikkim",
        "full": "National Institute of Technology Sikkim",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/NIT_Sikkim.jpg/640px-NIT_Sikkim.jpg",
        "website": "https://www.nitsikkim.ac.in"
    },
    {
        "name": "NIT Uttarakhand",
        "full": "National Institute of Technology Uttarakhand",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/NIT_Uttarakhand.jpg/640px-NIT_Uttarakhand.jpg",
        "website": "https://www.nituk.ac.in"
    },
    {
        "name": "NIT Andhra Pradesh",
        "full": "National Institute of Technology Andhra Pradesh",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/NIT_Andhra_Pradesh.jpg/640px-NIT_Andhra_Pradesh.jpg",
        "website": "https://www.nitandhra.ac.in"
    },
    {
        "name": "IIEST Shibpur",
        "full": "Indian Institute of Engineering Science and Technology, Shibpur",
        "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/IIEST_Shibpur_Main_Building.jpg/640px-IIEST_Shibpur_Main_Building.jpg",
        "website": "https://www.iiest.ac.in"
    }
]

# GATE CSE M.Tech cutoff data (approximate safe GATE Scores for General Category)
cutoff_data = {
    "IIT Bombay": 780, "IISc Bangalore": 850, "IIT Delhi": 780, "IIT Madras": 770,
    "IIT Kanpur": 750, "IIT Kharagpur": 720, "IIT Roorkee": 720, "IIT Guwahati": 700,
    "IIT Hyderabad": 670, "IIT (BHU) Varanasi": 660, "IIT (ISM) Dhanbad": 640,
    "NIT Tiruchirappalli": 680, "NIT Karnataka (Surathkal)": 660, "NIT Rourkela": 650,
    "NIT Warangal": 650, "NIT Calicut": 640, "MNIT Jaipur": 620, "MNNIT Allahabad": 610,
    "NIT Kurukshetra": 600
}

SIDEBAR = """
      <div class="sidebar-header">
        <div class="logo">GATE A TO Z</div>
      </div>
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
            <a href="login.html" class="nav-link" style="border: 1px solid var(--accent-primary); border-radius: var(--border-radius-sm);">
                <i class="fas fa-sign-in-alt"></i> Join GAZ (Optional)
            </a>
        </li>
      </ul>
"""

def card_html(inst, category):
    cutoff = cutoff_data.get(inst['name'], 0)
    cutoff_str = f"~{cutoff}+ Score" if cutoff else "Check Website"
    badge_class = "high" if category == "iit" else "medium"
    badge_label = "IIT" if category == "iit" else "NIT"
    wiki_url = f"https://en.wikipedia.org/wiki/{urllib.parse.quote(inst['full'])}"
    search_url = f"https://google.com/search?q={urllib.parse.quote(inst['full'] + ' MTech CSE admission cutoffs 2024')}"
    official_url = inst['website']
    
    return f"""
          <div class="institute-card {category}">
            <div class="inst-img-wrapper">
                <img src="{inst['img']}" alt="{inst['name']} campus" loading="lazy"
                     onerror="this.src='https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Gatto_europeo4.jpg/320px-Gatto_europeo4.jpg'">
                <span class="inst-badge badge {badge_class}">{badge_label}</span>
                {f'<span class="cutoff-tag">GATE: {cutoff}+</span>' if cutoff else ''}
            </div>
            <div class="inst-content">
                <h4 class="inst-name">{inst['name']}</h4>
                <div class="inst-links">
                    <a href="{official_url}" target="_blank" class="inst-link">Official <i class="fas fa-external-link-alt"></i></a>
                    <a href="{wiki_url}" target="_blank" class="inst-link">Wiki <i class="fas fa-wikipedia-w"></i></a>
                    <a href="{search_url}" target="_blank" class="inst-link">Cutoffs <i class="fas fa-search"></i></a>
                </div>
            </div>
          </div>"""

def generate_html():
    cards_html = ""
    for inst in iits:
        cards_html += card_html(inst, "iit")
    for inst in nits:
        cards_html += card_html(inst, "nit")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Institute Explorer | GATE A TO Z</title>
  <meta name="description" content="Explore all 23 IITs and 31 NITs with real campus photos, GATE CSE cutoffs, and official websites.">
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
        <p class="text-secondary mb-4">
          Explore all <strong>23 IITs</strong> and <strong>31 NITs</strong> offering M.Tech through GATE. 
          Includes official websites, Wikipedia links, and approximate GATE CS score cutoffs.
        </p>
        
        <div class="filters mb-4">
            <button class="filter-btn active" onclick="filterInst('all', this)">All (54)</button>
            <button class="filter-btn" onclick="filterInst('iit', this)">IITs (23)</button>
            <button class="filter-btn" onclick="filterInst('nit', this)">NITs / Others (31)</button>
        </div>

        <div class="institute-grid" id="inst-grid">
{cards_html}
        </div>
      </section>
    </main>
  </div>
  
  <script>
    function filterInst(type, btn) {{
        const cards = document.querySelectorAll('.institute-card');
        const buttons = document.querySelectorAll('.filter-btn');
        buttons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        let count = 0;
        cards.forEach(card => {{
            const show = type === 'all' || card.classList.contains(type);
            card.style.display = show ? 'flex' : 'none';
            if (show) count++;
        }});
    }}
  </script>
  <script src="js/app.js"></script>
</body>
</html>"""

def main():
    print("Generating Institute Explorer with real Wikipedia image URLs...")
    html_content = generate_html()
    with open("institutes.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Done! institutes.html created with {len(iits)} IITs and {len(nits)} NITs")

if __name__ == "__main__":
    main()
