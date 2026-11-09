/**
 * Interactive Testing Suite Controller
 * Manages 3-tab testing switch and dynamic simulated WhatsApp chat.
 */

export function initTabs() {
  window.switchMockupTab = function (tabName) {
    const chatTab = document.getElementById('mockup-tab-chat');
    const seoTab = document.getElementById('mockup-tab-seo');
    const serpTab = document.getElementById('mockup-tab-serp');

    const btnChat = document.getElementById('tab-btn-chat');
    const btnSeo = document.getElementById('tab-btn-seo');
    const btnSerp = document.getElementById('tab-btn-serp');

    const allTabs = [chatTab, seoTab, serpTab];
    const allBtns = [btnChat, btnSeo, btnSerp];

    allTabs.forEach((t) => {
      if (t) t.classList.add('hidden');
    });
    allBtns.forEach((b) => {
      if (b) {
        b.className =
          'px-3.5 py-1 rounded-full text-xs font-semibold bg-forest-elevated border border-[#30322a] text-pale-fern hover:text-white transition-all';
      }
    });

    const activeBtnClass =
      'px-3.5 py-1 rounded-full text-xs font-semibold bg-sprout text-onyx-olive transition-all';

    if (tabName === 'chat' && chatTab && btnChat) {
      chatTab.classList.remove('hidden');
      btnChat.className = activeBtnClass;
    } else if (tabName === 'seo' && seoTab && btnSeo) {
      seoTab.classList.remove('hidden');
      btnSeo.className = activeBtnClass;
    } else if (tabName === 'serp' && serpTab && btnSerp) {
      serpTab.classList.remove('hidden');
      btnSerp.className = activeBtnClass;
    }
  };

  window.addChatQuestion = function (questionText, answerText) {
    const thread = document.getElementById('chat-thread');
    if (!thread) return;

    const qDiv = document.createElement('div');
    qDiv.className = 'p-3 rounded-2xl bg-bone-white border border-mist-green/70 max-w-[85%]';
    qDiv.innerHTML = `<span class="text-[9px] font-mono text-moss-shadow font-bold block mb-0.5">Pertanyaan Tambahan</span><p class="text-onyx-olive font-medium">"${questionText}"</p>`;
    thread.appendChild(qDiv);

    setTimeout(() => {
      const aDiv = document.createElement('div');
      aDiv.className =
        'p-3 rounded-2xl bg-[#f0faeb] border border-sprout/40 ml-auto max-w-[85%] text-right';
      aDiv.innerHTML = `<span class="text-[9px] font-mono text-moss-shadow font-bold block mb-0.5">Jawaban WebCraft Studio</span><p class="text-onyx-olive font-medium">"${answerText}"</p>`;
      thread.appendChild(aDiv);
    }, 350);
  };
}
