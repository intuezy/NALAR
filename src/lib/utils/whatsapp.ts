import { siteConfig } from '$lib/config/site';

export type WhatsAppContext = 'general' | 'computer' | 'recovery' | 'linux' | 'web';

const CONTEXT_MESSAGES: Record<WhatsAppContext, string> = {
	general: 'Halo NALAR, saya mau konsultasi soal kendala IT yang sedang saya hadapi.',
	computer:
		'Halo NALAR, laptop / komputer saya sedang ada kendala. Mau tanya kemungkinan solusinya...',
	recovery:
		'Halo NALAR, storage saya bermasalah dan ada data penting di dalamnya. Mau konsultasi pengecekan...',
	linux: 'Halo NALAR, saya butuh bantuan untuk setup Linux / konfigurasi server VPS.',
	web: 'Halo NALAR, saya mau konsultasi soal pembuatan atau deployment website usaha.'
};

/**
 * Generates a clean, direct WhatsApp URL with prefilled contextual text.
 * No complicated forms required before contacting.
 */
export function buildWhatsAppUrl(
	context: WhatsAppContext = 'general',
	customNote?: string
): string {
	const baseMessage = CONTEXT_MESSAGES[context] || CONTEXT_MESSAGES.general;
	const fullMessage = customNote ? `${baseMessage} (${customNote})` : baseMessage;
	const encoded = encodeURIComponent(fullMessage);
	let number = siteConfig.whatsappNumber.replace(/[^0-9]/g, '');
	if (number.startsWith('0')) {
		number = '62' + number.slice(1);
	}

	return `https://wa.me/${number}?text=${encoded}`;
}
