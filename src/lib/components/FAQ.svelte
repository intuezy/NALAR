<script lang="ts">
	import { siteConfig } from '$lib';
</script>

<section id="faq" class="border-t border-border py-16 md:py-24" aria-labelledby="faq-heading">
	<!-- Section Header -->
	<div class="max-w-2xl">
		<div class="tag-mono mb-3 flex items-center gap-2 text-xs text-foreground-subtle">
			<span class="inline-flex gap-1 text-[8px] text-accent select-none" aria-hidden="true"
				>■ ■ ■</span
			>
			<span>08 / TANYA JAWAB</span>
		</div>
		<h2
			id="faq-heading"
			class="text-2xl font-bold tracking-tight text-foreground sm:text-3xl md:text-4xl"
		>
			Pertanyaan yang Sering Diajukan
		</h2>
		<p class="mt-3 text-base text-foreground-muted sm:text-lg">
			Jawaban terbuka seputar proses konsultasi, teknis pengerjaan, dan batasan layanan NALAR.
		</p>
	</div>

	<!-- Accessible Native <details> Stack (Zero JS dependency) -->
	<div class="mt-12 divide-y divide-border border-y border-border">
		{#each siteConfig.faq as item (item.question)}
			<details class="group">
				<summary
					class="flex w-full cursor-pointer list-none items-center justify-between py-5 text-left text-base font-semibold text-foreground transition-colors hover:text-accent focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent sm:text-lg [&::-webkit-details-marker]:hidden"
				>
					<span>{item.question}</span>
					<span
						class="ml-4 shrink-0 text-foreground-subtle transition-transform duration-200 group-open:rotate-180"
					>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							viewBox="0 0 20 20"
							fill="currentColor"
							class="h-5 w-5"
							aria-hidden="true"
						>
							<path
								fill-rule="evenodd"
								d="M5.23 7.21a.75.75 0 011.06.02L10 11.168l3.71-3.938a.75.75 0 111.08 1.04l-4.25 4.5a.75.75 0 01-1.08 0l-4.25-4.5a.75.75 0 01.02-1.06z"
								clip-rule="evenodd"
							/>
						</svg>
					</span>
				</summary>
				<div class="pt-1 pb-5 text-sm leading-relaxed text-foreground-muted sm:text-base">
					<p>{item.answer}</p>
				</div>
			</details>
		{/each}
	</div>
</section>
