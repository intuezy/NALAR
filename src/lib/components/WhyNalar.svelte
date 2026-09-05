<script lang="ts">
	import { siteConfig } from '$lib';
</script>

<section
	id="kenapa-nalar"
	class="border-t border-border py-16 md:py-24"
	aria-labelledby="why-nalar-heading"
>
	<!-- Section Header -->
	<div class="max-w-2xl">
		<div class="tag-mono mb-3 flex items-center gap-2 text-xs text-foreground-subtle">
			<span class="inline-flex gap-1 text-[8px] text-accent select-none" aria-hidden="true"
				>■ ■ ■</span
			>
			<span>06 / NILAI NALAR</span>
		</div>
		<h2
			id="why-nalar-heading"
			class="text-2xl font-bold tracking-tight text-foreground sm:text-3xl md:text-4xl"
		>
			Kenapa NALAR?
		</h2>
		<p class="mt-3 text-base text-foreground-muted sm:text-lg">
			Tanpa klaim berlebihan atau istilah rumit. Kami berfokus pada cara kerja yang jujur,
			transparan, dan solutif.
		</p>
	</div>

	<!-- 4 Value Points (2x2 Grid, Clean Editorial) -->
	<div class="mt-12 grid grid-cols-1 gap-8 sm:grid-cols-2 sm:gap-10 lg:gap-12">
		{#each siteConfig.whyNalar as item, idx (item.title)}
			<div class="border-t border-border pt-6">
				<div class="flex items-center gap-2">
					<span class="inline-block h-1.5 w-1.5 bg-accent select-none" aria-hidden="true"></span>
					<span class="font-mono text-xs font-semibold text-accent">
						0{idx + 1} / PRINSIP
					</span>
				</div>
				<h3 class="mt-2 text-xl font-bold tracking-tight text-foreground">
					{item.title}
				</h3>
				<p class="mt-2.5 text-sm leading-relaxed text-foreground-muted sm:text-base">
					{item.description}
				</p>
			</div>
		{/each}
	</div>
</section>
