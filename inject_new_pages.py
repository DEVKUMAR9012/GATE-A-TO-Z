"""
Update all existing HTML files to add new page links in their sidebars.
"""
import glob, os

new_links = """        <li class="nav-item"><a href="predictor.html" class="nav-link"><i class="fas fa-magic"></i> College Predictor</a></li>
        <li class="nav-item"><a href="calculator.html" class="nav-link"><i class="fas fa-calculator"></i> Score Calculator</a></li>
        <li class="nav-item"><a href="tracker.html" class="nav-link"><i class="fas fa-tasks"></i> Progress Tracker</a></li>
        <li class="nav-item"><a href="stats.html" class="nav-link"><i class="fas fa-chart-bar"></i> GATE Stats</a></li>
        <li class="nav-item"><a href="pyq.html" class="nav-link"><i class="fas fa-question-circle"></i> PYQ Explorer</a></li>
        <li class="nav-item"><a href="books.html" class="nav-link"><i class="fas fa-book-open"></i> Book Guide</a></li>
        <li class="nav-item"><a href="toppers.html" class="nav-link"><i class="fas fa-trophy"></i> Topper Stories</a></li>
        <li class="nav-item"><a href="faq.html" class="nav-link"><i class="fas fa-question"></i> FAQ</a></li>
"""

skip = {"predictor.html","calculator.html","tracker.html","stats.html","pyq.html","books.html","toppers.html","faq.html","institutes_template.html"}

for filepath in glob.glob("*.html"):
    if filepath in skip: continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    # Only add if not already present
    if "predictor.html" in content:
        print(f"Already updated: {filepath}")
        continue
    # Inject before the Institute Explorer link
    if 'href="institutes.html"' in content:
        content = content.replace('<li class="nav-item"><a href="institutes.html"', new_links + '        <li class="nav-item"><a href="institutes.html"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {filepath}")
    else:
        print(f"No injection point found: {filepath}")
