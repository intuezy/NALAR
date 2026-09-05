<script lang="ts">
	import { siteConfig, buildWhatsAppUrl, PixelIcon } from '$lib';
</script>

<section class="border-t border-border py-16 md:py-24" aria-labelledby="recovery-notice-heading">
	<div class="rounded-lg border border-notice-border bg-notice-bg p-6 sm:p-8 md:p-10">
		<div class="flex flex-col gap-6 lg:flex-row lg:items-center lg:justify-between">
			<div class="max-w-2xl">
				<div class="inline-flex items-center gap-2">
					<span
						class="flex h-5 w-5 items-center justify-center rounded-xs bg-notice-border/60 text-notice-text"
					>
						<PixelIcon name="warning" size={12} />
					</span>
					<span class="tag-mono text-xs font-semibold text-notice-text">
						PERHATIAN KHUSUS · DATA RECOVERY
					</span>
				</div>

				<h2
					id="recovery-notice-heading"
					class="mt-2 text-2xl font-bold tracking-tight text-foreground sm:text-3xl"
				>
					{siteConfig.recoveryNotice.heading}
				</h2>

				<p class="mt-3 text-base leading-relaxed text-foreground-muted sm:text-lg">
					{siteConfig.recoveryNotice.lead}
				</p>

				<p class="mt-3 text-sm font-medium text-foreground">
					{siteConfig.recoveryNotice.assurance}
				</p>
			</div>

			<div class="shrink-0 pt-2 lg:pt-0">
				<a
					href={buildWhatsAppUrl('recovery')}
					target="_blank"
					rel="noopener noreferrer"
					class="btn-primary inline-flex w-full justify-center text-sm font-medium sm:w-auto"
				>
					<span>{siteConfig.recoveryNotice.ctaText}</span>
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
		</div>
	</div>
</section>
