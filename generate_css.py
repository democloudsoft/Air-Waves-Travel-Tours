# -*- coding: utf-8 -*-

CSS = """
/* AIR WAVES TRAVEL & TOURS - CORE STYLESHEET */
:root {
  --awtt-primary: #0a2540;
  --awtt-primary-dark: #051424;
  --awtt-primary-light: #153c65;
  --awtt-accent: #0284c7;
  --awtt-accent-hover: #0369a1;
  --awtt-accent-light: #e0f2fe;
  --awtt-amber: #d97706;
  --awtt-text-main: #1e293b;
  --awtt-text-muted: #64748b;
  --awtt-text-light: #94a3b8;
  --awtt-bg-page: #f8fafc;
  --awtt-bg-subtle: #f1f5f9;
  --awtt-bg-card: #ffffff;
  --awtt-border: #e2e8f0;
  --awtt-border-focus: #0284c7;
  --awtt-radius: 8px;
  --awtt-radius-lg: 12px;
  --awtt-shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.06);
  --awtt-shadow-md: 0 4px 14px rgba(10, 37, 64, 0.08);
  --awtt-shadow-lg: 0 10px 28px rgba(10, 37, 64, 0.12);
  --awtt-transition: all 0.25s ease;
  --awtt-font: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  font-family: var(--awtt-font);
  font-size: 16px;
  line-height: 1.6;
  color: var(--awtt-text-main);
  background-color: var(--awtt-bg-page);
  -webkit-text-size-adjust: 100%;
}

body {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  color: var(--awtt-text-main);
  background-color: var(--awtt-bg-page);
  overflow-x: hidden;
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}

a {
  color: inherit;
  text-decoration: none;
  transition: var(--awtt-transition);
}

button, input, select, textarea {
  font-family: inherit;
  font-size: inherit;
}

button {
  cursor: pointer;
  border: none;
  background: none;
}

ul, ol {
  list-style: none;
}

.awtt-container {
  width: 100%;
  max-width: 1240px;
  margin-left: auto;
  margin-right: auto;
  padding-left: 20px;
  padding-right: 20px;
}

/* TOP CONTACT BAR */
.awtt-topbar {
  background-color: var(--awtt-primary-dark);
  color: #cbd5e1;
  font-size: 0.84rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  padding: 8px 0;
}

.awtt-topbar-inner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
}

.awtt-topbar-contact {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 20px;
}

.awtt-topbar-item {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  color: #e2e8f0;
}

.awtt-topbar-item svg {
  width: 14px;
  height: 14px;
  color: var(--awtt-accent);
}

.awtt-topbar-item a:hover {
  color: #ffffff;
  text-decoration: underline;
}

.awtt-topbar-social {
  display: flex;
  align-items: center;
  gap: 12px;
}

.awtt-social-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  color: #ffffff;
  transition: var(--awtt-transition);
}

.awtt-social-link:hover {
  background: var(--awtt-accent);
  color: #ffffff;
  transform: translateY(-1px);
}

.awtt-social-link svg {
  width: 14px;
  height: 14px;
}

/* HEADER & NAVBAR */
.awtt-header {
  position: sticky;
  top: 0;
  z-index: 1000;
  background-color: #ffffff;
  box-shadow: var(--awtt-shadow-sm);
  border-bottom: 1px solid var(--awtt-border);
}

.awtt-navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 0;
}

.awtt-brand {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
}

.awtt-logo-img {
  height: 52px;
  width: auto;
  max-width: 190px;
  object-fit: contain;
}

.awtt-brand-text {
  display: flex;
  flex-direction: column;
}

.awtt-brand-title {
  font-size: 1.18rem;
  font-weight: 700;
  letter-spacing: -0.01em;
  color: var(--awtt-primary);
  line-height: 1.2;
}

.awtt-brand-subtitle {
  font-size: 0.74rem;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--awtt-accent);
}

.awtt-nav-menu {
  display: flex;
  align-items: center;
  gap: 4px;
}

.awtt-nav-link {
  padding: 8px 12px;
  font-size: 0.92rem;
  font-weight: 500;
  color: var(--awtt-text-main);
  border-radius: var(--awtt-radius);
  transition: var(--awtt-transition);
}

.awtt-nav-link:hover {
  color: var(--awtt-accent);
  background-color: var(--awtt-bg-subtle);
}

.awtt-nav-link.awtt-active {
  color: var(--awtt-accent);
  font-weight: 600;
  background-color: var(--awtt-accent-light);
}

.awtt-header-actions {
  display: flex;
  align-items: center;
  gap: 12px;
}

.awtt-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 22px;
  font-size: 0.92rem;
  font-weight: 600;
  border-radius: var(--awtt-radius);
  transition: var(--awtt-transition);
  white-space: nowrap;
  text-decoration: none;
  cursor: pointer;
}

.awtt-btn-primary {
  background-color: var(--awtt-accent);
  color: #ffffff;
  box-shadow: 0 2px 8px rgba(2, 132, 199, 0.25);
}

.awtt-btn-primary:hover {
  background-color: var(--awtt-accent-hover);
  color: #ffffff;
  box-shadow: 0 4px 12px rgba(2, 132, 199, 0.35);
  transform: translateY(-1px);
}

.awtt-btn-secondary {
  background-color: #ffffff;
  color: var(--awtt-primary);
  border: 1px solid var(--awtt-border);
}

.awtt-btn-secondary:hover {
  border-color: var(--awtt-accent);
  color: var(--awtt-accent);
  background-color: var(--awtt-bg-subtle);
}

.awtt-btn-dark {
  background-color: var(--awtt-primary);
  color: #ffffff;
}

.awtt-btn-dark:hover {
  background-color: var(--awtt-primary-light);
  color: #ffffff;
}

.awtt-btn-sm {
  padding: 7px 14px;
  font-size: 0.85rem;
}

.awtt-btn-lg {
  padding: 13px 28px;
  font-size: 1rem;
}

/* MOBILE NAV TOGGLE */
.awtt-hamburger {
  display: none;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 40px;
  height: 40px;
  border-radius: var(--awtt-radius);
  border: 1px solid var(--awtt-border);
  color: var(--awtt-primary);
}

.awtt-hamburger svg {
  width: 22px;
  height: 22px;
}

/* MOBILE DRAWER */
.awtt-mobile-drawer {
  position: fixed;
  top: 0;
  right: -100%;
  width: 82%;
  max-width: 320px;
  height: 100vh;
  background-color: #ffffff;
  z-index: 2000;
  box-shadow: -4px 0 20px rgba(0, 0, 0, 0.15);
  display: flex;
  flex-direction: column;
  transition: right 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  padding: 20px;
  overflow-y: auto;
}

.awtt-mobile-drawer.awtt-open {
  right: 0;
}

.awtt-drawer-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--awtt-border);
  margin-bottom: 20px;
}

.awtt-drawer-close {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background-color: var(--awtt-bg-subtle);
  color: var(--awtt-text-main);
}

.awtt-drawer-links {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.awtt-drawer-link {
  padding: 12px 14px;
  font-size: 0.98rem;
  font-weight: 500;
  color: var(--awtt-text-main);
  border-radius: var(--awtt-radius);
  transition: var(--awtt-transition);
}

.awtt-drawer-link:hover, .awtt-drawer-link.awtt-active {
  background-color: var(--awtt-accent-light);
  color: var(--awtt-accent);
}

.awtt-drawer-contact {
  margin-top: auto;
  padding-top: 24px;
  border-top: 1px solid var(--awtt-border);
  display: flex;
  flex-direction: column;
  gap: 12px;
  font-size: 0.88rem;
}

.awtt-drawer-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(10, 37, 64, 0.5);
  z-index: 1999;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
}

.awtt-drawer-overlay.awtt-open {
  opacity: 1;
  pointer-events: auto;
}

/* VIEW ROUTING SECTIONS */
.awtt-view {
  display: none;
  animation: awttFadeIn 0.3s ease;
}

.awtt-view.awtt-view-active {
  display: block;
}

@keyframes awttFadeIn {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

/* HERO SECTION */
.awtt-hero {
  position: relative;
  background-color: var(--awtt-primary-dark);
  color: #ffffff;
  padding: 85px 0 95px;
  overflow: hidden;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.awtt-hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(6, 24, 43, 0.92) 0%, rgba(10, 37, 64, 0.85) 60%, rgba(2, 132, 199, 0.55) 100%);
  z-index: 1;
}

.awtt-hero-content {
  position: relative;
  z-index: 2;
  max-width: 820px;
}

.awtt-hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 0.82rem;
  font-weight: 500;
  color: #e0f2fe;
  margin-bottom: 20px;
}

.awtt-hero-badge svg {
  width: 14px;
  height: 14px;
  color: #38bdf8;
}

.awtt-hero h1 {
  font-size: 2.85rem;
  font-weight: 700;
  line-height: 1.22;
  color: #ffffff;
  margin-bottom: 20px;
  letter-spacing: -0.02em;
}

.awtt-hero p {
  font-size: 1.12rem;
  line-height: 1.65;
  color: #e2e8f0;
  margin-bottom: 34px;
  max-width: 680px;
}

.awtt-hero-buttons {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 14px;
}

/* QUICK SEARCH WIDGET */
.awtt-search-widget-wrap {
  margin-top: -45px;
  position: relative;
  z-index: 10;
}

.awtt-search-widget {
  background: #ffffff;
  border-radius: var(--awtt-radius-lg);
  box-shadow: var(--awtt-shadow-lg);
  border: 1px solid var(--awtt-border);
  padding: 24px;
}

.awtt-search-tabs {
  display: flex;
  gap: 8px;
  margin-bottom: 20px;
  border-bottom: 1px solid var(--awtt-border);
  padding-bottom: 12px;
  flex-wrap: wrap;
}

.awtt-search-tab-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 9px 18px;
  border-radius: var(--awtt-radius);
  font-size: 0.92rem;
  font-weight: 600;
  color: var(--awtt-text-muted);
  background-color: var(--awtt-bg-subtle);
  transition: var(--awtt-transition);
}

.awtt-search-tab-btn svg {
  width: 16px;
  height: 16px;
}

.awtt-search-tab-btn.awtt-tab-active {
  background-color: var(--awtt-primary);
  color: #ffffff;
}

.awtt-search-tab-content {
  display: none;
}

.awtt-search-tab-content.awtt-tab-content-active {
  display: block;
}

.awtt-form-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
  gap: 14px;
  align-items: flex-end;
}

.awtt-form-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.awtt-form-label {
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--awtt-text-main);
  display: flex;
  align-items: center;
  gap: 6px;
}

.awtt-form-label svg {
  width: 14px;
  height: 14px;
  color: var(--awtt-accent);
}

.awtt-input, .awtt-select, .awtt-textarea {
  width: 100%;
  padding: 10px 14px;
  border: 1px solid var(--awtt-border);
  border-radius: var(--awtt-radius);
  background-color: #ffffff;
  color: var(--awtt-text-main);
  font-size: 0.92rem;
  outline: none;
  transition: var(--awtt-transition);
}

.awtt-input:focus, .awtt-select:focus, .awtt-textarea:focus {
  border-color: var(--awtt-accent);
  box-shadow: 0 0 0 3px rgba(2, 132, 199, 0.15);
}

/* SECTION TITLES & LAYOUTS */
.awtt-section {
  padding: 72px 0;
}

.awtt-section-alt {
  background-color: var(--awtt-bg-subtle);
}

.awtt-section-header {
  text-align: center;
  max-width: 680px;
  margin: 0 auto 48px;
}

.awtt-section-header h2 {
  font-size: 2.1rem;
  font-weight: 700;
  color: var(--awtt-primary);
  margin-bottom: 12px;
  letter-spacing: -0.01em;
}

.awtt-section-header p {
  font-size: 1rem;
  color: var(--awtt-text-muted);
}

/* SERVICES GRID */
.awtt-services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}

.awtt-service-card {
  background: #ffffff;
  border: 1px solid var(--awtt-border);
  border-radius: var(--awtt-radius-lg);
  padding: 30px 24px;
  box-shadow: var(--awtt-shadow-sm);
  transition: var(--awtt-transition);
  display: flex;
  flex-direction: column;
}

.awtt-service-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--awtt-shadow-md);
  border-color: #bae6fd;
}

.awtt-service-icon {
  width: 52px;
  height: 52px;
  border-radius: var(--awtt-radius);
  background-color: var(--awtt-accent-light);
  color: var(--awtt-accent);
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}

.awtt-service-icon svg {
  width: 26px;
  height: 26px;
}

.awtt-service-card h3 {
  font-size: 1.18rem;
  font-weight: 600;
  color: var(--awtt-primary);
  margin-bottom: 10px;
}

.awtt-service-card p {
  font-size: 0.92rem;
  color: var(--awtt-text-muted);
  line-height: 1.6;
  margin-bottom: 18px;
  flex-grow: 1;
}

.awtt-card-cta {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--awtt-accent);
  margin-top: auto;
}

.awtt-card-cta:hover {
  color: var(--awtt-accent-hover);
  text-decoration: underline;
}

.awtt-card-cta svg {
  width: 14px;
  height: 14px;
  transition: transform 0.2s ease;
}

.awtt-card-cta:hover svg {
  transform: translateX(3px);
}

/* DESTINATION CARDS & FILTERS */
.awtt-filter-tabs {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 36px;
}

.awtt-filter-btn {
  padding: 8px 20px;
  border-radius: 30px;
  font-size: 0.9rem;
  font-weight: 500;
  background-color: #ffffff;
  color: var(--awtt-text-muted);
  border: 1px solid var(--awtt-border);
  transition: var(--awtt-transition);
}

.awtt-filter-btn.awtt-filter-active, .awtt-filter-btn:hover {
  background-color: var(--awtt-primary);
  color: #ffffff;
  border-color: var(--awtt-primary);
}

.awtt-dest-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 26px;
}

.awtt-dest-card {
  background: #ffffff;
  border-radius: var(--awtt-radius-lg);
  overflow: hidden;
  box-shadow: var(--awtt-shadow-sm);
  border: 1px solid var(--awtt-border);
  transition: var(--awtt-transition);
  display: flex;
  flex-direction: column;
}

.awtt-dest-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--awtt-shadow-md);
  border-color: #cbd5e1;
}

.awtt-dest-img-wrap {
  position: relative;
  width: 100%;
  height: 195px;
  background-color: #e2e8f0;
  overflow: hidden;
}

.awtt-dest-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}

.awtt-dest-card:hover .awtt-dest-img {
  transform: scale(1.04);
}

.awtt-dest-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  background: rgba(10, 37, 64, 0.85);
  backdrop-filter: blur(4px);
  color: #ffffff;
  font-size: 0.72rem;
  font-weight: 600;
  padding: 4px 10px;
  border-radius: 20px;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.awtt-dest-content {
  padding: 20px;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.awtt-dest-content h3 {
  font-size: 1.18rem;
  font-weight: 600;
  color: var(--awtt-primary);
  margin-bottom: 8px;
}

.awtt-dest-content p {
  font-size: 0.88rem;
  color: var(--awtt-text-muted);
  line-height: 1.55;
  margin-bottom: 18px;
  flex-grow: 1;
}

/* PACKAGE CARDS */
.awtt-packages-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 28px;
}

.awtt-pkg-card {
  background: #ffffff;
  border-radius: var(--awtt-radius-lg);
  border: 1px solid var(--awtt-border);
  overflow: hidden;
  box-shadow: var(--awtt-shadow-sm);
  display: flex;
  flex-direction: column;
  transition: var(--awtt-transition);
}

.awtt-pkg-card:hover {
  box-shadow: var(--awtt-shadow-md);
  transform: translateY(-4px);
}

.awtt-pkg-header {
  position: relative;
  height: 170px;
  background-color: var(--awtt-primary);
}

.awtt-pkg-header img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.awtt-pkg-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to top, rgba(10, 37, 64, 0.85) 0%, transparent 60%);
}

.awtt-pkg-title-wrap {
  position: absolute;
  bottom: 14px;
  left: 18px;
  right: 18px;
  color: #ffffff;
}

.awtt-pkg-title-wrap h3 {
  font-size: 1.22rem;
  font-weight: 600;
}

.awtt-pkg-duration {
  font-size: 0.8rem;
  color: #93c5fd;
  display: flex;
  align-items: center;
  gap: 5px;
}

.awtt-pkg-body {
  padding: 22px;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.awtt-pkg-desc {
  font-size: 0.9rem;
  color: var(--awtt-text-muted);
  line-height: 1.55;
  margin-bottom: 18px;
}

.awtt-pkg-inclusions {
  margin-bottom: 22px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.awtt-pkg-inc-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.85rem;
  color: var(--awtt-text-main);
}

.awtt-pkg-inc-item svg {
  width: 15px;
  height: 15px;
  color: var(--awtt-accent);
  flex-shrink: 0;
}

.awtt-pkg-footer {
  margin-top: auto;
  padding-top: 18px;
  border-top: 1px solid var(--awtt-border);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* WHY CHOOSE US & PROCESS */
.awtt-features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 24px;
}

.awtt-feature-box {
  background: #ffffff;
  padding: 26px;
  border-radius: var(--awtt-radius-lg);
  border: 1px solid var(--awtt-border);
  box-shadow: var(--awtt-shadow-sm);
}

.awtt-feature-num {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--awtt-accent);
  margin-bottom: 12px;
  display: inline-block;
  padding: 4px 10px;
  background-color: var(--awtt-accent-light);
  border-radius: var(--awtt-radius);
}

.awtt-feature-box h3 {
  font-size: 1.12rem;
  font-weight: 600;
  color: var(--awtt-primary);
  margin-bottom: 8px;
}

.awtt-feature-box p {
  font-size: 0.9rem;
  color: var(--awtt-text-muted);
  line-height: 1.55;
}

/* FAQ ACCORDION */
.awtt-faq-container {
  max-width: 820px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.awtt-faq-item {
  background: #ffffff;
  border: 1px solid var(--awtt-border);
  border-radius: var(--awtt-radius);
  overflow: hidden;
  transition: var(--awtt-transition);
}

.awtt-faq-item.awtt-faq-open {
  border-color: #93c5fd;
  box-shadow: var(--awtt-shadow-sm);
}

.awtt-faq-trigger {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 18px 22px;
  text-align: left;
  font-size: 1rem;
  font-weight: 600;
  color: var(--awtt-primary);
  background: none;
  cursor: pointer;
}

.awtt-faq-trigger:hover {
  background-color: var(--awtt-bg-subtle);
}

.awtt-faq-icon {
  width: 20px;
  height: 20px;
  color: var(--awtt-accent);
  transition: transform 0.25s ease;
  flex-shrink: 0;
  margin-left: 12px;
}

.awtt-faq-open .awtt-faq-icon {
  transform: rotate(180deg);
}

.awtt-faq-answer {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.awtt-faq-open .awtt-faq-answer {
  max-height: 380px;
}

.awtt-faq-answer-inner {
  padding: 0 22px 20px;
  font-size: 0.92rem;
  color: var(--awtt-text-muted);
  line-height: 1.65;
  border-top: 1px solid var(--awtt-border);
  padding-top: 14px;
}

/* BOOKING SECTION & FORMS */
.awtt-booking-box {
  background: #ffffff;
  border-radius: var(--awtt-radius-lg);
  border: 1px solid var(--awtt-border);
  box-shadow: var(--awtt-shadow-md);
  padding: 36px;
  max-width: 880px;
  margin: 0 auto;
}

.awtt-form-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 18px;
  margin-bottom: 18px;
}

/* BLOG CARDS */
.awtt-blog-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 28px;
}

.awtt-blog-card {
  background: #ffffff;
  border-radius: var(--awtt-radius-lg);
  border: 1px solid var(--awtt-border);
  overflow: hidden;
  box-shadow: var(--awtt-shadow-sm);
  display: flex;
  flex-direction: column;
  transition: var(--awtt-transition);
}

.awtt-blog-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--awtt-shadow-md);
}

.awtt-blog-img {
  height: 200px;
  width: 100%;
  object-fit: cover;
  background-color: #e2e8f0;
}

.awtt-blog-body {
  padding: 22px;
  display: flex;
  flex-direction: column;
  flex-grow: 1;
}

.awtt-blog-tag {
  font-size: 0.76rem;
  font-weight: 600;
  text-transform: uppercase;
  color: var(--awtt-accent);
  margin-bottom: 8px;
  letter-spacing: 0.05em;
}

.awtt-blog-body h3 {
  font-size: 1.15rem;
  font-weight: 600;
  color: var(--awtt-primary);
  margin-bottom: 10px;
  line-height: 1.4;
}

.awtt-blog-body p {
  font-size: 0.88rem;
  color: var(--awtt-text-muted);
  line-height: 1.6;
  margin-bottom: 18px;
  flex-grow: 1;
}

/* ABOUT & CONTENT PAGES */
.awtt-content-wrap {
  max-width: 900px;
  margin: 0 auto;
  background: #ffffff;
  border: 1px solid var(--awtt-border);
  border-radius: var(--awtt-radius-lg);
  padding: 40px;
  box-shadow: var(--awtt-shadow-sm);
}

.awtt-content-wrap h1 {
  font-size: 2.2rem;
  font-weight: 700;
  color: var(--awtt-primary);
  margin-bottom: 16px;
}

.awtt-content-wrap h2 {
  font-size: 1.45rem;
  font-weight: 600;
  color: var(--awtt-primary);
  margin: 28px 0 12px;
}

.awtt-content-wrap p {
  font-size: 0.96rem;
  color: var(--awtt-text-main);
  line-height: 1.7;
  margin-bottom: 16px;
}

.awtt-content-wrap ul {
  list-style: disc;
  margin-left: 24px;
  margin-bottom: 18px;
}

.awtt-content-wrap li {
  font-size: 0.94rem;
  color: var(--awtt-text-main);
  margin-bottom: 8px;
  line-height: 1.6;
}

/* CONTACT INFO CARDS */
.awtt-contact-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 22px;
  margin-bottom: 36px;
}

.awtt-contact-card {
  background: #ffffff;
  border: 1px solid var(--awtt-border);
  border-radius: var(--awtt-radius);
  padding: 24px;
  display: flex;
  gap: 16px;
  align-items: flex-start;
}

.awtt-contact-card-icon {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--awtt-accent-light);
  color: var(--awtt-accent);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.awtt-contact-card-icon svg {
  width: 20px;
  height: 20px;
}

.awtt-contact-card h4 {
  font-size: 1rem;
  font-weight: 600;
  color: var(--awtt-primary);
  margin-bottom: 6px;
}

.awtt-contact-card p, .awtt-contact-card a {
  font-size: 0.9rem;
  color: var(--awtt-text-muted);
  line-height: 1.5;
}

.awtt-contact-card a:hover {
  color: var(--awtt-accent);
  text-decoration: underline;
}

/* FOOTER */
.awtt-footer {
  background-color: var(--awtt-primary-dark);
  color: #cbd5e1;
  padding: 64px 0 24px;
  margin-top: auto;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.awtt-footer-grid {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 1.5fr;
  gap: 40px;
  margin-bottom: 48px;
}

.awtt-footer-col h4 {
  color: #ffffff;
  font-size: 1.05rem;
  font-weight: 600;
  margin-bottom: 18px;
  letter-spacing: -0.01em;
}

.awtt-footer-desc {
  font-size: 0.88rem;
  line-height: 1.65;
  color: #94a3b8;
  margin: 14px 0 20px;
}

.awtt-footer-links {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.awtt-footer-links a {
  font-size: 0.88rem;
  color: #94a3b8;
  transition: var(--awtt-transition);
}

.awtt-footer-links a:hover {
  color: #ffffff;
  transform: translateX(3px);
}

.awtt-footer-contact {
  display: flex;
  flex-direction: column;
  gap: 12px;
  font-size: 0.88rem;
  color: #94a3b8;
}

.awtt-footer-contact-item {
  display: flex;
  gap: 10px;
  align-items: flex-start;
}

.awtt-footer-contact-item svg {
  width: 16px;
  height: 16px;
  color: var(--awtt-accent);
  flex-shrink: 0;
  margin-top: 3px;
}

.awtt-footer-bottom {
  padding-top: 24px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
  font-size: 0.82rem;
  color: #64748b;
}

.awtt-footer-legal {
  display: flex;
  gap: 18px;
}

.awtt-footer-legal a {
  color: #94a3b8;
}

.awtt-footer-legal a:hover {
  color: #ffffff;
}

/* FLOATING WHATSAPP BUTTON */
.awtt-whatsapp-float {
  position: fixed;
  bottom: 24px;
  right: 24px;
  z-index: 999;
  display: flex;
  align-items: center;
  gap: 10px;
  background-color: #25d366;
  color: #ffffff;
  padding: 10px 18px 10px 14px;
  border-radius: 40px;
  box-shadow: 0 6px 20px rgba(37, 211, 102, 0.4);
  font-size: 0.9rem;
  font-weight: 600;
  text-decoration: none;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.awtt-whatsapp-float:hover {
  transform: translateY(-3px) scale(1.02);
  box-shadow: 0 8px 24px rgba(37, 211, 102, 0.5);
  color: #ffffff;
}

.awtt-whatsapp-icon {
  width: 28px;
  height: 28px;
  fill: currentColor;
}

/* IMAGE FALLBACK STYLING */
.awtt-img-fallback {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #0a2540 0%, #1e3a8a 100%);
  color: #ffffff;
  padding: 16px;
  text-align: center;
}

.awtt-img-fallback-title {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 4px;
}

.awtt-img-fallback-sub {
  font-size: 0.75rem;
  color: #93c5fd;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* TOAST NOTIFICATION */
.awtt-toast {
  position: fixed;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%) translateY(100px);
  background: #0f172a;
  color: #ffffff;
  padding: 14px 26px;
  border-radius: var(--awtt-radius);
  box-shadow: var(--awtt-shadow-lg);
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 0.92rem;
  font-weight: 500;
  z-index: 3000;
  opacity: 0;
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s ease;
  pointer-events: none;
}

.awtt-toast.awtt-toast-show {
  transform: translateX(-50%) translateY(0);
  opacity: 1;
  pointer-events: auto;
}

.awtt-toast svg {
  width: 20px;
  height: 20px;
  color: #22c55e;
  flex-shrink: 0;
}

/* RESPONSIVE BREAKPOINTS */
@media (max-width: 1024px) {
  .awtt-footer-grid {
    grid-template-columns: 1fr 1fr;
    gap: 30px;
  }
}

@media (max-width: 860px) {
  .awtt-nav-menu, .awtt-header-actions .awtt-btn {
    display: none;
  }
  .awtt-hamburger {
    display: flex;
  }
  .awtt-hero h1 {
    font-size: 2.2rem;
  }
  .awtt-hero {
    padding: 60px 0 80px;
  }
  .awtt-search-widget-wrap {
    margin-top: -30px;
  }
  .awtt-content-wrap {
    padding: 24px;
  }
}

@media (max-width: 600px) {
  .awtt-topbar-inner {
    flex-direction: column;
    align-items: flex-start;
  }
  .awtt-hero h1 {
    font-size: 1.85rem;
  }
  .awtt-hero p {
    font-size: 0.96rem;
  }
  .awtt-footer-grid {
    grid-template-columns: 1fr;
    gap: 28px;
  }
  .awtt-footer-bottom {
    flex-direction: column;
    text-align: center;
  }
  .awtt-footer-legal {
    justify-content: center;
  }
  .awtt-whatsapp-float span {
    display: none;
  }
  .awtt-whatsapp-float {
    padding: 12px;
    border-radius: 50%;
  }
}
"""

with open("awtt_styles.py", "w", encoding="utf-8") as f:
    f.write(f'CSS = """{CSS}"""\n')

print("CSS generator written")
