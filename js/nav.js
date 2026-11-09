/**
 * Navigation, Mobile Drawer & Reading Progress Controller
 * Strictly adheres to modular architecture (< 100 LOC) and zero fallbacks.
 */

export function initMobileMenu() {
  const btn = document.getElementById('mobile-menu-btn');
  const drawer = document.getElementById('mobile-nav-drawer');
  if (!btn || !drawer) return;

  const toggle = (open) => {
    const isOpen = open ?? !drawer.classList.contains('is-open');
    drawer.classList.toggle('is-open', isOpen);
    drawer.classList.toggle('is-closed', !isOpen);
    btn.setAttribute('aria-expanded', String(isOpen));
    document.body.classList.toggle('overflow-hidden', isOpen);
    if (window.webcraftLenis) isOpen ? window.webcraftLenis.stop() : window.webcraftLenis.start();
  };

  btn.addEventListener('click', (e) => {
    e.stopPropagation();
    toggle();
  });

  drawer.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', (e) => {
      toggle(false);
      const hash = link.getAttribute('href');
      if (hash?.startsWith('#') && hash !== '#') {
        const target = document.querySelector(hash);
        if (target) {
          e.preventDefault();
          if (window.webcraftLenis) window.webcraftLenis.scrollTo(target, { offset: -80, duration: 1.2 });
          else target.scrollIntoView({ behavior: 'smooth' });
        }
      }
    });
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('is-open')) toggle(false);
  });
  drawer.addEventListener('click', (e) => {
    if (e.target === drawer) toggle(false);
  });
}

export function initNav() {
  const bar = document.getElementById('reading-progress');
  const nav = document.getElementById('main-nav-pill');
  const lenis = window.webcraftLenis;

  const updateScroll = (pos, max) => {
    if (bar && max > 0) bar.style.width = `${(pos / max) * 100}%`;
    if (nav) nav.classList.toggle('nav-scrolled', pos > 40);
  };

  if (lenis) {
    lenis.on('scroll', (e) => updateScroll(e.scroll, e.limit));
  } else {
    window.addEventListener('scroll', () => {
      const top = document.documentElement.scrollTop || document.body.scrollTop;
      const max = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      updateScroll(top, max);
    }, { passive: true });
  }

  // Desktop Dropdown
  const wrap = document.getElementById('nav-dropdown-wrapper');
  const dropBtn = document.getElementById('nav-dropdown-btn');
  const dropMenu = document.getElementById('nav-dropdown-menu');
  const caret = document.getElementById('nav-dropdown-caret');

  if (dropBtn && dropMenu && wrap) {
    const toggleDrop = (show) => {
      dropMenu.classList.toggle('hidden', !show);
      if (caret) caret.style.transform = show ? 'rotate(180deg)' : 'rotate(0deg)';
      dropBtn.setAttribute('aria-expanded', String(show));
    };

    dropBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      toggleDrop(dropMenu.classList.contains('hidden'));
    });
    document.addEventListener('click', (e) => {
      if (!wrap.contains(e.target)) toggleDrop(false);
    });
    wrap.querySelectorAll('.dropdown-item').forEach((item) => {
      item.addEventListener('click', () => toggleDrop(false));
    });
  }

  initMobileMenu();
}
