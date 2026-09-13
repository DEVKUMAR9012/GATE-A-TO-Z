import urllib.parse
import os

iits = [
    "Indian Institute of Technology Kharagpur",
    "Indian Institute of Technology Bombay",
    "Indian Institute of Technology Madras",
    "Indian Institute of Technology Kanpur",
    "Indian Institute of Technology Delhi",
    "Indian Institute of Technology Guwahati",
    "Indian Institute of Technology Roorkee",
    "Indian Institute of Technology Ropar",
    "Indian Institute of Technology Bhubaneswar",
    "Indian Institute of Technology Gandhinagar",
    "Indian Institute of Technology Hyderabad",
    "Indian Institute of Technology Jodhpur",
    "Indian Institute of Technology Patna",
    "Indian Institute of Technology Indore",
    "Indian Institute of Technology Mandi",
    "Indian Institute of Technology (BHU) Varanasi",
    "Indian Institute of Technology Palakkad",
    "Indian Institute of Technology Tirupati",
    "Indian Institute of Technology (ISM) Dhanbad",
    "Indian Institute of Technology Bhilai",
    "Indian Institute of Technology Goa",
    "Indian Institute of Technology Jammu",
    "Indian Institute of Technology Dharwad"
]

nits = [
    "National Institute of Technology, Tiruchirappalli",
    "National Institute of Technology Karnataka",
    "National Institute of Technology Rourkela",
    "National Institute of Technology Warangal",
    "National Institute of Technology Calicut",
    "Visvesvaraya National Institute of Technology",
    "Malaviya National Institute of Technology Jaipur",
    "National Institute of Technology Kurukshetra",
    "National Institute of Technology Silchar",
    "National Institute of Technology Durgapur",
    "Motilal Nehru National Institute of Technology Allahabad",
    "Dr. B. R. Ambedkar National Institute of Technology Jalandhar",
    "National Institute of Technology Meghalaya",
    "Maulana Azad National Institute of Technology",
    "National Institute of Technology Raipur",
    "National Institute of Technology Agartala",
    "National Institute of Technology Goa",
    "National Institute of Technology Jamshedpur",
    "National Institute of Technology Patna",
    "National Institute of Technology Hamirpur",
    "National Institute of Technology Puducherry",
    "National Institute of Technology Manipur",
    "National Institute of Technology Arunachal Pradesh",
    "National Institute of Technology Srinagar",
    "National Institute of Technology Delhi",
    "National Institute of Technology Mizoram",
    "National Institute of Technology Nagaland",
    "National Institute of Technology Sikkim",
    "National Institute of Technology Uttarakhand",
    "National Institute of Technology Andhra Pradesh",
    "Indian Institute of Engineering Science and Technology, Shibpur" # Honorary NIT
]

def generate_html():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Institute Explorer | GATE A TO Z</title>
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
      <!-- SIDEBAR_PLACEHOLDER -->
    </nav>

    <main class="main-content">
      <section id="explorer" class="section searchable">
        <span class="section-tag">Directory</span>
        <h2 class="section-title">Institute Explorer</h2>
        <p class="text-secondary mb-4">Explore all 23 IITs and 31 NITs offering M.Tech through GATE. Due to Wikipedia's strict rate limits on fetching 54 images at once, the images below are high-quality placeholders. Click 'Wiki' for the real campus info.</p>
        
        <div class="filters mb-4">
            <button class="btn btn-primary filter-btn active" onclick="filterInst('all')">All</button>
            <button class="btn btn-secondary filter-btn" onclick="filterInst('iit')">IITs</button>
            <button class="btn btn-secondary filter-btn" onclick="filterInst('nit')">NITs</button>
        </div>

        <div class="institute-grid" id="inst-grid">
"""
    
    for i, title in enumerate(iits):
        short_name = title.replace('Indian Institute of Technology', 'IIT').replace('Varanasi', 'BHU').replace('Dhanbad', 'ISM')
        img_url = f"https://picsum.photos/seed/iit{i}/500/300"
        html += f"""
          <div class="institute-card iit">
            <div class="inst-img-wrapper">
                <img src="{img_url}" alt="{short_name}" loading="lazy">
                <span class="inst-badge badge high">IIT</span>
            </div>
            <div class="inst-content">
                <h4 class="inst-name">{short_name}</h4>
                <div class="inst-links">
                    <a href="https://en.wikipedia.org/wiki/{urllib.parse.quote(title)}" target="_blank" class="inst-link">Wiki <i class="fas fa-external-link-alt"></i></a>
                    <a href="https://google.com/search?q={urllib.parse.quote(title + " MTech cutoffs COAP")}" target="_blank" class="inst-link">Cutoffs <i class="fas fa-search"></i></a>
                </div>
            </div>
          </div>
        """

    for i, title in enumerate(nits):
        short_name = title.replace('National Institute of Technology', 'NIT').replace(',', '').strip()
        if "Visvesvaraya" in short_name: short_name = "VNIT Nagpur"
        if "Malaviya" in short_name: short_name = "MNIT Jaipur"
        if "Motilal Nehru" in short_name: short_name = "MNNIT Allahabad"
        if "Dr. B. R. Ambedkar" in short_name: short_name = "NIT Jalandhar"
        if "Maulana Azad" in short_name: short_name = "MANIT Bhopal"
        if "Indian Institute of Engineering" in short_name: short_name = "IIEST Shibpur"

        img_url = f"https://picsum.photos/seed/nit{i}/500/300"
        html += f"""
          <div class="institute-card nit">
            <div class="inst-img-wrapper">
                <img src="{img_url}" alt="{short_name}" loading="lazy">
                <span class="inst-badge badge medium">NIT</span>
            </div>
            <div class="inst-content">
                <h4 class="inst-name">{short_name}</h4>
                <div class="inst-links">
                    <a href="https://en.wikipedia.org/wiki/{urllib.parse.quote(title)}" target="_blank" class="inst-link">Wiki <i class="fas fa-external-link-alt"></i></a>
                    <a href="https://google.com/search?q={urllib.parse.quote(short_name + " MTech cutoffs CCMT")}" target="_blank" class="inst-link">Cutoffs <i class="fas fa-search"></i></a>
                </div>
            </div>
          </div>
        """

    html += """
        </div>
      </section>
    </main>
  </div>
  
  <script>
    function filterInst(type) {
        const cards = document.querySelectorAll('.institute-card');
        const buttons = document.querySelectorAll('.filter-btn');
        
        buttons.forEach(btn => {
            btn.classList.remove('btn-primary', 'active');
            btn.classList.add('btn-secondary');
        });
        event.target.classList.remove('btn-secondary');
        event.target.classList.add('btn-primary', 'active');

        cards.forEach(card => {
            if (type === 'all') {
                card.style.display = 'flex';
            } else if (card.classList.contains(type)) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    }
  </script>
  <script src="js/app.js"></script>
</body>
</html>
"""
    return html

def main():
    print("Generating HTML...")
    html_content = generate_html()
    
    with open("institutes.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Done!")

if __name__ == "__main__":
    main()
