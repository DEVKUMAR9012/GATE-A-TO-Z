import glob

new_link = '<li class="nav-item"><a href="institutes.html" class="nav-link"><i class="fas fa-landmark"></i> Institute Explorer</a></li>\n        <li class="nav-item mt-4">'

for filepath in glob.glob("*.html"):
    if filepath == "institutes_template.html": continue
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "institutes.html" not in content and '<li class="nav-item mt-4">' in content:
        content = content.replace('<li class="nav-item mt-4">', new_link)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filepath}")
