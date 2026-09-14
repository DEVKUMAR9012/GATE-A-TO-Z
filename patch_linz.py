import shutil

# Copy Linz cover
shutil.copy('img/books/linz_0763772062.jpg', 'img/books/0763774952.jpg')
print('Copied Linz cover')

# Patch books.html - find the Linz fallback section and add img tag
with open('books.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find where Linz card has no img (fallback only) and inject the img
old = '<span>Peter Linz</span>'
# Check if already has img
if 'img/books/0763774952.jpg' in content:
    print('Already patched')
else:
    # The Linz card fallback div is preceded by an empty book-cover-wrap
    # We just replace the fallback display:flex for Peter Linz
    content = content.replace(
        'alt="An Introduction to Formal Languages and Automata cover"',
        'alt="An Introduction to Formal Languages and Automata cover"'
    )
    # Simpler approach: just replace the specific marker
    marker = 'An Introduction to Formal Languages and Automata</h3>'
    if marker in content:
        # Find the book-cover-wrap before this marker
        idx = content.find(marker)
        # Search backwards for the nearest book-cover-wrap
        wrap_start = content.rfind('<div class="book-cover-wrap">', 0, idx)
        wrap_end = content.find('</div>', wrap_start) + 6  # close first inner div
        wrap_end = content.find('</div>', wrap_end) + 6    # close book-cover-wrap
        old_wrap = content[wrap_start:wrap_end]
        new_wrap = '''<div class="book-cover-wrap">
            <img src="img/books/0763774952.jpg" alt="Peter Linz book cover" loading="lazy" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">
            <div class="book-cover-fallback" style="display:none">
              <i class="fas fa-book"></i>
              <span>Peter Linz</span>
            </div>
          </div>'''
        content = content[:wrap_start] + new_wrap + content[wrap_end:]
        print('Patched Linz card in books.html')

with open('books.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
