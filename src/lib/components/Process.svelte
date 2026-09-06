<script lang="ts">
	import { siteConfig } from '$lib';
</script>

<section
	id="cara-kerja"
	class="border-t border-border py-16 md:py-24"
	aria-labelledby="process-heading"
>
	<!-- Section Header -->
	<div class="max-w-2xl">
		<p class="tag-mono mb-3 text-xs font-semibold tracking-wider text-accent">ALUR KERJA</p>
		<h2
			id="process-heading"
			class="text-2xl font-bold tracking-tight text-foreground sm:text-3xl md:text-4xl"
		>
			Nggak tahu masalahnya apa? Nggak apa-apa.
		</h2>
		<p class="mt-3 text-base text-foreground-muted sm:text-lg">
			Prosesnya dibuat sesederhana dan senyaman mungkin. Kamu cukup jelaskan apa yang terjadi tanpa
			khawatir istilah teknis.
		</p>
	</div>

	<!-- 4-Step Simple Numbered Flow (Clean, reassuring) -->
	<div class="mt-12 grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4">
		{#each siteConfig.process as step (step.number)}
			<div class="relative border-t border-border pt-6">
				<div class="flex items-center gap-2">
					<span class="inline-block h-1.5 w-1.5 bg-accent select-none" aria-hidden="true"></span>
					<span class="font-mono text-xs font-semibold text-accent">
						Langkah {step.number}
					</span>
				</div>
				<h3 class="mt-2 text-xl font-bold tracking-tight text-foreground">
					{step.title}
				</h3>
				<p class="mt-2.5 text-sm leading-relaxed text-foreground-muted">
					{step.description}
				</p>
			</div>
		{/each}
	</div>
</section>
