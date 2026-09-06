<script lang="ts">
	import { siteConfig, buildWhatsAppUrl, PixelIcon } from '$lib';

	const serviceIconMap: Record<string, 'computer' | 'recovery' | 'linux' | 'web'> = {
		computer: 'computer',
		'data-recovery': 'recovery',
		'linux-server': 'linux',
		web: 'web'
	};
</script>

<section
	id="layanan"
	class="border-t border-border py-16 md:py-24"
	aria-labelledby="services-heading"
>
	<!-- Section Header -->
	<div class="max-w-2xl">
		<p class="tag-mono mb-3 text-xs font-semibold tracking-wider text-accent">LAYANAN</p>
		<h2
			id="services-heading"
			class="text-2xl font-bold tracking-tight text-foreground sm:text-3xl md:text-4xl"
		>
			Yang bisa dibantu NALAR
		</h2>
		<p class="mt-3 text-base text-foreground-muted sm:text-lg">
			Pilih lingkup bantuan yang paling relevan dengan kendala atau kebutuhanmu saat ini.
		</p>
	</div>

	<!-- Numbered Editorial Rows (Content-first, not card soup) -->
	<div class="mt-12 divide-y divide-border border-y border-border">
		{#each siteConfig.services as service (service.id)}
			<article class="py-8 sm:py-10">
				<div class="grid grid-cols-1 gap-5 lg:grid-cols-12 lg:gap-10">
					<!-- Col 1: Number, Title & Desktop CTA -->
					<div class="flex flex-col justify-between lg:col-span-4">
						<div>
							<div class="flex items-center gap-2.5">
								<span
									class="flex h-6 w-6 items-center justify-center rounded-xs border border-border bg-canvas-subtle text-foreground shadow-[1px_1px_0px_0px_var(--color-border-strong)]"
								>
									<PixelIcon name={serviceIconMap[service.id] ?? 'computer'} size={13} />
								</span>
								<span class="tag-mono text-xs text-foreground-subtle">
									{service.number}
								</span>
							</div>
							<h3 class="mt-2 text-xl font-bold tracking-tight text-foreground sm:text-2xl">
								{service.title}
							</h3>
						</div>

						<!-- Desktop CTA: visible only on lg+ screens -->
						<div class="mt-6 hidden lg:block">
							<a
								href={buildWhatsAppUrl(service.whatsappContext)}
								target="_blank"
								rel="noopener noreferrer"
								class="inline-flex items-center gap-1.5 text-sm font-semibold text-accent transition-colors hover:text-accent-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
							>
								<span>{service.ctaLabel}</span>
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

					<!-- Col 2: Summary, Concrete Scope Details & Mobile CTA -->
					<div class="lg:col-span-8">
						<p class="text-base leading-relaxed font-medium text-foreground sm:text-lg">
							{service.shortDescription}
						</p>

						<ul class="mt-4 grid grid-cols-1 gap-2.5 text-sm text-foreground-muted sm:grid-cols-2">
							{#each service.details as detail (detail)}
								<li class="flex items-start gap-2">
									<span class="mt-0.5 text-accent select-none">•</span>
									<span>{detail}</span>
								</li>
							{/each}
						</ul>

						<!-- Mobile CTA: placed after descriptions and bullets on mobile/tablet screens -->
						<div class="mt-5 border-t border-border/60 pt-3 lg:hidden">
							<a
								href={buildWhatsAppUrl(service.whatsappContext)}
								target="_blank"
								rel="noopener noreferrer"
								class="inline-flex items-center gap-1.5 text-sm font-semibold text-accent transition-colors hover:text-accent-hover focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent"
							>
								<span>{service.ctaLabel}</span>
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
			</article>
		{/each}
	</div>
</section>
