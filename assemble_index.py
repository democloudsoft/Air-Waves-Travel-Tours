# -*- coding: utf-8 -*-
"""
Master index.html builder for Air Waves Travel & Tours
"""
from awtt_styles import CSS
from awtt_icons import ICONS
from awtt_scripts import JS
from build_destinations import destinations_data

def build_html():
    # Helper for destination cards
    def render_dest_card(d, is_home=False):
        img_loading = 'loading="lazy"'
        return f'''
        <div class="awtt-dest-card" data-category="{d['cat']}">
          <div class="awtt-dest-img-wrap">
            <img class="awtt-dest-img" src="{d['img']}" alt="{d['alt']}" width="400" height="220" {img_loading} decoding="async" onerror="handleImageError(this, '{d['name']}')">
            <span class="awtt-dest-badge">{d['badge']}</span>
          </div>
          <div class="awtt-dest-content">
            <h3>{d['name']}</h3>
            <p>{d['desc']}</p>
            <button type="button" class="awtt-btn awtt-btn-secondary awtt-btn-sm" data-book-destination="{d['name']}">
              Book This Trip {ICONS['arrowRight']}
            </button>
          </div>
        </div>
        '''

    home_dests_html = "".join([render_dest_card(d, True) for d in destinations_data[:8]])
    all_dests_html = "".join([render_dest_card(d, False) for d in destinations_data])

    packages = [
        {
            "title": "Hunza &amp; Gilgit Valley Tour",
            "duration": "7 Days / 6 Nights",
            "img": "https://iili.io/nH2hwTQ.jpg",
            "alt": "Hunza Valley tour package in Northern Pakistan",
            "desc": "Scenic exploration of Karimabad, Baltit Fort, Attabad Lake, Passu Cones, and Khunjerab Pass border.",
            "inclusions": ["Hotel accommodation in Hunza", "Private transport with driver", "Breakfast included", "Sightseeing excursions"]
        },
        {
            "title": "Skardu Shangrila &amp; Deosai",
            "duration": "7 Days / 6 Nights",
            "img": "https://iili.io/nH2h4yv.jpg",
            "alt": "Skardu tour package in Gilgit Baltistan",
            "desc": "Visit Shangrila Resort, Upper Kachura Lake, Katpana Cold Desert dunes, and scenic mountain viewpoints.",
            "inclusions": ["Deluxe hotel stays in Skardu", "4x4 Jeep for rugged routes", "Daily breakfast", "Airport pick &amp; drop"]
        },
        {
            "title": "Swat, Kalam &amp; Mahodand",
            "duration": "5 Days / 4 Nights",
            "img": "https://iili.io/nHJr0js.jpg",
            "alt": "Swat and Kalam tour package Pakistan",
            "desc": "Experience the lush green valleys of Swat, scenic riverbanks of Kalam, and alpine waters of Lake Mahodand.",
            "inclusions": ["Comfortable family hotels", "Dedicated tour vehicle", "Sightseeing to Malam Jabba", "Local road guidance"]
        },
        {
            "title": "Naran Kaghan &amp; Saif-ul-Malook",
            "duration": "4 Days / 3 Nights",
            "img": "https://iili.io/nH2hgaa.jpg",
            "alt": "Naran Kaghan valley holiday tour package",
            "desc": "Enjoy riverside stays along the Kunhar River, visit Lake Saif-ul-Malook by jeep, and cross Babusar Top.",
            "inclusions": ["Riverside hotel rooms", "Jeep ride to Saif-ul-Malook", "Daily breakfast", "Dedicated transport"]
        },
        {
            "title": "Dubai City &amp; Desert Safari",
            "duration": "5 Days / 4 Nights",
            "img": "https://iili.io/nH2hvG1.webp",
            "alt": "Dubai holiday travel package UAE",
            "desc": "City sightseeing, Dubai Mall, Burj Khalifa, thrilling 4x4 desert safari with BBQ dinner, and Marina Dhow cruise.",
            "inclusions": ["4-Star Dubai hotel stay", "Desert Safari with BBQ dinner", "Dhow Cruise Marina", "Airport transfers"]
        },
        {
            "title": "Baku Discovery &amp; Caspian Sea",
            "duration": "5 Days / 4 Nights",
            "img": "https://iili.io/nH2h86F.jpg",
            "alt": "Baku holiday travel package Azerbaijan",
            "desc": "Discover Old City Icherisheher, Flame Towers, Baku Boulevard, Fire Mountain Yanar Dag, and Ateshgah temple.",
            "inclusions": ["Centrally located Baku hotel", "Guided city tours", "Daily breakfast", "Return airport transfers"]
        },
        {
            "title": "Istanbul &amp; Turkey Highlights",
            "duration": "7 Days / 6 Nights",
            "img": "https://iili.io/nH2hsZN.webp",
            "alt": "Turkey and Istanbul tour package",
            "desc": "Blue Mosque, Hagia Sophia, Grand Bazaar, scenic Bosphorus cruise, and optional Cappadocia excursion.",
            "inclusions": ["Quality hotel accommodation", "Bosphorus boat cruise", "Historical city walking tours", "Daily breakfast"]
        },
        {
            "title": "Umrah Religious Travel Package",
            "duration": "Customized Durations",
            "img": "https://iili.io/nH3m8EN.jpg",
            "alt": "Umrah pilgrimage travel package Makkah and Madinah",
            "desc": "Tailored Umrah packages featuring comfortable hotels in Makkah and Madinah near the holy Haramain.",
            "inclusions": ["Haram-vicinity hotels", "Intercity private transport", "Visa &amp; ticketing assistance", "Ziyarat excursions"]
        }
    ]

    def render_pkg_card(p):
        inc_html = "".join([f'<div class="awtt-pkg-inc-item">{ICONS["check"]}<span>{item}</span></div>' for item in p["inclusions"]])
        return f'''
        <div class="awtt-pkg-card">
          <div class="awtt-pkg-header">
            <img src="{p['img']}" alt="{p['alt']}" width="400" height="170" loading="lazy" decoding="async" onerror="handleImageError(this, '{p['title']}')">
            <div class="awtt-pkg-overlay"></div>
            <div class="awtt-pkg-title-wrap">
              <h3>{p['title']}</h3>
              <div class="awtt-pkg-duration">{ICONS['calendar']} {p['duration']}</div>
            </div>
          </div>
          <div class="awtt-pkg-body">
            <p class="awtt-pkg-desc">{p['desc']}</p>
            <div class="awtt-pkg-inclusions">
              {inc_html}
            </div>
            <div class="awtt-pkg-footer">
              <span style="font-size:0.85rem;color:var(--awtt-text-muted);">Inquiry &amp; Rates</span>
              <button type="button" class="awtt-btn awtt-btn-primary awtt-btn-sm" data-book-destination="Package: {p['title']}">
                Request Details
              </button>
            </div>
          </div>
        </div>
        '''

    packages_html = "".join([render_pkg_card(p) for p in packages])

    blog_articles = [
        {
            "title": "Top Scenic Places to Visit in Northern Pakistan",
            "cat": "Domestic Travel Guide",
            "img": "https://iili.io/nH2hwTQ.jpg",
            "alt": "Northern Pakistan scenic mountains and valleys",
            "excerpt": "A comprehensive guide to exploring Hunza Valley, Skardu, Swat, and Naran-Kaghan with practical travel advice from Karachi.",
            "content": "<p>Northern Pakistan is blessed with some of the most dramatic mountain landscapes on Earth. From the snow-capped summits of the Karakoram and Himalayan ranges to turquoise glacial lakes, every valley offers an unforgettable encounter with nature.</p><p><strong>Hunza Valley:</strong> Known for Karimabad, Baltit Fort, and the surreal Attabad Lake, Hunza is ideal for families and mountain lovers. Traveling via Islamabad or direct Gilgit flights makes access more convenient than ever.</p><p><strong>Skardu:</strong> Home to the Cold Desert, Shangrila Lake, and Upper Kachura, Skardu serves as the starting point for world-famous trekking expeditions.</p><p><strong>Swat &amp; Kalam:</strong> Often called the Switzerland of Pakistan, Swat features verdant meadows, dense cedar forests, and the sparkling Mahodand Lake.</p><p>Air Waves Travel &amp; Tours provides end-to-end itinerary planning, vetted hotel reservations, and reliable transport for all northern destinations.</p>"
        },
        {
            "title": "Dubai Travel Guide: City Landmarks &amp; Desert Safaris",
            "cat": "International Travel",
            "img": "https://iili.io/nH2hvG1.webp",
            "alt": "Dubai modern skyline and Burj Khalifa",
            "excerpt": "Everything you need to know before visiting Dubai from Karachi, including visa processing, top attractions, and family itinerary tips.",
            "content": "<p>Dubai remains one of the most popular international destinations for Pakistani travelers due to frequent direct flights from Karachi and a rich variety of experiences.</p><p><strong>Top Sights:</strong> Be sure to visit Downtown Dubai to see the Burj Khalifa and Dubai Fountain, take a stroll through the Dubai Mall, and explore Old Dubai around Deira Creek for traditional gold and spice souks.</p><p><strong>Desert Safari:</strong> An afternoon dune-bashing excursion followed by a traditional desert camp dinner is an essential part of any Dubai holiday.</p><p>Our Karachi office assists with flight options on airlines such as Emirates, Flydubai, and Airblue, alongside certified hotel bookings across Deira, Bur Dubai, and Marina.</p>"
        },
        {
            "title": "Baku: Where Ancient Silk Road Meets Modern Seaside Charm",
            "cat": "International Destinations",
            "img": "https://iili.io/nH2h86F.jpg",
            "alt": "Baku city architectural landmarks and seaside boulevard",
            "excerpt": "Discover why Baku, Azerbaijan has become one of the favorite holiday destinations for families and solo travelers.",
            "content": "<p>Azerbaijan's capital Baku on the Caspian Sea effortlessly blends UNESCO-listed medieval stone heritage with futuristic glass architecture.</p><p><strong>Must-Visit Locations:</strong> Explore Icherisheher (the Old City) with its Maiden Tower, admire the Flame Towers illuminated at night, and walk along the picturesque Baku Boulevard on the Caspian shoreline.</p><p><strong>Day Trips:</strong> Discover the prehistoric rock art of Gobustan and the natural gas flames of Yanar Dag (Fire Mountain).</p><p>Air Waves Travel &amp; Tours arranges customized Baku packages with direct or convenient connecting flights, English-speaking guides, and comfortable downtown accommodations.</p>"
        },
        {
            "title": "Smart Flight Booking Tips: Securing the Best Airfares",
            "cat": "Travel Advice",
            "img": "https://iili.io/nHd5O5g.jpg",
            "alt": "Karachi airport and airline travel planning",
            "excerpt": "Practical advice from our experienced travel consultants on how to time your ticket purchase and select the right baggage options.",
            "content": "<p>Airfare pricing depends on booking class tiers, seasonal demand, and booking windows. By understanding these dynamics, travelers can save significantly on domestic and international journeys.</p><p><strong>Advance Planning:</strong> For peak travel seasons such as Eid, summer holidays, and school breaks, securing tickets 3 to 6 weeks early ensures access to lower fare buckets.</p><p><strong>Connecting vs. Direct Flights:</strong> Compare total travel duration against cost savings. Our agents carefully evaluate layover times to ensure smooth transitions without excessive airport waiting.</p><p>Contact our ticketing desk in Gulistan-e-Johar, Karachi for transparent airfare comparisons across domestic and international carriers.</p>"
        },
        {
            "title": "Planning Your Umrah Journey: Spiritual Preparation &amp; Logistics",
            "cat": "Religious Travel",
            "img": "https://iili.io/nH3m8EN.jpg",
            "alt": "Holy Kaaba and Masjid al-Haram sanctuary in Makkah",
            "excerpt": "Essential advice for pilgrims traveling from Karachi to Makkah and Madinah, focusing on hotel proximity and documentation.",
            "content": "<p>Performing Umrah is a profoundly meaningful spiritual journey that requires thoughtful preparation regarding health, documentation, and accommodation.</p><p><strong>Proximity Matters:</strong> Choosing hotels within walking distance of Masjid al-Haram in Makkah and Al-Masjid an-Nabawi in Madinah greatly facilitates daily prayers, especially for seniors and families with children.</p><p><strong>Documentation:</strong> Ensure your passport has at least six months of validity and keep your visa and vaccination records readily accessible.</p><p>Air Waves Travel &amp; Tours offers personalized Umrah packages tailored to your schedule, budget, and accommodation preferences.</p>"
        }
    ]

    def render_blog_card(b, idx):
        safe_content = b['content'].replace('"', '&quot;').replace("'", "&#39;")
        return f'''
        <div class="awtt-blog-card">
          <img class="awtt-blog-img" src="{b['img']}" alt="{b['alt']}" width="400" height="200" loading="lazy" decoding="async" onerror="handleImageError(this, '{b['title']}')">
          <div class="awtt-blog-body">
            <span class="awtt-blog-tag">{b['cat']}</span>
            <h3>{b['title']}</h3>
            <p>{b['excerpt']}</p>
            <button type="button" class="awtt-card-cta" onclick="openArticleModal('{b['title']}', '{b['cat']}', `{b['content']}`)">
              Read Full Guide {ICONS['arrowRight']}
            </button>
          </div>
        </div>
        '''

    blog_cards_html = "".join([render_blog_card(b, i) for i, b in enumerate(blog_articles)])

    full_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Air Waves Travel &amp; Tours | Travel Agency in Karachi</title>
  <meta name="description" content="Air Waves Travel &amp; Tours is a premier travel agency in Gulistan-e-Johar, Karachi. Offering domestic &amp; international flight bookings, hotel reservations, customized tour packages, and travel assistance.">
  <meta name="keywords" content="Air Waves Travel &amp; Tours Karachi, Travel Agency in Karachi, Travel Agency in Gulistan-e-Johar Karachi, Flight Booking in Karachi, International Travel Services in Karachi, Hotel Booking in Karachi, Travel Packages from Karachi, Umrah Packages Karachi">
  <link rel="canonical" href="https://airwavestravel.com/">

  <!-- Open Graph / Social -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://airwavestravel.com/">
  <meta property="og:title" content="Air Waves Travel &amp; Tours | Travel Agency in Karachi">
  <meta property="og:description" content="Book domestic &amp; international flights, curated holiday packages, and hotel stays with Air Waves Travel &amp; Tours, Karachi.">
  <meta property="og:image" content="https://iili.io/n2S5CCl.png">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Air Waves Travel &amp; Tours | Travel Agency in Karachi">
  <meta name="twitter:description" content="Book domestic &amp; international flights, curated holiday packages, and hotel stays with Air Waves Travel &amp; Tours, Karachi.">
  <meta name="twitter:image" content="https://iili.io/n2S5CCl.png">

  <!-- Google Fonts: Poppins -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <!-- Schema.org JSON-LD Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "TravelAgency",
    "name": "AIR WAVES TRAVEL & TOURS",
    "image": "https://iili.io/n2S5CCl.png",
    "telephone": "+923095795928",
    "email": "airwaves.travel.tour@gmail.com",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "U-34, Eastern Pride, Block 15 Gulistan-e-Johar",
      "addressLocality": "Karachi",
      "postalCode": "75290",
      "addressCountry": "PK"
    }},
    "sameAs": [
      "https://www.facebook.com/AirwavesTraveltours/",
      "https://www.instagram.com/airwaves_travel/"
    ],
    "priceRange": "$$"
  }}
  </script>

  <style>
{CSS}
  </style>
</head>
<body>

  <!-- TOP CONTACT BAR -->
  <div class="awtt-topbar">
    <div class="awtt-container awtt-topbar-inner">
      <div class="awtt-topbar-contact">
        <span class="awtt-topbar-item">
          {ICONS['mapPin']}
          <span>U-34, Eastern Pride, Block 15 Gulistan-e-Johar, Karachi</span>
        </span>
        <span class="awtt-topbar-item">
          {ICONS['phone']}
          <a href="tel:+923095795928">+92 309 5795928</a>
        </span>
        <span class="awtt-topbar-item">
          {ICONS['mail']}
          <a href="mailto:airwaves.travel.tour@gmail.com">airwaves.travel.tour@gmail.com</a>
        </span>
      </div>
      <div class="awtt-topbar-social">
        <span style="font-size:0.78rem;color:#94a3b8;margin-right:4px;">Connect with us:</span>
        <a href="https://www.facebook.com/AirwavesTraveltours/" target="_blank" rel="noopener noreferrer" class="awtt-social-link" aria-label="Air Waves Travel Facebook">
          {ICONS['facebook']}
        </a>
        <a href="https://www.instagram.com/airwaves_travel/" target="_blank" rel="noopener noreferrer" class="awtt-social-link" aria-label="Air Waves Travel Instagram">
          {ICONS['instagram']}
        </a>
      </div>
    </div>
  </div>

  <!-- HEADER & NAVIGATION -->
  <header class="awtt-header">
    <div class="awtt-container awtt-navbar">
      <a href="#home" class="awtt-brand" aria-label="Air Waves Travel &amp; Tours Home">
        <img class="awtt-logo-img" src="https://iili.io/n2S5CCl.png" alt="Air Waves Travel &amp; Tours Official Logo" width="190" height="52" onerror="handleLogoError(this)">
        <div class="awtt-brand-text">
          <span class="awtt-brand-title">AIR WAVES</span>
          <span class="awtt-brand-subtitle">TRAVEL &amp; TOURS</span>
        </div>
      </a>

      <!-- Desktop Nav -->
      <nav class="awtt-nav-menu" aria-label="Main Navigation">
        <a href="#home" class="awtt-nav-link">Home</a>
        <a href="#about" class="awtt-nav-link">About Us</a>
        <a href="#destinations" class="awtt-nav-link">Destinations</a>
        <a href="#flights" class="awtt-nav-link">Flights</a>
        <a href="#hotels" class="awtt-nav-link">Hotels</a>
        <a href="#packages" class="awtt-nav-link">Packages</a>
        <a href="#booking" class="awtt-nav-link">Booking</a>
        <a href="#blog" class="awtt-nav-link">Blog</a>
      </nav>

      <div class="awtt-header-actions">
        <a href="#booking" class="awtt-btn awtt-btn-primary awtt-btn-sm">
          Request a Quote
        </a>
        <button type="button" class="awtt-hamburger" id="awtt-hamburger-btn" aria-label="Open Navigation Menu">
          {ICONS['menu']}
        </button>
      </div>
    </div>
  </header>

  <!-- MOBILE DRAWER -->
  <div class="awtt-drawer-overlay" id="awtt-drawer-overlay"></div>
  <aside class="awtt-mobile-drawer" id="awtt-mobile-drawer" aria-label="Mobile Navigation">
    <div class="awtt-drawer-header">
      <div style="font-weight:700;color:var(--awtt-primary);font-size:1.1rem;">Menu</div>
      <button type="button" class="awtt-drawer-close" id="awtt-drawer-close-btn" aria-label="Close Menu">
        {ICONS['close']}
      </button>
    </div>
    <div class="awtt-drawer-links">
      <a href="#home" class="awtt-drawer-link">Home</a>
      <a href="#about" class="awtt-drawer-link">About Us</a>
      <a href="#destinations" class="awtt-drawer-link">Destinations</a>
      <a href="#flights" class="awtt-drawer-link">Flights</a>
      <a href="#hotels" class="awtt-drawer-link">Hotels</a>
      <a href="#packages" class="awtt-drawer-link">Packages</a>
      <a href="#booking" class="awtt-drawer-link">Booking</a>
      <a href="#blog" class="awtt-drawer-link">Blog</a>
      <a href="#privacy" class="awtt-drawer-link">Privacy Policy</a>
      <a href="#terms" class="awtt-drawer-link">Terms &amp; Conditions</a>
    </div>
    <div class="awtt-drawer-contact">
      <a href="tel:+923095795928" style="color:var(--awtt-primary);font-weight:600;display:flex;align-items:center;gap:8px;">
        {ICONS['phone']} +92 309 5795928
      </a>
      <span style="font-size:0.8rem;color:var(--awtt-text-muted);">
        Gulistan-e-Johar, Karachi, Pakistan
      </span>
    </div>
  </aside>

  <!-- MAIN CONTENT CONTAINER -->
  <main id="awtt-main-content">

    <!-- ============================================== -->
    <!-- VIEW: HOME                                     -->
    <!-- ============================================== -->
    <section class="awtt-view awtt-view-active" id="awtt-view-home">

      <!-- Hero Section with Eager Travel Photograph -->
      <div class="awtt-hero" style="background-image: url('https://iili.io/nH2hwTQ.jpg');">
        <div class="awtt-hero-overlay"></div>
        <div class="awtt-container">
          <div class="awtt-hero-content">
            <div class="awtt-hero-badge">
              {ICONS['compass']}
              <span>Air Waves Travel &amp; Tours • Karachi</span>
            </div>
            <h1>Your Trusted Travel Partner in Karachi</h1>
            <p>
              Specializing in domestic flights, international airline ticketing, curated hotel stays, and tailor-made tour packages across Pakistan and worldwide destinations.
            </p>
            <div class="awtt-hero-buttons">
              <a href="#booking" class="awtt-btn awtt-btn-primary awtt-btn-lg">
                Book Your Trip {ICONS['arrowRight']}
              </a>
              <a href="#destinations" class="awtt-btn awtt-btn-secondary awtt-btn-lg">
                Explore Destinations
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Search Widget -->
      <div class="awtt-container awtt-search-widget-wrap">
        <div class="awtt-search-widget">
          <div class="awtt-search-tabs">
            <button type="button" class="awtt-search-tab-btn awtt-tab-active" data-tab="flights">
              {ICONS['plane']} Flights
            </button>
            <button type="button" class="awtt-search-tab-btn" data-tab="hotels">
              {ICONS['hotel']} Hotels
            </button>
            <button type="button" class="awtt-search-tab-btn" data-tab="packages">
              {ICONS['compass']} Tour Packages
            </button>
          </div>

          <!-- Flights Tab -->
          <div class="awtt-search-tab-content awtt-tab-content-active" id="awtt-tab-flights">
            <form id="awtt-flight-search-form" class="awtt-form-grid">
              <div class="awtt-form-group">
                <label class="awtt-form-label" for="awtt-flight-from">{ICONS['mapPin']} From</label>
                <input type="text" id="awtt-flight-from" class="awtt-input" value="Karachi (KHI)" required>
              </div>
              <div class="awtt-form-group">
                <label class="awtt-form-label" for="awtt-flight-to">{ICONS['plane']} To Destination</label>
                <input type="text" id="awtt-flight-to" class="awtt-input" placeholder="e.g. Islamabad, Dubai, Baku" required>
              </div>
              <div class="awtt-form-group">
                <label class="awtt-form-label" for="awtt-flight-date">{ICONS['calendar']} Departure Date</label>
                <input type="date" id="awtt-flight-date" class="awtt-input" required>
              </div>
              <div class="awtt-form-group">
                <label class="awtt-form-label" for="awtt-flight-class">{ICONS['users']} Cabin Class</label>
                <select id="awtt-flight-class" class="awtt-select">
                  <option value="Economy">Economy</option>
                  <option value="Premium Economy">Premium Economy</option>
                  <option value="Business">Business Class</option>
                </select>
              </div>
              <div class="awtt-form-group">
                <button type="submit" class="awtt-btn awtt-btn-primary" style="height:44px;width:100%;">
                  {ICONS['search']} Find Flights
                </button>
              </div>
            </form>
          </div>

          <!-- Hotels Tab -->
          <div class="awtt-search-tab-content" id="awtt-tab-hotels">
            <form id="awtt-hotel-search-form" class="awtt-form-grid">
              <div class="awtt-form-group">
                <label class="awtt-form-label" for="awtt-hotel-dest">{ICONS['hotel']} Destination City</label>
                <input type="text" id="awtt-hotel-dest" class="awtt-input" placeholder="e.g. Hunza, Dubai, Skardu, Lahore" required>
              </div>
              <div class="awtt-form-group">
                <label class="awtt-form-label" for="awtt-hotel-in">{ICONS['calendar']} Check-in</label>
                <input type="date" id="awtt-hotel-in" class="awtt-input" required>
              </div>
              <div class="awtt-form-group">
                <label class="awtt-form-label" for="awtt-hotel-out">{ICONS['calendar']} Check-out</label>
                <input type="date" id="awtt-hotel-out" class="awtt-input" required>
              </div>
              <div class="awtt-form-group">
                <label class="awtt-form-label" for="awtt-hotel-guests">{ICONS['users']} Guests</label>
                <select id="awtt-hotel-guests" class="awtt-select">
                  <option value="1 Guest, 1 Room">1 Guest, 1 Room</option>
                  <option value="2 Guests, 1 Room" selected>2 Guests, 1 Room</option>
                  <option value="Family (3-4 Guests)">Family (3-4 Guests)</option>
                  <option value="Group (5+ Guests)">Group (5+ Guests)</option>
                </select>
              </div>
              <div class="awtt-form-group">
                <button type="submit" class="awtt-btn awtt-btn-primary" style="height:44px;width:100%;">
                  {ICONS['search']} Check Stays
                </button>
              </div>
            </form>
          </div>

          <!-- Packages Tab -->
          <div class="awtt-search-tab-content" id="awtt-tab-packages">
            <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:14px;">
              <div>
                <h4 style="font-size:1.05rem;color:var(--awtt-primary);margin-bottom:4px;">Tailored Holiday &amp; Tour Packages</h4>
                <p style="font-size:0.88rem;color:var(--awtt-text-muted);">Explore our popular domestic itineraries for Northern Pakistan, international city escapes, and Umrah travel.</p>
              </div>
              <a href="#packages" class="awtt-btn awtt-btn-primary">
                View All Packages {ICONS['arrowRight']}
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- Services Section -->
      <section class="awtt-section">
        <div class="awtt-container">
          <div class="awtt-section-header">
            <h2>Our Travel Services</h2>
            <p>Comprehensive travel solutions designed to provide convenience, transparent airfare options, and dependable booking assistance.</p>
          </div>
          <div class="awtt-services-grid">
            <div class="awtt-service-card">
              <div class="awtt-service-icon">{ICONS['plane']}</div>
              <h3>Domestic Flight Booking</h3>
              <p>Ticketing across all major domestic airlines connecting Karachi with Islamabad, Lahore, Peshawar, Skardu, Gilgit, and Quetta.</p>
              <a href="#flights" class="awtt-card-cta">Book Domestic Flight {ICONS['arrowRight']}</a>
            </div>
            <div class="awtt-service-card">
              <div class="awtt-service-icon">{ICONS['compass']}</div>
              <h3>International Flights</h3>
              <p>Reliable airline reservations to the Middle East, Central Asia, Southeast Asia, Europe, and worldwide with competitive route choices.</p>
              <a href="#flights" class="awtt-card-cta">Search International Flights {ICONS['arrowRight']}</a>
            </div>
            <div class="awtt-service-card">
              <div class="awtt-service-icon">{ICONS['hotel']}</div>
              <h3>Hotel Reservations</h3>
              <p>Verified hotel stays from budget accommodations to luxury resorts in domestic hubs and key international tourist cities.</p>
              <a href="#hotels" class="awtt-card-cta">Inquire Hotel Stays {ICONS['arrowRight']}</a>
            </div>
            <div class="awtt-service-card">
              <div class="awtt-service-icon">{ICONS['mapPin']}</div>
              <h3>Domestic Pakistan Tours</h3>
              <p>Curated holiday trips to Hunza Valley, Skardu, Naran-Kaghan, and Swat featuring trusted road transport and scenic itineraries.</p>
              <a href="#destinations" class="awtt-card-cta">Explore Pakistan Tours {ICONS['arrowRight']}</a>
            </div>
            <div class="awtt-service-card">
              <div class="awtt-service-icon">{ICONS['shieldCheck']}</div>
              <h3>Holiday Packages</h3>
              <p>Carefully planned leisure packages for families, couples, and groups traveling to Dubai, Baku, Turkey, Malaysia, and beyond.</p>
              <a href="#packages" class="awtt-card-cta">Browse Tour Packages {ICONS['arrowRight']}</a>
            </div>
            <div class="awtt-service-card">
              <div class="awtt-service-icon">{ICONS['users']}</div>
              <h3>Umrah &amp; Religious Travel</h3>
              <p>Facilitation for Umrah pilgrimage journeys with hotel bookings in Makkah and Madinah close to the holy Haramain.</p>
              <a href="#packages" class="awtt-card-cta">View Umrah Assistance {ICONS['arrowRight']}</a>
            </div>
          </div>
        </div>
      </section>

      <!-- Featured Destinations Section -->
      <section class="awtt-section awtt-section-alt">
        <div class="awtt-container">
          <div class="awtt-section-header">
            <h2>Featured Destinations</h2>
            <p>Discover handpicked domestic scenic valleys and sought-after international holiday destinations.</p>
          </div>
          <div class="awtt-dest-grid">
            {home_dests_html}
          </div>
          <div style="text-align:center;margin-top:40px;">
            <a href="#destinations" class="awtt-btn awtt-btn-dark">
              View All Destinations ({len(destinations_data)}) {ICONS['arrowRight']}
            </a>
          </div>
        </div>
      </section>

      <!-- Why Choose Us -->
      <section class="awtt-section">
        <div class="awtt-container">
          <div class="awtt-section-header">
            <h2>Why Choose Air Waves Travel &amp; Tours</h2>
            <p>Committed to providing attentive travel planning, straightforward ticketing, and helpful guidance for every trip.</p>
          </div>
          <div class="awtt-features-grid">
            <div class="awtt-feature-box">
              <div class="awtt-feature-num">01</div>
              <h3>Local Karachi Presence</h3>
              <p>Located in Eastern Pride, Block 15 Gulistan-e-Johar, Karachi. We provide accessible face-to-face consultation and local support.</p>
            </div>
            <div class="awtt-feature-box">
              <div class="awtt-feature-num">02</div>
              <h3>Personalized Travel Itineraries</h3>
              <p>Every itinerary is customized to match your schedule, group size, and budget rather than pushing rigid, generic tour options.</p>
            </div>
            <div class="awtt-feature-box">
              <div class="awtt-feature-num">03</div>
              <h3>Verified Partners &amp; Hotels</h3>
              <p>We work with trusted accommodation partners and certified transport operators in Northern Pakistan and abroad.</p>
            </div>
            <div class="awtt-feature-box">
              <div class="awtt-feature-num">04</div>
              <h3>Prompt Communication</h3>
              <p>Reach us directly via phone, WhatsApp, or email for quick ticketing confirmations, itinerary updates, and travel advisory.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- Booking Process -->
      <section class="awtt-section awtt-section-alt">
        <div class="awtt-container">
          <div class="awtt-section-header">
            <h2>Our Travel Planning Process</h2>
            <p>Four straightforward steps from initial inquiry to ticket confirmation and departure.</p>
          </div>
          <div class="awtt-features-grid">
            <div class="awtt-feature-box">
              <div class="awtt-feature-num">Step 1</div>
              <h3>Share Your Requirements</h3>
              <p>Submit your destination, preferred dates, traveler count, and budget through our booking form or WhatsApp chat.</p>
            </div>
            <div class="awtt-feature-box">
              <div class="awtt-feature-num">Step 2</div>
              <h3>Receive Tailored Options</h3>
              <p>Our consultants compare flight schedules and hotel choices to present clear, practical options with transparent pricing.</p>
            </div>
            <div class="awtt-feature-box">
              <div class="awtt-feature-num">Step 3</div>
              <h3>Confirmation &amp; Tickets</h3>
              <p>Finalize your chosen itinerary, receive your confirmed airline e-tickets, hotel vouchers, and comprehensive travel details.</p>
            </div>
            <div class="awtt-feature-box">
              <div class="awtt-feature-num">Step 4</div>
              <h3>Travel with Peace of Mind</h3>
              <p>Enjoy your trip knowing that our Karachi team remains accessible for flight adjustments or on-ground support inquiries.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- MAIN FAQ SECTION ON HOME PAGE -->
      <section class="awtt-section" id="awtt-faq-section">
        <div class="awtt-container">
          <div class="awtt-section-header">
            <h2>Frequently Asked Questions</h2>
            <p>Common questions regarding our flight ticketing, tour package bookings, and customer support.</p>
          </div>
          <div class="awtt-faq-container">
            <div class="awtt-faq-item">
              <button type="button" class="awtt-faq-trigger" aria-expanded="false">
                <span>How can I book a flight ticket through Air Waves Travel &amp; Tours?</span>
                <span class="awtt-faq-icon">{ICONS['chevronDown']}</span>
              </button>
              <div class="awtt-faq-answer">
                <div class="awtt-faq-answer-inner">
                  You can submit your travel details via our website booking form, message us on WhatsApp at +92 309 5795928, or visit our Karachi office in Gulistan-e-Johar. Our consultants will evaluate available airline schedules, advise on the best fares, and issue your official e-tickets upon confirmation.
                </div>
              </div>
            </div>

            <div class="awtt-faq-item">
              <button type="button" class="awtt-faq-trigger" aria-expanded="false">
                <span>Do you arrange domestic flights within Pakistan?</span>
                <span class="awtt-faq-icon">{ICONS['chevronDown']}</span>
              </button>
              <div class="awtt-faq-answer">
                <div class="awtt-faq-answer-inner">
                  Yes, we arrange domestic ticketing across all operational airlines in Pakistan including PIA, Airblue, SereneAir, and Fly Jinnah. Routes include Karachi to Islamabad, Lahore, Peshawar, Skardu, Gilgit, Sukkur, and Quetta.
                </div>
              </div>
            </div>

            <div class="awtt-faq-item">
              <button type="button" class="awtt-faq-trigger" aria-expanded="false">
                <span>Which international destinations do you cover?</span>
                <span class="awtt-faq-icon">{ICONS['chevronDown']}</span>
              </button>
              <div class="awtt-faq-answer">
                <div class="awtt-faq-answer-inner">
                  We arrange international flights and holiday packages to major global destinations including the United Arab Emirates (Dubai, Abu Dhabi, Sharjah), Azerbaijan (Baku), Thailand (Bangkok, Phuket), Turkey (Istanbul), Malaysia, Singapore, Maldives, and Saudi Arabia (Makkah &amp; Madinah for Umrah).
                </div>
              </div>
            </div>

            <div class="awtt-faq-item">
              <button type="button" class="awtt-faq-trigger" aria-expanded="false">
                <span>Can you help with hotel reservations?</span>
                <span class="awtt-faq-icon">{ICONS['chevronDown']}</span>
              </button>
              <div class="awtt-faq-answer">
                <div class="awtt-faq-answer-inner">
                  Yes, we provide verified hotel bookings tailored to your preferences. Whether you are seeking budget-conscious family rooms in Hunza and Skardu or 4-star and 5-star properties in Dubai and Baku, we ensure your stay is confirmed before departure.
                </div>
              </div>
            </div>

            <div class="awtt-faq-item">
              <button type="button" class="awtt-faq-trigger" aria-expanded="false">
                <span>Can I request a customized holiday package?</span>
                <span class="awtt-faq-icon">{ICONS['chevronDown']}</span>
              </button>
              <div class="awtt-faq-answer">
                <div class="awtt-faq-answer-inner">
                  Absolutely. We specialize in tailoring travel packages according to your group size, travel dates, and preferred pace. Tell us your destination and expectations, and we will build an itinerary that aligns with your requirements.
                </div>
              </div>
            </div>

            <div class="awtt-faq-item">
              <button type="button" class="awtt-faq-trigger" aria-expanded="false">
                <span>What documents do I need to book an international flight?</span>
                <span class="awtt-faq-icon">{ICONS['chevronDown']}</span>
              </button>
              <div class="awtt-faq-answer">
                <div class="awtt-faq-answer-inner">
                  For international flights, you will need a valid passport with at least six months of validity from your planned return date, along with the appropriate visa or entry permit for your destination. Our consultants can advise on specific documentation requirements.
                </div>
              </div>
            </div>

            <div class="awtt-faq-item">
              <button type="button" class="awtt-faq-trigger" aria-expanded="false">
                <span>How can I contact Air Waves Travel &amp; Tours?</span>
                <span class="awtt-faq-icon">{ICONS['chevronDown']}</span>
              </button>
              <div class="awtt-faq-answer">
                <div class="awtt-faq-answer-inner">
                  You can call or WhatsApp us at +92 309 5795928, email airwaves.travel.tour@gmail.com, or visit our office at U-34, Eastern Pride, Block 15 Gulistan-e-Johar, Karachi, 75290, Pakistan.
                </div>
              </div>
            </div>

            <div class="awtt-faq-item">
              <button type="button" class="awtt-faq-trigger" aria-expanded="false">
                <span>Do you assist with Umrah pilgrimage packages?</span>
                <span class="awtt-faq-icon">{ICONS['chevronDown']}</span>
              </button>
              <div class="awtt-faq-answer">
                <div class="awtt-faq-answer-inner">
                  Yes, we provide dedicated Umrah travel assistance including airline reservations to Jeddah and Madinah, comfortable hotel accommodations in close proximity to Masjid al-Haram and Al-Masjid an-Nabawi, and intercity transport arrangements.
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Booking CTA Banner -->
      <section class="awtt-section" style="background-color:var(--awtt-primary);color:#ffffff;text-align:center;padding:60px 0;">
        <div class="awtt-container">
          <h2 style="font-size:2.2rem;color:#ffffff;margin-bottom:14px;">Plan Your Next Journey with Confidence</h2>
          <p style="font-size:1.05rem;color:#cbd5e1;max-width:620px;margin:0 auto 28px;">
            Get in touch with our travel specialists in Karachi for fast quotations, flight availability, and customized itineraries.
          </p>
          <div style="display:flex;justify-content:center;gap:14px;flex-wrap:wrap;">
            <a href="#booking" class="awtt-btn awtt-btn-primary awtt-btn-lg">
              Request a Travel Quote {ICONS['arrowRight']}
            </a>
            <a href="tel:+923095795928" class="awtt-btn awtt-btn-secondary awtt-btn-lg">
              {ICONS['phone']} Call +92 309 5795928
            </a>
          </div>
        </div>
      </section>

    </section>


    <!-- ============================================== -->
    <!-- VIEW: ABOUT US                                 -->
    <!-- ============================================== -->
    <section class="awtt-view" id="awtt-view-about">
      <div class="awtt-section">
        <div class="awtt-container">
          <div class="awtt-content-wrap">
            <h1>About Air Waves Travel &amp; Tours</h1>
            <p>
              <strong>AIR WAVES TRAVEL &amp; TOURS</strong> is a dedicated travel agency based in Karachi, Pakistan. We specialize in providing reliable domestic and international flight reservations, tailored holiday tour packages, hotel bookings, and travel assistance for individuals, families, and corporate travelers.
            </p>

            <h2>Our Office in Karachi</h2>
            <p>
              Conveniently located at <strong>U-34, Eastern Pride, Block 15 Gulistan-e-Johar, Karachi, 75290, Pakistan</strong>, our agency is positioned to serve clients across Karachi and nationwide with responsive travel consultation.
            </p>

            <div class="awtt-contact-grid" style="margin-top:24px;">
              <div class="awtt-contact-card">
                <div class="awtt-contact-card-icon">{ICONS['mapPin']}</div>
                <div>
                  <h4>Physical Location</h4>
                  <p>U-34, Eastern Pride, Block 15 Gulistan-e-Johar, Karachi, 75290, Pakistan</p>
                </div>
              </div>
              <div class="awtt-contact-card">
                <div class="awtt-contact-card-icon">{ICONS['phone']}</div>
                <div>
                  <h4>Direct Telephone</h4>
                  <p><a href="tel:+923095795928">+92 309 5795928</a></p>
                </div>
              </div>
              <div class="awtt-contact-card">
                <div class="awtt-contact-card-icon">{ICONS['mail']}</div>
                <div>
                  <h4>Email Address</h4>
                  <p><a href="mailto:airwaves.travel.tour@gmail.com">airwaves.travel.tour@gmail.com</a></p>
                </div>
              </div>
            </div>

            <h2>What We Do</h2>
            <p>
              At Air Waves Travel &amp; Tours, our goal is to eliminate the stress of planning and booking travel. We assist our clients with:
            </p>
            <ul>
              <li><strong>Domestic Airline Bookings:</strong> Daily departures connecting Karachi with major cities and northern gateways.</li>
              <li><strong>International Ticketing:</strong> Strategic route comparisons and transparent fare structures across premier airlines.</li>
              <li><strong>Domestic Holiday Tours:</strong> Carefully organized group and private trips to Hunza Valley, Skardu, Swat, Kalam, and Naran-Kaghan.</li>
              <li><strong>International Packages:</strong> Popular destinations including Dubai, Baku, Bangkok, Turkey, Malaysia, Singapore, and Maldives.</li>
              <li><strong>Religious Travel:</strong> Dedicated Umrah travel assistance with accommodation options in Makkah and Madinah.</li>
              <li><strong>Accommodations:</strong> Verified hotel partnerships ensuring comfortable stays suited to family and business travel.</li>
            </ul>

            <h2>Our Core Values</h2>
            <p>
              We believe in honest travel consultation, transparent fares, and proactive communication. Our team works directly with travelers to understand their specific needs and provide solutions that combine convenience, comfort, and value.
            </p>

            <div style="margin-top:32px;display:flex;gap:14px;flex-wrap:wrap;">
              <a href="#booking" class="awtt-btn awtt-btn-primary">
                Contact Our Karachi Desk {ICONS['arrowRight']}
              </a>
              <a href="#destinations" class="awtt-btn awtt-btn-secondary">
                View Destinations
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>


    <!-- ============================================== -->
    <!-- VIEW: DESTINATIONS                             -->
    <!-- ============================================== -->
    <section class="awtt-view" id="awtt-view-destinations">
      <div class="awtt-section">
        <div class="awtt-container">
          <div class="awtt-section-header">
            <h1>Travel Destinations</h1>
            <p>Explore domestic scenic valleys across Pakistan, exciting international holiday getaways, and sacred religious destinations.</p>
          </div>

          <!-- Category Filter Tabs -->
          <div class="awtt-filter-tabs">
            <button type="button" class="awtt-filter-btn awtt-filter-active" data-filter="all">All Destinations</button>
            <button type="button" class="awtt-filter-btn" data-filter="domestic">Domestic Pakistan</button>
            <button type="button" class="awtt-filter-btn" data-filter="international">International</button>
            <button type="button" class="awtt-filter-btn" data-filter="religious">Religious / Umrah</button>
          </div>

          <!-- All Destination Cards -->
          <div class="awtt-dest-grid" id="awtt-all-destinations-grid">
            {all_dests_html}
          </div>
        </div>
      </div>
    </section>


    <!-- ============================================== -->
    <!-- VIEW: FLIGHTS                                  -->
    <!-- ============================================== -->
    <section class="awtt-view" id="awtt-view-flights">
      <div class="awtt-section">
        <div class="awtt-container">
          <div class="awtt-section-header">
            <h1>Flight Booking Services</h1>
            <p>Request domestic and international flight quotations with competitive airfare options and schedule comparisons.</p>
          </div>

          <div class="awtt-booking-box">
            <form id="awtt-flights-page-form">
              <div class="awtt-form-row">
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-fl-trip">Trip Type</label>
                  <select id="awtt-fl-trip" class="awtt-select">
                    <option value="Round Trip">Round Trip</option>
                    <option value="One Way">One Way</option>
                    <option value="Multi-City">Multi-City</option>
                  </select>
                </div>
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-fl-cabin">Cabin Class</label>
                  <select id="awtt-fl-cabin" class="awtt-select">
                    <option value="Economy">Economy</option>
                    <option value="Premium Economy">Premium Economy</option>
                    <option value="Business">Business Class</option>
                  </select>
                </div>
              </div>

              <div class="awtt-form-row">
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-fl-from">{ICONS['mapPin']} Origin Airport / City</label>
                  <input type="text" id="awtt-fl-from" class="awtt-input" value="Karachi (KHI)" required>
                </div>
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-fl-to">{ICONS['plane']} Destination Airport / City</label>
                  <input type="text" id="awtt-fl-to" class="awtt-input" placeholder="e.g. Islamabad, Dubai, Baku, Bangkok" required>
                </div>
              </div>

              <div class="awtt-form-row">
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-fl-dep">{ICONS['calendar']} Departure Date</label>
                  <input type="date" id="awtt-fl-dep" class="awtt-input" required>
                </div>
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-fl-ret">{ICONS['calendar']} Return Date (Optional)</label>
                  <input type="date" id="awtt-fl-ret" class="awtt-input">
                </div>
              </div>

              <div class="awtt-form-row">
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-fl-pax">{ICONS['users']} Number of Passengers</label>
                  <input type="number" id="awtt-fl-pax" class="awtt-input" min="1" max="20" value="1" required>
                </div>
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-fl-phone">{ICONS['phone']} Contact Phone / WhatsApp</label>
                  <input type="tel" id="awtt-fl-phone" class="awtt-input" placeholder="+92 300 1234567" required>
                </div>
              </div>

              <div style="margin-top:20px;">
                <button type="button" class="awtt-btn awtt-btn-primary awtt-btn-lg" style="width:100%;" onclick="showToast('Flight inquiry submitted! Our Karachi ticketing desk will contact you with options.')">
                  Request Flight Quotation {ICONS['arrowRight']}
                </button>
              </div>
            </form>
          </div>

          <div style="margin-top:54px;max-width:880px;margin-left:auto;margin-right:auto;">
            <h3 style="font-size:1.3rem;color:var(--awtt-primary);margin-bottom:14px;">Airline Booking Information</h3>
            <p style="font-size:0.94rem;color:var(--awtt-text-muted);line-height:1.65;margin-bottom:14px;">
              Air Waves Travel &amp; Tours provides personalized ticketing assistance for domestic routes within Pakistan (PIA, Airblue, SereneAir, Fly Jinnah) and international routes across the Middle East, Asia, and Europe.
            </p>
            <p style="font-size:0.94rem;color:var(--awtt-text-muted);line-height:1.65;">
              Because airline fares and seat allocations fluctuate continuously according to inventory tiers, our ticketing agents personally review and secure the most advantageous schedules and baggage allowances for your journey.
            </p>
          </div>
        </div>
      </div>
    </section>


    <!-- ============================================== -->
    <!-- VIEW: HOTELS                                   -->
    <!-- ============================================== -->
    <section class="awtt-view" id="awtt-view-hotels">
      <div class="awtt-section">
        <div class="awtt-container">
          <div class="awtt-section-header">
            <h1>Hotel Reservations</h1>
            <p>Reliable accommodation arrangements for business, family vacations, and group journeys.</p>
          </div>

          <div class="awtt-booking-box">
            <form id="awtt-hotels-page-form">
              <div class="awtt-form-row">
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-ht-city">{ICONS['hotel']} Destination City / Region</label>
                  <input type="text" id="awtt-ht-city" class="awtt-input" placeholder="e.g. Hunza, Skardu, Dubai, Baku, Makkah" required>
                </div>
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-ht-pref">Hotel Category Preference</label>
                  <select id="awtt-ht-pref" class="awtt-select">
                    <option value="Comfort / 3-Star">Comfort / 3-Star</option>
                    <option value="Deluxe / 4-Star">Deluxe / 4-Star</option>
                    <option value="Luxury / 5-Star">Luxury / 5-Star</option>
                    <option value="Family Suite / Resort">Family Suite / Resort</option>
                  </select>
                </div>
              </div>

              <div class="awtt-form-row">
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-ht-cin">{ICONS['calendar']} Check-in Date</label>
                  <input type="date" id="awtt-ht-cin" class="awtt-input" required>
                </div>
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-ht-cout">{ICONS['calendar']} Check-out Date</label>
                  <input type="date" id="awtt-ht-cout" class="awtt-input" required>
                </div>
              </div>

              <div class="awtt-form-row">
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-ht-rooms">{ICONS['hotel']} Number of Rooms</label>
                  <input type="number" id="awtt-ht-rooms" class="awtt-input" min="1" max="10" value="1" required>
                </div>
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-ht-guests">{ICONS['users']} Number of Guests</label>
                  <input type="number" id="awtt-ht-guests" class="awtt-input" min="1" max="30" value="2" required>
                </div>
              </div>

              <div class="awtt-form-group" style="margin-bottom:18px;">
                <label class="awtt-form-label" for="awtt-ht-notes">Specific Preferences / Requirements</label>
                <input type="text" id="awtt-ht-notes" class="awtt-input" placeholder="e.g. Near Haram in Makkah, river view in Hunza, extra bedding for children">
              </div>

              <button type="button" class="awtt-btn awtt-btn-primary awtt-btn-lg" style="width:100%;" onclick="showToast('Hotel reservation request submitted! Our team will provide availability and rates.')">
                Request Hotel Rates {ICONS['arrowRight']}
              </button>
            </form>
          </div>
        </div>
      </div>
    </section>


    <!-- ============================================== -->
    <!-- VIEW: TRAVEL PACKAGES                          -->
    <!-- ============================================== -->
    <section class="awtt-view" id="awtt-view-packages">
      <div class="awtt-section">
        <div class="awtt-container">
          <div class="awtt-section-header">
            <h1>Curated Travel Packages</h1>
            <p>Explore our popular domestic and international itineraries. All packages can be customized to match your travel dates and group preferences.</p>
          </div>

          <div class="awtt-packages-grid">
            {packages_html}
          </div>
        </div>
      </div>
    </section>


    <!-- ============================================== -->
    <!-- VIEW: BOOKING                                  -->
    <!-- ============================================== -->
    <section class="awtt-view" id="awtt-view-booking">
      <div class="awtt-section">
        <div class="awtt-container">
          <div class="awtt-section-header">
            <h1>Request a Travel Booking</h1>
            <p>Provide your travel details below and our consultants in Karachi will promptly assist with quotations, flight schedules, and booking options.</p>
          </div>

          <div class="awtt-booking-box">
            <form id="awtt-booking-form">
              <div class="awtt-form-row">
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-book-name">Full Name *</label>
                  <input type="text" id="awtt-book-name" class="awtt-input" placeholder="Your full name" required>
                </div>
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-book-phone">Phone / WhatsApp Number *</label>
                  <input type="tel" id="awtt-book-phone" class="awtt-input" placeholder="+92 309 5795928" required>
                </div>
              </div>

              <div class="awtt-form-row">
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-book-email">Email Address</label>
                  <input type="email" id="awtt-book-email" class="awtt-input" placeholder="name@example.com">
                </div>
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-book-service">Service Required *</label>
                  <select id="awtt-book-service" class="awtt-select">
                    <option value="Flight Booking">Flight Booking</option>
                    <option value="Domestic Tour Package">Domestic Tour Package</option>
                    <option value="International Holiday Package">International Holiday Package</option>
                    <option value="Hotel Reservation">Hotel Reservation</option>
                    <option value="Umrah Travel Assistance">Umrah Travel Assistance</option>
                  </select>
                </div>
              </div>

              <div class="awtt-form-row">
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-book-dest">Target Destination / Route *</label>
                  <input type="text" id="awtt-book-dest" class="awtt-input" placeholder="e.g. Hunza Valley, Dubai, Skardu, Baku" required>
                </div>
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-book-pax">Number of Travelers</label>
                  <input type="number" id="awtt-book-pax" class="awtt-input" min="1" max="50" value="2">
                </div>
              </div>

              <div class="awtt-form-row">
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-book-date">{ICONS['calendar']} Preferred Travel Date</label>
                  <input type="date" id="awtt-book-date" class="awtt-input">
                </div>
                <div class="awtt-form-group">
                  <label class="awtt-form-label" for="awtt-book-ret">{ICONS['calendar']} Return Date (If Round Trip)</label>
                  <input type="date" id="awtt-book-ret" class="awtt-input">
                </div>
              </div>

              <div class="awtt-form-group" style="margin-bottom:20px;">
                <label class="awtt-form-label" for="awtt-book-notes">Additional Requirements or Special Inquiries</label>
                <textarea id="awtt-book-notes" class="awtt-textarea" rows="4" placeholder="Mention preferred airlines, hotel ratings, budget guidelines, or any special requests..."></textarea>
              </div>

              <button type="submit" class="awtt-btn awtt-btn-primary awtt-btn-lg" style="width:100%;">
                Submit Booking Request {ICONS['arrowRight']}
              </button>
            </form>
          </div>

          <!-- Direct Office Information -->
          <div style="margin-top:48px;display:grid;grid-template-columns:repeat(auto-fit, minmax(260px, 1fr));gap:20px;">
            <div class="awtt-contact-card">
              <div class="awtt-contact-card-icon">{ICONS['mapPin']}</div>
              <div>
                <h4>Office Location</h4>
                <p>U-34, Eastern Pride, Block 15 Gulistan-e-Johar, Karachi, 75290, Pakistan</p>
              </div>
            </div>
            <div class="awtt-contact-card">
              <div class="awtt-contact-card-icon">{ICONS['phone']}</div>
              <div>
                <h4>Call / WhatsApp</h4>
                <p><a href="tel:+923095795928">+92 309 5795928</a></p>
              </div>
            </div>
            <div class="awtt-contact-card">
              <div class="awtt-contact-card-icon">{ICONS['mail']}</div>
              <div>
                <h4>Email Inquiries</h4>
                <p><a href="mailto:airwaves.travel.tour@gmail.com">airwaves.travel.tour@gmail.com</a></p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>


    <!-- ============================================== -->
    <!-- VIEW: BLOG                                     -->
    <!-- ============================================== -->
    <section class="awtt-view" id="awtt-view-blog">
      <div class="awtt-section">
        <div class="awtt-container">
          <div class="awtt-section-header">
            <h1>Travel Guides &amp; Insights</h1>
            <p>Practical travel advice, destination highlights, and flight booking tips from our experienced team in Karachi.</p>
          </div>

          <div class="awtt-blog-grid">
            {blog_cards_html}
          </div>
        </div>
      </div>
    </section>


    <!-- ============================================== -->
    <!-- VIEW: PRIVACY POLICY                           -->
    <!-- ============================================== -->
    <section class="awtt-view" id="awtt-view-privacy">
      <div class="awtt-section">
        <div class="awtt-container">
          <div class="awtt-content-wrap">
            <h1>Privacy Policy</h1>
            <p>Last updated: September 2026</p>
            <p>
              Air Waves Travel &amp; Tours ("we", "our", or "us") respects your privacy and is dedicated to safeguarding personal information collected when you visit our website or communicate with our travel agency in Karachi, Pakistan.
            </p>

            <h2>Information We Collect</h2>
            <p>
              When you submit an inquiry, search for flight or hotel rates, or request a booking through our website, we may collect:
            </p>
            <ul>
              <li>Contact details such as your full name, phone number, and email address.</li>
              <li>Travel details including travel dates, destinations, passenger counts, and cabin preferences.</li>
              <li>Passport or identification details strictly when required to issue confirmed airline tickets or hotel vouchers.</li>
            </ul>

            <h2>How We Use Your Information</h2>
            <p>
              The information you provide is used exclusively to:
            </p>
            <ul>
              <li>Process your travel requests, flight ticketing, and accommodation arrangements.</li>
              <li>Communicate quotes, flight schedules, and itinerary updates.</li>
              <li>Answer your inquiries submitted via our booking forms or WhatsApp channel.</li>
            </ul>

            <h2>Information Sharing with Service Providers</h2>
            <p>
              To complete your travel arrangements, relevant information (such as passenger names, dates of birth, and travel documents) is shared with airlines, hotels, and transport service providers as necessary to issue valid tickets and hotel vouchers. We do not sell or trade your personal data to unauthorized third parties.
            </p>

            <h2>Data Security</h2>
            <p>
              We implement reasonable security practices to protect your information from unauthorized access, alteration, or disclosure.
            </p>

            <h2>Contact Us</h2>
            <p>
              If you have any questions regarding this Privacy Policy or your personal information, please contact us:
            </p>
            <p>
              <strong>AIR WAVES TRAVEL &amp; TOURS</strong><br>
              U-34, Eastern Pride, Block 15 Gulistan-e-Johar, Karachi, 75290, Pakistan<br>
              Phone: +92 309 5795928<br>
              Email: <a href="mailto:airwaves.travel.tour@gmail.com">airwaves.travel.tour@gmail.com</a>
            </p>
          </div>
        </div>
      </div>
    </section>


    <!-- ============================================== -->
    <!-- VIEW: TERMS & CONDITIONS                       -->
    <!-- ============================================== -->
    <section class="awtt-view" id="awtt-view-terms">
      <div class="awtt-section">
        <div class="awtt-container">
          <div class="awtt-content-wrap">
            <h1>Terms &amp; Conditions</h1>
            <p>Last updated: September 2026</p>
            <p>
              Welcome to Air Waves Travel &amp; Tours. By browsing this website, requesting quotes, or engaging our travel booking services, you agree to comply with and be bound by the following terms and conditions.
            </p>

            <h2>1. Booking Requests &amp; Quotations</h2>
            <p>
              All booking inquiries, flight searches, and package requests submitted through this website constitute requests for quotation. Bookings are only finalized once confirmed by our ticketing team and official tickets or vouchers are issued.
            </p>

            <h2>2. Airline &amp; Hotel Availability</h2>
            <p>
              Airfares and accommodation rates are determined by third-party airlines and hotel operators and are subject to availability at the time of ticket issuance. We make every effort to provide accurate, competitive fare guidance.
            </p>

            <h2>3. Travel Documentation &amp; Visas</h2>
            <p>
              It is the sole responsibility of each traveler to ensure they possess valid passports (typically valid for at least 6 months), valid visas, health documentation, and compliance with entry regulations for their destination countries.
            </p>

            <h2>4. Cancellations, Changes &amp; Refunds</h2>
            <p>
              Cancellation and modification rules for flight tickets and hotel reservations are governed by the respective airline and hotel carrier policies. Any applicable refund or change fee is subject to the fare rules of the purchased ticket.
            </p>

            <h2>5. Limitation of Liability</h2>
            <p>
              While Air Waves Travel &amp; Tours works diligently to secure reliable travel arrangements, we act as a booking agent for airlines, hotels, and transport operators. We cannot be held liable for flight delays, schedule alterations, weather disruptions, or unforeseen events beyond our direct control.
            </p>

            <h2>6. Governing Contact</h2>
            <p>
              For inquiries regarding these terms, please contact:
            </p>
            <p>
              <strong>AIR WAVES TRAVEL &amp; TOURS</strong><br>
              U-34, Eastern Pride, Block 15 Gulistan-e-Johar, Karachi, 75290, Pakistan<br>
              Phone: +92 309 5795928<br>
              Email: <a href="mailto:airwaves.travel.tour@gmail.com">airwaves.travel.tour@gmail.com</a>
            </p>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- FOOTER -->
  <footer class="awtt-footer">
    <div class="awtt-container">
      <div class="awtt-footer-grid">
        <div class="awtt-footer-col">
          <div style="font-weight:700;font-size:1.25rem;color:#ffffff;line-height:1.2;">
            AIR WAVES TRAVEL &amp; TOURS
          </div>
          <p class="awtt-footer-desc">
            Professional travel agency located in Gulistan-e-Johar, Karachi. Offering domestic and international flight ticketing, hotel reservations, and customized holiday packages.
          </p>
          <div class="awtt-topbar-social">
            <a href="https://www.facebook.com/AirwavesTraveltours/" target="_blank" rel="noopener noreferrer" class="awtt-social-link" aria-label="Facebook Profile">
              {ICONS['facebook']}
            </a>
            <a href="https://www.instagram.com/airwaves_travel/" target="_blank" rel="noopener noreferrer" class="awtt-social-link" aria-label="Instagram Profile">
              {ICONS['instagram']}
            </a>
          </div>
        </div>

        <div class="awtt-footer-col">
          <h4>Navigation</h4>
          <div class="awtt-footer-links">
            <a href="#home">Home</a>
            <a href="#about">About Us</a>
            <a href="#destinations">Destinations</a>
            <a href="#flights">Flights</a>
            <a href="#hotels">Hotels</a>
            <a href="#packages">Tour Packages</a>
            <a href="#booking">Booking Request</a>
            <a href="#blog">Travel Blog</a>
          </div>
        </div>

        <div class="awtt-footer-col">
          <h4>Top Destinations</h4>
          <div class="awtt-footer-links">
            <a href="#destinations">Hunza Valley</a>
            <a href="#destinations">Skardu</a>
            <a href="#destinations">Swat &amp; Kalam</a>
            <a href="#destinations">Dubai, UAE</a>
            <a href="#destinations">Baku, Azerbaijan</a>
            <a href="#destinations">Turkey</a>
            <a href="#destinations">Makkah &amp; Madinah</a>
          </div>
        </div>

        <div class="awtt-footer-col">
          <h4>Contact Karachi Office</h4>
          <div class="awtt-footer-contact">
            <div class="awtt-footer-contact-item">
              {ICONS['mapPin']}
              <span>U-34, Eastern Pride, Block 15 Gulistan-e-Johar, Karachi, 75290, Pakistan</span>
            </div>
            <div class="awtt-footer-contact-item">
              {ICONS['phone']}
              <a href="tel:+923095795928" style="color:#ffffff;">+92 309 5795928</a>
            </div>
            <div class="awtt-footer-contact-item">
              {ICONS['mail']}
              <a href="mailto:airwaves.travel.tour@gmail.com" style="color:#ffffff;">airwaves.travel.tour@gmail.com</a>
            </div>
          </div>
        </div>
      </div>

      <div class="awtt-footer-bottom">
        <div>
          &copy; 2026 AIR WAVES TRAVEL &amp; TOURS. All Rights Reserved.
        </div>
        <div class="awtt-footer-legal">
          <a href="#privacy">Privacy Policy</a>
          <a href="#terms">Terms &amp; Conditions</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- DEDICATED FLOATING WHATSAPP CHAT BUTTON (NO WhatsApp as social icon!) -->
  <a href="https://wa.me/923095795928?text=Hello%20Air%20Waves%20Travel%20%26%20Tours,%20I%20would%20like%20to%20inquire%20about%20travel%20services." target="_blank" rel="noopener noreferrer" class="awtt-whatsapp-float" aria-label="Chat on WhatsApp with Air Waves Travel &amp; Tours">
    <span class="awtt-whatsapp-icon">{ICONS['whatsapp']}</span>
    <span>Chat on WhatsApp</span>
  </a>

  <!-- ARTICLE MODAL READER -->
  <div id="awtt-article-modal" style="display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(10,37,64,0.7);z-index:3500;align-items:center;justify-content:center;padding:20px;">
    <div style="background:#ffffff;border-radius:12px;max-width:740px;width:100%;max-height:88vh;overflow-y:auto;padding:32px;position:relative;box-shadow:0 15px 35px rgba(0,0,0,0.25);">
      <button type="button" onclick="closeArticleModal()" style="position:absolute;top:18px;right:18px;background:#f1f5f9;border-radius:50%;width:36px;height:36px;display:flex;align-items:center;justify-content:center;" aria-label="Close Article">
        {ICONS['close']}
      </button>
      <div id="awtt-modal-cat" style="font-size:0.8rem;font-weight:600;color:var(--awtt-accent);text-transform:uppercase;margin-bottom:8px;"></div>
      <h2 id="awtt-modal-title" style="font-size:1.65rem;font-weight:700;color:var(--awtt-primary);margin-bottom:20px;line-height:1.3;"></h2>
      <div id="awtt-modal-body" style="font-size:0.95rem;color:var(--awtt-text-main);line-height:1.7;"></div>
      <div style="margin-top:28px;padding-top:18px;border-top:1px solid #e2e8f0;display:flex;justify-content:flex-end;">
        <button type="button" class="awtt-btn awtt-btn-secondary" onclick="closeArticleModal()">Close</button>
      </div>
    </div>
  </div>

  <!-- TOAST NOTIFICATION -->
  <div class="awtt-toast" id="awtt-toast">
    {ICONS['shieldCheck']}
    <span id="awtt-toast-msg">Notification message</span>
  </div>

  <script>
{JS}
  </script>

</body>
</html>
'''
    return full_html

if __name__ == "__main__":
    html_output = build_html()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_output)
    print("Successfully built index.html! Size:", len(html_output), "bytes")
