/**
 * Interactive FAQ Accordion
 * Accessible single-open accordion controller.
 */

export function initFaq() {
  window.toggleFaq = function (el) {
    const allItems = document.querySelectorAll('.faq-item');
    const isActive = el.classList.contains('active');
    allItems.forEach((item) => {
      item.classList.remove('active');
      item.setAttribute('aria-expanded', 'false');
    });
    if (!isActive) {
      el.classList.add('active');
      el.setAttribute('aria-expanded', 'true');
    }
  };

  document.querySelectorAll('.faq-item').forEach((item) => {
    item.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        window.toggleFaq(item);
      }
    });
  });
}
