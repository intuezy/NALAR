# NALAR Landing Page — Master Implementation Prompt

You are the lead frontend engineer and product designer responsible for building the official landing page for **NALAR**, an Indonesian IT service brand.

The project must be implemented using **SvelteKit + TypeScript + Tailwind CSS**.

Your job is not merely to create a visually attractive website. The primary goal is to create a website that is:

- Extremely clear
- Fast
- Trustworthy
- Human
- Easy to scan
- Easy to understand for non-technical customers
- Professional without looking corporate
- Modern without looking like an AI-generated SaaS template
- Content-first
- Conversion-oriented
- Easy to maintain

The website will eventually be hosted at:

`jasa.intuezy.com`

**Intuezy is the personal/programmer brand. NALAR is the service brand.**

---

# 0. CORE BRAND CONTEXT

## Brand

**NALAR**

## Positioning

NALAR helps individuals and businesses solve practical technology problems.

NALAR is not positioned as a generic software house and not merely as a computer repair service.

The underlying philosophy is:

> Start with the problem. Understand it. Find the appropriate solution. Keep technology simple.

## Primary tagline

> **Ada Masalah, Ada NALAR.**

This means:

> When there is a technology problem, there is NALAR to help figure it out.

Do not translate the tagline into English on the website. The target audience is Indonesian.

## Brand tone

Use Indonesian.

Tone should be:

- Friendly
- Relaxed
- Clear
- Human
- Helpful
- Confident
- Not overly formal
- Not slang-heavy
- Not corporate
- Not childish

Avoid exaggerated marketing language.

Do NOT use phrases such as:

- "Solusi IT terbaik"
- "Jasa IT terpercaya nomor satu"
- "Revolusi digital"
- "Transform your business"
- "Cutting-edge technology"
- "Seamless digital experience"
- "One-stop IT solution"

Unless there is a specific reason and the wording is genuinely useful.

---

# 1. TARGET CUSTOMERS

NALAR serves two broad audiences.

## Individuals

Examples:

- Students
- Programmers
- Linux users
- Laptop owners
- People with Windows problems
- People who need data recovery
- People who need a new laptop configured
- People who want Linux or dual boot
- People who need help setting up their development environment

## Businesses

Primarily small businesses and organizations that need practical technology help.

Examples:

- UMKM
- Local businesses
- Small offices
- Freelancers
- Service businesses
- Shops
- Small organizations

Potential business needs:

- Website
- Website deployment
- Domain and hosting
- Basic server setup
- Website maintenance
- Simple internal systems
- Simple automation

Do not position NALAR as an enterprise consultancy.

---

# 2. CORE SERVICES

The initial service structure has four major categories.

## 01 — COMPUTER

Practical computer and laptop assistance.

Services may include:

- Windows installation
- Linux installation
- Dual boot
- Laptop setup
- Driver and software setup
- Troubleshooting
- Performance optimization
- Boot problems
- Wi-Fi/Bluetooth/printer problems
- Basic hardware/storage upgrades
- Backup and data transfer

---

## 02 — DATA RECOVERY

Data recovery from problematic storage devices.

Possible cases:

- Accidentally deleted files
- Drive not detected
- Partition problems
- File system corruption
- Disk corruption
- HDD/SSD problems
- Recoverable data from damaged storage

IMPORTANT:

Never promise 100% recovery.

Use wording such as:

> "Kami cek kondisi storage dan kemungkinan recovery terlebih dahulu."

Also communicate this important principle:

> If important data is lost, stop using the affected drive as much as possible to reduce the risk of overwriting the data.

Do not make the service sound like forensic laboratory recovery if the actual service does not provide that level of capability.

---

## 03 — LINUX & SERVER

Practical Linux and basic server assistance.

Services:

- Linux installation
- Dual boot
- Linux setup for programming
- Development environment setup
- Git setup
- Docker setup
- Linux troubleshooting
- VPS setup
- Basic Linux server configuration
- Nginx
- SSL
- Domain/DNS configuration
- Website deployment

Do not advertise advanced enterprise DevOps/cloud architecture services.

Do not claim capabilities that are not explicitly established.

---

## 04 — WEB

Simple, practical websites and deployment.

Services:

- Landing pages
- Business websites
- UMKM websites
- Portfolio websites
- Domain setup
- Hosting setup
- SSL
- Deployment
- Website maintenance
- Basic content updates

The selling point is not "we write code".

The selling point is:

> **A website that is ready to use.**

---

# 3. FUTURE SERVICES

NALAR may eventually offer:

- Simple information systems
- Internal dashboards
- Business workflow tools
- Simple automation

Do NOT make these future services the primary focus of the initial landing page.

If included, present them as:

> **Solusi khusus**

with copy explaining that customers can describe their workflow/problem and NALAR can assess whether a custom solution makes sense.

---

# 4. DESIGN PHILOSOPHY

This is extremely important.

The website must be **content-first**.

The user should immediately understand:

1. What NALAR is
2. What problems NALAR solves
3. What services are available
4. Whether NALAR can help them
5. What they should do next

---

# 5. ANTI AI-SLOP RULES

The following design patterns are explicitly prohibited unless there is a strong usability reason.

DO NOT create:

- Excessive glassmorphism
- Huge gradient blobs
- Random abstract 3D shapes
- Excessive floating cards
- Excessive pill badges
- Decorative cards everywhere
- Excessive icons
- Generic SaaS dashboard illustrations
- Random purple/blue AI gradients
- Fake statistics
- Fake testimonials
- Fake customer logos
- Fake reviews
- Fake portfolio items
- Excessive rounded rectangles
- Giant centered marketing headlines with meaningless copy
- Excessive animations
- Cursor-following effects
- Parallax for decoration
- "AI generated" visual noise
- Over-designed navigation
- Component soup

Do not use icons simply because there is empty space.

Every visual element must have a purpose.

---

# 6. VISUAL DIRECTION

The visual identity should be:

**Modern + simple + editorial + technical + human.**

Think:

- Strong typography
- Generous whitespace
- Clear hierarchy
- Precise spacing
- Subtle borders
- Restrained use of color
- Simple layouts
- Strong section headings
- Short paragraphs
- Clear CTAs

The website should feel intentionally designed rather than assembled from a component library.

---

# 7. BRAND CHARACTER

NALAR's visual identity should subtly communicate:

> Thinking before solving.

A possible recurring visual language is a simple numbered/problem-solving structure:

```text
01 / MASALAH
02 / NALAR
03 / SOLUSI
```

Use this sparingly.

It can become a recognizable NALAR design pattern.

Do not turn every section into numbered cards.

---

# 8. COLOR SYSTEM

Do not blindly use the default Tailwind color palette.

Create a small semantic color system.

Recommended direction:

- Neutral/off-white background
- Near-black primary text
- Muted gray secondary text
- One restrained accent color

The accent should be used primarily for:

- CTA
- Links
- Important highlights
- Small brand details

Do not create a rainbow palette.

Do not use gradients unless there is a very strong design reason.

The exact accent color can be refined during implementation, but the overall palette must remain restrained.

---

# 9. TYPOGRAPHY

Typography is one of the primary identity elements.

Prioritize:

- Excellent readability
- Strong hierarchy
- Comfortable line length
- Large but not absurd headings
- Clear body text

Do not use 5+ font families.

Prefer one primary sans-serif family with appropriate weights.

Use a monospace font only for small technical/metadata elements if useful.

Example:

```text
NALAR

01 / COMPUTER

Laptop bermasalah?
```

The typography should do most of the visual work.

---

# 10. RESPONSIVE DESIGN

Design mobile-first.

The website must work exceptionally well on:

- Mobile phones
- Tablets
- Desktop
- Large desktop screens

Do not simply stack desktop components on mobile.

Reconsider hierarchy and spacing for mobile.

The CTA must remain easy to access.

---

# 11. LANDING PAGE INFORMATION ARCHITECTURE

Create the following sections in this order.

---

## SECTION 01 — NAVIGATION

Keep navigation extremely simple.

Suggested:

```text
NALAR

Layanan
Cara Kerja
Tentang
FAQ

[Chat WhatsApp]
```

On mobile, use a simple mobile navigation.

Do not create a complicated mega-menu.

---

# SECTION 02 — HERO

The hero must immediately communicate what NALAR does.

Primary headline:

> **Ada Masalah, Ada NALAR.**

Supporting copy:

> Komputer bermasalah, data hilang, butuh Linux, atau website belum online? Ceritakan masalahnya. Kita bantu cari solusi yang masuk akal dan sesuai kebutuhan.

Primary CTA:

> **Konsultasi**

Secondary action may be:

> **Lihat Layanan**

Below the hero, show a simple text-based service summary:

```text
Computer · Data Recovery · Linux · Web
```

Do not clutter the hero with illustrations.

---

# SECTION 03 — PHILOSOPHY / APPROACH

Heading:

> **Mulai dari masalahnya.**

Copy:

> Nggak semua masalah butuh solusi yang rumit. Kami pahami dulu kebutuhannya, cari penyebabnya, lalu tentukan cara yang paling masuk akal untuk menyelesaikannya.

Introduce the three principles:

```text
PAHAMI
Pahami masalah sebelum menentukan solusi.

PECAHKAN
Cari solusi yang benar-benar sesuai kebutuhan.

SEDERHANAKAN
Teknologi seharusnya membuat sesuatu lebih mudah.
```

Design this as editorial content, NOT three generic cards.

---

# SECTION 04 — SERVICES

Heading:

> **Yang bisa dibantu NALAR**

Introduce four service groups.

### COMPUTER

> Install, setup, troubleshooting, dan optimasi komputer/laptop.

### DATA RECOVERY

> Membantu mengecek dan memulihkan data dari storage yang bermasalah, selama kondisi perangkat memungkinkan.

### LINUX & SERVER

> Linux, dual boot, development environment, VPS, dan deployment.

### WEB

> Landing page, website bisnis, domain, hosting, deployment, dan maintenance.

Each category should allow the user to understand the service without reading a wall of text.

Use numbered editorial rows or simple sections instead of four large cards.

---

# SECTION 05 — WHO IS IT FOR?

Heading:

> **Buat siapa?**

Split into two audiences.

## Individu

> Buat kamu yang punya laptop bermasalah, ingin pindah ke Linux, butuh setup komputer, atau kehilangan data.

Examples:

- Laptop error
- Install ulang
- Dual boot
- Linux setup
- Data recovery

## Bisnis

> Buat bisnis yang butuh website atau bantuan teknis untuk kebutuhan digital sehari-hari.

Examples:

- Website bisnis
- Domain & hosting
- Deployment
- Maintenance
- Solusi khusus

Keep this section concise.

---

# SECTION 06 — HOW IT WORKS

Heading:

> **Nggak tahu masalahnya apa? Nggak apa-apa.**

This section should reduce customer anxiety.

Steps:

### 01 — Ceritakan

> Jelaskan masalahnya sebisanya. Nggak perlu pakai istilah teknis.

### 02 — Kita cek

> Kami pahami kondisinya dan menentukan apa yang sebenarnya perlu dikerjakan.

### 03 — Sepakati

> Jika solusinya sudah jelas, kita sepakati pekerjaan dan biayanya terlebih dahulu.

### 04 — Beres

> Pekerjaan dilakukan sesuai kesepakatan dan hasilnya dijelaskan setelah selesai.

This should feel reassuring and human.

---

# SECTION 07 — DATA RECOVERY NOTICE

Because data recovery is potentially sensitive and high-stakes, give it a dedicated warning.

Heading:

> **Data penting hilang? Jangan buru-buru utak-atik.**

Copy:

> Kalau data penting tiba-tiba hilang atau drive tidak terbaca, sebisa mungkin hentikan penggunaan drive tersebut terlebih dahulu. Penggunaan lanjutan dapat meningkatkan risiko data tertimpa.

Then:

> NALAR bisa membantu mengecek kondisi storage dan kemungkinan recovery sebelum menentukan langkah berikutnya.

CTA:

> **Konsultasikan Data Recovery**

Do not guarantee recovery.

---

# SECTION 08 — WHY NALAR

Do not use generic claims like "professional", "trusted", or "best".

Instead communicate:

### Berangkat dari kebutuhan

> Kami tidak langsung menentukan teknologi. Kami pahami dulu masalahnya.

### Solusi seperlunya

> Kalau masalahnya sederhana, solusinya tidak perlu dibuat rumit.

### Bahasa manusia

> Kamu tidak harus mengerti istilah teknis untuk menjelaskan masalahmu.

### Transparan

> Pekerjaan dan biaya dibicarakan terlebih dahulu sebelum pengerjaan.

Do not invent certifications, years of experience, client counts, or awards.

---

# SECTION 09 — PORTFOLIO

If real portfolio items are not available, DO NOT fabricate them.

Instead create an empty-state section such as:

> **Beberapa hal yang sedang dikerjakan**

or temporarily omit the section.

The architecture should make it easy to add real projects later.

Each future project should use:

```text
MASALAH
Apa yang terjadi?

NALAR
Apa yang dianalisis?

SOLUSI
Apa yang dikerjakan?

HASIL
Apa yang berubah?
```

This structure reinforces the brand philosophy.

---

# SECTION 10 — FAQ

Include useful questions.

Suggested:

### Apakah harus tahu masalahnya dulu?

> Nggak. Ceritakan saja gejalanya atau apa yang terjadi. Kita bantu cek.

### Bisa datang langsung?

Only state this if a physical location is actually established. Otherwise do not claim it.

### Apakah data recovery pasti berhasil?

> Tidak selalu. Kemungkinan recovery tergantung kondisi storage dan bagaimana data tersebut hilang. Kami cek kondisinya terlebih dahulu.

### Bisa install Linux tanpa menghapus Windows?

> Bisa, jika perangkat dan kondisi partisinya memungkinkan. Salah satu opsi adalah dual boot.

### Apakah bisa membantu website yang sudah dibuat tapi belum online?

> Bisa. Kami dapat membantu setup domain, hosting/VPS, SSL, database, dan deployment sesuai kebutuhan.

### Apakah bisa membuat sistem khusus untuk bisnis?

> Bisa untuk kebutuhan tertentu. Ceritakan proses kerja atau masalahnya terlebih dahulu agar dapat dinilai apakah solusi custom memang diperlukan.

---

# SECTION 11 — FINAL CTA

Make this section visually strong but simple.

Headline:

> **Punya masalah IT? Ceritain aja.**

Supporting text:

> Nggak perlu tahu istilah teknisnya. Jelaskan apa yang terjadi, nanti kita bantu cari tahu langkah berikutnya.

CTA:

> **Chat WhatsApp**

Secondary small text:

> Konsultasi awal untuk memahami kebutuhan.

Do not promise "free consultation" unless that policy is actually established.

---

# SECTION 12 — FOOTER

Minimal footer.

```text
NALAR

Ada Masalah, Ada NALAR.

Computer · Data Recovery · Linux · Web

© [current year] NALAR
```

Because NALAR belongs to the Intuezy ecosystem, optionally include:

> Part of the Intuezy ecosystem.

Link to the main Intuezy website only if the actual URL is known/configured.

Do not invent URLs.

---

# 12. WHATSAPP CONVERSION FLOW

All primary CTAs should eventually lead to WhatsApp.

Use a configurable WhatsApp number through environment/configuration rather than hardcoding it throughout components.

Generate a contextual message.

Examples:

For general consultation:

> Halo NALAR, saya mau konsultasi soal kebutuhan IT.

For data recovery:

> Halo NALAR, saya mau konsultasi soal data recovery. Storage saya mengalami masalah...

For website:

> Halo NALAR, saya mau konsultasi soal pembuatan/setting website.

Do not require users to fill a complicated form before contacting NALAR.

---

# 13. TECHNICAL ARCHITECTURE

Use:

- SvelteKit
- TypeScript
- Tailwind CSS
- ESLint
- Prettier

Keep the architecture simple.

Suggested structure:

```text
src/
├── lib/
│   ├── components/
│   ├── config/
│   └── utils/
├── routes/
│   ├── +page.svelte
│   ├── +layout.svelte
│   └── ...
├── app.html
└── ...
```

Do not create unnecessary abstractions.

Do not create a design system library for a single landing page.

Reusable components are fine when they improve maintainability.

---

# 14. COMPONENT STRATEGY

Prefer semantic components such as:

```text
Navbar
Hero
SectionHeading
ServiceList
AudienceSection
ProcessSection
RecoveryNotice
WhyNalar
FAQ
FinalCTA
Footer
```

Do not create generic components like:

```text
CardContainer
GradientBox
FancySection
MagicWrapper
UniversalContainer
```

unless they genuinely improve the code.

Components should correspond to actual design concepts.

---

# 15. PERFORMANCE REQUIREMENTS

Performance is a priority.

Avoid unnecessary client-side JavaScript.

Prefer:

- Server/static rendering
- CSS for visual effects
- Optimized assets
- Lazy loading where appropriate
- Minimal dependencies

Do not add animation libraries unless absolutely necessary.

Do not add a carousel.

Do not add a client-side state management library.

Do not add a UI component framework.

The website should remain fast on low-end mobile devices.

---

# 16. SEO

Implement proper basic SEO.

Include:

- Title
- Meta description
- Canonical URL
- Open Graph metadata
- Twitter/X metadata if appropriate
- Semantic HTML
- Proper heading hierarchy
- Descriptive link text
- Favicon
- robots.txt
- sitemap

Suggested title:

> NALAR — Ada Masalah, Ada NALAR | IT Solutions

Suggested meta description:

> NALAR membantu individu dan bisnis menyelesaikan kebutuhan IT, dari komputer dan data recovery hingga Linux, server, dan website.

Do not keyword-stuff.

---

# 17. ACCESSIBILITY

Follow accessibility best practices.

Requirements:

- Semantic HTML
- Keyboard navigation
- Visible focus states
- Proper contrast
- Alt text for meaningful images
- Decorative images should not create unnecessary screen-reader noise
- Buttons must be actual buttons
- Links must be actual links
- Form controls must have labels
- Do not rely solely on color

---

# 18. ANIMATION

Animation should be subtle and purposeful.

Allowed:

- Small fade/slide on section entrance
- Hover state
- Button interaction
- Navigation transition

Avoid:

- Excessive scroll animations
- Parallax
- Floating elements
- Constant movement
- Bouncy UI
- Cursor effects

The content should remain the focus.

---

# 19. CONTENT RULES

Write all customer-facing content in natural Indonesian.

Prefer:

> "Ceritain aja."

over:

> "Silakan jelaskan permasalahan teknologi yang sedang Anda alami."

Prefer:

> "Nggak perlu ngerti istilah teknis."

over:

> "Tidak diperlukan pengetahuan teknis."

But do not overdo slang.

The tone should feel like a technically capable person talking normally to another person.

---

# 20. TRUST RULES

Never fabricate:

- Testimonials
- Customer logos
- Reviews
- Number of customers
- Certifications
- Awards
- Years of experience
- Company statistics
- Case studies
- Portfolio projects

If real data is unavailable, omit it.

Authenticity is more important than visual credibility tricks.

---

# 21. IMPLEMENTATION TASKS

Do NOT attempt everything blindly in one pass.

Execute the project in the following small tasks.

---

## TASK 01 — Inspect Existing Repository

Before changing anything:

1. Inspect the existing project structure.
2. Identify current framework and dependencies.
3. Identify whether SvelteKit is already configured.
4. Inspect package.json.
5. Inspect existing routes/components.
6. Inspect existing Tailwind configuration.
7. Identify reusable code.
8. Do not delete existing work without understanding it.

Output a concise implementation plan before making major structural changes.

---

## TASK 02 — Establish SvelteKit Foundation

If the repository is not already a SvelteKit project:

1. Set up SvelteKit.
2. Configure TypeScript.
3. Configure Tailwind CSS.
4. Configure ESLint.
5. Configure Prettier.
6. Ensure the project builds successfully.

Keep dependencies minimal.

---

## TASK 03 — Establish Design Tokens

Create the NALAR visual foundation:

- Typography
- Background
- Text colors
- Muted text
- Border
- Accent
- Spacing
- Container width
- Radius
- Focus styles

Do not build the full page yet.

Create a small internal visual language.

---

## TASK 04 — Implement Global Layout

Implement:

- Global CSS
- Body
- Typography
- Main container
- Responsive breakpoints
- Base links
- Buttons
- Selection/focus behavior

Verify mobile and desktop behavior.

---

## TASK 05 — Implement Navbar

Build the minimal navigation.

Requirements:

- Responsive
- Accessible
- Clear CTA
- No unnecessary visual decoration

Test keyboard navigation.

---

## TASK 06 — Implement Hero

Build the hero exactly around:

> Ada Masalah, Ada NALAR.

Prioritize readability.

Do not add decorative illustrations unless they materially improve comprehension.

---

## TASK 07 — Implement Philosophy Section

Implement:

> Mulai dari masalahnya.

Use the:

```text
PAHAMI
PECAHKAN
SEDERHANAKAN
```

structure.

Avoid generic cards.

---

## TASK 08 — Implement Services

Implement:

- Computer
- Data Recovery
- Linux & Server
- Web

Use a content-first editorial layout.

Do not turn every service into a giant card.

---

## TASK 09 — Implement Audience Section

Implement:

- Individu
- Bisnis

Make it immediately obvious which problems each audience can bring.

---

## TASK 10 — Implement Process

Implement:

```text
01 Ceritakan
02 Kita cek
03 Sepakati
04 Beres
```

Keep the visual design simple.

---

## TASK 11 — Implement Data Recovery Notice

Make this section visually distinguishable but not alarming.

Clearly communicate:

- Stop using the drive if possible.
- Recovery is not guaranteed.
- NALAR will assess the situation first.

---

## TASK 12 — Implement Why NALAR

Use the four principles:

- Berangkat dari kebutuhan
- Solusi seperlunya
- Bahasa manusia
- Transparan

Avoid generic marketing claims.

---

## TASK 13 — Implement Portfolio Placeholder

Only implement if useful.

Do not fabricate portfolio items.

Make the component easy to populate later.

---

## TASK 14 — Implement FAQ

Create accessible FAQ behavior.

Prefer native HTML `<details>` / `<summary>` if it provides sufficient UX.

Avoid unnecessary JavaScript.

---

## TASK 15 — Implement Final CTA

Use:

> Punya masalah IT? Ceritain aja.

Make WhatsApp the dominant action.

---

## TASK 16 — Implement Footer

Keep it minimal.

Include NALAR identity and current year.

---

## TASK 17 — Implement SEO

Add:

- Metadata
- Open Graph
- Canonical
- Sitemap
- Robots
- Favicon
- Semantic structure

---

## TASK 18 — Performance Audit

Check:

- JavaScript payload
- Unused dependencies
- Image sizes
- Font loading
- Layout shift
- Mobile performance
- Unnecessary client-side rendering

Remove anything unnecessary.

---

## TASK 19 — Accessibility Audit

Check:

- Keyboard navigation
- Focus states
- Heading hierarchy
- Contrast
- Link names
- Button labels
- Mobile navigation
- Screen reader semantics

Fix issues.

---

## TASK 20 — Final Visual Audit

Review the website as a real customer.

Ask:

1. Can I understand NALAR in 5 seconds?
2. Can I identify the services immediately?
3. Do I know whether NALAR can help me?
4. Does the website feel trustworthy without fake claims?
5. Is the CTA obvious?
6. Does it look like a real human-designed website?
7. Does anything look like generic AI-generated SaaS UI?
8. Is there unnecessary decoration?
9. Is the typography readable?
10. Does mobile feel intentional?

If the answer to any question is no, fix it.

---

# 22. IMPORTANT EXECUTION RULE

Do not optimize for "more features".

Optimize for:

> **clarity → trust → action**

The final page should feel intentionally restrained.

If there is a choice between:

**more visual effects**

and

**better information hierarchy**

always choose information hierarchy.

If there is a choice between:

**more components**

and

**simpler content**

choose simpler content.

If there is a choice between:

**more marketing claims**

and

**specific useful information**

choose useful information.

---

# 23. DEFINITION OF DONE

The implementation is considered complete only when:

- SvelteKit builds successfully
- TypeScript has no errors
- Lint passes
- Formatting passes
- The page is responsive
- Navigation works
- WhatsApp CTAs work through a centralized configuration
- SEO metadata exists
- Accessibility basics are satisfied
- No fake testimonials/statistics/portfolio exist
- No unnecessary dependencies exist
- No obvious AI-slop visual patterns exist
- Content is understandable in Indonesian
- The website communicates NALAR's philosophy clearly
- The primary CTA is obvious
- Mobile performance is good

Do not stop after merely making the page "look good".

The final result must be a usable business landing page.

---

# 24. DEVELOPMENT PRINCIPLE

Build deliberately.

Before implementing each task:

1. Understand the requirement.
2. Inspect existing code.
3. Make the smallest appropriate change.
4. Run the relevant checks.
5. Fix problems immediately.
6. Continue to the next task.

Do not make broad destructive changes.

Do not introduce abstractions without a concrete need.

Do not invent business information.

When information is unknown, create a clearly marked configuration placeholder rather than fabricating it.

The goal is a small, fast, maintainable, human-looking website for a real service business.

**Build NALAR around the problem, not around the technology.**
