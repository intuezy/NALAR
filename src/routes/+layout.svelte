<script lang="ts">
	import './layout.css';
	import favicon from '$lib/assets/favicon.svg';
	import { siteConfig } from '$lib';
	import Navbar from '$lib/components/Navbar.svelte';
	import Footer from '$lib/components/Footer.svelte';
	import MobileFloatingCTA from '$lib/components/MobileFloatingCTA.svelte';

	let { children } = $props();

	const structuredData = JSON.stringify({
		'@context': 'https://schema.org',
		'@type': 'ProfessionalService',
		name: siteConfig.name,
		alternateName: 'NALAR IT Services',
		url: siteConfig.url,
		slogan: siteConfig.tagline,
		description: siteConfig.metaDescription,
		areaServed: 'ID',
		parentOrganization: {
			'@type': 'Organization',
			name: siteConfig.ecosystem,
			url: siteConfig.parentUrl
		},
		serviceType: [
			'Perbaikan & Optimasi Komputer / Laptop',
			'Pengecekan & Pemulihan Data (Data Recovery)',
			'Instalasi Linux & Setup Server / VPS',
			'Pembuatan Website & Deployment'
		]
	});

	const jsonLdScript = `<script type="application/ld+json">${structuredData}<` + `/script>`;
</script>

<svelte:head>
	<link rel="icon" type="image/svg+xml" href={favicon} />
	<title>{siteConfig.metaTitle}</title>
	<meta name="description" content={siteConfig.metaDescription} />
	<link rel="canonical" href="{siteConfig.url}/" />

	<!-- Open Graph / Facebook -->
	<meta property="og:type" content="website" />
	<meta property="og:site_name" content={siteConfig.name} />
	<meta property="og:locale" content="id_ID" />
	<meta property="og:url" content="{siteConfig.url}/" />
	<meta property="og:title" content={siteConfig.metaTitle} />
	<meta property="og:description" content={siteConfig.metaDescription} />

	<!-- Twitter / X -->
	<meta name="twitter:card" content="summary" />
	<meta name="twitter:url" content="{siteConfig.url}/" />
	<meta name="twitter:title" content={siteConfig.metaTitle} />
	<meta name="twitter:description" content={siteConfig.metaDescription} />

	<!-- Structured Data (JSON-LD) -->
	<!-- eslint-disable-next-line svelte/no-at-html-tags -->
	{@html jsonLdScript}
</svelte:head>

<!-- Skip Link for Accessibility -->
<a
	href="#main-content"
	class="sr-only fixed top-4 left-4 z-50 rounded-md bg-foreground px-4 py-2 text-sm font-medium text-canvas focus:not-sr-only focus:ring-2 focus:ring-accent focus:outline-none"
>
	Menuju konten utama
</a>

<div class="flex min-h-screen flex-col bg-canvas text-foreground">
	<Navbar />
	<main id="main-content" class="flex-1">
		{@render children()}
	</main>
	<Footer />
	<MobileFloatingCTA />
</div>
