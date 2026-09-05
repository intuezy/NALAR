<script lang="ts">
	import { siteConfig, buildWhatsAppUrl, PixelIcon } from '$lib';

	let isMobileMenuOpen = $state(false);
	let scrollY = $state(0);

	const isScrolled = $derived(scrollY > 20);

	function toggleMobileMenu() {
		isMobileMenuOpen = !isMobileMenuOpen;
	}

	function closeMobileMenu() {
		isMobileMenuOpen = false;
	}

	function handleKeydown(event: KeyboardEvent) {
		if (event.key === 'Escape' && isMobileMenuOpen) {
			closeMobileMenu();
		}
	}
</script>

<svelte:window bind:scrollY onkeydown={handleKeydown} />

<header
	class="fixed inset-x-0 top-0 z-40 transition-all duration-300 {isScrolled || isMobileMenuOpen
		? 'border-b border-border bg-canvas/92 shadow-xs backdrop-blur-md'
		: 'border-b border-transparent bg-transparent shadow-none'}"
>
	<div class="mx-auto flex h-16 max-w-5xl items-center justify-between px-4 sm:px-6 lg:px-8">
		<!-- Brand / Logo -->
		<a
			href="/"
			class="group flex items-center gap-2.5 rounded-sm focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
			aria-label="NALAR Beranda"
		>
			<span
				class="flex h-7 w-7 items-center justify-center rounded-sm bg-foreground text-canvas shadow-[1.5px_1.5px_0px_0px_#1754cf] transition-transform group-hover:scale-105"
			>
				<PixelIcon name="brand" size={14} />
			</span>
			<span class="text-xl font-bold tracking-tight text-foreground">
				{siteConfig.name}
			</span>
		</a>

		<!-- Desktop Navigation -->
		<nav class="hidden items-center gap-7 md:flex" aria-label="Navigasi Utama">
			<ul class="flex items-center gap-6 text-sm font-medium text-foreground-muted">
				{#each siteConfig.navItems as item (item.href)}
					<li>
						<a
							href={item.href}
							class="rounded-sm transition-colors hover:text-foreground focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
						>
							{item.label}
						</a>
					</li>
				{/each}
			</ul>

			<!-- CTA Button -->
			<a
				href={buildWhatsAppUrl('general')}
				target="_blank"
				rel="noopener noreferrer"
				class="btn-primary text-sm font-medium"
			>
				<span>Chat WhatsApp</span>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					viewBox="0 0 20 20"
					fill="currentColor"
					class="h-4 w-4"
					aria-hidden="true"
				>
					<path
						fill-rule="evenodd"
						d="M5.22 14.78a.75.75 0 001.06 0l7.22-7.22v5.69a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75h-7.5a.75.75 0 000 1.5h5.69l-7.22 7.22a.75.75 0 000 1.06z"
						clip-rule="evenodd"
					/>
				</svg>
			</a>
		</nav>

		<!-- Mobile Hamburger Toggle -->
		<div class="flex items-center gap-2 md:hidden">
			<a
				href={buildWhatsAppUrl('general')}
				target="_blank"
				rel="noopener noreferrer"
				class="btn-primary px-3.5 py-2 text-xs font-medium"
			>
				WhatsApp
			</a>

			<button
				type="button"
				onclick={toggleMobileMenu}
				aria-expanded={isMobileMenuOpen}
				aria-controls="mobile-navigation"
				aria-label={isMobileMenuOpen ? 'Tutup menu navigasi' : 'Buka menu navigasi'}
				class="inline-flex h-11 w-11 items-center justify-center rounded-md border border-border bg-canvas text-foreground transition-colors hover:bg-canvas-subtle focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
			>
				{#if isMobileMenuOpen}
					<!-- Close Icon -->
					<svg
						xmlns="http://www.w3.org/2000/svg"
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
						stroke-linecap="round"
						stroke-linejoin="round"
						class="h-5 w-5"
						aria-hidden="true"
					>
						<line x1="18" y1="6" x2="6" y2="18" />
						<line x1="6" y1="6" x2="18" y2="18" />
					</svg>
				{:else}
					<!-- Hamburger Icon -->
					<svg
						xmlns="http://www.w3.org/2000/svg"
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
						stroke-linecap="round"
						stroke-linejoin="round"
						class="h-5 w-5"
						aria-hidden="true"
					>
						<line x1="4" y1="8" x2="20" y2="8" />
						<line x1="4" y1="16" x2="20" y2="16" />
					</svg>
				{/if}
			</button>
		</div>
	</div>

	<!-- Mobile Dropdown Navigation -->
	{#if isMobileMenuOpen}
		<div
			id="mobile-navigation"
			class="border-b border-border bg-canvas px-4 pt-2 pb-6 md:hidden"
			role="region"
			aria-label="Menu navigasi ponsel"
		>
			<nav class="flex flex-col gap-1">
				{#each siteConfig.navItems as item (item.href)}
					<a
						href={item.href}
						onclick={closeMobileMenu}
						class="rounded-md px-3.5 py-3 text-base font-medium text-foreground transition-colors hover:bg-canvas-subtle"
					>
						{item.label}
					</a>
				{/each}

				<div class="mt-4 border-t border-border pt-4">
					<a
						href={buildWhatsAppUrl('general')}
						target="_blank"
						rel="noopener noreferrer"
						onclick={closeMobileMenu}
						class="btn-primary w-full justify-center text-sm font-medium"
					>
						<span>Chat WhatsApp</span>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							viewBox="0 0 20 20"
							fill="currentColor"
							class="h-4 w-4"
							aria-hidden="true"
						>
							<path
								fill-rule="evenodd"
								d="M5.22 14.78a.75.75 0 001.06 0l7.22-7.22v5.69a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75h-7.5a.75.75 0 000 1.5h5.69l-7.22 7.22a.75.75 0 000 1.06z"
								clip-rule="evenodd"
							/>
						</svg>
					</a>
				</div>
			</nav>
		</div>
	{/if}
</header>
