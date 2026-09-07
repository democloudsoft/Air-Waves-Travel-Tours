"""Script to assemble the complete production index.html for Air Waves Travel & Tours"""
import os

html_head = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Air Waves Travel &amp; Tours | Flight Booking, Tour Packages &amp; Hotels in Karachi</title>
  <meta name="description" content="Air Waves Travel &amp; Tours is a premier travel agency in Gulistan-e-Johar, Karachi offering domestic and international flight bookings, customized tour packages, hotel reservations, and travel assistance.">
  <meta name="keywords" content="Air Waves Travel &amp; Tours Karachi, Travel Agency in Karachi, Travel Agency in Gulistan-e-Johar Karachi, Flight Booking in Karachi, International Travel Services in Karachi, Hotel Booking in Karachi, Travel Packages from Karachi">
  <link rel="canonical" href="https://airwavestravel.com/">

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://airwavestravel.com/">
  <meta property="og:title" content="Air Waves Travel &amp; Tours | Travel Agency in Karachi">
  <meta property="og:description" content="Book domestic &amp; international flights, curated holiday packages, and hotel stays with Air Waves Travel &amp; Tours, Karachi.">
  <meta property="og:image" content="https://iili.io/n2S5CCl.png">

  <!-- Twitter / X -->
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
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": "24.9180",
      "longitude": "67.1332"
    },
    "sameAs": [
      "https://www.facebook.com/AirwavesTraveltours/",
      "https://www.instagram.com/airwaves_travel/"
    ],
    "priceRange": "$$"
  }
  </script>
'''

print("Head prepared")
