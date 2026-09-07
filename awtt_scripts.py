JS = """
// Centralized image mapping configuration
const AWTT_IMAGES = {
  logo: "https://iili.io/n2S5CCl.png",
  hero: "https://iili.io/nH2hwTQ.jpg",
  baku: "https://iili.io/nH2h86F.jpg",
  bangkok: "https://iili.io/nH2hQnI.jpg",
  dubai: "https://iili.io/nH2hvG1.webp",
  hunza: "https://iili.io/nH2hwTQ.jpg",
  islamabad: "https://iili.io/n9OS5pn.jpg",
  karachi: "https://iili.io/nHd5O5g.jpg",
  lahore: "https://iili.io/nHdBog4.jpg",
  naranKaghan: "https://iili.io/nH2hgaa.jpg",
  skardu: "https://iili.io/nH2h4yv.jpg",
  swatKalamMahodand: "https://iili.io/nHJr0js.jpg",
  turkey: "https://iili.io/nH2hsZN.webp",
  malaysia: "https://iili.io/nH32FWb.jpg",
  singapore: "https://iili.io/nH37Ujs.jpg",
  maldives: "https://iili.io/nH3XDAv.png",
  madinah: "https://iili.io/nH3bYVp.webp",
  makkah: "https://iili.io/nH3m8EN.jpg"
};

// Safe image error handler
function handleImageError(img, destinationName) {
  if (!img) return;
  img.onerror = null;
  const parent = img.parentElement;
  if (parent) {
    parent.innerHTML = `
      <div class="awtt-img-fallback">
        <div class="awtt-img-fallback-title">${destinationName || 'Destination'}</div>
        <div class="awtt-img-fallback-sub">Air Waves Travel &amp; Tours</div>
      </div>
    `;
  }
}

// Logo image error fallback
function handleLogoError(img) {
  if (!img) return;
  img.onerror = null;
  img.style.display = 'none';
  const parent = img.parentElement;
  if (parent && !parent.querySelector('.awtt-fallback-logo-svg')) {
    const svg = document.createElement('div');
    svg.className = 'awtt-fallback-logo-svg';
    svg.innerHTML = `
      <div style="font-weight:700;font-size:1.1rem;color:#0a2540;line-height:1.2;">
        AIR WAVES
        <span style="display:block;font-size:0.7rem;color:#0284c7;letter-spacing:0.08em;">TRAVEL &amp; TOURS</span>
      </div>
    `;
    parent.insertBefore(svg, parent.firstChild);
  }
}

// Show Toast Message
function showToast(message) {
  const toast = document.getElementById('awtt-toast');
  const toastText = document.getElementById('awtt-toast-msg');
  if (toast && toastText) {
    toastText.textContent = message;
    toast.classList.add('awtt-toast-show');
    setTimeout(() => {
      toast.classList.remove('awtt-toast-show');
    }, 4500);
  }
}

// Single-file hash routing
function initRouting() {
  const views = document.querySelectorAll('.awtt-view');
  const navLinks = document.querySelectorAll('.awtt-nav-link, .awtt-drawer-link');

  function renderRoute() {
    let hash = window.location.hash.replace('#', '').trim();
    if (!hash) hash = 'home';

    const validViews = ['home', 'about', 'destinations', 'flights', 'hotels', 'packages', 'booking', 'blog', 'privacy', 'terms'];
    if (!validViews.includes(hash)) {
      hash = 'home';
    }

    views.forEach(v => {
      v.classList.remove('awtt-view-active');
    });

    const activeView = document.getElementById('awtt-view-' + hash);
    if (activeView) {
      activeView.classList.add('awtt-view-active');
    }

    navLinks.forEach(link => {
      const linkHash = link.getAttribute('href');
      if (linkHash === '#' + hash || (hash === 'home' && (linkHash === '#' || linkHash === '#home'))) {
        link.classList.add('awtt-active');
      } else {
        link.classList.remove('awtt-active');
      }
    });

    closeMobileMenu();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  window.addEventListener('hashchange', renderRoute);
  renderRoute();
}

// Mobile drawer controls
function initMobileMenu() {
  const hamburger = document.getElementById('awtt-hamburger-btn');
  const closeBtn = document.getElementById('awtt-drawer-close-btn');
  const drawer = document.getElementById('awtt-mobile-drawer');
  const overlay = document.getElementById('awtt-drawer-overlay');

  if (hamburger) {
    hamburger.addEventListener('click', () => {
      if (drawer) drawer.classList.add('awtt-open');
      if (overlay) overlay.classList.add('awtt-open');
      document.body.style.overflow = 'hidden';
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener('click', closeMobileMenu);
  }

  if (overlay) {
    overlay.addEventListener('click', closeMobileMenu);
  }
}

function closeMobileMenu() {
  const drawer = document.getElementById('awtt-mobile-drawer');
  const overlay = document.getElementById('awtt-drawer-overlay');
  if (drawer) drawer.classList.remove('awtt-open');
  if (overlay) overlay.classList.remove('awtt-open');
  document.body.style.overflow = '';
}

// FAQ Accordion
function initFAQ() {
  const triggers = document.querySelectorAll('.awtt-faq-trigger');
  triggers.forEach(trigger => {
    trigger.addEventListener('click', () => {
      const item = trigger.closest('.awtt-faq-item');
      if (!item) return;
      const isOpen = item.classList.contains('awtt-faq-open');
      document.querySelectorAll('.awtt-faq-item').forEach(el => {
        el.classList.remove('awtt-faq-open');
        const btn = el.querySelector('.awtt-faq-trigger');
        if (btn) btn.setAttribute('aria-expanded', 'false');
      });
      if (!isOpen) {
        item.classList.add('awtt-faq-open');
        trigger.setAttribute('aria-expanded', 'true');
      }
    });
  });
}

// Search widget tab switching
function initSearchWidget() {
  const tabs = document.querySelectorAll('.awtt-search-tab-btn');
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const target = tab.getAttribute('data-tab');
      tabs.forEach(t => t.classList.remove('awtt-tab-active'));
      tab.classList.add('awtt-tab-active');

      document.querySelectorAll('.awtt-search-tab-content').forEach(c => {
        c.classList.remove('awtt-tab-content-active');
      });
      const targetContent = document.getElementById('awtt-tab-' + target);
      if (targetContent) {
        targetContent.classList.add('awtt-tab-content-active');
      }
    });
  });
}

// Destination Category Filters
function initDestinationFilters() {
  const filterBtns = document.querySelectorAll('.awtt-filter-btn');
  const cards = document.querySelectorAll('.awtt-dest-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const filter = btn.getAttribute('data-filter');
      filterBtns.forEach(b => b.classList.remove('awtt-filter-active'));
      btn.classList.add('awtt-filter-active');

      cards.forEach(card => {
        const cat = card.getAttribute('data-category');
        if (filter === 'all' || cat === filter) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

// Booking and Inquiry Form Handlers
function initForms() {
  const bookingForm = document.getElementById('awtt-booking-form');
  if (bookingForm) {
    bookingForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('awtt-book-name').value;
      const email = document.getElementById('awtt-book-email').value;
      const phone = document.getElementById('awtt-book-phone').value;
      const destination = document.getElementById('awtt-book-dest').value;

      if (!name || !phone || !destination) {
        showToast('Please fill in your name, phone number, and destination.');
        return;
      }

      showToast('Thank you, ' + name + '! Your inquiry has been received. Our team will contact you shortly.');
      bookingForm.reset();
    });
  }

  // Pre-fill destination when user clicks "Book This Trip" or "Inquire"
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('[data-book-destination]');
    if (btn) {
      const dest = btn.getAttribute('data-book-destination');
      const destInput = document.getElementById('awtt-book-dest');
      if (destInput && dest) {
        destInput.value = dest;
      }
      window.location.hash = '#booking';
    }
  });

  // Flight search submit handler
  const flightSearchForm = document.getElementById('awtt-flight-search-form');
  if (flightSearchForm) {
    flightSearchForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const from = document.getElementById('awtt-flight-from')?.value || '';
      const to = document.getElementById('awtt-flight-to')?.value || '';
      if (to) {
        const destInput = document.getElementById('awtt-book-dest');
        if (destInput) destInput.value = 'Flight: ' + from + ' to ' + to;
      }
      window.location.hash = '#booking';
      showToast('Please complete your contact details below to receive live airline fares.');
    });
  }

  // Hotel search submit handler
  const hotelSearchForm = document.getElementById('awtt-hotel-search-form');
  if (hotelSearchForm) {
    hotelSearchForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const dest = document.getElementById('awtt-hotel-dest')?.value || '';
      if (dest) {
        const destInput = document.getElementById('awtt-book-dest');
        if (destInput) destInput.value = 'Hotel Booking: ' + dest;
      }
      window.location.hash = '#booking';
      showToast('Please submit your contact details below to receive hotel availability and rates.');
    });
  }
}

// Article modal reader
function openArticleModal(title, category, content) {
  const modal = document.getElementById('awtt-article-modal');
  if (!modal) return;
  document.getElementById('awtt-modal-title').textContent = title;
  document.getElementById('awtt-modal-cat').textContent = category;
  document.getElementById('awtt-modal-body').innerHTML = content;
  modal.style.display = 'flex';
  document.body.style.overflow = 'hidden';
}

function closeArticleModal() {
  const modal = document.getElementById('awtt-article-modal');
  if (!modal) return;
  modal.style.display = 'none';
  document.body.style.overflow = '';
}

// Master initialization
document.addEventListener('DOMContentLoaded', () => {
  initRouting();
  initMobileMenu();
  initFAQ();
  initSearchWidget();
  initDestinationFilters();
  initForms();
});
"""
