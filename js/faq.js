/**
 * Interactive FAQ Accordion
 * Accessible single-open accordion controller.
 */

export function initFaq() {
  window.toggleFaq = function (el) {
    const allItems = document.querySelectorAll('.faq-item');
    const isActive = el.classList.contains('active');
    allItems.forEach((item) => item.classList.remove('active'));
    if (!isActive) {
      el.classList.add('active');
    }
  };
}
