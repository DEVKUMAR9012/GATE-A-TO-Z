document.addEventListener('DOMContentLoaded', () => {
  // Mobile menu toggle
  const menuBtn = document.getElementById('menu-btn');
  const sidebar = document.getElementById('sidebar');
  
  if (menuBtn && sidebar) {
    menuBtn.addEventListener('click', () => {
      sidebar.classList.toggle('open');
    });
  }

  // Close sidebar on click outside on mobile
  document.addEventListener('click', (e) => {
    if (window.innerWidth <= 1024) {
      if (!sidebar.contains(e.target) && !menuBtn.contains(e.target) && sidebar.classList.contains('open')) {
        sidebar.classList.remove('open');
      }
    }
  });

  // Accordion functionality
  const accordions = document.querySelectorAll('.accordion-header');
  accordions.forEach(acc => {
    acc.addEventListener('click', function() {
      const item = this.parentElement;
      item.classList.toggle('active');
    });
  });

  // Active navigation link highlighting on scroll
  const sections = document.querySelectorAll('.section, .hero');
  const navLinks = document.querySelectorAll('.nav-link');

  window.addEventListener('scroll', () => {
    let current = '';
    const scrollY = window.pageYOffset;

    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.clientHeight;
      if (scrollY >= (sectionTop - 150)) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  });

  // Search functionality
  const searchInput = document.getElementById('global-search');
  if (searchInput) {
    searchInput.addEventListener('input', function(e) {
      const term = e.target.value.toLowerCase();
      // Simple search implementation hiding/showing sections or cards based on term
      // A more robust implementation would require a dedicated search index array.
      
      const searchableElements = document.querySelectorAll('.searchable');
      searchableElements.forEach(el => {
        const text = el.innerText.toLowerCase();
        if (text.includes(term)) {
          el.style.display = '';
        } else {
          el.style.display = 'none';
        }
      });
    });
  }

  // Interactive Decision Tree
  const renderDecisionTree = (nodeId) => {
    // Simple mock logic for demonstration
    const contentArea = document.getElementById('decision-content');
    if (!contentArea) return;
    
    let content = '';
    
    if (nodeId === 'start') {
      content = `
        <div class="decision-node" onclick="renderTree('strong')">Very Strong Score (AIR 1-300)</div>
        <div class="decision-node" onclick="renderTree('good')">Good Score (AIR 300-1500)</div>
        <div class="decision-node" onclick="renderTree('moderate')">Moderate Score (AIR 1500-4000)</div>
      `;
    } else if (nodeId === 'strong') {
      content = `
        <h4 class="mb-2 text-cyan">Top Choice</h4>
        <p>Direct M.Tech in CSE/AI at Top 5 IITs or IISc.</p>
        <p>PSU Executive Recruitment (ONGC, IOCL) if eligible.</p>
        <button class="btn btn-secondary mt-4" onclick="renderTree('start')">Back</button>
      `;
    } else if (nodeId === 'good') {
      content = `
        <h4 class="mb-2 text-blue">Top Choice</h4>
        <p>M.Tech at New IITs or Top NITs (Trichy, Surathkal, Warangal).</p>
        <p>MS by Research at Top IITs.</p>
        <button class="btn btn-secondary mt-4" onclick="renderTree('start')">Back</button>
      `;
    } else if (nodeId === 'moderate') {
      content = `
        <h4 class="mb-2 text-muted">Top Choice</h4>
        <p>M.Tech at Mid-tier NITs or IIITs via CCMT.</p>
        <p>Consider reattempt or focus on B.Tech placements.</p>
        <button class="btn btn-secondary mt-4" onclick="renderTree('start')">Back</button>
      `;
    }
    
    contentArea.innerHTML = `<div style="display:flex; flex-direction:column; gap:1rem; align-items:center;">${content}</div>`;
  };

  // Expose to window for inline onclicks
  window.renderTree = renderDecisionTree;
  
  // Initial render
  renderDecisionTree('start');
});
