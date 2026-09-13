import os
import glob
from bs4 import BeautifulSoup

def main():
    html_files = glob.glob('*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            
        search_container = soup.find('div', class_='search-container')
        if search_container:
            # Check if results container already exists
            if not search_container.find('div', id='search-results'):
                results_div = soup.new_tag('div')
                results_div['id'] = 'search-results'
                results_div['class'] = 'search-results-container'
                search_container.append(results_div)
                
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                    
    print(f"Added search results container to {len(html_files)} files.")

if __name__ == '__main__':
    main()
