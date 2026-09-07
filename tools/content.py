# -*- coding: utf-8 -*-
"""Copy for the case studies and articles.

Editing this file and re-running tools/build.py regenerates the pages. The
generated HTML is committed, so the site still works with no build step — the
generator only exists so thirteen pages cannot drift apart from each other.

HONESTY RULE: the studio has no clients yet. Every case study is written as an
example build and says so in its own first line. Do not add a client name, a
logo or a results metric here until there is a real project behind it.
"""

# --------------------------------------------------------------------------
# CASE STUDIES
# --------------------------------------------------------------------------
# thumb: reuses one of the .proj__thumb--a/b/c line drawings from the home page

CASE_STUDIES = [
    {
        "slug": "restaurant-ordering-app",
        "glance": [
            ("Type", "Mobile app + web dashboards"),
            ("Build time", "About 7 weeks"),
            ("Platforms", "iOS, Android, tablet"),
            ("Starts at", "₹20,000*"),
        ],
        "pains": [
            "Every repeat order pays 25–30% commission to an aggregator",
            "Phone orders get written down wrong at peak time",
            "No idea which outlet is behind until a customer complains",
            "Sold-out items are only discovered after someone has paid",
        ],
        "category": "Mobile App",
        "thumb": "a",
        "title": "Restaurant Ordering App",
        "summary": "Menu, cart, live order tracking and a simple kitchen dashboard "
                   "for a multi-outlet restaurant.",
        "situation": [
            "A restaurant with three outlets takes orders over the phone and on a "
            "delivery aggregator that keeps 25–30% of every bill. The owner wants "
            "their own ordering channel for regulars, so repeat customers stop "
            "costing commission on every order.",
            "The hard part is never the menu screen. It is what happens after "
            "someone taps Pay: which kitchen sees the order, what the customer "
            "sees while they wait, and what happens when an item is out of stock "
            "at one outlet but not the others.",
        ],
        "scope": [
            ("Menu that the owner controls",
             "Items, prices, photos, and per-outlet availability. Marking something "
             "sold out takes one tap and applies to that outlet only."),
            ("Cart and checkout",
             "Address, delivery or pickup, and a payment gateway. No account "
             "required to order — a phone number and an OTP is the whole signup."),
            ("Live order tracking",
             "Accepted → cooking → out for delivery → delivered, pushed to the "
             "customer's phone as it changes. This is the screen that decides "
             "whether people order again."),
            ("Kitchen dashboard",
             "A tablet screen per outlet showing incoming orders large enough to "
             "read across a kitchen, with one button to advance an order's state."),
            ("Owner view",
             "Today's orders, today's revenue, and which items are actually "
             "selling. Three numbers, not a business-intelligence suite."),
        ],
        "excluded": [
            "Loyalty points and coupon engines — worth building once there is "
            "repeat-order data to design them around.",
            "In-house delivery-rider tracking. Most restaurants at this size use a "
            "third-party rider fleet at first.",
            "Table reservations and dine-in QR ordering. A separate problem with a "
            "separate set of screens.",
        ],
        "stack": [
            ("Customer app", "React Native, so iOS and Android ship from one codebase"),
            ("Kitchen and owner screens", "A responsive web app — a tablet browser "
             "is cheaper and easier to replace than a native install"),
            ("Backend", "Node with a Postgres database"),
            ("Realtime", "WebSockets for order state, so the kitchen screen updates "
             "without anyone refreshing anything"),
            ("Payments", "A standard Indian gateway (Razorpay or equivalent)"),
        ],
        "timeline": [
            ("Week 1", "Menu structure, outlet model and the order state machine "
                       "agreed on a call. This is the part that is expensive to get wrong."),
            ("Weeks 2–4", "Customer app and checkout."),
            ("Weeks 5–6", "Kitchen dashboard, live tracking, owner view."),
            ("Week 7", "One outlet runs it live for a week before the others switch on."),
        ],
        "note": "The app-store fees, the payment gateway's per-transaction cut and "
                "the cloud hosting are billed to you directly by those providers. "
                "They are not part of the build price.",
    },
    {
        "slug": "coaching-management-platform",
        "glance": [
            ("Type", "Web app, staff and parents"),
            ("Build time", "About 8 weeks"),
            ("Platforms", "Desktop and mobile browser"),
            ("Starts at", "₹20,000*"),
        ],
        "pains": [
            "Attendance on paper, fees in one person's spreadsheet",
            "Test scores scattered across WhatsApp groups",
            "Parents phone the front desk for every update",
            "Fee reminders go out when someone remembers",
        ],
        "category": "Web App",
        "thumb": "b",
        "title": "Coaching Management Platform",
        "summary": "Batches, attendance, online tests and fee payments in one "
                   "dashboard for students and staff.",
        "situation": [
            "A coaching institute runs eleven batches across two centres. "
            "Attendance is on paper, fees are tracked in a spreadsheet that one "
            "person owns, test scores are on WhatsApp, and parents phone the front "
            "desk to ask how their child is doing.",
            "Nothing here is technically difficult. The value is entirely in "
            "getting four scattered records into one place, and in the fee "
            "reminders going out on their own instead of when someone remembers.",
        ],
        "scope": [
            ("Batches and enrolment",
             "Students, batches, subjects and the timetable. One student can sit in "
             "more than one batch without being entered twice."),
            ("Attendance",
             "Marked from a teacher's phone in under a minute per class. Absentees "
             "generate a message to the parent the same evening."),
            ("Online tests",
             "Objective tests with automatic scoring, a per-student score history "
             "and a batch-level view of which topics the class got wrong."),
            ("Fees",
             "Instalment schedule per student, an online payment link, an automatic "
             "reminder before each due date, and a receipt the parent can keep."),
            ("Parent access",
             "Read-only: attendance, test scores, fee status. This one screen "
             "removes most of the calls to the front desk."),
        ],
        "excluded": [
            "Live video classes. Zoom or Meet already does this better than a "
            "custom build ever will — link them from the timetable instead.",
            "A content library and recorded lectures. A big product on its own; "
            "worth doing after the operational side is running.",
            "Subjective and handwritten answer evaluation.",
        ],
        "stack": [
            ("Web app", "React, used by staff on desktop and parents on phones"),
            ("Backend", "Node with Postgres — the data here is deeply relational "
             "and a relational database is the honest answer"),
            ("Payments", "A gateway with recurring-payment support for instalments"),
            ("Messaging", "A transactional SMS or WhatsApp Business provider for "
             "reminders"),
            ("Hosting", "A single cloud instance; this load does not need anything "
             "elaborate"),
        ],
        "timeline": [
            ("Week 1", "The data model: what a batch is, what happens when a student "
                       "switches one, how a part payment is recorded."),
            ("Weeks 2–4", "Batches, enrolment, attendance and the staff dashboard."),
            ("Weeks 5–6", "Fees, payment links and automated reminders."),
            ("Weeks 7–8", "Tests, scoring and the parent view."),
        ],
        "note": "Every SMS and WhatsApp message costs a few paise, billed by the "
                "messaging provider directly to you. At a few thousand messages a "
                "month it is small, but it is a running cost and it is not included "
                "in the build price.",
    },
    {
        "slug": "business-automation-dashboard",
        "glance": [
            ("Type", "Scheduled jobs + dashboard"),
            ("Build time", "About 6 weeks"),
            ("Platforms", "Browser, alerts to email or chat"),
            ("Starts at", "₹20,000*"),
        ],
        "pains": [
            "Two hours a day spent exporting and pasting",
            "One person understands the master file",
            "Six people read yesterday's numbers, not today's",
            "Everyone sees everything, including margins",
        ],
        "category": "Web App",
        "thumb": "b",
        "title": "Business Automation Dashboard",
        "summary": "Replaces daily spreadsheet work with automated reports, alerts "
                   "and role-based access.",
        "situation": [
            "Someone spends the first two hours of every working day exporting "
            "files, pasting them into a master spreadsheet, fixing what did not "
            "line up, and emailing the result to six people. That file has become "
            "load-bearing, and exactly one person understands it.",
            "This is the most common software problem in a growing business, and "
            "the most under-rated one to fix. It is not glamorous. It buys back "
            "roughly five hundred hours a year and removes a single point of failure.",
        ],
        "scope": [
            ("Pull instead of paste",
             "Scheduled jobs that fetch from the source systems directly — an API, "
             "a database, an SFTP drop, or a mailbox that receives a daily CSV."),
            ("The rules, written down",
             "Every fix that currently happens by hand becomes an explicit, tested "
             "transformation. The ones that cannot be pinned down get flagged for a "
             "human rather than silently guessed."),
            ("The dashboard",
             "The numbers those six people actually read, live, instead of as "
             "yesterday's attachment."),
            ("Alerts",
             "A message when a number crosses a threshold or when a source fails to "
             "arrive. Silence should mean everything is fine."),
            ("Role-based access",
             "Finance sees margins, the floor sees volumes. Right now the "
             "spreadsheet shows everyone everything."),
        ],
        "excluded": [
            "Predictive analytics and forecasting. Get the reporting trustworthy "
            "first; a forecast on top of shaky data is worse than no forecast.",
            "Replacing the source systems themselves.",
            "A mobile app. Alerts go to email or WhatsApp; the dashboard is "
            "responsive and that covers the phone case.",
        ],
        "stack": [
            ("Scheduled jobs", "Python, which is the right tool for pulling and "
             "reshaping messy data"),
            ("Storage", "Postgres, with the raw pulls kept alongside the cleaned "
             "output so any number can be traced back"),
            ("Dashboard", "React with a charting library"),
            ("Alerts", "Email plus a WhatsApp or Slack webhook"),
            ("Hosting", "One small cloud instance and a scheduler"),
        ],
        "timeline": [
            ("Week 1", "Sit with whoever owns the spreadsheet and write down every "
                       "manual step. This week matters more than the rest."),
            ("Weeks 2–3", "Data pulls and the transformation rules, checked against "
                          "the last three months of the existing file."),
            ("Weeks 4–5", "Dashboard, roles and alerts."),
            ("Week 6", "Both systems run in parallel and the numbers are compared "
                       "daily until they match."),
        ],
        "note": "Running both the old spreadsheet and the new system side by side "
                "for a couple of weeks is not wasted time. It is the only way to "
                "prove the new numbers are right before anyone trusts them.",
    },
    {
        "slug": "real-estate-listing-portal",
        "glance": [
            ("Type", "Public website + CRM"),
            ("Build time", "About 7 weeks"),
            ("Platforms", "Browser, agents on mobile"),
            ("Starts at", "₹20,000*"),
        ],
        "pains": [
            "Paid leads sit unread in a shared mailbox",
            "No record of who called whom, or when",
            "Listings live on portals you do not control",
            "Follow-ups depend on an agent remembering",
        ],
        "category": "Website + CRM",
        "thumb": "c",
        "title": "Real Estate Listing Portal",
        "summary": "Property search, enquiry capture and a lead pipeline a sales "
                   "team will actually use.",
        "situation": [
            "A property business advertises on the big portals, pays for every "
            "lead, and loses some of them because enquiries arrive as emails that "
            "someone has to notice. There is no record of which agent called whom, "
            "or when.",
            "Two things are being built here, and only one of them is the website. "
            "The site brings enquiries in; the CRM decides whether they turn into "
            "anything. Most projects like this over-invest in the first and "
            "under-invest in the second.",
        ],
        "scope": [
            ("Public listings",
             "Search and filter by locality, budget, configuration and status. "
             "Fast, and indexable by Google — the listings are the marketing."),
            ("Property pages",
             "Photos, floor plans, location, and an enquiry form that is short "
             "enough that people finish it."),
            ("Lead capture",
             "Every enquiry, from the site or a portal-forwarded email, lands in "
             "one inbox and is assigned to an agent within a minute."),
            ("Pipeline",
             "New → contacted → visit booked → negotiating → closed or lost. Each "
             "move requires a note. This is the discipline the tool is buying."),
            ("Follow-up reminders",
             "A lead with no activity for three days surfaces at the top of the "
             "agent's list. Most lost leads are lost to silence, not to price."),
        ],
        "excluded": [
            "Virtual tours and 3D walkthroughs — better bought from a specialist "
            "vendor and embedded.",
            "Document management and agreement generation.",
            "A public agent-facing mobile app. The CRM is responsive; agents work "
            "from their phone browsers in v1.",
        ],
        "stack": [
            ("Public site", "Server-rendered with Next.js, because search engines "
             "have to be able to read the listings"),
            ("CRM", "React, behind a login"),
            ("Backend", "Node with Postgres"),
            ("Images", "Resized on upload and served from object storage — property "
             "photos are the heaviest thing on the page"),
            ("Email intake", "A parser that turns portal enquiry emails into leads"),
        ],
        "timeline": [
            ("Week 1", "Listing structure and the pipeline stages, agreed with "
                       "whoever runs sales rather than whoever runs marketing."),
            ("Weeks 2–4", "Public site, search and property pages."),
            ("Weeks 5–6", "Lead capture, assignment and the pipeline."),
            ("Week 7", "Reminders, reporting and the sales team's first week on it."),
        ],
        "note": "A CRM only works if the team enters things into it. Half of this "
                "project's success is deciding how few fields an agent has to fill "
                "in after a call. Fewer is almost always better.",
    },
    {
        "slug": "delivery-tracking-app",
        "glance": [
            ("Type", "Driver app + owner board"),
            ("Build time", "About 8 weeks"),
            ("Platforms", "Android and iOS, offline-capable"),
            ("Starts at", "₹20,000*"),
        ],
        "pains": [
            "Finding a consignment means phoning the driver",
            "Proof of delivery is paper that arrives days later",
            "Delivery disputes get settled from memory",
            "Apps that need signal are useless in a dead zone",
        ],
        "category": "Mobile App",
        "thumb": "a",
        "title": "Delivery Tracking App",
        "summary": "Driver app with live location, proof-of-delivery photos and an "
                   "owner-side status board.",
        "situation": [
            "A logistics operator runs a fleet of drivers and finds out where a "
            "consignment is by calling the driver. Proof of delivery is a signature "
            "on paper that reaches the office days later, and disputes about "
            "whether something arrived are settled from memory.",
            "The constraint that shapes the whole build is that drivers work in "
            "patchy network coverage. An app that only works online is not an app "
            "for drivers.",
        ],
        "scope": [
            ("Driver app, offline-first",
             "The day's stops are downloaded in the morning. Everything a driver "
             "does is recorded on the device and syncs when signal returns. Nothing "
             "is lost in a basement or a highway dead zone."),
            ("Location tracking",
             "Batched and sent periodically rather than streamed continuously — the "
             "difference between a phone that lasts a shift and one that dies at 2pm."),
            ("Proof of delivery",
             "A photo and a recipient name, timestamped and location-stamped, "
             "attached to the consignment permanently."),
            ("Owner status board",
             "Every active vehicle on one map, with delayed stops highlighted "
             "instead of buried in a list."),
            ("Customer tracking link",
             "A link showing an ETA and no more. Customers do not need to see the "
             "driver's live position all day."),
        ],
        "excluded": [
            "Route optimisation. A genuinely hard problem; buy it from a "
            "specialist API later rather than build it now.",
            "Fuel, maintenance and driver payroll — a separate system.",
            "Barcode scanning at each hop, unless the operation already labels "
            "consignments consistently.",
        ],
        "stack": [
            ("Driver app", "React Native with a local database on the device and a "
             "sync queue — this is where most of the engineering effort goes"),
            ("Owner board", "React with a mapping library"),
            ("Backend", "Node with Postgres and PostGIS for the location data"),
            ("Photos", "Compressed on the device before upload; drivers are often "
             "on mobile data they pay for"),
        ],
        "timeline": [
            ("Week 1", "The consignment lifecycle and what a driver does at each "
                       "stop, watched in person if possible."),
            ("Weeks 2–5", "Driver app, offline storage and sync. The long stretch."),
            ("Weeks 6–7", "Owner board, map and delay alerts."),
            ("Week 8", "Two drivers run it alongside paper for a week."),
        ],
        "note": "Offline-first roughly doubles the effort of a driver app compared "
                "with an online-only one. It is also the difference between drivers "
                "using it and drivers going back to the phone call. Budget for it "
                "deliberately.",
    },
    {
        "slug": "booking-and-scheduling-mvp",
        "glance": [
            ("Type", "Booking MVP"),
            ("Build time", "About 4 weeks"),
            ("Platforms", "One shareable link, any browser"),
            ("Starts at", "₹20,000*"),
        ],
        "pains": [
            "Bookings arrive by WhatsApp, phone and walk-in",
            "Double bookings happen and cost goodwill",
            "No-shows are absorbed silently",
            "The desk cannot book and serve at the same time",
        ],
        "category": "MVP",
        "thumb": "c",
        "title": "Booking &amp; Scheduling MVP",
        "summary": "Ships in weeks, not months: online booking, reminders and "
                   "payments for a local service business.",
        "situation": [
            "A salon, clinic or studio books appointments over WhatsApp and by "
            "phone. Double bookings happen. No-shows are absorbed silently. The "
            "front desk cannot take a booking and serve a walk-in at the same time.",
            "This is the clearest example of what an MVP is for. The whole thing is "
            "small enough to be genuinely useful in a few weeks, and every week it "
            "runs teaches the owner something they would otherwise have guessed at.",
        ],
        "scope": [
            ("A bookable calendar",
             "Services, durations, staff members and working hours. A slot exists "
             "only if the staff member and the service both fit in it."),
            ("Public booking page",
             "One link, shareable on Instagram and WhatsApp. No app to install and "
             "no account to create."),
            ("Reminders",
             "A message 24 hours and 2 hours before. This alone typically moves "
             "the no-show rate more than anything else in the build."),
            ("Deposits",
             "Optional prepayment for slots that get abandoned. Turned on per "
             "service, not globally."),
            ("Front-desk view",
             "Today at a glance, plus the ability to block time and add a walk-in "
             "in two taps."),
        ],
        "excluded": [
            "Inventory and product sales.",
            "Staff payroll and commission calculation.",
            "A customer mobile app. A booking link works better than an app "
            "someone installs once and deletes.",
        ],
        "stack": [
            ("Everything", "One Next.js app — the booking page needs to be public "
             "and fast, and the admin side is small enough to live in the same "
             "codebase"),
            ("Database", "Postgres, with the availability rules enforced in the "
             "database so two people cannot take the same slot"),
            ("Reminders", "A scheduled job plus a WhatsApp or SMS provider"),
            ("Payments", "A gateway, for deposits only"),
        ],
        "timeline": [
            ("Week 1", "Services, staff, hours and the rules for what counts as an "
                       "available slot."),
            ("Weeks 2–3", "Booking page and the front-desk view."),
            ("Week 4", "Reminders, deposits, and live with real customers."),
        ],
        "note": "This is the shape of build that starts at ₹20,000. What moves the "
                "price is the number of staff-and-service rules, whether payments "
                "are involved, and how much of the existing customer list has to be "
                "imported.",
    },
    {
        "slug": "saas-subscription-starter",
        "glance": [
            ("Type", "Multi-tenant SaaS"),
            ("Build time", "About 9 weeks"),
            ("Platforms", "Browser, any device"),
            ("Starts at", "₹20,000*"),
        ],
        "pains": [
            "Every customer needs their own separated data",
            "Billing, trials and downgrades all have to agree",
            "One customer's heavy usage slows everyone down",
            "Adding a teammate should not need a developer",
        ],
        "category": "SaaS Product",
        "thumb": "b",
        "title": "SaaS Subscription Starter",
        "summary": "Sign-up, workspaces, plans and recurring billing — the "
                   "unglamorous half of a SaaS product, built once and properly.",
        "situation": [
            "A founder has a genuinely good idea for a tool and a clear first "
            "customer. What stands between them is the part that is identical in "
            "every SaaS product ever built: accounts, workspaces, invitations, "
            "roles, plans, trials, card failures and invoices.",
            "None of that is the product. All of it has to be right, because "
            "getting billing or data isolation wrong is the kind of mistake that "
            "is discovered by a customer rather than by you.",
        ],
        "scope": [
            ("Accounts and workspaces",
             "Sign up, verify, create a workspace, invite teammates. One person "
             "can belong to several workspaces without a second account."),
            ("Roles that actually restrict",
             "Owner, admin and member, enforced on the server. A permission check "
             "that only hides a button is not a permission check."),
            ("Plans and trials",
             "A free trial with a real end date, paid plans, upgrades, downgrades "
             "and the awkward states in between — expired card, failed renewal, "
             "cancelled but still inside the paid period."),
            ("Recurring billing",
             "A payment provider handles the card. We handle what happens to the "
             "customer's access when a charge succeeds, fails or is refunded."),
            ("Tenant isolation",
             "Every query is scoped to a workspace at the data layer, not by "
             "remembering to add a filter. This is the part that must not be a "
             "convention."),
        ],
        "excluded": [
            "Usage-based and metered pricing. Start with flat plans; metering is "
            "a project on its own and is easier once you know how people use it.",
            "SSO and SAML. Enterprise customers ask for it. You do not have "
            "enterprise customers on day one.",
            "An admin back-office with everything in it. Start with the three "
            "screens support actually needs.",
        ],
        "stack": [
            ("App", "Next.js, so the marketing pages and the product share one "
             "codebase and one deployment"),
            ("Backend", "Node with Postgres, workspace isolation enforced with "
             "row-level security"),
            ("Billing", "Stripe or Razorpay subscriptions, driven entirely by "
             "webhooks rather than by what the browser reports"),
            ("Auth", "Email and password plus Google, with sessions that survive "
             "a server restart"),
            ("Email", "A transactional provider for invites, receipts and "
             "failed-payment warnings"),
        ],
        "timeline": [
            ("Week 1", "The tenancy model: what a workspace owns, what happens "
                       "when someone is removed, what a downgrade takes away."),
            ("Weeks 2–4", "Accounts, workspaces, invitations and roles."),
            ("Weeks 5–7", "Plans, trials and billing, including every failure path."),
            ("Weeks 8–9", "Your actual product feature, on top of the foundation."),
        ],
        "note": "Payment providers charge per transaction and most take a cut of "
                "each subscription. That is billed to you by them, not by us, and "
                "it scales with your revenue rather than with the build.",
    },
    {
        "slug": "business-website-that-converts",
        "glance": [
            ("Type", "Marketing website"),
            ("Build time", "About 3 weeks"),
            ("Platforms", "Browser, mobile-first"),
            ("Starts at", "₹20,000*"),
        ],
        "pains": [
            "The current site takes eight seconds to load on mobile data",
            "Enquiries arrive as email nobody checks on weekends",
            "Nothing on the page says what to do next",
            "Editing an address means calling whoever built it",
        ],
        "category": "Website",
        "thumb": "c",
        "title": "Business Website That Converts",
        "summary": "A fast, mobile-first site that turns visitors into enquiries "
                   "— and that you can edit yourself.",
        "situation": [
            "A local business has a website built years ago on a page builder. It "
            "is slow, it looks wrong on a phone, and it produces almost no "
            "enquiries. Most of its visitors arrive from Instagram, look at it on "
            "mobile data, and leave before it finishes loading.",
            "This is the cheapest project on this list and often the highest "
            "return, because the traffic already exists. The work is in speed, in "
            "saying one clear thing, and in making the next step obvious.",
        ],
        "scope": [
            ("Fast on a phone, on mobile data",
             "The whole page under a few hundred kilobytes, images sized properly, "
             "no framework shipped to a visitor who only needs to read."),
            ("One clear message and one next step",
             "What you do, who for, and what to click. Most small-business sites "
             "fail at this before they fail at anything technical."),
            ("Enquiry capture that reaches a human",
             "A short form plus a WhatsApp and call button, with each enquiry "
             "landing somewhere someone actually looks."),
            ("Findable on Google",
             "Real HTML, correct headings, a sitemap, and a Google Business "
             "Profile that matches the site."),
            ("Editable by you",
             "The handful of things that change — hours, prices, photos, offers "
             "— editable without a developer."),
        ],
        "excluded": [
            "A blog, unless someone has genuinely committed to writing it. An "
            "empty blog dated two years ago is worse than none.",
            "Online payments, until there is something to sell online.",
            "A carousel on the homepage. Nobody sees slide two.",
        ],
        "stack": [
            ("Site", "Static HTML and CSS, or Astro if there are more than a dozen "
             "pages — no server to be slow"),
            ("Hosting", "A CDN, which is free or nearly free at this size"),
            ("Forms", "A form service or a small serverless endpoint; a static "
             "site needs no database for this"),
            ("Images", "Compressed and served in modern formats, sized per device"),
        ],
        "timeline": [
            ("Week 1", "What the site has to say, and to whom. Copy first, "
                       "design after — the other order produces pretty nonsense."),
            ("Week 2", "Design and build."),
            ("Week 3", "Content, Google setup, and live."),
        ],
        "note": "A website only earns its keep if the enquiries reach someone. "
                "Decide before launch who answers them and how fast — that "
                "decision affects the results more than any design choice here.",
    },
    {
        "slug": "inventory-and-billing-for-retail",
        "glance": [
            ("Type", "Custom software"),
            ("Build time", "About 7 weeks"),
            ("Platforms", "Counter desktop, phone for stock"),
            ("Starts at", "₹20,000*"),
        ],
        "pains": [
            "Stock on paper never matches stock on the shelf",
            "Fast-selling items run out before anyone notices",
            "Bills are handwritten and GST is reconciled monthly by hand",
            "No idea which products actually make money",
        ],
        "category": "Custom Software",
        "thumb": "b",
        "title": "Inventory &amp; Billing for Retail",
        "summary": "Stock that matches the shelf, GST-ready bills in seconds, and "
                   "an alert before a fast seller runs out.",
        "situation": [
            "A retailer with two shops tracks stock in a register and bills by "
            "hand. Nobody knows what is genuinely in stock until someone counts "
            "it, and the count is wrong by the time it is finished.",
            "The temptation is to buy an off-the-shelf POS. Sometimes that is the "
            "right answer and I will say so. It stops being the right answer when "
            "the business has a real quirk — loose quantities, custom bundles, "
            "credit for regulars — that the packaged product refuses to model.",
        ],
        "scope": [
            ("Products and stock",
             "Per-shop stock levels, purchase entry, and a stock adjustment that "
             "records who changed what and why."),
            ("Billing at the counter",
             "Fast enough to use with a customer waiting: barcode or search, "
             "quantity, discount, GST-compliant invoice, print or WhatsApp."),
            ("Low-stock alerts",
             "Per product, based on how fast it actually sells rather than a "
             "number someone guessed once."),
            ("Day-end summary",
             "Sales, payment modes, and what left the shelf. One screen the owner "
             "reads on the way home."),
            ("Simple margins",
             "Purchase price against selling price, so the products that look "
             "busy but earn nothing become visible."),
        ],
        "excluded": [
            "Full accounting. Export to whatever the accountant already uses "
            "instead of rebuilding Tally badly.",
            "E-commerce and online ordering — a separate project once the stock "
            "data is trustworthy.",
            "Loyalty schemes, until there is purchase history to base one on.",
        ],
        "stack": [
            ("Counter app", "A web app that works offline for billing, because a "
             "shop cannot stop selling when the internet drops"),
            ("Stock app", "The same app on a phone, for counting on the shelf"),
            ("Backend", "Node with Postgres"),
            ("Printing", "Standard thermal printers over the browser"),
            ("Invoices", "GST-compliant numbering and formats from day one — "
             "retrofitting this later is genuinely painful"),
        ],
        "timeline": [
            ("Week 1", "Watch a real day at the counter. What gets typed, what "
                       "gets skipped, where the queue builds."),
            ("Weeks 2–4", "Products, stock and purchase entry."),
            ("Weeks 5–6", "Billing, printing and GST formats."),
            ("Week 7", "One shop runs it alongside the register for a week."),
        ],
        "note": "Getting the opening stock right is the hardest day of this "
                "project and it is your team's day, not mine. Budget a full "
                "count before go-live; every wrong number carries forward.",
    },
    {
        "slug": "clinic-appointments-and-records",
        "glance": [
            ("Type", "Web app"),
            ("Build time", "About 7 weeks"),
            ("Platforms", "Desktop at the desk, phone for patients"),
            ("Starts at", "₹20,000*"),
        ],
        "pains": [
            "Appointments in a diary that only the front desk can see",
            "Patient history in paper files that go missing",
            "Waiting rooms full because everyone was told “morning”",
            "No reminder, so a fifth of slots are no-shows",
        ],
        "category": "Web App",
        "thumb": "b",
        "title": "Clinic Appointments &amp; Records",
        "summary": "Appointments, patient history and prescriptions in one place, "
                   "with reminders that cut the empty slots.",
        "situation": [
            "A two-doctor clinic books appointments in a paper diary and keeps "
            "patient history in files. Patients are given a vague time and wait. "
            "Records are hard to find when someone returns after a year.",
            "Patient data raises the stakes here. This is health information: it "
            "needs proper access control, an audit trail, and an honest "
            "conversation about where it is stored before a line is written.",
        ],
        "scope": [
            ("Real appointment slots",
             "Per doctor, with actual durations, so a patient is given a time "
             "rather than a session."),
            ("Patient records",
             "History, visits, prescriptions, and uploaded reports, searchable by "
             "phone number — the only identifier patients reliably remember."),
            ("Prescriptions",
             "Written on screen, printed on the clinic's letterhead, and kept "
             "against the visit."),
            ("Reminders",
             "A message the day before and an hour before. This alone typically "
             "pays for the system."),
            ("Access control and audit",
             "Reception sees the schedule, not clinical notes. Every record "
             "opened is logged, with who and when."),
        ],
        "excluded": [
            "Insurance claim processing — a specialist domain with its own "
            "integrations and its own experts.",
            "Lab and pharmacy modules, unless the clinic runs them in-house.",
            "Video consultations. Link an existing tool from the appointment.",
        ],
        "stack": [
            ("Web app", "React, used at the desk and in the consulting room"),
            ("Backend", "Node with Postgres, with access logging built in rather "
             "than bolted on"),
            ("Storage", "Reports encrypted at rest, in an Indian cloud region"),
            ("Reminders", "SMS or WhatsApp, with the clinic name in the message"),
            ("Backups", "Automated daily, and restored once in front of you so "
             "you know the restore works"),
        ],
        "timeline": [
            ("Week 1", "The visit flow, and a decision about where patient data "
                       "lives and who may see it."),
            ("Weeks 2–4", "Appointments, the schedule and the front-desk view."),
            ("Weeks 5–6", "Records, prescriptions and uploads."),
            ("Week 7", "Reminders, access logs, backup restore test, live."),
        ],
        "note": "Patient records carry legal obligations in most places, "
                "including India. I build the access control, encryption and "
                "audit trail; you should still have someone confirm your specific "
                "compliance duties. I will tell you what the system does and does "
                "not cover, in writing.",
    },
    {
        "slug": "gym-membership-app",
        "glance": [
            ("Type", "Mobile app + desk web"),
            ("Build time", "About 6 weeks"),
            ("Platforms", "iOS, Android, desk browser"),
            ("Starts at", "₹20,000*"),
        ],
        "pains": [
            "Memberships expire quietly and nobody follows up",
            "Check-in is a register nobody fills in properly",
            "Class capacity is managed by shouting",
            "Renewal reminders depend on someone remembering",
        ],
        "category": "Mobile App",
        "thumb": "a",
        "title": "Gym Membership App",
        "summary": "Digital membership, quick check-in, class booking and renewal "
                   "reminders that actually go out.",
        "situation": [
            "A gym with about four hundred members tracks memberships in a "
            "spreadsheet and check-ins in a register. Expiries are noticed late, "
            "which means renewals are lost, which is the entire business.",
            "Retention is the whole game here. The features that matter are the "
            "ones that put the member back in the building: a renewal nudge "
            "before expiry, and a class they have already booked.",
        ],
        "scope": [
            ("Digital membership",
             "Plan, start and end dates, and a member's own screen showing exactly "
             "when it runs out."),
            ("Fast check-in",
             "A QR scan at the desk. Under two seconds, because there is a queue "
             "at 7am."),
            ("Class booking",
             "Schedule, capacity, and a waitlist that promotes automatically when "
             "someone cancels."),
            ("Renewal reminders",
             "Seven days out, on the day, and after expiry, with a payment link "
             "in the message."),
            ("Owner numbers",
             "Active members, expiring this week, and attendance by hour. Enough "
             "to staff the floor properly."),
        ],
        "excluded": [
            "Workout plans and exercise libraries. Members already use apps for "
            "that and yours will not beat them.",
            "Wearable and fitness-tracker integrations.",
            "Diet plans, which are a licensing question before they are a "
            "software one.",
        ],
        "stack": [
            ("Member app", "React Native, one codebase for both stores"),
            ("Desk app", "A web app, since the desk has a browser and a scanner"),
            ("Backend", "Node with Postgres"),
            ("Check-in", "QR codes that rotate, so a screenshot cannot be passed "
             "around the car park"),
            ("Payments", "A gateway for renewals, with the link inside the reminder"),
        ],
        "timeline": [
            ("Week 1", "Plans, freezes, transfers and the awkward cases the "
                       "spreadsheet handles informally today."),
            ("Weeks 2–4", "Member app, membership and check-in."),
            ("Week 5", "Classes, capacity and waitlist."),
            ("Week 6", "Reminders, payments, owner view, live."),
        ],
        "note": "App-store publishing adds about a week the first time and needs "
                "developer accounts in your name, not mine — Apple charges "
                "yearly, Google once. You keep ownership of both.",
    },
    {
        "slug": "field-service-job-app",
        "glance": [
            ("Type", "Mobile app + dispatch web"),
            ("Build time", "About 8 weeks"),
            ("Platforms", "Android and iOS, offline-capable"),
            ("Starts at", "₹20,000*"),
        ],
        "pains": [
            "Jobs are assigned by phone call and forgotten",
            "Proof of work is a photo in someone's personal WhatsApp",
            "Invoices go out days after the job is done",
            "Nobody knows which technician is free right now",
        ],
        "category": "Mobile App",
        "thumb": "a",
        "title": "Field Service Job App",
        "summary": "Dispatch, on-site checklists, photo proof and an invoice "
                   "raised before the technician leaves.",
        "situation": [
            "A service business — appliance repair, AC servicing, pest control "
            "— runs a team of technicians. Jobs are assigned over the phone, "
            "completion is reported by WhatsApp, and invoicing happens later from "
            "memory. Payment slips by days for no reason other than paperwork.",
            "Like the delivery app, this lives or dies on working without signal. "
            "Technicians go into basements, lift shafts and buildings with no "
            "coverage, and the job still has to be recorded.",
        ],
        "scope": [
            ("Dispatch board",
             "Today's jobs, who is free, and assignment by drag rather than by "
             "phone call."),
            ("Technician app, offline-first",
             "The day's jobs download in the morning. Everything recorded on site "
             "syncs when signal comes back."),
            ("On-site checklist",
             "Per job type, so the work is consistent and the parts used are "
             "captured while the technician is still standing there."),
            ("Proof of work",
             "Before and after photos, plus a customer signature, timestamped and "
             "attached to the job permanently."),
            ("Invoice on completion",
             "Generated from the checklist and parts, sent by WhatsApp before the "
             "technician leaves the site."),
        ],
        "excluded": [
            "Route optimisation across the whole team — buy it from a "
            "specialist API when the volume justifies it.",
            "Parts inventory across a warehouse. Start with what is on the van.",
            "Customer self-service booking, until the dispatch side is steady.",
        ],
        "stack": [
            ("Technician app", "React Native with an on-device database and a "
             "sync queue — the bulk of the engineering"),
            ("Dispatch board", "React, used on a desktop at the office"),
            ("Backend", "Node with Postgres"),
            ("Photos", "Compressed on the device before upload"),
            ("Invoices", "GST-compliant, generated server-side so numbering can "
             "never collide"),
        ],
        "timeline": [
            ("Week 1", "Ride along with a technician for a day. This changes the "
                       "design more than any meeting will."),
            ("Weeks 2–5", "Technician app, offline storage and sync."),
            ("Weeks 6–7", "Dispatch board and assignment."),
            ("Week 8", "Invoicing, then two technicians run it live for a week."),
        ],
        "note": "Offline sync is the expensive part and the reason the app gets "
                "used. If the budget forces a choice, cut features rather than "
                "cutting offline — an app that needs signal will be abandoned in "
                "the first basement.",
    },
]


# --------------------------------------------------------------------------
# ARTICLES
# --------------------------------------------------------------------------
# body: a list of blocks. ("h2", text) | ("p", text) | ("ul", [items])
#       | ("quote", text) | ("ol", [items])

ARTICLES = [
    {
        "slug": "do-you-need-a-vector-database",
        "title": "Do you actually need a vector database?",
        "date": "2026-09-07",
        "date_label": "7 September 2026",
        "read": "6 min read",
        "tag": "AI",
        "caveat": True,
        "summary": "Almost every AI feature proposal now includes one. For most "
                   "of them, Postgres with a search extension is enough, and the "
                   "difference is a month of work.",
        "body": [
            ("p", "If your project involves AI, someone will suggest a vector "
                  "database. Sometimes that is right. Often it adds a second "
                  "datastore, a sync problem and a monthly bill to a feature that "
                  "would have worked without it."),
            ("h2", "What the thing actually does"),
            ("p", "Text gets converted into a long list of numbers — an embedding "
                  "— chosen so that passages about similar things end up close "
                  "together. Search then means \"find the stored vectors nearest "
                  "to this one\". A vector database is storage plus a fast index "
                  "for that nearest-neighbour lookup."),
            ("p", "That is genuinely useful. It finds a document about \"cancelling "
                  "my subscription\" when the user typed \"how do I stop being "
                  "charged\", which keyword search misses entirely."),
            ("h2", "The question that decides it"),
            ("p", "How many documents are you searching?"),
            ("ul", [
                "<strong>Under about fifty thousand chunks.</strong> Postgres with "
                "the pgvector extension is fine. It is one database, one backup, "
                "one thing to operate, and queries land in tens of milliseconds.",
                "<strong>Hundreds of thousands to a few million.</strong> Still "
                "usually Postgres, with attention paid to the index type and to "
                "how much memory it gets.",
                "<strong>Tens of millions, or heavy write traffic.</strong> Now a "
                "dedicated vector store earns its keep.",
            ]),
            ("p", "Most business AI features — a support bot over your help pages, "
                  "search across a few thousand documents, a policy assistant — "
                  "live comfortably in the first bucket. A company handbook is a "
                  "few hundred chunks, not a few million."),
            ("h2", "The part that actually decides quality"),
            ("p", "Here is what a year of building these teaches you: the "
                  "retrieval quality is dominated by how you split the documents, "
                  "not by which database holds the vectors. Chunks that break "
                  "mid-table or mid-sentence produce bad answers on any engine."),
            ("p", "Two things move the needle far more than the storage choice. "
                  "First, chunking that respects the document's structure — "
                  "headings, sections, table boundaries. Second, combining vector "
                  "search with plain keyword search and merging the results, "
                  "because exact terms like an order number or an error code are "
                  "precisely what embeddings are worst at."),
            ("quote", "Teams routinely migrate to a specialist vector database, "
                      "get the same mediocre answers, and only then fix their "
                      "chunking."),
            ("h2", "What I would build first"),
            ("ol", [
                "Postgres with pgvector, alongside the data you already have.",
                "Chunk on structure, not on a fixed character count.",
                "Add keyword search next to vector search and merge the rankings.",
                "Log every question and the passages retrieved for it. This log "
                "is the most valuable thing you will build.",
                "Read that log. Fix the retrieval failures it shows you.",
            ]),
            ("p", "If, after all that, the index genuinely cannot keep up, moving "
                  "to a dedicated vector store is a contained piece of work — and "
                  "by then you will know exactly what you need from it."),
        ],
    },
    {
        "slug": "what-ai-coding-agents-are-good-at",
        "title": "What AI coding agents are good at, and what they're not",
        "date": "2026-08-05",
        "date_label": "5 August 2026",
        "read": "7 min read",
        "tag": "AI",
        "caveat": True,
        "summary": "A working note from someone who uses them daily and still "
                   "reads every line. Where they save real time, and the three "
                   "places they quietly cost you money.",
        "body": [
            ("p", "I use coding agents every working day. They have genuinely "
                  "changed how much one person can ship. They have also produced "
                  "the two most expensive mistakes I have had to unpick this year. "
                  "Both things are true."),
            ("h2", "Where they earn their keep"),
            ("ul", [
                "<strong>Work with an obvious right answer.</strong> A CRUD "
                "endpoint, a form with validation, a migration, a config file. "
                "Shapes that exist a million times over.",
                "<strong>Mechanical change across many files.</strong> Renaming a "
                "concept in sixty places. Tedious and error-prone by hand; a "
                "machine does it exactly.",
                "<strong>Getting oriented in unfamiliar code.</strong> \"Where "
                "does this request get authorised?\" answered in seconds rather "
                "than an afternoon of grepping.",
                "<strong>Test data and fixtures.</strong> Realistic, varied, in "
                "bulk, instantly.",
                "<strong>The first draft of anything.</strong> Editing something "
                "mediocre is faster than starting at a blank file.",
            ]),
            ("h2", "The three places they cost you"),
            ("h2", "1. Confidently wrong code that reads fine"),
            ("p", "This is the big one. Broken code announces itself. Subtly wrong "
                  "code does not. An authorisation check that is slightly too "
                  "permissive, an edge case in a refund path, an off-by-one in a "
                  "date range — all of these read perfectly well at a glance, and "
                  "a glance is exactly what they tend to get."),
            ("p", "Which is why the rule here is that no line goes live unread. "
                  "Not skimmed. Read."),
            ("h2", "2. Plausible-looking architecture"),
            ("p", "Ask for a feature and you will get one, built the most common "
                  "way that feature is built on the internet. That is often right. "
                  "It is wrong precisely when your business has the quirk that "
                  "made a custom build necessary in the first place — and it will "
                  "flatten that quirk without mentioning it."),
            ("h2", "3. Volume that hides the absence of thinking"),
            ("p", "A four-hundred-line pull request feels like progress. Sometimes "
                  "it is eighty lines of thinking and three hundred of scaffolding "
                  "nobody needed. The cost is not writing it; it is that someone "
                  "maintains it for years."),
            ("quote", "The scarce resource stopped being typing. It is judgement "
                      "about what should exist at all."),
            ("h2", "How I actually work with them"),
            ("p", "The data model, anything touching money, authentication or "
                  "personal data, and any decision about what to build — those I "
                  "do myself, slowly. Everything downstream of those decisions is "
                  "fair game, reviewed line by line."),
            ("p", "The practical test I apply: if this is wrong, how will I find "
                  "out? If the answer is \"it fails immediately and loudly\", let "
                  "the machine write it. If the answer is \"a customer tells me in "
                  "three months\", I write it."),
            ("h2", "What it means if you are paying for software"),
            ("p", "Ask whoever is building for you how they use these tools. "
                  "\"We don't\" is a slightly worrying answer in 2026. So is "
                  "\"the AI writes it and we ship it\". The answer you want "
                  "describes a line: what the machine does, what a person does, "
                  "and who reads the result before it reaches you."),
        ],
    },
    {
        "slug": "start-with-postgres",
        "title": "Start with Postgres. Almost always.",
        "date": "2026-07-22",
        "date_label": "22 July 2026",
        "read": "6 min read",
        "tag": "Engineering",
        "summary": "Database choice is the decision most likely to be made for "
                   "the wrong reasons, and the most expensive to revisit. Here is "
                   "the short version.",
        "body": [
            ("p", "Choosing the database is one of the earliest decisions in a "
                  "project and among the hardest to reverse. It also attracts more "
                  "fashion-driven argument than almost anything else in the field."),
            ("p", "My default is Postgres, and the bar for departing from it is "
                  "high. Here is the reasoning, in a form you can push back on."),
            ("h2", "Your data is relational. It just is."),
            ("p", "Customers have orders. Orders have items. Items reference "
                  "products. Students belong to batches, batches have sessions, "
                  "sessions have attendance. Nearly every business application is "
                  "a graph of related things, and a relational database is what "
                  "that shape was designed for."),
            ("p", "The classic failure is picking a document store because early "
                  "development feels faster, then spending the next year "
                  "reimplementing joins in application code — slower, buggier, and "
                  "without transactions."),
            ("h2", "Constraints are a feature, not friction"),
            ("p", "A foreign key that refuses to let an order exist without a "
                  "customer prevents a class of bug permanently. A unique "
                  "constraint on an invoice number means duplicate numbers cannot "
                  "happen, no matter what the application code does under load. "
                  "Rules enforced by the database hold even when your code is "
                  "wrong — and your code will sometimes be wrong."),
            ("h2", "One database instead of four"),
            ("p", "Modern Postgres covers a startling amount of ground: JSON "
                  "columns when data genuinely is unstructured, full-text search, "
                  "vector similarity through pgvector, geographic queries through "
                  "PostGIS, and a queue via SKIP LOCKED that is enough for most "
                  "workloads."),
            ("p", "Each of those has a specialist that beats it. The specialist "
                  "also brings another thing to deploy, monitor, back up, secure "
                  "and keep in sync. For a small team, one very good database "
                  "usually beats four excellent ones."),
            ("quote", "Every additional datastore is a sync problem you have "
                      "agreed to own forever."),
            ("h2", "When I would not use it"),
            ("ul", [
                "<strong>Genuinely enormous append-only volumes</strong> — "
                "telemetry, sensor readings, clickstreams at real scale. A "
                "time-series or columnar store is the right tool.",
                "<strong>A cache.</strong> Redis exists and is excellent. Use it as "
                "a cache, not as your source of truth.",
                "<strong>Files.</strong> Images, videos and PDFs belong in object "
                "storage with the path in the database, never the file itself.",
                "<strong>Your platform has already decided.</strong> If you are "
                "deep in a stack with its own managed database, fighting it is "
                "rarely worth the win.",
            ]),
            ("h2", "The honest summary"),
            ("p", "Almost no small or medium business application outgrows "
                  "Postgres. Plenty outgrow the team's ability to operate five "
                  "different datastores. Start boring; the exciting choice is "
                  "still available later, and you will make it with real "
                  "information."),
        ],
    },
    {
        "slug": "server-rendered-or-single-page",
        "title": "Server-rendered or single-page? A plain answer",
        "date": "2026-07-08",
        "date_label": "8 July 2026",
        "read": "6 min read",
        "tag": "Engineering",
        "caveat": True,
        "summary": "The argument that has run for a decade, reduced to the two "
                   "questions that actually decide it for your project.",
        "body": [
            ("p", "Every few months the industry re-litigates this. The framework "
                  "names change; the underlying tradeoff has not moved in ten "
                  "years."),
            ("h2", "The two approaches, briefly"),
            ("p", "<strong>Server-rendered:</strong> the server sends finished "
                  "HTML. The page appears fast and search engines can read it. "
                  "Interactions typically involve a round trip."),
            ("p", "<strong>Single-page:</strong> the browser downloads an "
                  "application which then draws the pages. Slower to first appear, "
                  "then very responsive, and it can hold complex state without "
                  "asking the server again."),
            ("p", "Everything else — the frameworks, the hybrid rendering modes, "
                  "the streaming and the islands — is machinery for getting more "
                  "of both, and it works. But the two questions below still decide "
                  "which side you should start from."),
            ("h2", "Question one: does a stranger need to see it?"),
            ("p", "Anything a search engine or a first-time visitor must reach — "
                  "marketing pages, property listings, articles, a product catalogue "
                  "— should be server-rendered. Not because search engines cannot "
                  "run JavaScript, but because speed on a phone on mobile data "
                  "decides whether the visitor is still there, and shipping an "
                  "application to someone who wanted to read a paragraph is a poor "
                  "trade."),
            ("h2", "Question two: how long does someone stay?"),
            ("p", "A dispatch board someone watches for six hours has entirely "
                  "different economics. One heavier initial load buys a day of "
                  "instant interaction. That is a good deal, and a bad one for a "
                  "visitor who arrived from Instagram and will leave in forty "
                  "seconds."),
            ("h2", "In practice, most projects are both"),
            ("p", "The listings portal in our case studies is server-rendered on "
                  "the public side and a single-page app behind the login. That is "
                  "not a compromise, it is the correct answer: the two halves have "
                  "different users with different needs."),
            ("quote", "Pick per surface, not per project. A marketing page and an "
                      "operations console have nothing in common but a domain name."),
            ("h2", "What I would not do"),
            ("ul", [
                "Ship a single-page app for a five-page brochure site. It happens "
                "constantly and it is always slower than the thing it replaced.",
                "Server-render a heavily interactive dashboard out of principle, "
                "then fight the framework for months.",
                "Choose based on what a conference talk said. The talk does not "
                "know who your visitors are or what network they are on.",
            ]),
            ("p", "Ask instead: who arrives here, on what connection, and how long "
                  "do they stay? The answer picks the approach without any "
                  "ideology being involved."),
        ],
    },
    {
        "slug": "passkeys-and-when-to-bother",
        "title": "Passkeys, and when to bother",
        "date": "2026-06-24",
        "date_label": "24 June 2026",
        "read": "5 min read",
        "tag": "Security",
        "caveat": True,
        "summary": "They are genuinely better than passwords and genuinely not a "
                   "drop-in replacement. Where they fit, and the recovery problem "
                   "nobody mentions.",
        "body": [
            ("p", "Passkeys replace the password with a key pair held by the "
                  "device. The private half never leaves it, so there is nothing "
                  "to phish, nothing to reuse across sites, and nothing useful for "
                  "an attacker to steal from your database."),
            ("p", "That is a real improvement over passwords, which are the cause "
                  "of most account compromises. It still does not make them "
                  "automatically right for your product."),
            ("h2", "What actually improves"),
            ("ul", [
                "Phishing largely stops working, because the credential is bound "
                "to your domain and simply will not offer itself to a lookalike.",
                "A database breach no longer leaks anything an attacker can log "
                "in with.",
                "Sign-in is a fingerprint or a face rather than a password plus an "
                "SMS code — faster, and people stop reusing passwords they were "
                "reusing anyway.",
            ]),
            ("h2", "The problem nobody puts on the slide"),
            ("p", "Account recovery. A password can be reset by email. A passkey "
                  "lives on a device, and devices get lost, broken, sold and "
                  "replaced."),
            ("p", "The major platforms sync passkeys through their own accounts, "
                  "which covers most people most of the time. It does not cover "
                  "the user who moves between ecosystems, the one who lost the "
                  "only phone they own, or the shared machine at a shop counter."),
            ("p", "So you build a recovery path — and a recovery path is, by "
                  "definition, another way in. Build it carelessly and you have "
                  "reintroduced the weakness you removed. This is the actual work "
                  "in a passkey project, and it is where the time goes."),
            ("quote", "Any authentication system is exactly as strong as its "
                      "account-recovery flow. Passkeys do not change that."),
            ("h2", "What I would do today"),
            ("ol", [
                "Offer passkeys as an additional way to sign in, not the only one.",
                "Keep one conventional fallback — email link or password — until "
                "your own numbers show most users have enrolled.",
                "Encourage enrolling more than one device.",
                "Design the recovery flow deliberately, and make it as hard to "
                "abuse as the front door.",
                "Watch how many people actually use it. That number decides "
                "whether step two ever ends.",
            ]),
            ("h2", "Is it worth it for a small product?"),
            ("p", "If you hold anything users would be upset to lose — money, "
                  "business data, personal records — yes, as an option. If you are "
                  "building a booking page for a salon, an email link is simpler "
                  "and perfectly adequate. Match the effort to what is behind the "
                  "door."),
        ],
    },
    {
        "slug": "build-for-the-metro",
        "title": "Build for the metro: offline is a product decision",
        "date": "2026-06-10",
        "date_label": "10 June 2026",
        "read": "6 min read",
        "tag": "Mobile",
        "summary": "Most apps are built on office wifi and used on a train. "
                   "Treating the network as optional is a decision about who gets "
                   "to use your product.",
        "body": [
            ("p", "Software is written in places with excellent internet and used "
                  "in basements, lifts, warehouses, moving trains and buildings "
                  "with thick walls. An app that assumes a connection is an app "
                  "that stops working exactly when someone needed it."),
            ("h2", "The failure mode is worse than it looks"),
            ("p", "A dead connection is not the hard case. The hard case is a "
                  "connection that technically exists and delivers nothing: the "
                  "request neither succeeds nor fails, the spinner turns, and the "
                  "person watches it. Then they tap the button again."),
            ("p", "Any app that will be used away from a desk needs an answer for "
                  "this, and the answer has to be designed rather than discovered "
                  "in production."),
            ("h2", "Three levels, increasing in cost"),
            ("ul", [
                "<strong>Fail honestly.</strong> Detect it, say so, keep what the "
                "user typed, offer a retry. Cheap, and enormously better than a "
                "spinner. Every app should do at least this.",
                "<strong>Read offline.</strong> Cache what was already fetched so "
                "the app opens and shows something. Moderate effort, and covers "
                "most consumer cases.",
                "<strong>Work offline.</strong> Actions are recorded locally and "
                "sync later. This is a real engineering project, and it is what "
                "field work actually requires.",
            ]),
            ("h2", "The expensive part is not storage"),
            ("p", "Keeping data on the device is straightforward. The cost is in "
                  "reconciliation: two people edited the same record while "
                  "disconnected, and one of them has to lose. Or a job was marked "
                  "complete twice because the first attempt did sync, silently, "
                  "before the phone gave up."),
            ("p", "Which is why the design work comes first. Give every action an "
                  "identifier generated on the device so a replay cannot duplicate "
                  "it. Decide per data type who wins a conflict — last write, "
                  "server always, or ask the user. Show sync state honestly, "
                  "because a technician needs to know whether the office has seen "
                  "their work."),
            ("quote", "Offline support is not a feature you add. It is an "
                      "assumption you either make on day one or retrofit at three "
                      "times the price."),
            ("h2", "Deciding, in one question"),
            ("p", "Where is this used? If the honest answer includes a basement, a "
                  "van, a lift, a factory floor or a train, offline is not a "
                  "nice-to-have and cutting it will produce an app your users "
                  "abandon. If it is used at a desk, fail honestly and spend the "
                  "money elsewhere."),
            ("p", "The delivery and field service builds in our case studies both "
                  "assume offline from the first week, and both say plainly that "
                  "if the budget forces a choice, cut features instead."),
        ],
    },
    {
        "slug": "what-an-mvp-actually-is",
        "title": "What an MVP actually is, and what it isn't",
        "date": "2026-08-12",
        "date_label": "12 August 2026",
        "read": "6 min read",
        "tag": "Building",
        "summary": "Most people asking for an MVP describe a full product with a "
                   "smaller budget. That is not the same thing, and the difference "
                   "decides whether the money teaches you anything.",
        "body": [
            ("p", "Almost every first conversation I have includes the words "
                  "\"let's start with an MVP\". Then the feature list arrives and "
                  "it is a complete product with the polish removed. Those are "
                  "different things, and confusing them is the single most "
                  "expensive mistake I see."),
            ("h2", "An MVP is an experiment, not a discount"),
            ("p", "A minimum viable product exists to answer a question you cannot "
                  "answer by thinking harder. Will people book through a link "
                  "instead of calling? Will drivers actually use the app? Will "
                  "anyone pay for this? The MVP is the cheapest honest way to find "
                  "out."),
            ("p", "That reframes the whole scoping conversation. The question stops "
                  "being \"what can we afford to build?\" and becomes \"what is the "
                  "least we can build that would change our mind?\" Those produce "
                  "very different feature lists."),
            ("h2", "Cheap versions of everything is the failure mode"),
            ("p", "The tempting move is to keep all fifteen features and build each "
                  "one to 40%. It feels fair — everybody's favourite thing survives. "
                  "It is also the reliable way to produce something nobody wants to "
                  "use, which teaches you nothing except that the thing was bad, "
                  "when in fact only the execution was."),
            ("p", "Two features that work properly beat fifteen that half work. If a "
                  "feature is in, it should be good enough that its failure means "
                  "something."),
            ("h2", "How to actually cut the list"),
            ("p", "Go through the features and ask one question of each: if this "
                  "were missing on day one, would a real user walk away? Not \"would "
                  "they complain\" — complaints are fine, and are useful data. Would "
                  "they stop using it."),
            ("ul", [
                "Login with email, phone, Google and Apple — pick one. You can add "
                "the rest in an afternoon once people are actually signing up.",
                "An admin panel to edit everything — start with the three things "
                "that change weekly. The rest can be a database change for now.",
                "Notifications on every event — pick the one that brings someone "
                "back to the product.",
                "Analytics dashboards — you have almost no data yet. A spreadsheet "
                "export is enough for months.",
            ]),
            ("h2", "The part people skip"),
            ("p", "An MVP is only worth building if you have decided, in advance, "
                  "what you will do with the answer. Before I start, I ask what "
                  "number would count as working and what would count as failed. If "
                  "there is no answer, we are not building an experiment — we are "
                  "just building a small product, and we should be honest about "
                  "that instead."),
            ("quote", "The point of shipping early is not to save money. It is to "
                      "stop spending money on the wrong thing sooner."),
            ("h2", "What this looks like in practice"),
            ("p", "The booking system in our examples runs about four weeks. It has "
                  "a calendar, a public booking link, reminders and optional "
                  "deposits. It does not have inventory, payroll, a loyalty scheme "
                  "or a customer app. Not because those are bad ideas — because "
                  "after four weeks the owner knows whether customers will book "
                  "online at all, and every one of those features would be designed "
                  "better with that answer in hand."),
            ("p", "If it works, you build the next thing knowing something. If it "
                  "does not, you found out for the price of a month rather than the "
                  "price of a year."),
        ],
    },
    {
        "slug": "what-twenty-thousand-buys",
        "title": "What ₹20,000 buys you — and what it doesn't",
        "date": "2026-08-19",
        "date_label": "19 August 2026",
        "read": "5 min read",
        "tag": "Pricing",
        "summary": "A starting price is only useful if you know what moves it. "
                   "Here is what sits inside that number, what sits outside it, "
                   "and the running costs nobody mentions until the invoice lands.",
        "body": [
            ("p", "MVPs here start at ₹20,000. Starting prices are close to "
                  "meaningless unless someone tells you what changes them, so this "
                  "is that explanation."),
            ("h2", "What that number is"),
            ("p", "It is the floor for a genuinely small, genuinely useful first "
                  "version: one clear job, a handful of screens, a database, a "
                  "deployment, and a person who read every line before it went "
                  "live. The booking MVP is the honest shape of it."),
            ("h2", "What pushes it up"),
            ("ul", [
                "<strong>Payments.</strong> Money means reconciliation, refunds, "
                "failed-payment states and a testing burden that non-payment "
                "features never have.",
                "<strong>Offline support.</strong> A mobile app that has to work "
                "without signal is roughly twice the work of one that doesn't. "
                "Sync conflicts are their own project.",
                "<strong>Roles and permissions.</strong> Two user types is a "
                "little work. Five, with overlapping rules about who sees which "
                "numbers, is a lot.",
                "<strong>Integrations.</strong> Anything that has to talk to a "
                "system you already own is priced after I have seen that system's "
                "documentation, never before.",
                "<strong>Migrating existing data.</strong> Old data is always "
                "messier than anyone remembers. This is frequently the most "
                "underestimated line in a project.",
            ]),
            ("h2", "What is never included"),
            ("p", "Third-party costs are billed to you, by those third parties, at "
                  "whatever they charge. I do not mark them up, and I do not "
                  "absorb them:"),
            ("ul", [
                "Cloud hosting and databases.",
                "Domain registration and renewal.",
                "Apple's ₹8,000-ish yearly developer fee and Google's one-time "
                "Play Console fee, if you are publishing apps.",
                "Payment gateway commission on every transaction.",
                "SMS and WhatsApp message costs — small individually, real at "
                "volume.",
                "Any paid API or library the project needs.",
            ]),
            ("p", "For a small MVP these usually land somewhere between a few "
                  "hundred and a few thousand rupees a month. I will give you an "
                  "estimate before we start, and I would rather over-estimate it."),
            ("h2", "The question worth asking"),
            ("p", "Not \"how much is an app?\" — nobody can answer that honestly. "
                  "Ask instead: what is the smallest version of this that would be "
                  "worth paying for, and what would that cost? That question has a "
                  "real answer, and getting to it is what the free call is for."),
            ("quote", "If a quote arrives without questions attached to it, it is "
                      "a guess wearing a suit."),
        ],
    },
    {
        "slug": "how-i-use-ai-without-shipping-garbage",
        "title": "How I use AI to build faster without shipping garbage",
        "date": "2026-08-26",
        "date_label": "26 August 2026",
        "read": "7 min read",
        "tag": "AI",
        "summary": "AI writes a lot of the typing in this studio and none of the "
                   "decisions. Here is exactly where the line sits, and why it "
                   "sits there.",
        "body": [
            ("p", "The studio is called HumansOfCoding, which is a claim I should "
                  "probably back up. AI is genuinely central to how fast I can "
                  "work. It is also nowhere near the thing making the decisions. "
                  "Here is the actual division of labour."),
            ("h2", "What the machine does"),
            ("ul", [
                "Boilerplate. Project scaffolding, form validation, CRUD endpoints "
                "— code that has been written a million times and has one right "
                "shape.",
                "Repetitive refactors. Renaming a concept across sixty files. "
                "Tedious, error-prone by hand, and exactly what a machine is for.",
                "Test data. Realistic fixtures in bulk.",
                "First drafts of tests, which I then read carefully, because a test "
                "that asserts the wrong thing is worse than no test.",
                "Explaining unfamiliar libraries faster than reading the docs "
                "end to end.",
            ]),
            ("h2", "What it does not do"),
            ("ul", [
                "Decide what to build. That comes out of a conversation with you, "
                "and it is the part of the project with the highest leverage.",
                "Decide the data model. Get this wrong and every week afterwards "
                "is more expensive. It is worth a human afternoon.",
                "Own anything to do with money, authentication or personal data. I "
                "write those slowly, by hand, and then read them again.",
                "Go live unread. Every line is reviewed by me before it ships. Not "
                "skimmed — read.",
            ]),
            ("h2", "Why the line sits there"),
            ("p", "Modern models are excellent at producing code that looks right. "
                  "That is precisely the danger. Confidently wrong code passes a "
                  "quick glance in a way that obviously-broken code never does, and "
                  "the failure modes cluster in the worst places: an authorisation "
                  "check that is subtly too permissive, an edge case in a refund "
                  "path, a race condition that appears only under load."),
            ("p", "So the rule is simple. AI is allowed to be fast where being "
                  "wrong is cheap and obvious. Where being wrong is expensive or "
                  "silent, a human writes it and a human checks it."),
            ("quote", "The machine does the typing. A person does the thinking, and "
                      "answers the phone when it breaks."),
            ("h2", "What you get out of it"),
            ("p", "Concretely: more of your budget goes into the parts users feel. "
                  "If AI absorbs the mechanical third of a build, that third of the "
                  "money goes into the flow that actually decides whether someone "
                  "comes back — instead of into me typing out a login form for the "
                  "hundredth time."),
            ("h2", "The part that matters when something breaks"),
            ("p", "At 11pm on a Saturday, when payments are failing, you do not "
                  "want a tool. You want a person who understands why the code is "
                  "shaped the way it is, because they shaped it. That is the "
                  "difference the name is pointing at, and it is why I read "
                  "everything before it ships."),
        ],
    },
    {
        "slug": "app-or-website-first",
        "title": "Should you build an app or a website first?",
        "date": "2026-09-02",
        "date_label": "2 September 2026",
        "read": "5 min read",
        "tag": "Building",
        "summary": "Almost everyone asks for an app. For most businesses, for the "
                   "first version, a website is the better answer — and here is "
                   "the specific test for when it isn't.",
        "body": [
            ("p", "\"I want an app\" is how roughly four out of five first "
                  "conversations begin. Sometimes that is right. More often, for a "
                  "first version, a website gets there faster and finds out more."),
            ("h2", "The case for a website first"),
            ("ul", [
                "<strong>Nothing to install.</strong> An app asks for a download "
                "before it has proved it is worth anything. Most people say no, "
                "and you never learn why.",
                "<strong>One build, every device.</strong> No iOS and Android "
                "split, no separate testing.",
                "<strong>You can ship on a Tuesday.</strong> No review queue "
                "between you and a fix.",
                "<strong>Google can find it.</strong> App stores are not a "
                "discovery channel for a business nobody is searching for yet.",
                "<strong>It can be sent as a link.</strong> Which matters enormously "
                "if your customers arrive from Instagram or WhatsApp.",
            ]),
            ("h2", "When an app is genuinely the right call"),
            ("p", "There is a real test, and it is short. You need an app when the "
                  "thing you are building depends on something only an app can do:"),
            ("ul", [
                "It has to work without a network connection — a driver in a dead "
                "zone, a field technician in a basement.",
                "It needs push notifications people will genuinely act on. Not "
                "marketing pushes; operational ones.",
                "It needs continuous access to the camera, GPS or Bluetooth while "
                "running in the background.",
                "People use it every day, for years, and the icon on the home "
                "screen is doing real work.",
            ]),
            ("p", "If none of those are true, an app is usually a more expensive "
                  "route to the same place."),
            ("h2", "The middle option nobody mentions"),
            ("p", "A well-built website can be installed to a phone's home screen, "
                  "run full-screen without a browser bar, and work offline for "
                  "read-only content. For a lot of businesses this covers "
                  "everything they actually wanted from \"an app\", at the cost of "
                  "a website. It is worth ten minutes of the first call."),
            ("h2", "A concrete sequence"),
            ("ol", [
                "Build the website version. Get real people using it.",
                "Watch what they do on phones specifically, and where they drop off.",
                "If the thing standing between you and growth is genuinely a "
                "native capability, build the app then — with a year of real usage "
                "data telling you exactly which screens matter.",
            ]),
            ("p", "That order is cheaper, faster, and produces a better app at the "
                  "end of it than starting with the app would have."),
        ],
    },
    {
        "slug": "questions-to-ask-before-hiring-a-developer",
        "title": "Seven questions to ask before hiring any developer",
        "date": "2026-09-05",
        "date_label": "5 September 2026",
        "read": "6 min read",
        "tag": "Hiring",
        "summary": "Including me. If someone cannot answer these clearly, that is "
                   "the answer.",
        "body": [
            ("p", "Hiring someone to build software is hard precisely when you "
                  "cannot evaluate the work yourself. You can still evaluate the "
                  "answers to these. Ask them of me too."),
            ("h2", "1. Who owns the code?"),
            ("p", "The answer should be you, in writing, in a repository you have "
                  "an account on from day one. If the code lives somewhere you "
                  "cannot see and you would lose it by leaving, you are renting "
                  "your own product."),
            ("h2", "2. What happens if you disappear?"),
            ("p", "Everyone gets ill and everyone eventually moves on. Ask what "
                  "another developer would need to pick this up. \"The code is "
                  "documented and the deployment is scripted\" is a real answer. "
                  "\"That won't happen\" is not."),
            ("h2", "3. What is not included in this price?"),
            ("p", "If the answer is \"nothing, it's all covered\", they have not "
                  "thought about it. Cloud hosting, domains, app-store fees, "
                  "payment-gateway commission and message costs are always paid by "
                  "someone. Find out now, not in month three."),
            ("h2", "4. What would you cut if the budget were half?"),
            ("p", "This is the best question on the list. Someone who has actually "
                  "shipped things will answer immediately and specifically, because "
                  "they have made this trade before. Someone who has not will say "
                  "it all matters."),
            ("h2", "5. How will I see progress?"),
            ("p", "You should be looking at something that runs, weekly, from the "
                  "second or third week. Not screenshots and not a percentage. A "
                  "long silence followed by a big reveal is where projects go to "
                  "fail."),
            ("h2", "6. What have you got wrong before?"),
            ("p", "Anyone with a decade of experience has broken production, "
                  "under-estimated a project or shipped a bug that cost someone "
                  "money. A candid, specific answer tells you they learned "
                  "something. A blank one tells you they either have not done much "
                  "or will not tell you when it happens on yours."),
            ("h2", "7. Who exactly writes the code?"),
            ("p", "Worth asking plainly in 2026. Some of it will be AI-assisted at "
                  "almost any studio — that is fine and it makes things faster. "
                  "What you want to know is whether a human reads all of it before "
                  "it goes live, and whether that human will still be reachable "
                  "when something breaks."),
            ("quote", "My own answer to all seven is on this site. If any of it "
                      "stops being true, it should stop being written here."),
            ("h2", "One more, for free"),
            ("p", "Ask whether they will tell you not to build something. A "
                  "developer whose advice is always \"yes, and it'll cost this "
                  "much\" is a supplier. One who occasionally says \"you don't need "
                  "that yet\" is worth considerably more than they charge."),
        ],
    },
]

# Newest first, everywhere they are listed. Sorting here rather than at each
# call site means the index, the nav panel and the home page cannot disagree
# about the order.
ARTICLES.sort(key=lambda a: a["date"], reverse=True)

ARTICLE_TAGS = []
for _a in ARTICLES:
    if _a["tag"] not in ARTICLE_TAGS:
        ARTICLE_TAGS.append(_a["tag"])
