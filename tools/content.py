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
]


# --------------------------------------------------------------------------
# ARTICLES
# --------------------------------------------------------------------------
# body: a list of blocks. ("h2", text) | ("p", text) | ("ul", [items])
#       | ("quote", text) | ("ol", [items])

ARTICLES = [
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
        "tag": "Human + AI",
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
