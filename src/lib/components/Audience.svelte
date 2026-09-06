<script lang="ts">
	import { siteConfig } from '$lib';
</script>

<section
	id="audiens"
	class="border-t border-border py-16 md:py-24"
	aria-labelledby="audience-heading"
>
	<!-- Section Header -->
	<div class="max-w-2xl">
		<p class="tag-mono mb-3 text-xs font-semibold tracking-wider text-accent">UNTUK SIAPA</p>
		<h2
			id="audience-heading"
			class="text-2xl font-bold tracking-tight text-foreground sm:text-3xl md:text-4xl"
		>
			Buat siapa?
		</h2>
		<p class="mt-3 text-base text-foreground-muted sm:text-lg">
			Bantuan teknologi praktis yang dirancang tepat guna, baik untuk kebutuhan personal maupun
			usaha.
		</p>
	</div>

	<!-- 2-Column Clean Editorial Layout -->
	<div class="mt-12 grid grid-cols-1 gap-10 md:grid-cols-2 md:gap-12 lg:gap-16">
		{#each siteConfig.audiences as audience (audience.category)}
			<div class="flex flex-col">
				<div class="border-b border-border pb-4">
					<span class="tag-mono text-xs text-foreground-subtle">Kategori</span>
					<h3 class="mt-1 text-2xl font-bold tracking-tight text-foreground">
						{audience.category}
					</h3>
					<p class="mt-2 text-sm leading-relaxed text-foreground-muted sm:text-base">
						{audience.lead}
					</p>
				</div>

				<ul class="mt-6 flex flex-col gap-3 text-sm text-foreground-muted">
					{#each audience.items as item (item)}
						<li class="flex items-start gap-2.5">
							<span class="mt-0.5 font-bold text-accent select-none">✓</span>
							<span class="leading-relaxed text-foreground">{item}</span>
						</li>
					{/each}
				</ul>
			</div>
		{/each}
	</div>
</section>
