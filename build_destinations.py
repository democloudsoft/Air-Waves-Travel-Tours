# -*- coding: utf-8 -*-
"""
Full single-file index.html generator for Air Waves Travel & Tours
"""
import json
from awtt_styles import CSS
from awtt_icons import ICONS
from awtt_scripts import JS

# Verify icons are present
assert "plane" in ICONS
assert "whatsapp" in ICONS
assert "facebook" in ICONS
assert "instagram" in ICONS

destinations_data = [
    # Domestic
    {
        "id": "hunza",
        "name": "Hunza Valley",
        "cat": "domestic",
        "badge": "Northern Pakistan",
        "img": "https://iili.io/nH2hwTQ.jpg",
        "alt": "Hunza Valley mountain landscape and scenic valley in Pakistan",
        "desc": "Majestic peaks, tranquil terraced villages, Attabad Lake, and Karimabad historical forts in Gilgit-Baltistan."
    },
    {
        "id": "skardu",
        "name": "Skardu",
        "cat": "domestic",
        "badge": "Northern Pakistan",
        "img": "https://iili.io/nH2h4yv.jpg",
        "alt": "Skardu valley and cold desert landscape in Gilgit Baltistan Pakistan",
        "desc": "Gateway to the high Karakorams, Upper Kachura Lake, Shangrila Resort, and the iconic Katpana Cold Desert."
    },
    {
        "id": "naranKaghan",
        "name": "Naran-Kaghan",
        "cat": "domestic",
        "badge": "Khyber Pakhtunkhwa",
        "img": "https://iili.io/nH2hgaa.jpg",
        "alt": "Naran Kaghan scenic valley and Saif-ul-Malook lake landscape in Pakistan",
        "desc": "Lush alpine meadows, Kunhar River, Babusar Top, and the legendary waters of Lake Saif-ul-Malook."
    },
    {
        "id": "swatKalamMahodand",
        "name": "Swat-Kalam-Mahodand",
        "cat": "domestic",
        "badge": "Khyber Pakhtunkhwa",
        "img": "https://iili.io/nHJr0js.jpg",
        "alt": "Swat Kalam Mahodand scenic valley landscape and river in Pakistan",
        "desc": "Known as the Switzerland of Pakistan, featuring dense pine forests, Kalam Valley, and Mahodand Lake."
    },
    {
        "id": "karachi",
        "name": "Karachi",
        "cat": "domestic",
        "badge": "Sindh",
        "img": "https://iili.io/nHd5O5g.jpg",
        "alt": "Karachi cityscape and coastal travel destination in Pakistan",
        "desc": "Pakistan's bustling economic hub on the Arabian Sea, featuring Clifton Beach, historic architecture, and rich dining."
    },
    {
        "id": "islamabad",
        "name": "Islamabad",
        "cat": "domestic",
        "badge": "Federal Capital",
        "img": "https://iili.io/n9OS5pn.jpg",
        "alt": "Islamabad Faisal Mosque and Margalla Hills landscape in Pakistan",
        "desc": "The picturesque capital nestled against the Margalla Hills, featuring Faisal Mosque and serene greenery."
    },
    {
        "id": "lahore",
        "name": "Lahore",
        "cat": "domestic",
        "badge": "Punjab",
        "img": "https://iili.io/nHdBog4.jpg",
        "alt": "Lahore Badshahi Mosque and historical heritage in Pakistan",
        "desc": "The cultural heart of Pakistan, famous for Badshahi Mosque, Lahore Fort, vibrant food streets, and heritage."
    },
    # International
    {
        "id": "dubai",
        "name": "Dubai",
        "cat": "international",
        "badge": "United Arab Emirates",
        "img": "https://iili.io/nH2hvG1.webp",
        "alt": "Dubai skyline architecture and modern cityscape in UAE",
        "desc": "World-class architectural marvels, luxury shopping, Burj Khalifa, and exhilarating desert safari excursions."
    },
    {
        "id": "baku",
        "name": "Baku",
        "cat": "international",
        "badge": "Azerbaijan",
        "img": "https://iili.io/nH2h86F.jpg",
        "alt": "Baku architecture and Caspian Sea city scenery in Azerbaijan",
        "desc": "The vibrant capital on the Caspian Sea, combining ancient Old City fortress walls with modern Flame Towers."
    },
    {
        "id": "bangkok",
        "name": "Bangkok",
        "cat": "international",
        "badge": "Thailand",
        "img": "https://iili.io/nH2hQnI.jpg",
        "alt": "Bangkok grand temples and river landscape in Thailand",
        "desc": "Dynamic city life, ornate Buddhist temples, lively night markets, and delicious culinary traditions."
    },
    {
        "id": "turkey",
        "name": "Turkey",
        "cat": "international",
        "badge": "Eurasia",
        "img": "https://iili.io/nH2hsZN.webp",
        "alt": "Turkey historical scenery and Cappadocia landscape",
        "desc": "Where East meets West across the Bosphorus in Istanbul, alongside surreal hot air balloon vistas in Cappadocia."
    },
    {
        "id": "malaysia",
        "name": "Malaysia",
        "cat": "international",
        "badge": "Southeast Asia",
        "img": "https://iili.io/nH32FWb.jpg",
        "alt": "Malaysia Kuala Lumpur Petronas Towers and tropical landscape",
        "desc": "Kuala Lumpur's Petronas Twin Towers, lush tea plantations in Cameron Highlands, and diverse culture."
    },
    {
        "id": "singapore",
        "name": "Singapore",
        "cat": "international",
        "badge": "Southeast Asia",
        "img": "https://iili.io/nH37Ujs.jpg",
        "alt": "Singapore Marina Bay Sands and futuristic garden architecture",
        "desc": "Clean and modern city-state with futuristic Gardens by the Bay, Marina Bay Sands, and Sentosa Island."
    },
    {
        "id": "maldives",
        "name": "Maldives",
        "cat": "international",
        "badge": "Indian Ocean",
        "img": "https://iili.io/nH3XDAv.png",
        "alt": "Maldives luxury overwater bungalows and turquoise ocean",
        "desc": "Pristine white-sand atolls, turquoise lagoons, and private island resorts for relaxing beach getaways."
    },
    # Religious
    {
        "id": "makkah",
        "name": "Makkah",
        "cat": "religious",
        "badge": "Saudi Arabia",
        "img": "https://iili.io/nH3m8EN.jpg",
        "alt": "Makkah Masjid al-Haram holy sanctuary in Saudi Arabia",
        "desc": "The holiest city in Islam, home to Masjid al-Haram and the Kaaba. Complete Umrah assistance and hotel packages."
    },
    {
        "id": "madinah",
        "name": "Madinah",
        "cat": "religious",
        "badge": "Saudi Arabia",
        "img": "https://iili.io/nH3bYVp.webp",
        "alt": "Madinah Prophet's Mosque Al-Masjid an-Nabawi in Saudi Arabia",
        "desc": "The blessed city of the Prophet, featuring the peaceful courtyards of Al-Masjid an-Nabawi and sacred Ziyarat sites."
    }
]

print("Loaded destinations:", len(destinations_data))
