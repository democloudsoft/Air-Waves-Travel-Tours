# -*- coding: utf-8 -*-
import sys

def get_html():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Air Waves Travel &amp; Tours | Travel Agency in Karachi | Flights, Hotels &amp; Tour Packages</title>
  <meta name="description" content="Air Waves Travel &amp; Tours is a premier travel agency in Gulistan-e-Johar, Karachi. Offering domestic and international flight bookings, tour packages, hotel reservations, and travel assistance.">
  <meta name="keywords" content="Air Waves Travel &amp; Tours Karachi, Travel Agency in Karachi, Travel Agency in Gulistan-e-Johar Karachi, Flight Booking in Karachi, International Travel Services in Karachi, Hotel Booking in Karachi, Travel Packages from Karachi, Umrah Travel Karachi">
  <link rel="canonical" href="https://airwavestravel.com/">

  <!-- Open Graph / Social Media -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://airwavestravel.com/">
  <meta property="og:title" content="Air Waves Travel &amp; Tours | Travel Agency in Karachi">
  <meta property="og:description" content="Book domestic &amp; international flights, curated holiday packages, and hotel stays with Air Waves Travel &amp; Tours, Karachi.">
  <meta property="og:image" content="https://iili.io/n2S5CCl.png">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Air Waves Travel &amp; Tours | Travel Agency in Karachi">
  <meta name="twitter:description" content="Book domestic &amp; international flights, curated holiday packages, and hotel stays with Air Waves Travel &amp; Tours, Karachi.">
  <meta name="twitter:image" content="https://iili.io/n2S5CCl.png">

  <!-- Poppins Font from Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "TravelAgency",
    "name": "AIR WAVES TRAVEL & TOURS",
    "image": "https://iili.io/n2S5CCl.png",
    "telephone": "+923095795928",
    "email": "airwaves.travel.tour@gmail.com",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "U-34, Eastern Pride, Block 15 Gulistan-e-Johar",
      "addressLocality": "Karachi",
      "postalCode": "75290",
      "addressCountry": "PK"
    },
    "sameAs": [
      "https://www.facebook.com/AirwavesTraveltours/",
      "https://www.instagram.com/airwaves_travel/"
    ]
  }
  </script>
'''

with open("generate_site_part_a.py", "w", encoding="utf-8") as f:
    f.write(get_html())
print("Part A written")
