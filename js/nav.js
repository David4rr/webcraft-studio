/**
 * Navigation & Progress Bar Controller
 * Handles reading progress, floating pill morphing, and accessible dropdowns.
 */

export function initNav() {
  const bar = document.getElementById('reading-progress');
  const nav = document.getElementById('main-nav-pill');
  const lenis = window.webcraftLenis;

  const updateScrollState = (scrollPos, maxScroll) => {
    if (bar && maxScroll > 0) {
      bar.style.width = (scrollPos / maxScroll) * 100 + '%';
    }
    if (nav) {
      if (scrollPos > 40) nav.classList.add('nav-scrolled');
      else nav.classList.remove('nav-scrolled');
    }
  };

  if (lenis) {
    lenis.on('scroll', (e) => {
      updateScrollState(e.scroll, e.limit);
    });
  } else {
    window.addEventListener(
      'scroll',
      () => {
        const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        updateScrollState(winScroll, height);
      },
      { passive: true }
    );
  }

  // Interactive Navbar Dropdown
  const dropdownWrapper = document.getElementById('nav-dropdown-wrapper');
  const dropdownBtn = document.getElementById('nav-dropdown-btn');
  const dropdownMenu = document.getElementById('nav-dropdown-menu');
  const dropdownCaret = document.getElementById('nav-dropdown-caret');

  if (dropdownBtn && dropdownMenu && dropdownWrapper) {
    const toggleDropdown = (show) => {
      if (show) {
        dropdownMenu.classList.remove('hidden');
        if (dropdownCaret) dropdownCaret.style.transform = 'rotate(180deg)';
        dropdownBtn.setAttribute('aria-expanded', 'true');
      } else {
        dropdownMenu.classList.add('hidden');
        if (dropdownCaret) dropdownCaret.style.transform = 'rotate(0deg)';
        dropdownBtn.setAttribute('aria-expanded', 'false');
      }
    };

    dropdownBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const isHidden = dropdownMenu.classList.contains('hidden');
      toggleDropdown(isHidden);
    });

    document.addEventListener('click', (e) => {
      if (!dropdownWrapper.contains(e.target)) {
        toggleDropdown(false);
      }
    });

    document.querySelectorAll('.dropdown-item').forEach((item) => {
      item.addEventListener('click', () => toggleDropdown(false));
    });
  }
}
