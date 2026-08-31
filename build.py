#!/usr/bin/env python3
"""Static site generator for Creek Line Limited.
Regenerates every HTML page from the templates and content defined below.
Run: python3 build.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Category data
# ---------------------------------------------------------------------------
CATEGORIES = [
    {
        "slug": "auto-spare-parts",
        "nav": "Auto Spare Parts",
        "summary": "OEM and aftermarket components sourced and verified against exact specifications.",
        "banner": "Auto Spare Parts Sourced to Exact Specification",
        "title_tag": "Auto Spare Parts",
        "overview": "Creek Line Limited sources OEM and aftermarket parts for passenger, commercial, and heavy-duty vehicles. Each part is verified against the applicable specification &mdash; dimensions, materials, and markings &mdash; prior to shipment. This standard applies equally to individual component orders and bulk distribution orders.",
        "extra": [
            "Parts are checked against technical drawings or reference samples where these are provided by the client.",
            "Order volumes range from individual components to full container shipments, with the same verification process applied in each case.",
        ],
        "cta_line": "Submit a part number or technical drawing.",
        "cta_button": "Request an Auto Parts Quote",
        "icon": "gear",
    },
    {
        "slug": "heavy-equipment-machinery",
        "nav": "Heavy Equipment &amp; Machinery",
        "summary": "Construction, agricultural, and industrial machinery, inspected prior to shipment.",
        "banner": "Heavy Equipment and Machinery, Inspected Prior to Delivery",
        "title_tag": "Heavy Equipment &amp; Machinery",
        "overview": "Creek Line Limited sources construction, earthmoving, agricultural, and industrial machinery. Each unit is inspected against the agreed specification prior to shipment, and spare parts availability is confirmed in advance of purchase.",
        "extra": [
            "New and refurbished equipment options are available, with the relevant trade-offs presented clearly to the client prior to purchase.",
            "Spare parts sourcing can be arranged on an ongoing basis following the initial purchase.",
        ],
        "cta_line": "Tell us about the machinery you need to source.",
        "cta_button": "Request a Machinery Quote",
        "icon": "machinery",
    },
    {
        "slug": "electronics-it-equipment",
        "nav": "Electronics &amp; IT Equipment",
        "summary": "Computing and networking equipment sourced for corporate and institutional buyers.",
        "banner": "Electronics and IT Equipment Sourced for Corporate Buyers",
        "title_tag": "Electronics &amp; IT Equipment",
        "overview": "Creek Line Limited sources computers, networking equipment, and office electronics for corporate and institutional buyers. All orders are supported by warranty and authenticity documentation, and the company supports both individual and recurring bulk orders.",
        "extra": [
            "Suppliers are required to provide documentation confirming product authenticity and applicable warranty terms.",
            "Recurring, high-volume orders are managed under standard procurement terms agreed with the client.",
        ],
        "cta_line": "Send us your equipment list or technical requirements.",
        "cta_button": "Request an Electronics Quote",
        "icon": "chip",
    },
    {
        "slug": "software-trading",
        "nav": "Software Trading",
        "summary": "Licensed enterprise software supplied through authorized vendors and distributors.",
        "banner": "Licensed Software Supplied Through Authorized Channels",
        "title_tag": "Software Trading",
        "overview": "Creek Line Limited supplies enterprise and business software through authorized vendors and distributors. Each license is provided with documentation confirming its authenticity and transferability.",
        "extra": [
            "All licenses are verified for authenticity and proper transfer documentation prior to supply.",
            "Vendor partnerships allow for competitive pricing without compromising licensing compliance.",
        ],
        "cta_line": "Tell us which licenses or software titles you require.",
        "cta_button": "Request a Software Quote",
        "icon": "window",
    },
    {
        "slug": "textiles",
        "nav": "Textiles",
        "summary": "Fabrics and finished textiles sourced for fashion, home, and industrial applications.",
        "banner": "Textiles Verified Against Approved Samples",
        "title_tag": "Textiles",
        "overview": "Creek Line Limited sources fabrics and finished textiles for fashion, home goods, and industrial applications. Bulk shipments are checked against the approved sample prior to dispatch to confirm consistency in weight, weave, and color.",
        "extra": [
            "Sample approval is required prior to bulk production.",
            "Minimum order quantities vary by manufacturer and can be discussed on request.",
        ],
        "cta_line": "Share your fabric specification or reference sample.",
        "cta_button": "Request a Textiles Quote",
        "icon": "textile",
    },
    {
        "slug": "household-electronics-equipment",
        "nav": "Household Electronics &amp; Equipment",
        "summary": "Appliances and equipment sourced for retail and commercial distribution.",
        "banner": "Household Equipment Sourced for Retail and Distribution",
        "title_tag": "Household Electronics &amp; Equipment",
        "overview": "Creek Line Limited sources household appliances and equipment for retailers, distributors, and commercial buyers. Each order is matched to the target market on brand, price tier, and applicable compliance documentation before it is placed.",
        "extra": [
            "Recurring bulk orders are supported, with consistent quality standards applied across shipments.",
            "Multiple brand and price-tier options are available to match different target markets.",
        ],
        "cta_line": "Tell us what you need for your retail or distribution range.",
        "cta_button": "Request a Household Equipment Quote",
        "icon": "appliance",
    },
    {
        "slug": "food-production-equipment",
        "nav": "Food &amp; Food Production Equipment",
        "summary": "Food products and processing equipment sourced with full regulatory documentation.",
        "banner": "Food Products and Production Equipment",
        "title_tag": "Food &amp; Food Production Equipment",
        "overview": "Creek Line Limited sources both food products and the equipment used to process and package them. All orders in this category are supported by the certifications and safety documentation required for import and resale in the relevant market.",
        "extra": [
            "Certifications and safety documentation are confirmed prior to order placement.",
            "Product and equipment sourcing can be managed within a single engagement where both are required.",
        ],
        "cta_line": "Tell us about the products or equipment you need.",
        "cta_button": "Request a Food Sector Quote",
        "icon": "food",
    },
    {
        "slug": "chemicals",
        "nav": "Chemicals",
        "summary": "Industrial, agricultural, and specialty chemicals supplied with complete safety documentation.",
        "banner": "Chemicals Supplied With Complete Documentation",
        "title_tag": "Chemicals",
        "overview": "Creek Line Limited sources industrial, agricultural, and specialty chemicals. Each order is supplied with complete safety data sheets and applicable regulatory documentation.",
        "extra": [
            "Documentation is prepared in advance of shipment to support customs clearance.",
            "Logistics partners are selected on the basis of experience in chemical handling and transport.",
        ],
        "cta_line": "Tell us which chemicals or specifications you require.",
        "cta_button": "Request a Chemicals Quote",
        "icon": "flask",
    },
]

CAT_BY_SLUG = {c["slug"]: c for c in CATEGORIES}

# ---------------------------------------------------------------------------
# Icons (inline SVG, stroke-based, currentColor)
# ---------------------------------------------------------------------------
ICONS = {
    "gear": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3.2"/><path d="M19.4 13.5a1.7 1.7 0 0 0 .34 1.87l.06.06a2.05 2.05 0 1 1-2.9 2.9l-.06-.06a1.7 1.7 0 0 0-1.87-.34 1.7 1.7 0 0 0-1.03 1.56v.17a2.05 2.05 0 1 1-4.1 0v-.1a1.7 1.7 0 0 0-1.11-1.56 1.7 1.7 0 0 0-1.87.34l-.06.06a2.05 2.05 0 1 1-2.9-2.9l.06-.06a1.7 1.7 0 0 0 .34-1.87 1.7 1.7 0 0 0-1.56-1.03h-.17a2.05 2.05 0 1 1 0-4.1h.1a1.7 1.7 0 0 0 1.56-1.11 1.7 1.7 0 0 0-.34-1.87l-.06-.06a2.05 2.05 0 1 1 2.9-2.9l.06.06a1.7 1.7 0 0 0 1.87.34h.08a1.7 1.7 0 0 0 1.03-1.56v-.17a2.05 2.05 0 1 1 4.1 0v.1a1.7 1.7 0 0 0 1.03 1.56h.08a1.7 1.7 0 0 0 1.87-.34l.06-.06a2.05 2.05 0 1 1 2.9 2.9l-.06.06a1.7 1.7 0 0 0-.34 1.87v.08a1.7 1.7 0 0 0 1.56 1.03h.17a2.05 2.05 0 1 1 0 4.1h-.1a1.7 1.7 0 0 0-1.56 1.03z"/></svg>',
    "machinery": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 20h13"/><path d="M4 20V9l6-4 3 3v12"/><path d="M13 11h4l4 4v3a1 1 0 0 1-1 1h-1"/><circle cx="8" cy="20" r="1.6"/><circle cx="17.5" cy="20" r="1.6"/></svg>',
    "chip": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="7" y="7" width="10" height="10" rx="1.4"/><path d="M9 3v3M15 3v3M9 18v3M15 18v3M3 9h3M3 15h3M18 9h3M18 15h3"/></svg>',
    "window": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4.5" width="18" height="15" rx="1.6"/><path d="M3 9h18"/><path d="M9 14l-2 2 2 2M15 14l2 2-2 2"/></svg>',
    "textile": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4c3 2 3 5 0 7s-3 5 0 7"/><path d="M9 4c3 2 3 5 0 7s-3 5 0 7"/><path d="M14 4c3 2 3 5 0 7s-3 5 0 7"/><path d="M19 4c1 2 1 5 0 7s-1 5 0 7"/></svg>',
    "appliance": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="2.5" width="14" height="19" rx="1.6"/><circle cx="12" cy="14" r="3.4"/><path d="M8 6.5h.01M11 6.5h.01"/></svg>',
    "food": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 8.5l8-5 8 5"/><path d="M4 8.5V19a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1V8.5"/><path d="M9 20v-6h6v6"/></svg>',
    "flask": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M9 2.5h6"/><path d="M10 3v6.2L4.6 18a1.6 1.6 0 0 0 1.4 2.5h12a1.6 1.6 0 0 0 1.4-2.5L14 9.2V3"/><path d="M7.5 15h9"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "handshake": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12l4-4 3.5 3.5a1.5 1.5 0 0 0 2 0l.2-.2a1.5 1.5 0 0 1 2 0L17 14"/><path d="M22 12l-4-4-3 3"/><path d="M8 8l3-3a2 2 0 0 1 2.5-.2L18 8"/><path d="M6.5 14L10 17.5a1.7 1.7 0 0 0 2.4 0 1.7 1.7 0 0 0 2.4 0 1.7 1.7 0 0 0 2.4 0L19 15.5"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.5l7.5 3v6c0 5-3.2 8.4-7.5 10-4.3-1.6-7.5-5-7.5-10v-6z"/><path d="M8.7 12l2.2 2.2 4.4-4.4"/></svg>',
    "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="3.6"/><path d="M4.5 20c1.4-3.6 4.4-5.5 7.5-5.5s6.1 1.9 7.5 5.5"/></svg>',
    "globe": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.7 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.7-3.8-9S9.5 5.6 12 3z"/></svg>',
    "clipboard": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="5.5" y="4.5" width="13" height="16" rx="1.6"/><path d="M9 4.5V3a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v1.5"/><path d="M8.5 11h7M8.5 15h7"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="1.6"/><path d="M3.5 6.5l8.5 6 8.5-6"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s7-6.5 7-12a7 7 0 1 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.4"/></svg>',
}

def icon(name):
    return ICONS[name]

# ---------------------------------------------------------------------------
# Shared partials
# ---------------------------------------------------------------------------

def nav(active=""):
    dropdown_items = "\n".join(
        f'<a href="{c["slug"]}.html">{c["nav"]}</a>' for c in CATEGORIES
    )
    def cls(key):
        return " active" if active == key else ""
    return f'''  <div class="topbar">
    <div class="container">
      <span>Global Procurement and Sourcing &mdash; Hong Kong</span>
      <div class="topbar-links">
        <a href="mailto:info@creek-line.com">info@creek-line.com</a>
      </div>
    </div>
  </div>
  <nav class="navbar">
    <div class="container">
      <a href="index.html" class="logo-text"><img src="images/logo.jpg" alt="Creek Line Limited"> Creek Line Limited</a>
      <button class="burger" aria-label="Toggle navigation" aria-expanded="false"><span></span><span></span><span></span></button>
      <ul class="nav-links">
        <li><a href="index.html" class="{cls('home')}">Home</a></li>
        <li><a href="about.html" class="{cls('about')}">About</a></li>
        <li class="has-dropdown">
          <a href="products.html" class="{cls('products')}">Products &amp; Services <span class="chevron"></span></a>
          <div class="dropdown">
{dropdown_items}
            <div class="dropdown-foot"><a href="products.html">View all categories &rarr;</a></div>
          </div>
        </li>
        <li><a href="process.html" class="{cls('process')}">Procurement Process</a></li>
        <li><a href="suppliers.html" class="{cls('suppliers')}">Supplier Network</a></li>
        <li><a href="contact.html" class="{cls('contact')}">Contact</a></li>
        <li><a href="quote.html" class="nav-cta">Request a Quote</a></li>
      </ul>
    </div>
  </nav>
'''.replace('class=""', '')


def footer():
    cat_links = "\n".join(
        f'<li><a href="{c["slug"]}.html">{c["nav"]}</a></li>' for c in CATEGORIES[:6]
    )
    return f'''  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <div class="footer-brand">Creek Line Limited</div>
          <p>A procurement and trading company managing sourcing, quality verification, and logistics across eight core categories, connecting buyers worldwide with verified manufacturers.</p>
        </div>
        <div>
          <h4>Company</h4>
          <ul>
            <li><a href="about.html">About Us</a></li>
            <li><a href="process.html">Procurement Process</a></li>
            <li><a href="suppliers.html">Supplier Network</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>
        <div>
          <h4>Categories</h4>
          <ul>
{cat_links}
            <li><a href="products.html">View all &rarr;</a></li>
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <ul>
            <li><a href="mailto:info@creek-line.com">info@creek-line.com</a></li>
            <li>RM A08 Unit F3, 2/F, Koon Wo Industrial Building,<br>Nos. 63&ndash;75 Ta Chuen Ping Street,<br>Kwai Chung, New Territories, Hong Kong</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; 2026 Creek Line Limited. All rights reserved.</span>
        <span><a href="quote.html">Request a Quote</a></span>
      </div>
    </div>
  </footer>
  <script src="js/main.js"></script>
'''


def page(*, active, title, description, canonical, body, extra_head="", body_class=""):
    body_class_attr = f' class="{body_class}"' if body_class else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://creek-line.com/{canonical}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
  <link rel="icon" href="favicon.ico" type="image/x-icon">
{extra_head}</head>
<body{body_class_attr}>
{nav(active)}
{body}
{footer()}
</body>
</html>
'''

def reveal(html, extra_class=""):
    cls = f"reveal {extra_class}".strip()
    return f'<div class="{cls}">{html}</div>'

# ---------------------------------------------------------------------------
# Category summary cards (reused on Home + Products landing)
# ---------------------------------------------------------------------------

def category_cards(cols=4, with_link=True):
    cards = []
    for c in CATEGORIES:
        link = f'\n          <a class="card-link stretched" href="{c["slug"]}.html">Learn more {icon("arrow")}</a>' if with_link else ""
        cards.append(f'''        <div class="icon-card reveal">
          <div class="icon">{icon(c["icon"])}</div>
          <h3>{c["nav"]}</h3>
          <p>{c["summary"]}</p>{link}
        </div>''')
    return f'      <div class="grid-cards{" cols-3" if cols == 3 else ""}">\n' + "\n".join(cards) + "\n      </div>\n"


def cat_nav(current_slug):
    links = []
    for c in CATEGORIES:
        cls = " active" if c["slug"] == current_slug else ""
        links.append(f'<a href="{c["slug"]}.html" class="{cls}">{c["nav"]}</a>'.replace(' class=""', ''))
    return '      <div class="cat-nav">\n        ' + "\n        ".join(links) + "\n      </div>\n"

print("build.py loaded: run build_all.py to generate pages")
