<script lang="ts">
	import { siteConfig } from '$lib';
</script>

<section
	id="tentang"
	class="border-t border-border py-16 md:py-24"
	aria-labelledby="philosophy-heading"
>
	<div class="grid grid-cols-1 gap-12 lg:grid-cols-12 lg:gap-16">
		<!-- Left Column: Headline & Narrative Context -->
		<div class="lg:col-span-5">
			<div class="tag-mono mb-3 flex items-center gap-2 text-xs text-foreground-subtle">
				<span class="inline-flex gap-1 text-[8px] text-accent select-none" aria-hidden="true"
					>■ ■ ■</span
				>
				<span>02 / PENDEKATAN</span>
			</div>
			<h2
				id="philosophy-heading"
				class="text-2xl font-bold tracking-tight text-foreground sm:text-3xl md:text-4xl"
			>
				{siteConfig.philosophy.heading}
			</h2>
			<p class="mt-4 text-base leading-relaxed text-foreground-muted sm:text-lg">
				{siteConfig.philosophy.lead}
			</p>
		</div>

		<!-- Right Column: Editorial Content Flow (Not generic cards) -->
		<div class="lg:col-span-7">
			<div class="divide-y divide-border border-y border-border">
				{#each siteConfig.philosophy.pillars as pillar, idx (pillar.tag)}
					<div class="py-6 first:pt-4 last:pb-4 sm:py-8">
						<div class="flex items-center gap-3">
							<!-- 3-Step Pixel Progression: ■ □ □ -> ■ ■ □ -> ■ ■ ■ -->
							<span class="inline-flex gap-1 select-none" aria-hidden="true">
								<span class="inline-block h-2 w-2 bg-accent"></span>
								<span
									class="inline-block h-2 w-2 {idx >= 1
										? 'bg-accent'
										: 'border border-border-strong bg-canvas-subtle'}"
								></span>
								<span
									class="inline-block h-2 w-2 {idx >= 2
										? 'bg-accent'
										: 'border border-border-strong bg-canvas-subtle'}"
								></span>
							</span>
							<span class="tag-mono text-xs font-semibold text-accent">
								{pillar.tag}
							</span>
							<span class="font-mono text-xs text-foreground-subtle">
								/ 0{idx + 1}
							</span>
						</div>
						<h3 class="mt-2.5 text-lg font-semibold text-foreground sm:text-xl">
							{pillar.title}
						</h3>
						<p class="mt-2 text-sm leading-relaxed text-foreground-muted sm:text-base">
							{pillar.description}
						</p>
					</div>
				{/each}
			</div>
		</div>
	</div>
</section>
