/**
 * Main Application Orchestrator
 * Bootstraps all modules on DOMContentLoaded.
 */

import { initMotion } from './motion.js';
import { initNav } from './nav.js';
import { initTabs } from './tabs.js';
import { initCalculator } from './calculator.js';
import { initFaq } from './faq.js';

function boot() {
  initMotion();
  initNav();
  initTabs();
  initCalculator();
  initFaq();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', boot);
} else {
  boot();
}
