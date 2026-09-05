<script lang="ts">
	import Hero from '$lib/components/Hero.svelte';
	import Philosophy from '$lib/components/Philosophy.svelte';
	import Services from '$lib/components/Services.svelte';
	import Audience from '$lib/components/Audience.svelte';
	import Process from '$lib/components/Process.svelte';
	import RecoveryNotice from '$lib/components/RecoveryNotice.svelte';
	import WhyNalar from '$lib/components/WhyNalar.svelte';
	import Portfolio from '$lib/components/Portfolio.svelte';
	import FAQ from '$lib/components/FAQ.svelte';
	import FinalCTA from '$lib/components/FinalCTA.svelte';
</script>

<!-- Full-width Hero section with edge-to-edge pixel art background -->
<Hero />

<!-- Standard constrained container for editorial sections -->
<div class="mx-auto w-full max-w-5xl px-4 sm:px-6 lg:px-8">
	<Philosophy />
	<Services />
	<Audience />
	<Process />
	<RecoveryNotice />
	<WhyNalar />
	<Portfolio />
	<FAQ />
	<FinalCTA />
</div>
