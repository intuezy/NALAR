<script lang="ts">
	import { buildWhatsAppUrl } from '$lib';

	let scrollY = $state(0);

	// Shows only after scrolling past the Hero section (~380px)
	const isVisible = $derived(scrollY > 380);
</script>

<svelte:window bind:scrollY />

<aside
	class="fixed right-4 bottom-[calc(1.25rem+env(safe-area-inset-bottom,0px))] z-40 transition-all duration-300 ease-out md:hidden {isVisible
		? 'pointer-events-auto translate-y-0 opacity-100'
		: 'pointer-events-none translate-y-6 opacity-0'}"
	aria-label="Konsultasi cepat via WhatsApp"
>
	<a
		href={buildWhatsAppUrl('general')}
		target="_blank"
		rel="noopener noreferrer"
		class="group inline-flex items-center gap-2.5 rounded-full border border-border-strong bg-foreground px-4 py-2.5 text-xs font-semibold text-canvas shadow-[2px_2px_0px_0px_#1754cf] transition-all hover:bg-foreground/90 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-accent active:translate-y-0.5"
		aria-label="Konsultasi kendala teknis via WhatsApp"
	>
		<span class="flex h-2 w-2 rounded-full bg-emerald-400" aria-hidden="true"></span>
		<span class="tracking-wide">Konsultasi WhatsApp</span>
		<svg
			xmlns="http://www.w3.org/2000/svg"
			viewBox="0 0 20 20"
			fill="currentColor"
			class="h-3.5 w-3.5 transition-transform group-hover:translate-x-0.5"
			aria-hidden="true"
		>
			<path
				fill-rule="evenodd"
				d="M5.22 14.78a.75.75 0 001.06 0l7.22-7.22v5.69a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75h-7.5a.75.75 0 000 1.5h5.69l-7.22 7.22a.75.75 0 000 1.06z"
				clip-rule="evenodd"
			/>
		</svg>
	</a>
</aside>
