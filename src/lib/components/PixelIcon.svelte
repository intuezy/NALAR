<script lang="ts">
	interface Props {
		name: 'brand' | 'computer' | 'recovery' | 'linux' | 'web' | 'warning' | 'cursor';
		size?: number;
		class?: string;
	}

	let { name, size = 16, class: className = '' }: Props = $props();
</script>

<svg
	xmlns="http://www.w3.org/2000/svg"
	viewBox="0 0 16 16"
	width={size}
	height={size}
	fill="currentColor"
	class="inline-block shrink-0 {className}"
	style="shape-rendering: crispEdges;"
	aria-hidden="true"
>
	{#if name === 'brand'}
		<!-- Bespoke 16-bit Pixel N with Accent Dot -->
		<path d="M2 2h3v12H2V2zm9 0h3v12h-3V2zM5 5h2v2H5V5zm2 2h2v2H7V7zm2 2h2v2H9V9z" />
		<rect x="12" y="11" width="3" height="3" fill="#1754cf" />
	{:else if name === 'computer'}
		<!-- 16-bit Pixel Monitor & Hardware -->
		<path d="M1 2h14v9H1V2zm2 2v5h10V4H3z" />
		<path d="M6 12h4v1H6v-1zm-3 2h10v1H3v-1z" />
		<rect x="4" y="5" width="2" height="2" fill="#1754cf" />
		<rect x="7" y="5" width="4" height="1" fill="currentColor" />
		<rect x="7" y="7" width="2" height="1" fill="currentColor" />
	{:else if name === 'recovery'}
		<!-- 16-bit Pixel Storage Drive & Recovery Pulse -->
		<path d="M2 2h12v12H2V2zm2 2v8h8V4H4z" />
		<rect x="6" y="5" width="4" height="4" fill="currentColor" />
		<rect x="7" y="6" width="2" height="2" fill="#faf9f6" />
		<rect x="5" y="10" width="2" height="1" fill="#1754cf" />
		<rect x="9" y="10" width="2" height="1" fill="#1754cf" />
	{:else if name === 'linux'}
		<!-- 16-bit Pixel Terminal Prompt & Server -->
		<path d="M1 2h14v12H1V2zm2 2v8h10V4H3z" />
		<!-- Terminal >_ prompt -->
		<path d="M4 6h2v1H4V6zm2 1h2v1H6V7zm-2 1h2v1H4V8z" />
		<rect x="9" y="8" width="3" height="1" fill="#1754cf" />
	{:else if name === 'web'}
		<!-- 16-bit Pixel Browser Window -->
		<path d="M1 2h14v12H1V2zm2 2v8h10V4H3z" />
		<rect x="3" y="3" width="1" height="1" fill="currentColor" />
		<rect x="5" y="3" width="1" height="1" fill="currentColor" />
		<rect x="7" y="3" width="1" height="1" fill="currentColor" />
		<!-- Code brackets { } -->
		<path d="M5 6h1v4H5V6zm5 0h1v4h-1V6zm-3 1h2v1H7V7zm0 2h2v1H7V9z" fill="#1754cf" />
	{:else if name === 'warning'}
		<!-- 16-bit Pixel Caution Triangle -->
		<path d="M7 2h2v2H7V2zm-2 3h6v2H5V5zm-2 3h10v2H3V8zm-2 3h14v2H1v-2z" />
		<rect x="7" y="6" width="2" height="3" fill="#9a3412" />
		<rect x="7" y="10" width="2" height="1" fill="#9a3412" />
	{:else if name === 'cursor'}
		<!-- Blinking Pixel Cursor -->
		<rect x="0" y="0" width="16" height="16" fill="#1754cf" />
	{/if}
</svg>
