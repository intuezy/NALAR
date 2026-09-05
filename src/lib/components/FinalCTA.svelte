<script lang="ts">
	import { siteConfig, buildWhatsAppUrl } from '$lib';
</script>

<section
	id="kontak"
	class="border-t border-border py-20 md:py-28"
	aria-labelledby="final-cta-heading"
>
	<div
		class="mx-auto max-w-3xl rounded-xl border border-border bg-canvas-subtle px-6 py-12 text-center shadow-[2px_2px_0px_0px_var(--color-border)] sm:px-12 sm:py-16"
	>
		<div class="inline-flex items-center gap-2">
			<span class="inline-flex gap-1 text-[8px] text-accent select-none" aria-hidden="true"
				>■ ■ ■</span
			>
			<span class="tag-mono text-xs text-foreground-subtle">09 / KONSULTASI</span>
		</div>

		<h2
			id="final-cta-heading"
			class="mt-3 text-3xl font-extrabold tracking-tight text-foreground sm:text-4xl md:text-5xl"
		>
			{siteConfig.finalCta.headline}
		</h2>

		<p class="mx-auto mt-4 max-w-xl text-base leading-relaxed text-foreground-muted sm:text-lg">
			{siteConfig.finalCta.subheadline}
		</p>

		<div class="mt-8 flex flex-col items-center justify-center gap-3 sm:flex-row sm:gap-4">
			<a
				href={buildWhatsAppUrl('general')}
				target="_blank"
				rel="noopener noreferrer"
				class="btn-primary w-full justify-center px-6 py-3.5 text-base font-semibold shadow-xs sm:w-auto"
			>
				<span>{siteConfig.finalCta.primaryAction}</span>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					viewBox="0 0 20 20"
					fill="currentColor"
					class="h-5 w-5"
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

		<p class="mt-4 text-xs text-foreground-subtle">
			{siteConfig.finalCta.note}
		</p>
	</div>
</section>
