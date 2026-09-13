import os
from bs4 import BeautifulSoup

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Define mapping from old IDs to new filenames
    sections_map = {
        'home': 'index.html',
        'basics': 'basics.html',
        'papers': 'papers.html',
        'cs-syllabus': 'syllabus.html',
        'opportunities': 'opportunities.html',
        'admissions': 'admissions.html',
        'psu': 'psu.html',
        'scholarship': 'scholarship.html',
        'foreign': 'abroad.html',
        'roadmap': 'roadmap.html',
        'decision-tree': 'decision-tree.html',
        'targets': 'targets.html',
        'resources': 'resources.html'
    }
    
    # 1. Update the sidebar links in the global soup template
    nav_links = soup.find_all('a', class_='nav-link')
    for link in nav_links:
        href = link.get('href', '')
        if href.startswith('#'):
            sec_id = href[1:]
            if sec_id in sections_map:
                link['href'] = sections_map[sec_id]
                
    # Also update any internal anchors (like 'Explore GATE' button) to point to correct pages
    all_links = soup.find_all('a')
    for link in all_links:
        href = link.get('href', '')
        if href.startswith('#') and 'nav-link' not in link.get('class', []):
            sec_id = href[1:]
            if sec_id in sections_map:
                link['href'] = sections_map[sec_id]
                
    # 2. Extract all sections
    main_content = soup.find('main', class_='main-content')
    all_sections = main_content.find_all(['section'], recursive=False)
    
    # Clone the soup to act as a template where main_content is empty
    template_soup = BeautifulSoup(str(soup), 'html.parser')
    template_main = template_soup.find('main', class_='main-content')
    template_main.clear()
    
    # Write each file
    for section in all_sections:
        sec_id = section.get('id')
        if not sec_id or sec_id not in sections_map:
            continue
            
        filename = sections_map[sec_id]
        
        # Make a copy of the template
        page_soup = BeautifulSoup(str(template_soup), 'html.parser')
        page_main = page_soup.find('main', class_='main-content')
        
        # Append this specific section
        page_main.append(BeautifulSoup(str(section), 'html.parser'))
        
        # Update active nav link for this page
        for link in page_soup.find_all('a', class_='nav-link'):
            if link.get('href') == filename:
                link['class'] = link.get('class', []) + ['active']
            else:
                if 'active' in link.get('class', []):
                    link['class'].remove('active')
                    
        # Write to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(page_soup))
            
    print("Files split successfully.")

if __name__ == '__main__':
    main()
