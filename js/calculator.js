/**
 * Interactive Pricing Calculator
 * Computes live estimates based on package tier and add-ons.
 */

export function initCalculator() {
  window.calculateTotal = function () {
    let base = 750000;
    const radios = document.getElementsByName('calc-base');
    for (const r of radios) {
      if (r.checked) {
        base = parseInt(r.value, 10);
        break;
      }
    }

    let addon = 0;
    const optDomain = document.getElementById('opt-domain');
    const optGmb = document.getElementById('opt-gmb');
    const optSpeed = document.getElementById('opt-speed');

    if (optDomain && optDomain.checked) addon += parseInt(optDomain.value, 10);
    if (optGmb && optGmb.checked) addon += parseInt(optGmb.value, 10);
    if (optSpeed && optSpeed.checked) addon += parseInt(optSpeed.value, 10);

    const total = base + addon;
    const formatted = 'Rp ' + total.toLocaleString('id-ID');
    const display = document.getElementById('calc-total-display');
    if (display) display.innerText = formatted;

    const btn = document.getElementById('calc-whatsapp-btn');
    if (btn) {
      btn.href = `https://wa.me/6281234567890?text=Halo%20WebCraft%20Studio,%20saya%20sudah%20hitung%20estimasi%20layanan%20sebesar%20${encodeURIComponent(
        formatted
      )}.`;
    }
  };
}
