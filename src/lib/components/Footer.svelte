<script lang="ts">
	import { siteConfig, PixelIcon } from '$lib';

	const currentYear = new Date().getFullYear();
</script>

<footer class="mt-20 border-t border-border bg-canvas py-12 text-sm text-foreground-muted md:py-16">
	<div class="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8">
		<div class="flex flex-col gap-8 md:flex-row md:items-start md:justify-between">
			<!-- Brand Info -->
			<div class="max-w-sm">
				<div class="flex items-center gap-2.5">
					<span
						class="flex h-6 w-6 items-center justify-center rounded-xs bg-foreground text-canvas shadow-[1px_1px_0px_0px_#1754cf]"
					>
						<PixelIcon name="brand" size={12} />
					</span>
					<span class="text-xl font-bold tracking-tight text-foreground">
						{siteConfig.name}
					</span>
				</div>
				<p class="mt-2 font-medium text-foreground">
					{siteConfig.tagline}
				</p>
				<p class="mt-2 text-xs text-foreground-subtle">
					{siteConfig.hero.serviceSummary.join(' · ')}
				</p>
			</div>

			<!-- Navigation Links -->
			<nav class="flex flex-wrap gap-x-6 gap-y-2 text-sm" aria-label="Navigasi Footer">
				{#each siteConfig.navItems as item (item.href)}
					<a
						href={item.href}
						class="transition-colors hover:text-foreground focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
					>
						{item.label}
					</a>
				{/each}
			</nav>
		</div>

		<!-- Bottom Copyright & Ecosystem Notice -->
		<div
			class="mt-10 flex flex-col items-center justify-between gap-4 border-t border-border pt-6 text-xs text-foreground-subtle sm:flex-row"
		>
			<p>© {currentYear} {siteConfig.name}. Hak cipta dilindungi.</p>

			<p>
				Bagian dari ekosistem
				<a
					href={siteConfig.parentUrl}
					target="_blank"
					rel="noopener noreferrer"
					class="font-medium text-foreground underline transition-colors hover:text-accent focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
				>
					{siteConfig.ecosystem}
				</a>
			</p>
		</div>
	</div>
</footer>
