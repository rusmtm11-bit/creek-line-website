#!/usr/bin/env python3
import os
from build import (
    ROOT, CATEGORIES, CAT_BY_SLUG, icon, nav, footer, page, reveal,
    category_cards, cat_nav,
)

OUT = []

def write(path, content):
    full = os.path.join(ROOT, path)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    OUT.append(path)

CHECK = icon("check")

# ===========================================================================
# HOME
# ===========================================================================
home_body = f'''  <header class="hero">
    <div class="container">
      <div class="reveal">
        <div class="eyebrow">Procurement &amp; Sourcing</div>
        <h1>Procurement Built on Verified Manufacturing Relationships</h1>
        <p class="lede">Creek Line Limited manages procurement across industries, working directly with manufacturers on multiple continents to ensure that products meet exact specifications.</p>
        <div class="hero-actions">
          <a href="quote.html" class="btn btn-primary">Request a Quote {icon("arrow")}</a>
          <a href="products.html" class="btn btn-outline">Explore Categories</a>
        </div>
      </div>
      <div class="hero-visual reveal" style="--reveal-delay:0.15s">
        <img src="images/logo.jpg" alt="Creek Line Limited">
      </div>
    </div>
  </header>

  <div class="marquee-wrap">
    <div class="marquee-track">
      {"".join(f'<span>{c["nav"]}</span>' for c in CATEGORIES) * 2}
    </div>
  </div>

  <section class="section">
    <div class="container container--narrow reveal" style="text-align:center">
      <p style="font-size:1.15rem;color:var(--text-light)">Creek Line Limited is a procurement and trading company serving businesses that require reliable access to global manufacturing. Our team manages sourcing, quality verification, and logistics across core categories, allowing clients to focus on their own operations rather than on supplier management.</p>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-head center reveal">
        <h2 class="section-title">Eight Core Sourcing Categories</h2>
        <p class="section-subtitle">Each category is managed by team members with direct experience in the relevant industry standards and buyer requirements.</p>
      </div>
      <div class="stagger">
{category_cards()}      </div>
      <div style="text-align:center;margin-top:1rem" class="reveal">
        <a href="products.html" class="btn btn-outline">View All Products &amp; Services {icon("arrow")}</a>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center reveal">
        <h2 class="section-title">Why Clients Work With Creek Line Limited</h2>
      </div>
      <div class="split reveal">
        <div>
          <div class="value-row">
            <div class="icon">{icon("handshake")}</div>
            <div>
              <h3>Direct Manufacturer Relationships</h3>
              <p>Creek Line Limited works directly with manufacturers rather than through intermediary brokers, which reduces cost and improves the accuracy of communication regarding specifications and timelines.</p>
            </div>
          </div>
          <div class="value-row">
            <div class="icon">{icon("shield")}</div>
            <div>
              <h3>Pre-Shipment Quality Verification</h3>
              <p>Every order is verified against the agreed specification prior to shipment, through sample inspection, documentation review, or both, depending on the product category.</p>
            </div>
          </div>
          <div class="value-row">
            <div class="icon">{icon("user")}</div>
            <div>
              <h3>Dedicated Account Management</h3>
              <p>Each client is assigned a single point of contact for the duration of the relationship, from initial enquiry through subsequent orders.</p>
            </div>
          </div>
        </div>
        <div class="panel">
          <h3>Our procurement process is structured and documented at every stage.</h3>
          <p style="color:var(--text-light);margin-bottom:1.5rem">From enquiry to delivery, every order follows the same six-stage process, so clients know exactly what to expect at each point.</p>
          <a href="process.html" class="btn btn-outline">See the Full Process {icon("arrow")}</a>
        </div>
      </div>
    </div>
  </section>

  <section class="stat-strip section-alt">
    <div class="container">
      <div class="stat-grid">
        <div class="stat reveal"><div class="num"><span data-count="8">0</span></div><div class="label">Core Sourcing Categories</div></div>
        <div class="stat reveal" style="--reveal-delay:0.1s"><div class="num"><span data-count="1">0</span> Day</div><div class="label">Standard Enquiry Response Time</div></div>
        <div class="stat reveal" style="--reveal-delay:0.2s"><div class="num"><span data-count="6">0</span></div><div class="label">Stage Procurement Process</div></div>
        <div class="stat reveal" style="--reveal-delay:0.3s"><div class="num"><span data-count="100" data-suffix="%">0%</span></div><div class="label">Orders Pre-Shipment Verified</div></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container reveal" style="text-align:center">
      <div class="section-head center">
        <h2 class="section-title">Working With Creek Line Limited</h2>
        <p class="section-subtitle">Organizations that have engaged Creek Line Limited for procurement services rely on a single, accountable partner across sourcing, verification, and logistics.</p>
      </div>
    </div>
  </section>

  <section class="section-tight">
    <div class="container">
      <div class="callout reveal">
        <div>
          <h2>Submit your procurement requirements.</h2>
          <p>Our team will respond within one business day.</p>
        </div>
        <a href="quote.html" class="btn btn-primary">Request a Quote {icon("arrow")}</a>
      </div>
    </div>
  </section>
'''

write("index.html", page(
    active="home",
    title="Creek Line Limited | Global Procurement and Sourcing",
    description="Creek Line Limited provides procurement and sourcing services across different industries, connecting buyers worldwide with verified manufacturers.",
    canonical="",
    body=home_body,
))

# ===========================================================================
# ABOUT
# ===========================================================================
about_body = f'''  <header class="page-hero">
    <div class="container reveal">
      <div class="breadcrumb"><a href="index.html">Home</a> / About</div>
      <h1>About Creek Line Limited</h1>
      <p class="lede">A procurement company built on verified manufacturing relationships.</p>
    </div>
  </header>

  <section class="section">
    <div class="container">
      <div class="split reveal">
        <div>
          <h2>Our Story</h2>
          <p>Creek Line Limited was established to address a specific challenge faced by businesses sourcing internationally: identifying manufacturers capable of meeting exact specifications reliably and at a fair price.</p>
          <p>Since then, the company has expanded from a limited number of categories into eight core areas &mdash; automotive parts, heavy machinery, electronics, software licensing, textiles, household goods, food and food production equipment, and industrial chemicals &mdash; supported by manufacturing relationships across multiple regions.</p>
          <p>Our approach has remained consistent throughout this expansion: assess the client&rsquo;s requirement thoroughly, identify a manufacturer capable of meeting it, and manage the process through to delivery.</p>
        </div>
        <div class="panel">
          <h3>Global Presence</h3>
          <p>Creek Line Limited maintains sourcing relationships across multiple manufacturing regions, including Mainland China, Southeast Asia, and South Asia.</p>
          <p style="margin-top:1rem">The company is headquartered in Hong Kong.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="grid-cards cols-2 stagger">
        <div class="icon-card reveal">
          <div class="icon">{icon("clipboard")}</div>
          <h3>Mission</h3>
          <p>To provide businesses with reliable, transparent access to global manufacturing.</p>
        </div>
        <div class="icon-card reveal" style="--reveal-delay:0.1s">
          <div class="icon">{icon("globe")}</div>
          <h3>Vision</h3>
          <p>To be recognized as a dependable procurement partner across the industries we serve.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head center reveal">
        <h2 class="section-title">Core Values</h2>
      </div>
      <div class="grid-cards stagger">
        <div class="icon-card reveal">
          <h3>Integrity</h3>
          <p>Creek Line Limited represents the interests of its clients. Supplier recommendations are based on capability and fit, not on commercial arrangements with any individual manufacturer.</p>
        </div>
        <div class="icon-card reveal" style="--reveal-delay:0.08s">
          <h3>Accuracy</h3>
          <p>Specifications, quantities, and delivery timelines are treated as binding commitments rather than estimates.</p>
        </div>
        <div class="icon-card reveal" style="--reveal-delay:0.16s">
          <h3>Transparency</h3>
          <p>Clients receive clear, documented information at each stage of an order.</p>
        </div>
        <div class="icon-card reveal" style="--reveal-delay:0.24s">
          <h3>Continuity</h3>
          <p>Creek Line Limited aims to build long-term relationships with clients through consistent performance across successive orders.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-tight">
    <div class="container">
      <div class="callout reveal">
        <div>
          <h2>Work with a procurement partner that documents every stage.</h2>
          <p>Get in touch to discuss your sourcing requirements.</p>
        </div>
        <a href="contact.html" class="btn btn-primary">Contact Us {icon("arrow")}</a>
      </div>
    </div>
  </section>
'''

write("about.html", page(
    active="about",
    title="About Creek Line Limited",
    description="Creek Line Limited is a procurement company serving clients across eight industries through verified manufacturing partnerships worldwide.",
    canonical="about.html",
    body=about_body,
))

# ===========================================================================
# PRODUCTS LANDING
# ===========================================================================
products_body = f'''  <header class="page-hero">
    <div class="container reveal">
      <div class="breadcrumb"><a href="index.html">Home</a> / Products &amp; Services</div>
      <h1>Products and Services</h1>
      <p class="lede">Creek Line Limited sources across eight core categories. Each category is managed by team members with direct experience in the relevant industry standards and buyer requirements.</p>
    </div>
  </header>

  <section class="section">
    <div class="container">
      <div class="stagger">
{category_cards()}      </div>
    </div>
  </section>

  <section class="section-tight">
    <div class="container">
      <div class="callout reveal">
        <div>
          <h2>Don&rsquo;t see your category listed?</h2>
          <p>Submit your requirements and our team will confirm whether we can source it.</p>
        </div>
        <a href="quote.html" class="btn btn-primary">Request a Quote {icon("arrow")}</a>
      </div>
    </div>
  </section>
'''

write("products.html", page(
    active="products",
    title="Products and Services | Creek Line Limited",
    description="Creek Line Limited sources across eight product categories, including auto parts, machinery, electronics, textiles, and chemicals.",
    canonical="products.html",
    body=products_body,
))

# ===========================================================================
# CATEGORY PAGES
# ===========================================================================
for c in CATEGORIES:
    extra_items = "\n".join(f'<li><span class="icon">{CHECK}</span>{item}</li>' for item in c["extra"])
    others = [o for o in CATEGORIES if o["slug"] != c["slug"]]
    related = others[:3]
    related_cards = "\n".join(
        f'''        <div class="icon-card reveal">
          <div class="icon">{icon(o["icon"])}</div>
          <h3>{o["nav"]}</h3>
          <p>{o["summary"]}</p>
          <a class="card-link stretched" href="{o["slug"]}.html">Learn more {icon("arrow")}</a>
        </div>''' for o in related
    )

    body = f'''  <header class="cat-hero">
    <div class="cat-icon-mark">{icon(c["icon"])}</div>
    <div class="container reveal">
      <div class="breadcrumb"><a href="index.html">Home</a> / <a href="products.html">Products &amp; Services</a> / {c["nav"]}</div>
      <h1 style="max-width:760px">{c["banner"]}</h1>
    </div>
  </header>

  <section class="section-tight">
    <div class="container">
{cat_nav(c["slug"])}    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="container">
      <div class="split reveal">
        <div>
          <h2>Overview</h2>
          <p>{c["overview"]}</p>
        </div>
        <div>
          <div class="info-panel">
            <h4>Additional Information</h4>
            <ul class="checklist">
{extra_items}
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section-tight">
    <div class="container">
      <div class="callout reveal">
        <div>
          <h2>{c["cta_line"]}</h2>
          <p>Our team will review the request and respond within one business day.</p>
        </div>
        <a href="quote.html?category={c["slug"]}" class="btn btn-primary">{c["cta_button"]} {icon("arrow")}</a>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-head center reveal">
        <h2 class="section-title">Other Categories</h2>
      </div>
      <div class="grid-cards cols-3 stagger">
{related_cards}
      </div>
    </div>
  </section>
'''

    write(f"{c['slug']}.html", page(
        active="products",
        title=f"{c['title_tag']} | Creek Line Limited",
        description=c["summary"],
        canonical=f"{c['slug']}.html",
        body=body,
    ))

# ===========================================================================
# PROCESS
# ===========================================================================
steps = [
    ("Enquiry and Requirements Review", "The client submits product, specification, quantity, and timeline information. Our team reviews the request and follows up with any clarifying questions within one business day."),
    ("Supplier Identification", "Suitable manufacturers are identified based on capability, pricing, and lead time relative to the stated requirement."),
    ("Quotation and Confirmation", "A formal quotation is provided, including pricing, lead time, and applicable certifications. The order is placed upon client confirmation."),
    ("Quality Verification", "Prior to shipment, the order is verified against the agreed specification through the method appropriate to the category — inspection, documentation review, or both."),
    ("Logistics and Delivery", "Shipping and customs documentation are managed on the client’s behalf, with status updates provided throughout."),
    ("Post-Delivery Support", "The assigned point of contact remains available to address any issues following delivery, and for subsequent orders."),
]
step_html = "\n".join(
    f'''        <div class="timeline-step reveal">
          <div class="marker">{i+1}</div>
          <h3>{i+1}. {name}</h3>
          <p>{desc}</p>
        </div>''' for i, (name, desc) in enumerate(steps)
)

process_body = f'''  <header class="page-hero">
    <div class="container reveal">
      <div class="breadcrumb"><a href="index.html">Home</a> / Procurement Process</div>
      <h1>Our Procurement Process</h1>
      <p class="lede">The following outlines the standard process applied to orders managed by Creek Line Limited, from initial enquiry through to delivery.</p>
    </div>
  </header>

  <section class="section">
    <div class="container">
      <div class="timeline">
{step_html}
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="grid-cards cols-2 stagger">
        <div class="icon-card reveal">
          <div class="icon">{icon("shield")}</div>
          <h3>Quality Verification</h3>
          <p>Quality verification is incorporated into every order rather than applied only when specifically requested. The method used depends on the product category and may include measurement, sample inspection, or documentation review.</p>
        </div>
        <div class="icon-card reveal" style="--reveal-delay:0.1s">
          <div class="icon">{icon("globe")}</div>
          <h3>Logistics</h3>
          <p>Shipping and customs arrangements are managed by logistics partners selected for reliability on the specific route and region involved, in order to support consistent delivery timelines.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-tight">
    <div class="container">
      <div class="callout reveal">
        <div>
          <h2>Ready to start an enquiry?</h2>
          <p>Submit your requirements and our team will respond within one business day.</p>
        </div>
        <a href="quote.html" class="btn btn-primary">Request a Quote {icon("arrow")}</a>
      </div>
    </div>
  </section>
'''

write("process.html", page(
    active="process",
    title="Procurement Process | Creek Line Limited",
    description="An overview of Creek Line Limited's procurement process, from initial enquiry to delivery.",
    canonical="process.html",
    body=process_body,
))

# ===========================================================================
# SUPPLIERS
# ===========================================================================
suppliers_body = f'''  <header class="page-hero">
    <div class="container reveal">
      <div class="breadcrumb"><a href="index.html">Home</a> / Supplier Network</div>
      <h1>Our Supplier Network</h1>
      <p class="lede">Creek Line Limited maintains relationships with manufacturing partners across multiple regions. Each supplier is reviewed prior to inclusion in a client order, and performance is monitored on an ongoing basis thereafter.</p>
    </div>
  </header>

  <section class="section">
    <div class="container">
      <div class="split reveal">
        <div>
          <h2>Sourcing Regions</h2>
          <p>Creek Line Limited sources from manufacturing partners across a number of regions, including Mainland China, Southeast Asia, and South Asia, selected on the basis of category-specific capability.</p>
        </div>
        <div class="panel">
          <h3>Supplier Evaluation</h3>
          <p>Suppliers are evaluated on production capability, quality control practices, compliance documentation, and a verifiable track record prior to inclusion in our network. This evaluation continues throughout the course of the relationship.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container reveal" style="text-align:center">
      <div class="section-head center">
        <h2 class="section-title">Partner Brands</h2>
        <p class="section-subtitle">A list of manufacturers and brands represented in our network will be published once logos and permissions are confirmed.</p>
      </div>
    </div>
  </section>

  <section class="section-tight">
    <div class="container">
      <div class="callout reveal">
        <div>
          <h2>Looking for a specific manufacturer or region?</h2>
          <p>Tell us your requirement and we will confirm supplier availability.</p>
        </div>
        <a href="quote.html" class="btn btn-primary">Request a Quote {icon("arrow")}</a>
      </div>
    </div>
  </section>
'''

write("suppliers.html", page(
    active="suppliers",
    title="Our Supplier Network | Creek Line Limited",
    description="Creek Line Limited works with a vetted network of manufacturing partners across multiple regions.",
    canonical="suppliers.html",
    body=suppliers_body,
))

# ===========================================================================
# QUOTE
# ===========================================================================
category_options = "\n".join(
    f'              <option value="{c["nav"].replace("&amp;", "&")}">{c["nav"].replace("&amp;", "&")}</option>' for c in CATEGORIES
)

quote_body = f'''  <header class="page-hero">
    <div class="container reveal">
      <div class="breadcrumb"><a href="index.html">Home</a> / Request a Quote</div>
      <h1>Request a Quote</h1>
      <p class="lede">Submit your requirements using the form below. Our team will review the request and respond within one business day.</p>
    </div>
  </header>

  <section class="section">
    <div class="container container--narrow">
      <div class="form-card reveal">
        <form id="quoteForm" data-form="quote" action="https://formsubmit.co/info@creek-line.com" method="POST" enctype="multipart/form-data">
          <input type="hidden" name="_subject" value="New quote request &ndash; Creek Line Limited website">
          <input type="hidden" name="_captcha" value="false">
          <input type="hidden" name="_template" value="table">
          <input type="hidden" name="_next" value="thankyou.html">

          <div class="form-grid">
            <div class="form-group full">
              <label class="static" for="category">Category</label>
              <select id="category" name="category" required>
                <option value="">Select a category&hellip;</option>
{category_options}
              <option value="Other">Other</option>
              </select>
            </div>

            <div class="form-group full">
              <label class="static" for="details">Product / Service Details</label>
              <textarea id="details" name="product_service_details" required></textarea>
            </div>

            <div class="form-group">
              <label class="static" for="quantity">Quantity</label>
              <input type="text" id="quantity" name="quantity" required>
            </div>

            <div class="form-group">
              <label class="static" for="location">Delivery Location</label>
              <input type="text" id="location" name="delivery_location" required>
            </div>

            <div class="form-group full">
              <label class="static" for="specs">Specifications or Requirements</label>
              <textarea id="specs" name="specifications_or_requirements"></textarea>
            </div>

            <div class="form-group full">
              <label class="static" for="attachment">Attachment</label>
              <input type="file" id="attachment" name="attachment">
              <div class="form-hint">Specification sheet, drawing, or reference document. Accepted formats: PDF, JPG, PNG, DOCX, XLSX. Maximum file size: 10MB.</div>
            </div>

            <div class="form-group">
              <label class="static" for="name">Full Name</label>
              <input type="text" id="name" name="full_name" required>
            </div>

            <div class="form-group">
              <label class="static" for="company">Company Name</label>
              <input type="text" id="company" name="company_name" required>
            </div>

            <div class="form-group">
              <label class="static" for="email">Email Address</label>
              <input type="email" id="email" name="email" required>
            </div>

            <div class="form-group">
              <label class="static" for="phone">Phone Number (with country code)</label>
              <input type="tel" id="phone" name="phone_number" placeholder="+1 000 000 0000" required>
            </div>
          </div>

          <div class="consent-group">
            <input type="checkbox" id="consent" name="consent" value="yes" required>
            <label for="consent">I agree to the processing of my personal data in accordance with the applicable law.</label>
          </div>
          <div class="consent-error">Please confirm your consent to the processing of personal data before sending the request.</div>

          <button type="submit" class="btn btn-primary btn-submit">Submit Request</button>
        </form>
      </div>
    </div>
  </section>

  <script>
    (function () {{
      var params = new URLSearchParams(window.location.search);
      var cat = params.get('category');
      if (cat) {{
        var select = document.getElementById('category');
        for (var i = 0; i < select.options.length; i++) {{
          if (select.options[i].value.toLowerCase().replace(/[^a-z]+/g, '-').indexOf(cat.toLowerCase()) !== -1 ||
              cat.toLowerCase().indexOf(select.options[i].value.toLowerCase().replace(/&/g, 'and').replace(/[^a-z]+/g, '-')) !== -1) {{
            select.selectedIndex = i;
          }}
        }}
      }}
    }})();
  </script>
'''

write("quote.html", page(
    active="products",
    title="Request a Quote | Creek Line Limited",
    description="Submit your procurement requirements to Creek Line Limited for a formal quotation.",
    canonical="quote.html",
    body=quote_body,
))

# ===========================================================================
# CONTACT
# ===========================================================================
contact_body = f'''  <header class="page-hero">
    <div class="container reveal">
      <div class="breadcrumb"><a href="index.html">Home</a> / Contact</div>
      <h1>Contact Us</h1>
      <p class="lede">For procurement enquiries or general questions, please contact us using the details below.</p>
    </div>
  </header>

  <section class="section">
    <div class="container">
      <div class="split reveal">
        <div>
          <div class="info-panel">
            <h4>Email</h4>
            <p><a href="mailto:info@creek-line.com" style="color:var(--blue);text-decoration:none;font-weight:600">info@creek-line.com</a></p>
          </div>
          <div class="info-panel">
            <h4>Registered Office &mdash; Hong Kong</h4>
            <p>Creek Line Limited<br>RM A08 Unit F3, 2/F, Koon Wo Industrial Building,<br>Nos. 63&ndash;75 Ta Chuen Ping Street,<br>Kwai Chung, New Territories, Hong Kong</p>
          </div>
          <div class="info-panel">
            <h4>Response Time</h4>
            <p>Our team reviews all enquiries and responds within one business day.</p>
          </div>
        </div>

        <div class="form-card">
          <form id="contactForm" data-form="contact" action="https://formsubmit.co/info@creek-line.com" method="POST">
            <input type="hidden" name="_subject" value="New contact form message &ndash; Creek Line Limited website">
            <input type="hidden" name="_captcha" value="false">
            <input type="hidden" name="_template" value="table">
            <input type="hidden" name="_next" value="thankyou.html">

            <div class="form-group">
              <label class="static" for="c_name">Full Name</label>
              <input type="text" id="c_name" name="full_name" required>
            </div>
            <div class="form-group">
              <label class="static" for="c_email">Email Address</label>
              <input type="email" id="c_email" name="email" required>
            </div>
            <div class="form-group">
              <label class="static" for="c_subject">Subject</label>
              <input type="text" id="c_subject" name="subject" required>
            </div>
            <div class="form-group">
              <label class="static" for="c_message">Message</label>
              <textarea id="c_message" name="message" required></textarea>
            </div>

            <div class="consent-group">
              <input type="checkbox" id="c_consent" name="consent" value="yes" required>
              <label for="c_consent">I agree to the processing of my personal data in accordance with the applicable law.</label>
            </div>
            <div class="consent-error">Please confirm your consent to the processing of personal data before sending the message.</div>

            <button type="submit" class="btn btn-primary btn-submit">Send Message</button>
          </form>
        </div>
      </div>
    </div>
  </section>
'''

write("contact.html", page(
    active="contact",
    title="Contact | Creek Line Limited",
    description="Contact details for Creek Line Limited.",
    canonical="contact.html",
    body=contact_body,
))

# ===========================================================================
# THANK YOU
# ===========================================================================
thankyou_body = f'''  <section class="section">
    <div class="container thankyou-section reveal is-visible">
      <div class="thankyou-icon">{CHECK}</div>
      <h1 class="thankyou-title">Thank You</h1>
      <p class="thankyou-message">Your request has been received and will be reviewed by our team within one business day.</p>
      <a href="index.html" class="btn btn-primary">Return to Home {icon("arrow")}</a>
    </div>
  </section>
'''

write("thankyou.html", page(
    active="",
    title="Thank You | Creek Line Limited",
    description="Thank you for contacting Creek Line Limited.",
    canonical="thankyou.html",
    body=thankyou_body,
))

print(f"Generated {len(OUT)} pages:")
for p in OUT:
    print(" -", p)
