<script lang="ts">
	import { siteConfig } from '$lib';

	const hasProjects = siteConfig.projects && siteConfig.projects.length > 0;
</script>

<section
	id="portofolio"
	class="border-t border-border py-16 md:py-24"
	aria-labelledby="portfolio-heading"
>
	<div class="max-w-2xl">
		<div class="tag-mono mb-3 flex items-center gap-2 text-xs text-foreground-subtle">
			<span class="inline-flex gap-1 text-[8px] text-accent select-none" aria-hidden="true"
				>■ ■ ■</span
			>
			<span>07 / PORTOFOLIO</span>
		</div>
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

	{#if hasProjects}
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
	{:else}
		<!-- Authentic Empty-State Explaining the Case Study Framework -->
		<div class="mt-12 rounded-lg border border-dashed border-border bg-canvas-subtle p-6 sm:p-8">
			<div class="max-w-2xl">
				<p class="tag-mono text-xs text-foreground-subtle">STANDAR STUDI KASUS NALAR</p>
				<h3 class="mt-1.5 text-lg font-semibold text-foreground">
					Pendokumentasian Masalah dan Solusi Riil
				</h3>
				<p class="mt-2 text-sm leading-relaxed text-foreground-muted sm:text-base">
					Kami menghindari testimoni dan portfolio rekaan. Studi kasus teknis disusun secara terbuka
					dengan kerangka empat fase:
				</p>
			</div>

			<div class="mt-6 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
				<div class="rounded-md border border-border bg-canvas p-4">
					<span class="font-mono text-xs font-semibold text-accent">01 / MASALAH</span>
					<p class="mt-1 text-xs text-foreground-muted">Apa kendala atau gejala yang dialami?</p>
				</div>
				<div class="rounded-md border border-border bg-canvas p-4">
					<span class="font-mono text-xs font-semibold text-accent">02 / NALAR</span>
					<p class="mt-1 text-xs text-foreground-muted">
						Apa analisis teknis dan penyebab yang ditemukan?
					</p>
				</div>
				<div class="rounded-md border border-border bg-canvas p-4">
					<span class="font-mono text-xs font-semibold text-accent">03 / SOLUSI</span>
					<p class="mt-1 text-xs text-foreground-muted">
						Langkah apa yang disepakati dan dikerjakan?
					</p>
				</div>
				<div class="rounded-md border border-border bg-canvas p-4">
					<span class="font-mono text-xs font-semibold text-accent">04 / HASIL</span>
					<p class="mt-1 text-xs text-foreground-muted">
						Apa perubahan konkret setelah pekerjaan selesai?
					</p>
				</div>
			</div>
		</div>
	{/if}
</section>
