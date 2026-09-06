<script lang="ts">
	import { siteConfig } from '$lib';

	const hasProjects = siteConfig.projects && siteConfig.projects.length > 0;
</script>

{#if hasProjects}
	<section
		id="portofolio"
		class="border-t border-border py-16 md:py-24"
		aria-labelledby="portfolio-heading"
	>
		<div class="max-w-2xl">
			<p class="tag-mono mb-3 text-xs font-semibold tracking-wider text-accent">PORTOFOLIO</p>
			<h2
				id="portfolio-heading"
				class="text-2xl font-bold tracking-tight text-foreground sm:text-3xl md:text-4xl"
			>
				Beberapa hal yang sedang dikerjakan
			</h2>
			<p class="mt-3 text-base text-foreground-muted sm:text-lg">
				Dokumentasi penyelesaian masalah riil. Kami menyajikan studi kasus berbasis alur yang
				transparan tanpa klaim atau ulasan rekaan.
			</p>
		</div>

		<!-- List of real projects when available -->
		<div class="mt-12 divide-y divide-border border-y border-border">
			{#each siteConfig.projects as project (project.id)}
				<article class="py-8 sm:py-10">
					<div class="flex items-center gap-3">
						<span class="tag-mono text-xs text-accent">{project.category}</span>
						<span class="text-xs text-foreground-subtle">·</span>
						<h3 class="text-xl font-bold text-foreground">{project.title}</h3>
					</div>

					<div class="mt-6 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
						<div class="border-t border-border pt-4">
							<span class="tag-mono text-xs text-foreground-subtle">MASALAH</span>
							<p class="mt-1.5 text-sm text-foreground-muted">{project.problem}</p>
						</div>
						<div class="border-t border-border pt-4">
							<span class="tag-mono text-xs text-foreground-subtle">NALAR</span>
							<p class="mt-1.5 text-sm text-foreground-muted">{project.analysis}</p>
						</div>
						<div class="border-t border-border pt-4">
							<span class="tag-mono text-xs text-foreground-subtle">SOLUSI</span>
							<p class="mt-1.5 text-sm text-foreground-muted">{project.solution}</p>
						</div>
						<div class="border-t border-border pt-4">
							<span class="tag-mono text-xs font-semibold text-accent">HASIL</span>
							<p class="mt-1.5 text-sm font-medium text-foreground">{project.result}</p>
						</div>
					</div>
				</article>
			{/each}
		</div>
	</section>
{/if}
