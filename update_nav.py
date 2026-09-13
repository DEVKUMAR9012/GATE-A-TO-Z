import os
import glob
from bs4 import BeautifulSoup

def main():
    # Base structure we want
    login_li = '''
        <li class="nav-item mt-4">
            <a href="login.html" class="nav-link" style="border: 1px solid var(--accent-primary); border-radius: var(--border-radius-sm);">
                <i class="fas fa-sign-in-alt"></i> Join GAZ (Optional)
            </a>
        </li>
    '''
    
    # 1. Grab the current nav list from index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    nav_list = soup.find('ul', class_='nav-list')
    if not nav_list:
        print("Could not find nav-list in index.html")
        return
        
    # Check if login is already there
    has_login = False
    for link in nav_list.find_all('a'):
        if link.get('href') == 'login.html':
            has_login = True
            break
            
    if not has_login:
        nav_list.append(BeautifulSoup(login_li, 'html.parser'))
        
    base_nav_html = str(nav_list)
    
    # 2. Iterate all HTML files and replace nav-list
    html_files = glob.glob('*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            file_soup = BeautifulSoup(f, 'html.parser')
            
        target_nav = file_soup.find('ul', class_='nav-list')
        if target_nav:
            # Replace target_nav with the base nav
            new_nav = BeautifulSoup(base_nav_html, 'html.parser').find('ul')
            
            # Correctly handle active class
            for link in new_nav.find_all('a', class_='nav-link'):
                if link.get('href') == file:
                    if 'active' not in link.get('class', []):
                        link['class'] = link.get('class', []) + ['active']
                else:
                    if 'active' in link.get('class', []):
                        link['class'].remove('active')
            
            target_nav.replace_with(new_nav)
            
            # Write back
            with open(file, 'w', encoding='utf-8') as f:
                f.write(str(file_soup))
                
    print(f"Updated navigation in {len(html_files)} files.")

if __name__ == '__main__':
    main()
