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
        "questions": [
            "How many outlets, and do prices or menus differ between them?",
            "Who answers the phone at 8pm on a Friday, and what breaks first?",
            "Do you deliver with your own riders or a third-party fleet?",
            "Roughly what share of orders are repeat customers today?",
            "Is there a POS the kitchen already uses that this has to sit beside?",
        ],
        "hard": ("Keeping three kitchens and one customer in agreement", [
            "The screens are the easy half. The difficulty is that an order is a "
            "shared piece of state being changed by four parties — the customer, "
            "the kitchen, the rider and the payment gateway — none of whom are "
            "looking at the same screen and any of whom can act at a moment the "
            "others do not expect.",
            "The specific failure to design against: a customer pays, and the "
            "kitchen then discovers the item is finished. Money has moved and the "
            "product cannot be delivered. That path needs a decided answer — "
            "automatic refund, substitution offer, or a call — before a line of "
            "code exists, because retrofitting it means touching payments, "
            "notifications and the kitchen screen at once.",
            "The other one is stock. Marking an item sold out has to reach every "
            "device holding a menu within seconds, or two more customers order it "
            "while the kitchen is still typing. That is why order state runs over "
            "a live connection rather than being polled every thirty seconds.",
        ]),
        "success": [
            "A third of repeat orders move off the aggregator within three months "
            "— that is the commission this is meant to save.",
            "Kitchens accept new orders within ninety seconds during peak hours.",
            "Under two per cent of paid orders are cancelled after payment.",
            "The owner opens the daily summary without being reminded to.",
        ],
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
        "questions": [
            "How many batches and centres, and how often do students move between them?",
            "Who owns the fee spreadsheet today, and what happens when they are on leave?",
            "Do the parents you need to reach have smartphones, or is SMS the realistic channel?",
            "What happens to fees when a student joins mid-term or drops out?",
            "Are tests objective, subjective, or both?",
        ],
        "hard": ("Attendance a teacher will actually mark", [
            "Every feature here is straightforward except this one, and this one "
            "decides whether the whole system is worth anything. If attendance is "
            "not marked reliably, the parent messages are wrong, the reports are "
            "wrong, and staff go back to the register within a fortnight.",
            "The constraint is that a teacher will give this about forty seconds, "
            "standing up, at the start of a class, on their own phone, sometimes "
            "with no signal in a basement classroom. That rules out a form with a "
            "dropdown per student. It means the batch opens pre-marked present, "
            "the teacher taps only the absentees, and the whole thing saves "
            "locally and syncs later.",
            "It also means being careful about what happens when a class is "
            "cancelled, a substitute teaches, or a student attends a different "
            "batch that day. Those are the cases that make the data untrustworthy, "
            "and the moment the data is untrustworthy nobody uses the system.",
        ]),
        "success": [
            "Attendance is marked for over ninety per cent of classes in the first "
            "month, without anyone chasing teachers.",
            "The gap between a fee falling due and being collected drops.",
            "Front-desk calls asking about attendance or marks fall noticeably.",
            "Parents log in more than once — a single visit means the screen did "
            "not answer their question.",
        ],
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
        "questions": [
            "Which systems does the data come from, and can we get API or database access?",
            "How many manual corrections happen in a normal week, and what are they?",
            "Who signs off that the numbers are right today?",
            "What should happen when a source file simply does not arrive?",
            "Who is allowed to see margins, and who is not?",
        ],
        "hard": ("The rules nobody wrote down", [
            "The technical work here is ordinary. The hard part is that the "
            "spreadsheet contains years of accumulated judgement that exists only "
            "in one person's head: this branch codes its returns differently, that "
            "supplier's file has a blank first row, these two product names are "
            "the same thing, this number is always wrong on the first of the month "
            "and gets fixed by hand.",
            "None of that is documented, and the person doing it often cannot list "
            "it on request — they only recognise it when they see it. So the "
            "discovery week is not a meeting. It is sitting beside them while they "
            "do the job and writing down every decision, including the ones they "
            "make without noticing.",
            "What comes out of that gets split in two. Rules that can be stated "
            "precisely become code with tests. Rules that cannot get a flag: the "
            "system stops and asks a human rather than guessing. Guessing silently "
            "is how automated reporting loses people's trust, and trust here is "
            "the entire product.",
        ]),
        "success": [
            "The two hours a day come back, and the person who owned the "
            "spreadsheet is doing something else.",
            "New numbers and old numbers agree for thirty consecutive days before "
            "the spreadsheet is retired.",
            "An alert fires before a human notices the problem, at least once.",
            "More than one person can run and explain the report.",
        ],
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
        "questions": [
            "How many listings, and who keeps them current?",
            "Where do leads arrive from today, and what does each one cost you?",
            "How many agents, and how are leads shared between them now?",
            "What is your follow-up rule — and is it actually followed?",
            "Do you want prices public, on request, or a mix?",
        ],
        "hard": ("A CRM salespeople will actually use", [
            "The website is the straightforward half. CRMs fail for a reason that "
            "has nothing to do with engineering: they ask a salesperson to do "
            "admin, and a salesperson under target will not do admin.",
            "So the design question is not what data would be useful to capture. "
            "It is what is the least a person can enter after a call, and how do "
            "we make entering it faster than not entering it. In practice that "
            "means two taps for the common outcomes — no answer, call back, visit "
            "booked — a free-text note that is optional, and never a required "
            "field the agent has to think about.",
            "The other half is making the tool give something back immediately. An "
            "agent who logs a call should see their follow-up list reorder itself "
            "in front of them. If the CRM only takes and never gives, it becomes "
            "the thing that gets updated on Friday afternoon from memory, and at "
            "that point the pipeline is fiction.",
        ]),
        "success": [
            "Every incoming lead is assigned to a named agent within five minutes.",
            "No lead sits with no activity for more than forty-eight hours.",
            "Agents log outcomes on the day, not at the end of the week.",
            "Listing pages appear in Google results for the localities you care about.",
        ],
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
        "questions": [
            "How many drivers, and are the phones theirs or yours?",
            "Where does coverage actually fail on a normal route?",
            "What counts as proof of delivery today, and who asks for it?",
            "Do you own the vehicles, or is it a contracted fleet?",
            "How are disputes about non-delivery settled at the moment?",
        ],
        "hard": ("Sync that survives a basement", [
            "An app that needs a connection is not an app for drivers. The whole "
            "build is shaped by that, and the cost sits almost entirely in one "
            "place: reconciling what happened on the device with what the server "
            "believes, after a gap of minutes or hours.",
            "The failure that matters is not the obvious one. A phone with no bars "
            "is easy — you queue and retry. The expensive case is a connection "
            "that half works: the request reaches the server, the server records "
            "it, and the response never gets back. The driver sees a failure, taps "
            "again, and now the delivery is recorded twice. Every action therefore "
            "carries an identifier generated on the device, so a replay is "
            "recognised and discarded rather than duplicated.",
            "Battery is the other constraint that shapes the code. Streaming "
            "location continuously kills a phone by mid-afternoon, and a dead "
            "phone records nothing at all — so positions are batched and sent "
            "periodically, which is less precise on the map and far more useful in "
            "practice.",
        ]),
        "success": [
            "Over ninety-five per cent of stops are recorded on the device the day "
            "they happen.",
            "Every completed delivery has a photo and a name attached to it.",
            "A delivery dispute is settled from the record rather than from memory.",
            "A driver's phone still has charge at the end of a shift.",
        ],
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
        "questions": [
            "What services do you offer, and how long does each actually take?",
            "How many staff, and can any of them do any service?",
            "What share of customers are walk-ins versus booked?",
            "Do you want deposits, and on which services?",
            "Is there an existing customer list, and in what shape?",
        ],
        "hard": ("Two people, one slot", [
            "This is the smallest build on the list and it still has one genuinely "
            "hard problem: two customers opening the booking page at the same "
            "moment and choosing the same eleven o'clock with the same stylist.",
            "The naive version checks whether the slot is free and then writes the "
            "booking. Between those two steps the other customer does the same "
            "thing, both checks pass, and you have a double booking that the "
            "software created — worse than the paper diary it replaced.",
            "The fix is to make the database refuse it, with a constraint that "
            "cannot allow two bookings to overlap for the same staff member, "
            "rather than relying on application code to check first. That is a "
            "small amount of work done early and an unpleasant amount of work done "
            "late, which is why it belongs in week one.",
        ]),
        "success": [
            "Around a third of bookings arrive through the link within a month.",
            "Zero double bookings, because the database will not permit one.",
            "No-shows fall measurably once reminders are running.",
            "The front desk can serve a walk-in without losing a phone booking.",
        ],
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
        "questions": [
            "Who is the first paying customer, and what do they need on day one?",
            "Per-seat or flat pricing — and what happens when a team shrinks?",
            "How long is the trial, and what does an expired trial still allow?",
            "What must a downgraded customer lose, and what must they keep?",
            "Are there data-residency requirements from your target customers?",
        ],
        "hard": ("Billing state and access state must never disagree", [
            "The product features are yours. The part that goes wrong is the "
            "relationship between what the payment provider believes and what your "
            "application allows, because those are two systems and they will drift.",
            "The rule that prevents most of the pain: access is decided by what "
            "the provider's webhooks have told you, never by what the browser "
            "reported after a checkout. A user who closes the tab mid-redirect has "
            "still paid. A card that fails on renewal at 3am has still failed, "
            "whether or not anyone was looking.",
            "Then there are the states nobody designs for until a customer hits "
            "one: cancelled but paid until the end of the month, downgraded with "
            "more data than the smaller plan allows, a failed payment inside its "
            "retry window, a refund after the period started. Each needs a decided "
            "answer. Most of the support burden in a young SaaS comes from these, "
            "not from the actual product.",
        ]),
        "success": [
            "Access always follows the webhook, and no one has ever edited the "
            "database by hand to fix a subscription.",
            "Trial-to-paid conversion is a number you can see, not a guess.",
            "A failed renewal warns the customer before it cuts them off.",
            "Every workspace's data is provably isolated, tested rather than assumed.",
        ],
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
        "questions": [
            "Where does your traffic come from — Instagram, Google, word of mouth?",
            "What is the single action you want a visitor to take?",
            "Who answers enquiries, and how quickly can they realistically reply?",
            "What changes often enough that you need to edit it yourself?",
            "Do you already own the domain, and is there analytics on the current site?",
        ],
        "hard": ("Saying one thing", [
            "The engineering here is genuinely easy. The hard part is the part "
            "most people want to skip: deciding what the page says.",
            "Almost every small-business site fails the same way. It tries to say "
            "everything — every service, every audience, every reassurance — and a "
            "visitor who arrives from Instagram with fifteen seconds of patience "
            "reads none of it. A page that says one thing clearly outperforms a "
            "page that says nine things completely, and the gap is not small.",
            "Which is why week one is copy, not design, and why it is a "
            "conversation rather than a form. What you actually do, who you do it "
            "for, why someone would pick you, and what you want them to do next. "
            "Design after that is comparatively mechanical. Doing it in the other "
            "order produces something attractive that does not work.",
        ]),
        "success": [
            "The page is usable in under two seconds on a mid-range phone on "
            "mobile data.",
            "Enquiries increase from the same traffic — the traffic already exists.",
            "Every enquiry is answered within one working day.",
            "You changed the hours or a price yourself, without calling anyone.",
        ],
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
        "questions": [
            "Roughly how many distinct products, and how often do they change?",
            "Which GST slabs apply, and do you issue credit notes?",
            "Are products barcoded, or is it search by name at the counter?",
            "Do regular customers buy on credit, and how is that tracked now?",
            "When was stock last counted properly?",
        ],
        "hard": ("Billing fast enough for a queue", [
            "Every design decision at the counter is governed by one number: how "
            "long the customer in front is willing to stand there. If billing is "
            "slower than the handwritten book, staff will keep the book, and every "
            "other feature — stock, alerts, margins — is built on data that never "
            "arrives.",
            "That pushes hard on the interface. Search that matches on partial "
            "names and local spellings, because nobody types a full product name "
            "with a queue forming. Keyboard-first operation, since a mouse is "
            "slower than a barcode scanner and a numeric keypad. Quantity and "
            "discount reachable without leaving the keyboard.",
            "And it has to keep working when the internet does not. A shop cannot "
            "stop selling because a router rebooted, so billing runs against local "
            "storage and syncs after — which then brings back the reconciliation "
            "problem, and is why invoice numbers are issued in a way that cannot "
            "collide when two terminals come back online together.",
        ]),
        "success": [
            "A typical five-item bill takes under thirty seconds end to end.",
            "Counted stock and recorded stock are within a couple of per cent.",
            "Low-stock alerts are acted on rather than dismissed.",
            "The day-end total matches the till without anyone reconciling by hand.",
        ],
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
        "questions": [
            "How many doctors, and how long is a real consultation versus a booked one?",
            "Who takes bookings today — front desk, phone, WhatsApp, all three?",
            "What records exist now, and do old paper files need to come across?",
            "Where is patient data allowed to be stored, and who has decided that?",
            "Who besides the doctor needs to see clinical notes?",
        ],
        "hard": ("Records that are private and findable", [
            "These two requirements pull against each other, and most clinic "
            "software picks a side. Locked down so tightly that the doctor cannot "
            "find last year's visit during a consultation, or so open that "
            "reception can read everyone's history.",
            "The resolution is that access is by role and by relationship, not by "
            "a single switch. Reception sees the schedule, contact details and fee "
            "status. The doctor sees clinical history for the patient in front of "
            "them. Every record opened is logged with who and when — not because "
            "anyone expects misuse, but because an access log is the only way to "
            "answer the question honestly if it is ever asked.",
            "Finding a record is its own problem. Patients return after a year, "
            "having forgotten any identifier except their phone number, and "
            "sometimes give a relative's. So search works on phone number, name "
            "and approximate date together, and the system tolerates a patient "
            "existing twice by making merging easy rather than by pretending "
            "duplicates cannot happen.",
        ]),
        "success": [
            "Patients are given a time and waiting room time falls.",
            "No-shows drop once reminders are running.",
            "A returning patient's history is on screen in under ten seconds.",
            "The access log has been reviewed at least once, by you.",
        ],
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
        "questions": [
            "How many active members, and how many lapsed in the last six months?",
            "What plans exist, and can members freeze or transfer them?",
            "Do you run classes with limited capacity?",
            "Who chases renewals today, and how do they know who to chase?",
            "Is there a desk computer, and does it have a scanner?",
        ],
        "hard": ("Renewals are the product", [
            "It is tempting to treat this as a check-in app with membership "
            "attached. That has it backwards. A gym's revenue is renewals, and "
            "renewals are lost to silence — an expiry nobody noticed, a member who "
            "drifted for three weeks and was never asked why.",
            "So the system is built around expiry rather than around entry. Who "
            "expires in the next fortnight, who has not attended in twenty days, "
            "who cancelled a class twice and did not rebook. Those lists are the "
            "product; check-in is the mechanism that keeps them accurate.",
            "The awkward part is everything that makes a membership not a clean "
            "date range: freezes for travel or injury, transfers between members, "
            "upgrades mid-term, the regular whom the owner informally lets slide "
            "for a fortnight. The spreadsheet handles these by a human ignoring "
            "the rules. Software cannot ignore rules, so the rules have to be "
            "agreed in week one — which is usually the first time anyone has "
            "written them down.",
        ]),
        "success": [
            "The renewal rate improves against the same period last year.",
            "Check-in takes under two seconds at the 7am queue.",
            "The expiring-soon list is worked through every week.",
            "Classes fill closer to capacity, with the waitlist doing the work.",
        ],
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
        "questions": [
            "How many technicians, and how many jobs does each do in a day?",
            "What job types are there, and does each have a standard procedure?",
            "Do technicians carry parts on the van, and who tracks them?",
            "How is an invoice raised today, and how long after the job?",
            "Where does coverage fail — basements, lifts, industrial sites?",
        ],
        "hard": ("Offline sync with money attached", [
            "This build has the delivery app's offline problem plus a complication "
            "that makes it materially harder: the outcome of the job produces an "
            "invoice. A duplicate delivery record is embarrassing. A duplicate "
            "invoice is a phone call from a customer who has been billed twice.",
            "So the sync design has to be stricter. Every job completion carries "
            "an identifier created on the device, and the server treats a repeat "
            "as the same event rather than a new one. Invoice numbers are issued "
            "server-side, never on the device, because two technicians coming back "
            "online in the same minute must not be able to produce the same number.",
            "There is a human constraint too. A technician finishing a job wants "
            "to leave, so anything between them and the van has to be worth its "
            "seconds. The checklist is the invoice — parts used and work done "
            "become line items automatically — because asking someone to enter the "
            "same information twice guarantees the second entry never happens.",
        ]),
        "success": [
            "Jobs are recorded on the day they are done, not reconstructed later.",
            "The invoice leaves before the technician does.",
            "The gap between work done and payment received shrinks.",
            "A disputed job is settled with photos and a timestamp.",
        ],
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
            ("h2", 'What the numbers actually look like'),
            ("p", 'Abstract advice is easy to ignore, so here is the arithmetic. A typical embedding is a list of somewhere between 384 and 1,536 numbers. At four bytes each, one embedding is roughly 1.5KB to 6KB. Ten thousand chunks of text is therefore something in the region of 15MB to 60MB of vectors.'),
            ("p", 'That is a rounding error for any database. It fits in memory on the smallest instance you can rent. The mental image people have — of vectors as some enormous specialised payload — comes from companies operating at a scale most businesses never approach.'),
            ("p", 'Where it does get heavy is the index. Approximate-nearest-neighbour indexes trade memory for speed, and a badly-tuned one on a small instance will either eat the RAM or fall back to scanning everything. That is a configuration problem, not a reason to buy another database.'),
            ("h2", 'Cost, honestly'),
            ("p", 'A managed vector database typically starts somewhere around $70 a month for a production-grade tier, before usage. Adding pgvector to a Postgres instance you are already paying for costs nothing extra.'),
            ("p", 'That difference is small if you are funded and enormous if you are a business testing whether an AI feature is worth having at all. It is also recurring, which is the kind of cost that quietly outlives the feature that justified it.'),
            ("p", 'The other cost is operational and rarely counted. A second datastore means a second thing to back up, monitor, secure, upgrade and keep in sync with the first. When a document is deleted from Postgres, something has to remember to delete its vectors too. That “something” is code you now maintain.'),
            ("h2", 'The bit that gets skipped: evaluation'),
            ("p", 'Almost nobody building a retrieval feature sets up a way to tell whether it is getting better. Then a change gets made — a different embedding model, a new chunk size — and the judgement of whether it helped is somebody trying three questions they happen to remember.'),
            ("p", 'You do not need anything elaborate. Twenty to fifty real questions with the passage that should be retrieved for each, and a script that reports how often the right passage appears in the top five results. An afternoon of work, and it converts every future change from an argument into a measurement.'),
            ("quote", 'Without an evaluation set you are not tuning a system. You are rearranging it and hoping.'),
            ("h2", 'A short glossary, for the meeting'),
            ("ul", [
                '<strong>Embedding</strong> — the list of numbers representing a piece of text. Produced by a model; the same model must be used for storing and for searching, or the numbers are not comparable.',
                '<strong>Chunk</strong> — the unit of text you store. Choosing these well is the single biggest lever on quality.',
                '<strong>RAG</strong> — retrieval-augmented generation. Find relevant passages, put them in the prompt, ask the model to answer using them. Most “AI on your documents” products are this.',
                '<strong>Hybrid search</strong> — combining vector and keyword results. Almost always better than either alone, and frequently omitted.',
                '<strong>Re-ranking</strong> — a second, slower model reorders the top twenty results. Often a bigger quality win than changing databases.',
            ]),
            ("h2", 'If someone tells you that you need one'),
            ("p", 'Ask two questions. How many chunks will we have in a year? And what does this give us that pgvector does not, at that number? Both have concrete answers. If neither comes back with one, the recommendation is habit rather than analysis.'),
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
            ("h2", 'A worked example of confidently wrong'),
            ("p", 'The abstract warning is easy to nod along to, so here is the shape of a real one. Ask for an endpoint that lets a user fetch their own orders. You will reliably get something that reads the user id from the request, queries orders for that id, and returns them. It looks correct. It has tests. The tests pass.'),
            ("p", "The problem is where the user id came from. If it was taken from a parameter the client sends rather than from the verified session, then any logged-in customer can read any other customer's orders by changing a number in the URL. The code is not broken — it does exactly what it says. It is just answering the wrong question about who is asking."),
            ("p", 'This class of bug does not announce itself. Nothing crashes, no test fails, and the feature works perfectly in every manual check you would think to do. It is found by someone reading the code and asking where each value came from — or by a customer, later, which is considerably worse.'),
            ("h2", 'How to review AI-written code quickly'),
            ("p", 'Reading every line sounds slow. In practice it is fast if you know what you are looking for, because the failure modes cluster.'),
            ("ol", [
                '<strong>Follow the untrusted input.</strong> Anything from the browser is a claim, not a fact. Where does it get checked?',
                '<strong>Check the authorisation, not the authentication.</strong> “Is this a real user” is usually right. “Is this user allowed this particular record” is where it goes wrong.',
                '<strong>Look at the error paths.</strong> Happy paths are nearly always fine. What happens when the payment provider times out halfway?',
                '<strong>Question anything clever.</strong> Unusual constructs are where a model has pattern-matched onto something from a different context.',
                '<strong>Read the tests as claims.</strong> A test asserting the wrong behaviour is worse than no test, because it makes the wrong behaviour official.',
            ]),
            ("h2", 'What it means for how long things take'),
            ("p", 'The honest accounting is less dramatic than the marketing. Writing code is perhaps thirty per cent of building software. The rest is deciding what to build, understanding the existing system, testing, fixing, deploying and explaining.'),
            ("p", 'So even a tool that made typing instantaneous would not make projects three times faster. What it does is shift where the time goes: less on mechanical production, more on judgement and review. My estimates have not halved. They have become more reliable, because the boring parts no longer vary much.'),
            ("p", 'There is a second-order effect that matters more. Because scaffolding is nearly free, it is now cheap to build a rough version of something and find out it was the wrong idea. Being wrong sooner is worth more than typing faster.'),
            ("h2", 'Where this is heading, carefully'),
            ("p", 'These tools improve quickly and any specific claim I make about their limits will age. What seems durable is the shape of the problem: systems that generate plausible output need someone accountable for whether it is correct, and that accountability is not a technical problem that a better model dissolves.'),
            ("p", 'So the question to ask a studio is not whether they use AI. It is who answers the phone when the thing it wrote breaks at 11pm, and whether that person understands why the code is shaped the way it is.'),
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
            ("h2", 'The migration nobody budgets for'),
            ("p", 'The argument for picking a specialised database early is usually that migrating later will be painful. That is true. It is also true that the migration you are trying to avoid is far less likely than the one you will cause.'),
            ("p", 'In practice, moving from Postgres to something else because you genuinely outgrew it is rare, well-understood and happens when you have revenue and engineers. Moving from a document store to Postgres because you need transactions and joins is common, is done under pressure, and happens exactly when you can least afford it.'),
            ("p", 'Optimising for the second scenario is the better bet, and it is the one people talk about less because it is embarrassing.'),
            ("h2", 'Things people believe Postgres cannot do'),
            ("ul", [
                "<strong>“It can't handle unstructured data.”</strong> JSONB columns store arbitrary documents, can be indexed and queried, and sit beside your relational columns in the same row.",
                "<strong>“It can't scale.”</strong> Read replicas, connection pooling and a correctly indexed schema carry applications far beyond where most businesses ever reach. Most “Postgres doesn't scale” stories are a missing index.",
                '<strong>“You need a separate search engine.”</strong> Full-text search with ranking and stemming is built in and adequate up to a surprisingly large corpus.',
                '<strong>“You need a message queue.”</strong> SELECT ... FOR UPDATE SKIP LOCKED gives a safe work queue. Not the right answer at enormous throughput; entirely right for sending emails and generating reports.',
            ]),
            ("h2", 'How not to paint yourself into a corner'),
            ("p", 'Choosing well matters less than a handful of habits that keep the choice reversible.'),
            ("ol", [
                '<strong>Keep schema changes in version control</strong> as migration files, applied by a script. Never by hand on a live database.',
                '<strong>Do not scatter database queries through the application.</strong> Keep them behind a layer, so replacing the store later touches a boundary rather than everything.',
                '<strong>Use real types.</strong> Dates as dates, money as a decimal type — never a float, which will eventually lose you a paisa in a way that is maddening to trace.',
                '<strong>Let the database enforce what must be true.</strong> Foreign keys, unique constraints, not-null. Application code has bugs; constraints do not stop being enforced because a code path was missed.',
                '<strong>Test your restore, not your backup.</strong> A backup nobody has restored is a belief, not a backup.',
            ]),
            ("h2", 'The one-line version'),
            ("p", 'Start with the boring, well-understood thing that does eighty per cent of everything adequately. Add a specialist when you have a specific measured problem it solves. That order costs less, breaks less, and leaves you with fewer things to be woken up by.'),
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
            ("h2", 'What “fast” actually means to the person waiting'),
            ("p", 'Both camps claim speed, and both are telling the truth about different moments. It helps to name them.'),
            ("ul", [
                '<strong>Time until something appears.</strong> Server rendering wins, usually decisively. The browser gets HTML and paints it.',
                '<strong>Time until it responds to a tap.</strong> This is where server-rendered pages can disappoint — the pixels arrived, the JavaScript that makes the menu work has not.',
                '<strong>Time for the next screen.</strong> A single-page app wins here, because it already has the code and often the data.',
            ]),
            ("p", 'The gap that annoys users most is the second one: a page that looks ready and ignores you. It reads as broken in a way a visible spinner does not, and it is the specific failure of shipping a large JavaScript bundle to a mid-range phone.'),
            ("h2", 'The costs a single-page app adds'),
            ("p", 'Beyond the initial download, choosing to render in the browser means taking on work the server used to do for free.'),
            ("ol", [
                '<strong>Routing.</strong> The back button, deep links and refresh all have to be made to work. They were free before.',
                '<strong>Data fetching and caching.</strong> When to refetch, what to show while waiting, what to do when it fails. Every screen, forever.',
                '<strong>Two places to keep in step.</strong> Validation rules, permissions and formatting now exist on both sides and can disagree.',
                '<strong>Error handling in the browser.</strong> A server error page is automatic; a client-side crash shows a blank white screen unless you build for it.',
            ]),
            ("p", 'None of these are reasons not to do it. They are reasons it costs more, and that cost should be paid for a screen that earns it rather than out of habit.'),
            ("h2", 'A decision table you can actually use'),
            ("ul", [
                '<strong>Marketing pages, articles, listings, catalogues</strong> — server-rendered. Strangers arrive here from search and social.',
                '<strong>Dashboards, consoles, editors, anything behind a login</strong> — single-page. People stay, and interaction speed is the product.',
                '<strong>Checkout and forms</strong> — server-rendered with light interactivity. Reliability beats slickness where money is involved.',
                '<strong>Booking flows</strong> — either, but keep the first page fast; that is where people leave.',
            ]),
            ("h2", 'What I would ask before choosing'),
            ("p", 'What device and connection does a typical user have? Do strangers arrive on this screen, or only people who logged in? How long is a session? Does search need to read it?'),
            ("p", 'Four questions, and between them they decide it. Notice that none of them is about which framework is currently fashionable, which is what the argument is usually actually about.'),
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
            ("h2", 'What it costs to build'),
            ("p", 'Adding passkeys as an option to an existing login is not a large project — the browser APIs do the cryptography and libraries exist for every common backend. Reckon on a week or so for the happy path.'),
            ("p", 'The estimate goes wrong when the recovery flow, the multi-device story and the admin tooling are treated as details. Realistically, budget two to three times the happy path for everything around it: enrolling a second device, replacing a lost one, letting support see which credentials an account has, and revoking one.'),
            ("p", 'That ratio is not unusual for authentication work. It is just unusually often left out of the estimate, because the demo is the happy path and the demo is what gets costed.'),
            ("h2", 'The things worth doing before this'),
            ("p", 'If account security is the goal and the budget is finite, passkeys are not the first thing I would spend it on. In rough order of value per rupee:'),
            ("ol", [
                '<strong>Rate-limit the login endpoint.</strong> Credential-stuffing is the most common attack on small products and it is largely stopped by sensible limits and lockouts.',
                '<strong>Store passwords correctly.</strong> A modern hashing algorithm with a proper work factor. If this is wrong, nothing else matters.',
                '<strong>Offer two-factor at all.</strong> Even SMS, imperfect as it is, beats a single factor for most accounts.',
                '<strong>Check new passwords against known-breached lists.</strong> Cheap to add, and it stops the reuse that causes most compromises.',
                '<strong>Then passkeys</strong>, as an additional option.',
            ]),
            ("h2", 'What it looks like to a user who has never seen one'),
            ("p", 'Worth being blunt about: many people will not know what a passkey is, and a sign-in screen offering an unfamiliar thing loses users. The wording matters more than the cryptography.'),
            ("p", 'What works is describing the outcome rather than the mechanism — “use your fingerprint or face to sign in next time” rather than “register a passkey”. Offer it after a successful login, not instead of one, so nobody is blocked by a concept they did not ask about.'),
            ("quote", 'Every authentication improvement is also a chance to lock out the people you were protecting. That is the tradeoff to design around.'),
            ("h2", 'Where they are genuinely worth the trouble'),
            ("p", 'If your users are businesses, if the account holds money or client data, or if you have already seen credential-stuffing attempts in your logs, passkeys move the needle and are worth the recovery work.'),
            ("p", 'If you are building a booking page where the worst outcome of a compromised account is a cancelled haircut, an email link is simpler, cheaper and honestly proportionate. Security effort should match what is behind the door, not what is fashionable to have implemented.'),
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
            ("h2", 'What syncing actually involves'),
            ("p", '“It works offline” sounds like one feature. It is four, and each has to be decided rather than discovered.'),
            ("ol", [
                '<strong>A queue of intents.</strong> Not “the new state” but “what the user did” — mark job complete, add photo, change quantity. Actions replay cleanly; states overwrite each other.',
                '<strong>An identifier per action, made on the device.</strong> So the server can recognise the same action arriving twice and ignore the second. Without this, every flaky connection creates duplicates.',
                '<strong>A conflict rule per data type.</strong> Last write wins is fine for a note and wrong for a stock count. Decide per type, in advance.',
                '<strong>Visible sync state.</strong> Saved on device, sending, sent, failed. A technician needs to know whether the office has seen their work; a silent spinner is not an answer.',
            ]),
            ("h2", 'The conflict question, concretely'),
            ("p", 'Two people edit the same record while disconnected. Both come back online. Something has to give, and pretending otherwise just means the outcome is decided by whichever request happened to arrive second.'),
            ("p", "For most business data, server-wins with the loser's version kept and flagged is the humane answer — nothing is destroyed and a person can look. For counts and totals, neither side should win: the correct answer is usually to apply both changes as deltas, or to refuse and ask. For anything with money attached, refuse and ask. Always."),
            ("h2", 'How to test it, since it will not test itself'),
            ("p", 'This is the part that gets skipped, and it is why offline features ship broken. Testing on office wifi proves nothing at all.'),
            ("ul", [
                'Use the network throttling in developer tools, and the offline mode.',
                'Test the half-connection deliberately: request sent, response lost. This is the case that creates duplicates and it will not occur by accident on your desk.',
                'Kill the app mid-sync. The queue has to survive being force-closed.',
                'Let the device sit offline for a full day of work, then reconnect. Twenty queued actions behave differently from two.',
                'Test two devices making conflicting changes to the same record.',
            ]),
            ("h2", 'What it costs, so you can decide'),
            ("p", 'As a rough rule, a mobile app that must work offline is around twice the effort of the same app online-only. Not because storage is hard, but because every feature now has a disconnected path, a sync path and a conflict path, and all three need building and testing.'),
            ("p", 'That is a real number and it deserves an honest decision rather than being discovered in month three. If the app is used at a desk, spend the money on features. If it is used in a van, spend it here — because the alternative is an app your team quietly stops opening.'),
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
            ("h2", 'How long an MVP should take'),
            ("p", 'If the answer is more than about eight weeks, it is not an MVP any more, whatever anyone is calling it. That is not a rule about budgets; it is about what the timescale does to the exercise.'),
            ("p", 'Past a couple of months, three things go wrong. The market you were testing has moved. The team has become attached to the thing and will interpret ambiguous results generously. And the cost has grown large enough that admitting it did not work has become expensive in a way that has nothing to do with money.'),
            ("p", 'Four to eight weeks keeps all three honest. It is short enough that you can afford to be wrong and long enough to build something a real person will actually use.'),
            ("h2", 'What happens after — the part nobody plans'),
            ("p", 'Most MVP conversations stop at launch, which is roughly like planning a wedding and not a marriage. Three things follow and all three should be agreed before the build starts.'),
            ("ol", [
                '<strong>Who watches it?</strong> Someone has to look at what users actually do, daily, for the first fortnight. If nobody owns that, you have bought a product and not an experiment.',
                '<strong>What is the decision date?</strong> A day, in the calendar, when you look at the numbers and decide continue, change or stop. Without one, MVPs drift into being the product by default.',
                '<strong>Who fixes it?</strong> Real users find real bugs in week one. If there is no arrangement for that, the experiment dies of neglect and you will wrongly conclude the idea failed.',
            ]),
            ("h2", 'The MVP that should not be built'),
            ("p", 'Sometimes the honest advice is not to build software at all, and a developer who never says this is a supplier rather than an adviser.'),
            ("p", 'If the question is whether people want the service, you can often answer it with a landing page and a phone number for a fraction of the cost. If the process is not yet settled, software will freeze a bad version of it in place. If nobody has ever done the job manually, you do not yet know what to automate — do it by hand for a month, badly, and build the thing you learn you needed.'),
            ("p", 'I have talked people out of builds on this basis. It costs me the project and it saves them a year, which is a trade I am comfortable with, because the ones who come back are the ones worth working for.'),
            ("h2", 'A short checklist before you commit'),
            ("ul", [
                'Can you write down, in one sentence, what this will tell you?',
                'Do you know what result would make you stop?',
                'Is there a real person who will use it in week one, by name?',
                'Is it under eight weeks?',
                'Have you removed everything that would not change the answer?',
            ]),
            ("p", 'Five yeses and it is worth building. A no on the first two means the conversation is not finished, and building anyway is how budgets disappear into things nobody can evaluate.'),
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
            ("h2", 'A worked example'),
            ("p", 'Take the booking MVP from the case studies — a real shape rather than an abstraction. Roughly where the effort goes:'),
            ("ul", [
                '<strong>Week one: the rules.</strong> Services, durations, staff, opening hours, and what counts as an available slot. No code. This is the week that prevents the expensive mistakes.',
                '<strong>Weeks two and three: the build.</strong> Public booking page, the calendar, the front-desk view, and the database constraint that makes a double booking impossible.',
                '<strong>Week four: live.</strong> Reminders, deposits if wanted, real customers, and the fixes that only real customers surface.',
            ]),
            ("p", 'That is the shape that starts at ₹20,000. Add three more staff with different service lists, an existing customer database to import, and deposits on some services but not others, and it is a different number — not because anyone is being greedy, but because each of those adds rules that have to be modelled and tested.'),
            ("h2", 'Fixed price or by the hour?'),
            ("p", 'I quote fixed prices for well-defined work, and I am straightforward about why that is not generosity. A fixed price transfers risk to me, so it includes a margin for the risk. If the work is genuinely well-understood, that margin is small and you get certainty cheaply.'),
            ("p", 'Where a fixed price goes wrong is when the scope is not actually known. Then one of two things happens: the price carries a large buffer you pay for whether or not it is needed, or it does not, and the project quietly turns into a negotiation about what was implied. Neither is good for either side.'),
            ("p", 'So for exploratory work — integrating with a system nobody has documented, or a first version where the requirements are genuinely still forming — I would rather work in short, priced blocks with a decision point at the end of each. You can stop after any of them.'),
            ("h2", 'What a change costs mid-project'),
            ("p", 'Changes are normal and I am not going to pretend otherwise. What varies enormously is when they arrive.'),
            ("ul", [
                '<strong>During the first week</strong> — usually free. Nothing is built yet; we are still deciding what to build.',
                '<strong>During the build, in an area not yet started</strong> — small. Reordering work is cheap.',
                '<strong>During the build, in something already finished</strong> — the real cost of the change, plus retesting what it touches.',
                '<strong>A change to the data model, after there is live data</strong> — the most expensive kind by a distance, because existing records have to be migrated and the migration has to be right the first time.',
            ]),
            ("p", 'That last line is why I push so hard on getting the data model right in week one, and why I will spend an unglamorous afternoon on it while you are keen to see screens.'),
            ("h2", 'How to compare two quotes honestly'),
            ("p", 'A cheaper number is not a cheaper project. Before comparing, make both sides answer the same four questions.'),
            ("ol", [
                'What exactly is included, written as a list you could tick off?',
                'What third-party costs will I be billed for, by whom, and roughly how much per month?',
                'What happens after launch — is any fixing included, and for how long?',
                'Who owns the code and the accounts, in writing?',
            ]),
            ("p", 'Two quotes that look ₹15,000 apart routinely turn out to be for different projects entirely. Ask these and the gap usually explains itself, in one direction or the other.'),
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
            ("h2", 'A day, in practice'),
            ("p", 'Abstract policy is easy to state and hard to check, so here is what it actually looks like on a normal working day.'),
            ("p", 'Morning is usually the part with no AI in it: reading what a client sent, deciding what the next piece of work is, and — if it touches the shape of the data — drawing it out and thinking about what happens in a year. That work is slow on purpose and it is the highest-value hour of the day.'),
            ("p", "The middle of the day is where the tools earn their place. Scaffolding the screens, the endpoints, the forms, the test fixtures. I read every diff as it lands rather than at the end, because reviewing four hundred lines at five o'clock is how things get waved through."),
            ("p", 'The end of the day is review and deletion. A surprising amount of what gets generated is technically fine and unnecessary — an abstraction for one use, a config option nobody asked for, error handling for a case that cannot occur. Removing it costs nothing today and saves whoever reads this in two years.'),
            ("h2", 'The things I do not let it touch'),
            ("ul", [
                '<strong>The data model.</strong> Get it wrong and every week afterwards is more expensive. It is worth a human afternoon and a whiteboard.',
                '<strong>Authorisation.</strong> Not “is this a real user” but “is this user allowed this record”. The single most common place I see plausible, wrong code.',
                '<strong>Money.</strong> Payments, refunds, invoice numbering, anything with a currency in it. Slowly, by hand, then read again the next morning.',
                '<strong>Anything with personal data.</strong> What is stored, for how long, who can see it, and what the access log records.',
                '<strong>Deletion.</strong> Any code that removes something permanently gets written by a person and tested against a copy first.',
            ]),
            ("h2", 'Why the review is not optional'),
            ("p", "The uncomfortable truth about reviewing generated code is that it is harder than reviewing a colleague's. A colleague's mistakes have a grain to them — you learn where a particular person tends to slip. Generated code is uniformly confident, and the errors are distributed differently: rare, but with no tell."),
            ("p", 'So the review has to be systematic rather than instinctive. Where did this value come from. What happens if this fails halfway. Who is allowed to call this. That is a checklist rather than a feeling, and running it is the actual job now.'),
            ("h2", 'What you are paying for'),
            ("p", 'It is worth being direct about this, since it bears on the price. You are not paying me to type. You are paying for the decisions about what should exist, the judgement about which parts are dangerous, and the fact that someone read all of it and will answer for it.'),
            ("p", 'The typing being cheap is why an MVP can start at ₹20,000 rather than at several lakh. The reading being expensive is why it is not free, and why I would be suspicious of anyone quoting as though it were.'),
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
            ("h2", 'What an app costs that a website does not'),
            ("p", 'The build itself is only part of it. An app brings a set of ongoing obligations that a website simply does not have, and they are rarely in the first conversation.'),
            ("ul", [
                '<strong>Two platforms.</strong> Even sharing a codebase, iOS and Android differ in permissions, notifications, background behaviour and review rules. Testing is doubled.',
                "<strong>Store accounts and fees.</strong> Apple charges yearly, Google once. Both must be in your name, not your developer's — this matters enormously if you ever change developer.",
                '<strong>Review queues.</strong> A fix is not live when you press publish. It is live when a reviewer approves it, which can be hours or days, and can be rejected for reasons that surprise you.',
                '<strong>Users on old versions.</strong> People do not update. Your server has to keep speaking to a version of the app from eight months ago, or you have to force upgrades, which loses users.',
                '<strong>OS updates.</strong> Both platforms change things yearly. An app left alone for two years often will not build, let alone run.',
            ]),
            ("p", 'None of this is a reason to avoid apps. It is a reason to be sure you need one, because these costs continue long after the build is paid for.'),
            ("h2", 'The store part nobody warns you about'),
            ("p", "First submissions get rejected routinely, and usually for something unrelated to the app's quality: a missing privacy policy, a login screen with no way to try the app, a permission whose justification was not written clearly enough, or an account-deletion route that must exist inside the app."),
            ("p", 'Budget a week for the first submission and do not schedule a launch event on the assumption it appears on a particular day. This is the single most common cause of a missed launch date on mobile projects, and it is entirely predictable, which makes missing it avoidable.'),
            ("h2", 'What “install to home screen” actually gets you'),
            ("p", "A well-built website can be added to a phone's home screen, open full-screen without browser chrome, cache content so it opens offline, and — on Android reliably, on iOS with caveats — send push notifications."),
            ("p", 'What it still cannot do well: run in the background, use Bluetooth or the sensors freely, or appear in an app store where people look for things. If none of those matter to you, this route gives most of what people mean by “an app” at the cost of a website, with no review queue between you and a fix.'),
            ("quote", 'Ask what specifically you need that only an app can do. If the answer is “it feels more serious”, that is a design problem, not a platform one.'),
            ("h2", 'The order I would actually recommend'),
            ("p", 'Website first, in almost every case. Get real people using it and watch where they struggle on a phone. Then, if what stands between you and growth is genuinely a native capability, build the app — with a year of usage data telling you exactly which three screens matter.'),
            ("p", 'The apps built that way are smaller, better and cheaper than the ones built first, because they are built from evidence instead of from guesses about what people would want.'),
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
            ("h2", 'Three answers that should worry you'),
            ("p", 'Beyond the questions themselves, some replies are informative in ways the speaker does not intend.'),
            ("ul", [
                "<strong>“That won't be a problem.”</strong> To any question about risk. Every project has problems; someone who has shipped things knows which ones are likely and will name them.",
                '<strong>A quote with no questions attached.</strong> If a price arrives before anyone has asked how many users, what it integrates with, or what happens to your existing data, the number is decoration.',
                "<strong>“You wouldn't understand the technical details.”</strong> Anything in this field can be explained to an intelligent person who does not do it for a living. Refusing to is either an inability to explain or an unwillingness to be checked.",
            ]),
            ("h2", 'What to agree in writing before money moves'),
            ("p", 'Not a forty-page contract. A single page covering six things prevents almost every dispute I have seen or heard about.'),
            ("ol", [
                '<strong>What is being built</strong>, as a list specific enough to tick off. “A booking system” is not a scope.',
                '<strong>What is not included</strong>, explicitly. This line saves more arguments than any other.',
                '<strong>Who owns the code and the accounts.</strong> You, in a repository you have access to from day one.',
                '<strong>Payment schedule tied to visible progress</strong>, not to dates. You should be able to see something running before each payment.',
                '<strong>What happens to bugs after launch</strong>, and for how long.',
                '<strong>How either side ends it</strong>, and what you keep if they do.',
            ]),
            ("h2", 'How to tell it is going well, three weeks in'),
            ("p", 'You will not be able to judge the code. You can judge these, and they correlate better than most people expect.'),
            ("ul", [
                'You have seen something running — not a screenshot, not a percentage — in at least two of the three weeks.',
                'They have said no to something, or proposed a cheaper way to do it.',
                'Questions come back to you as questions, rather than assumptions being made silently and revealed later.',
                'Bad news arrives early and unprompted. A developer who only reports good news is not having a smooth project; they are managing you.',
            ]),
            ("h2", 'And if it is going badly'),
            ("p", 'Stop early. The instinct is to keep paying because of what has already been spent, and that instinct is expensive — the money is gone either way, and the only question is whether more follows it.'),
            ("p", 'This is exactly why the payment schedule should be tied to visible progress and why the code should be in your repository from the first week. Both make leaving cheap, which is precisely when you find out whether the arrangement was fair.'),
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

# Read times are derived rather than typed, so they cannot drift away from the
# text after an edit. 200 words a minute is the usual reading estimate.
def _words(article):
    n = 0
    for kind, value in article["body"]:
        n += len(" ".join(value).split()) if kind in ("ul", "ol") else len(str(value).split())
    return n


for _a in ARTICLES:
    _a["read"] = "%d min read" % max(3, round(_words(_a) / 200.0))
