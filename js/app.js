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
      if (sidebar && menuBtn && !sidebar.contains(e.target) && !menuBtn.contains(e.target) && sidebar.classList.contains('open')) {
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

  // Global Search Functionality
  const searchIndex = [
    { title: "Overview / Home", url: "index.html", keywords: "home, overview, welcome, start" },
    { title: "GATE Basics", url: "basics.html", keywords: "what is gate, eligibility, validity, score, marks, pattern, total" },
    { title: "GATE CS Syllabus", url: "syllabus.html", keywords: "syllabus, weightage, books, algorithms, data structures, os, dbms, networks, coa, toc, compiler, math" },
    { title: "GATE Papers", url: "papers.html", keywords: "papers, primary, secondary, da, data science, ec, electronics" },
    { title: "Opportunities", url: "opportunities.html", keywords: "opportunities, mtech, psu, phd, ms, abroad, future, career" },
    { title: "PSU Recruitment", url: "psu.html", keywords: "psu, jobs, ongc, iocl, drdo, barc, salary, government, recruitment, cutoff, rank" },
    { title: "Admissions (IIT/NIT)", url: "admissions.html", keywords: "iit, nit, iiit, ccmt, coap, mtech, ms, phd, admission, cutoff, rank" },
    { title: "Study Abroad", url: "abroad.html", keywords: "abroad, foreign, germany, singapore, nus, ntu, tum, ms, international" },
    { title: "Scholarship & Stipend", url: "scholarship.html", keywords: "scholarship, stipend, aicte, hrd, 12400, money, finance" },
    { title: "Preparation Roadmap", url: "roadmap.html", keywords: "roadmap, strategy, timeline, plan, preparation, study, months" },
    { title: "Interactive Decision Tree", url: "decision-tree.html", keywords: "decision, tree, wizard, confused, what next, top rank, low rank, qualified" },
    { title: "Other Target Exams", url: "targets.html", keywords: "targets, isro, barc, tifr, isi, bits hd, pget, state exams, iiit" },
    { title: "Resources", url: "resources.html", keywords: "resources, links, books, videos, nptel, free" },
    { title: "Login / Join GAZ", url: "login.html", keywords: "login, signup, join, register, account" }
  ];

  const searchInput = document.getElementById('global-search');
  const searchResultsContainer = document.getElementById('search-results');

  if (searchInput && searchResultsContainer) {
    searchInput.addEventListener('input', function(e) {
      const term = e.target.value.toLowerCase().trim();
      
      if (term.length < 2) {
        searchResultsContainer.style.display = 'none';
        return;
      }
      
      const results = searchIndex.filter(item => 
        item.title.toLowerCase().includes(term) || 
        item.keywords.includes(term)
      );
      
      if (results.length > 0) {
        searchResultsContainer.innerHTML = results.map(res => `
          <a href="${res.url}" class="search-result-item">
            <div class="search-result-title">${res.title}</div>
            <div class="search-result-desc">Matches: ${term}</div>
          </a>
        `).join('');
        searchResultsContainer.style.display = 'block';
      } else {
        searchResultsContainer.innerHTML = `
          <div class="search-result-item" style="color:var(--text-muted); text-align:center;">
            No results found
          </div>
        `;
        searchResultsContainer.style.display = 'block';
      }
    });

    // Hide when clicking outside
    document.addEventListener('click', function(e) {
      if (!searchInput.contains(e.target) && !searchResultsContainer.contains(e.target)) {
        searchResultsContainer.style.display = 'none';
      }
    });
    
    // Show again when clicking input if there is text
    searchInput.addEventListener('focus', function(e) {
      if (e.target.value.trim().length >= 2) {
        searchResultsContainer.style.display = 'block';
      }
    });
  }

  // Interactive Decision Tree Wizard
  const wizardData = {
    start: {
      question: "How strong is your GATE Result?",
      choices: [
        { id: 'top', title: 'Top Rank', desc: 'AIR < 500', next: 'top_goal' },
        { id: 'mid', title: 'Mid Rank', desc: 'AIR 500 - 2500', next: 'mid_goal' },
        { id: 'qual', title: 'Qualified', desc: 'AIR 2500+', next: 'qual_goal' },
        { id: 'fail', title: 'Not Qualified', desc: 'Below Cutoff', next: 'out_fail' }
      ]
    },
    top_goal: {
      question: "What is your primary goal?",
      choices: [
        { id: 't1', title: 'High Salary / Core Job', desc: 'Direct employment', next: 'out_psu' },
        { id: 't2', title: 'Premier Education', desc: 'M.Tech / Direct PhD', next: 'out_top_iit' },
        { id: 't3', title: 'Study Abroad', desc: 'Singapore / Germany', next: 'out_abroad' }
      ]
    },
    mid_goal: {
      question: "What is your preference?",
      choices: [
        { id: 'm1', title: 'Best Available M.Tech', desc: 'New IITs / Top NITs', next: 'out_mid_mtech' },
        { id: 'm2', title: 'Research Focus', desc: 'MS (Research) at Old IITs', next: 'out_ms' }
      ]
    },
    qual_goal: {
      question: "What is your next move?",
      choices: [
        { id: 'q1', title: 'Join a College', desc: 'State Gov / Private Univ', next: 'out_low_mtech' },
        { id: 'q2', title: 'Try Again', desc: 'Prepare for next year', next: 'out_drop' }
      ]
    }
  };

  const outcomeData = {
    out_psu: {
      title: "PSU Executive Recruitment",
      pros: ["Very high starting salary", "Job security (Government)", "Great perks and allowances"],
      cons: ["Fewer vacancies for CSE compared to Core", "Transferable jobs across India"],
      links: [{ text: "View PSU Details", url: "psu.html", class: "btn-primary" }]
    },
    out_top_iit: {
      title: "Top 5 IITs or IISc",
      pros: ["World-class faculty & peers", "Elite placements (FAANG/HFT)", "Excellent alumni network"],
      cons: ["Highly competitive coding rounds for MS/AI", "Rigorous academic schedule"],
      links: [{ text: "View Admission Flow", url: "admissions.html", class: "btn-primary" }]
    },
    out_abroad: {
      title: "Foreign Universities",
      pros: ["Global exposure", "High-paying international roles", "Cutting-edge research"],
      cons: ["Very expensive if no scholarship", "GATE is only accepted by a few (NUS/NTU/TUM)"],
      links: [{ text: "View Abroad Options", url: "abroad.html", class: "btn-primary" }]
    },
    out_mid_mtech: {
      title: "New IITs or Top NITs via CCMT",
      pros: ["Solid placements (10-20LPA+)", "Good brand value", "M.Tech Stipend (₹12,400)"],
      cons: ["May not match Old IIT elite status", "Location constraints for some New IITs"],
      links: [{ text: "View CCMT Flow", url: "admissions.html", class: "btn-primary" }]
    },
    out_ms: {
      title: "MS (Research) at Old IITs",
      pros: ["Study at an Old IIT with lower cutoff", "Deep dive into a specific domain (AI/Systems)"],
      cons: ["Duration is 2.5 to 3 years", "Heavy research workload"],
      links: [{ text: "View Admission Flow", url: "admissions.html", class: "btn-primary" }]
    },
    out_low_mtech: {
      title: "State Gov / Private Universities",
      pros: ["Can still get the AICTE stipend", "Time to prepare for off-campus placements"],
      cons: ["Average to poor on-campus placements", "Lower peer quality"],
      links: [{ text: "View Stipend Details", url: "scholarship.html", class: "btn-primary" }, { text: "Restart Wizard", url: "#", class: "btn-secondary restart-btn" }]
    },
    out_drop: {
      title: "Take a Drop / Reattempt",
      pros: ["Chance to dramatically improve rank", "Better understanding of syllabus"],
      cons: ["Gap year on resume", "Mental pressure and burnout risk"],
      links: [{ text: "View Roadmap", url: "roadmap.html", class: "btn-primary" }]
    },
    out_fail: {
      title: "Analyze & Pivot",
      pros: ["Early realization allows quick pivot to other exams (TIFR, ISI, State) or Placements"],
      cons: ["GATE specific opportunities closed for this year"],
      links: [{ text: "View Next Targets", url: "targets.html", class: "btn-primary" }, { text: "View Roadmap", url: "roadmap.html", class: "btn-secondary" }]
    }
  };

  const renderDecisionTree = (nodeId) => {
    const contentArea = document.getElementById('decision-content');
    if (!contentArea) return;
    
    // Clear and trigger animation restart
    contentArea.innerHTML = '';
    
    setTimeout(() => {
      let content = '';
      
      if (wizardData[nodeId]) {
        // Render Question Step
        const step = wizardData[nodeId];
        let choicesHtml = step.choices.map(c => `
          <div class="wizard-choice" onclick="renderTree('${c.next}')">
            <h4>${c.title}</h4>
            <p>${c.desc}</p>
          </div>
        `).join('');
        
        content = `
          <div class="wizard-step">
            <h3 class="wizard-question">${step.question}</h3>
            <div class="wizard-choices">${choicesHtml}</div>
            ${nodeId !== 'start' ? `<div style="text-align:center; margin-top:2rem;"><a href="#" onclick="event.preventDefault(); renderTree('start')" style="color:var(--text-muted); font-size:0.9rem;">← Start Over</a></div>` : ''}
          </div>
        `;
      } else if (outcomeData[nodeId]) {
        // Render Outcome Card
        const outcome = outcomeData[nodeId];
        
        let prosHtml = outcome.pros.map(p => `<li style="color:var(--accent-primary);"><i class="fas fa-plus-circle" style="margin-right:8px;"></i>${p}</li>`).join('');
        let consHtml = outcome.cons.map(c => `<li><i class="fas fa-minus-circle" style="margin-right:8px; color:var(--text-muted);"></i>${c}</li>`).join('');
        let linksHtml = outcome.links.map(l => `<a href="${l.url}" class="btn ${l.class}">${l.text}</a>`).join('');
        
        content = `
          <div class="wizard-step wizard-outcome">
            <div class="wizard-outcome-header text-center">
              <span class="badge high mb-2">Recommended Path</span>
              <h3 style="color:var(--text-primary); font-size:2rem; margin:0;">${outcome.title}</h3>
            </div>
            
            <div class="wizard-pros-cons">
              <div>
                <h4 class="mb-2" style="color:var(--text-primary);">Advantages</h4>
                <ul style="list-style:none; padding:0; display:flex; flex-direction:column; gap:0.5rem;">${prosHtml}</ul>
              </div>
              <div>
                <h4 class="mb-2" style="color:var(--text-primary);">Challenges</h4>
                <ul style="list-style:none; padding:0; display:flex; flex-direction:column; gap:0.5rem;">${consHtml}</ul>
              </div>
            </div>
            
            <div class="wizard-outcome-actions">
              ${linksHtml}
            </div>
            <div class="text-center mt-4">
              <a href="#" onclick="event.preventDefault(); renderTree('start')" style="color:var(--text-muted); font-size:0.9rem;">← Start Over</a>
            </div>
          </div>
        `;
      }
      
      contentArea.innerHTML = content;
      
      // Re-attach listener for restart-btn if used in outcome links
      const restartBtn = contentArea.querySelector('.restart-btn');
      if (restartBtn) {
        restartBtn.addEventListener('click', (e) => {
          e.preventDefault();
          renderTree('start');
        });
      }
    }, 50); // slight delay to allow CSS animation re-trigger
  };

  // Expose to window for inline onclicks
  window.renderTree = renderDecisionTree;
  
  // Initial render if decision tree exists on this page
  if (document.getElementById('decision-content')) {
    renderDecisionTree('start');
  }
});
