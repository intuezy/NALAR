<script lang="ts">
	import { siteConfig, buildWhatsAppUrl } from '$lib';
</script>

<section
	class="relative w-full overflow-hidden border-b border-border bg-canvas pt-24 pb-14 sm:pt-28 sm:pb-18 md:pt-32 md:pb-22 lg:pt-36 lg:pb-28"
	aria-labelledby="hero-heading"
>
	<!-- Full-Width Pixel Art Background Layer -->
	<div class="pointer-events-none absolute inset-0 overflow-hidden select-none" aria-hidden="true">
		<img
			src="/images/nalar-pixel-techlab.webp"
			alt=""
			class="h-full w-full object-cover object-[75%_center] sm:object-[80%_center] lg:object-right"
			style="image-rendering: pixelated;"
			fetchpriority="high"
		/>

		<!-- Desktop Gradient Overlay: Solid canvas on text side, smooth fade revealing workstation on right -->
		<div
			class="absolute inset-0 hidden md:block"
			style="background: linear-gradient(to right, #faf9f6 0%, #faf9f6 38%, rgba(250, 249, 246, 0.94) 52%, rgba(250, 249, 246, 0.4) 75%, rgba(250, 249, 246, 0.1) 100%);"
		></div>

		<!-- Subtle top vignette to protect navbar link contrast -->
		<div
			class="absolute inset-x-0 top-0 hidden h-24 md:block"
			style="background: linear-gradient(to bottom, rgba(250, 249, 246, 0.35) 0%, transparent 100%);"
		></div>

		<!-- Mobile / Tablet Gradient Overlay: Top-to-bottom fade for effortless readability -->
		<div
			class="absolute inset-0 block md:hidden"
			style="background: linear-gradient(to bottom, #faf9f6 0%, rgba(250, 249, 246, 0.96) 45%, rgba(250, 249, 246, 0.8) 75%, rgba(250, 249, 246, 0.38) 100%);"
		></div>

		<!-- Subtle bottom blend into page background -->
		<div
			class="absolute inset-x-0 bottom-0 h-12"
			style="background: linear-gradient(to top, #faf9f6 0%, transparent 100%);"
		></div>
	</div>

	<!-- Content Layer (Aligned with global grid container) -->
	<div class="relative z-10 mx-auto w-full max-w-5xl px-4 sm:px-6 lg:px-8">
		<div class="max-w-2xl">
			<!-- Category / Status Indicator -->
			<div
				class="mb-4 inline-flex items-center gap-2 rounded-sm border border-border/90 bg-canvas/90 px-3 py-1 text-xs shadow-[1.5px_1.5px_0px_0px_var(--color-border)] backdrop-blur-xs"
			>
				<span
					class="inline-block h-2 w-2 bg-accent shadow-[0_0_0_2px_rgba(23,84,207,0.2)]"
					aria-hidden="true"
				></span>
				<span class="tag-mono text-[11px] font-semibold text-foreground-muted"
					>{siteConfig.hero.badge}</span
				>
			</div>

			<!-- Main Headline with subtle blinking pixel terminal cursor -->
			<h1
				id="hero-heading"
				class="text-[2rem] leading-[1.18] font-extrabold tracking-tight text-foreground sm:text-5xl sm:leading-tight md:text-6xl"
			>
				{siteConfig.hero.headline}<span
					class="ml-1.5 inline-block h-6 w-1.5 animate-pulse bg-accent align-middle select-none sm:h-9 sm:w-2.5 md:h-11 md:w-3"
					aria-hidden="true"
				></span>
			</h1>

			<!-- Supporting Copy -->
			<p class="mt-6 text-lg leading-relaxed text-foreground-muted sm:text-xl">
				{siteConfig.hero.subheadline}
			</p>

			<!-- Call to Actions -->
			<div class="mt-8 flex flex-col gap-3 sm:flex-row sm:items-center sm:gap-4">
				<a
					href={buildWhatsAppUrl('general')}
					target="_blank"
					rel="noopener noreferrer"
					class="btn-primary w-full justify-center sm:w-auto"
				>
					<span>{siteConfig.hero.primaryCta}</span>
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

				<a
					href="#layanan"
					class="btn-secondary w-full justify-center bg-canvas/80 backdrop-blur-xs sm:w-auto"
				>
					{siteConfig.hero.secondaryCta}
				</a>
			</div>
		</div>

		<!-- Service Summary (Editorial Row with Pixel Accent) -->
		<div class="mt-14 border-t border-border/80 pt-6">
			<p class="tag-mono text-xs font-semibold tracking-wider text-foreground-subtle">
				FOKUS LAYANAN
			</p>
			<div class="mt-3 flex flex-wrap items-center gap-2 sm:gap-2.5">
				{#each siteConfig.hero.serviceSummary as service (service)}
					<span
						class="inline-flex items-center gap-1.5 rounded-sm border border-border/80 bg-canvas/80 px-2.5 py-1 font-mono text-xs font-medium text-foreground-muted backdrop-blur-xs transition-colors hover:border-accent/50 hover:text-foreground"
					>
						<span class="h-1.5 w-1.5 bg-accent/80 select-none" aria-hidden="true"></span>
						<span>{service}</span>
					</span>
				{/each}
			</div>
		</div>
	</div>
</section>
