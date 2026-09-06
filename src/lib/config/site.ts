export interface NavItem {
	label: string;
	href: string;
}

export interface ServiceItem {
	id: string;
	number: string;
	title: string;
	shortDescription: string;
	details: string[];
	whatsappContext: 'computer' | 'recovery' | 'linux' | 'web';
	ctaLabel: string;
}

export interface StepItem {
	number: string;
	title: string;
	description: string;
}

export interface ValueItem {
	title: string;
	description: string;
}

export interface ProjectItem {
	id: string;
	title: string;
	category: string;
	problem: string;
	analysis: string;
	solution: string;
	result: string;
}

export interface FAQItem {
	question: string;
	answer: string;
}

export const siteConfig = {
	name: 'NALAR',
	ecosystem: 'Intuezy',
	tagline: 'Ada Masalah, Ada NALAR.',
	domain: 'nalar.intuezy.my.id',
	parentUrl: 'https://intuezy.my.id',
	url: 'https://nalar.intuezy.my.id',
	metaTitle: 'NALAR — Ada Masalah, Ada NALAR | IT Solutions',
	metaDescription:
		'NALAR membantu individu dan bisnis menyelesaikan kebutuhan IT, dari komputer dan data recovery hingga Linux, server, dan website.',

	// Official WhatsApp number
	whatsappNumber: '6285788141307',

	navItems: [
		{ label: 'Layanan', href: '#layanan' },
		{ label: 'Cara Kerja', href: '#cara-kerja' },
		{ label: 'Tentang', href: '#tentang' },
		{ label: 'FAQ', href: '#faq' }
	] as NavItem[],

	hero: {
		badge: 'Bantuan IT Praktis & Masuk Akal',
		headline: 'Ada Masalah, Ada NALAR.',
		subheadline:
			'Laptop tiba-tiba error, data penting nggak terbaca, atau bingung cara online-kan website? Ceritakan kendalamu pakai bahasa sehari-hari. NALAR bantu urai masalahnya dan tentukan solusi yang paling tepat sasaran.',
		serviceSummary: [
			'Komputer & Laptop',
			'Data Recovery',
			'Linux & Server',
			'Website & Deployment'
		],
		primaryCta: 'Konsultasikan Masalahmu',
		secondaryCta: 'Lihat Layanan'
	},

	philosophy: {
		heading: 'Mulai dari masalahnya.',
		lead: 'Nggak semua masalah butuh solusi yang rumit. Kami pahami dulu kebutuhannya, cari penyebabnya, lalu tentukan cara yang paling masuk akal untuk menyelesaikannya.',
		pillars: [
			{
				tag: 'PAHAMI',
				title: 'Pahami Masalah',
				description: 'Pahami kondisi dan akar masalah sebelum buru-buru menentukan tindakan.'
			},
			{
				tag: 'PECAHKAN',
				title: 'Solusi Seperlunya',
				description:
					'Solusi yang benar-benar kamu butuhkan — tanpa memaksakan teknologi mahal yang sebetulnya tidak perlu.'
			},
			{
				tag: 'SEDERHANAKAN',
				title: 'Sederhanakan Hasilnya',
				description:
					'Teknologi seharusnya membuat sesuatu lebih mudah dan tenang, bukan makin bikin pusing.'
			}
		]
	},

	services: [
		{
			id: 'computer',
			number: '01',
			title: 'Komputer & Laptop',
			shortDescription: 'Install, setup, troubleshooting, dan optimasi komputer maupun laptop.',
			details: [
				'Instalasi Windows / Linux & Dual Boot',
				'Setup laptop baru, driver, dan software pendukung',
				'Troubleshooting masalah boot, lemot, Wi-Fi, dan printer',
				'Upgrade RAM & storage SSD',
				'Backup dan transfer data antar perangkat'
			],
			whatsappContext: 'computer',
			ctaLabel: 'Tanya kendala laptop / PC'
		},
		{
			id: 'data-recovery',
			number: '02',
			title: 'Data Recovery',
			shortDescription:
				'Membantu mengecek dan memulihkan data dari storage yang bermasalah, selama kondisi fisik perangkat memungkinkan.',
			details: [
				'Pengecekan kondisi harddisk / SSD / flashdisk',
				'File penting terhapus secara tidak sengaja',
				'Partisi storage hilang atau terbaca RAW',
				'Penyelamatan data sebelum install ulang sistem'
			],
			whatsappContext: 'recovery',
			ctaLabel: 'Konsultasi recovery storage'
		},
		{
			id: 'linux-server',
			number: '03',
			title: 'Linux & Server',
			shortDescription:
				'Bantuan praktis instalasi Linux, development environment, VPS, dan server dasar.',
			details: [
				'Instalasi distro Linux & konfigurasi dual boot aman',
				'Setup workstation programming (Git, Docker, runtime dev)',
				'Setup dan konfigurasi awal Linux VPS',
				'Web server dasar (Nginx, SSL/HTTPS, domain & DNS)',
				'Deployment aplikasi & website ke server'
			],
			whatsappContext: 'linux',
			ctaLabel: 'Diskusi setup Linux & VPS'
		},
		{
			id: 'web',
			number: '04',
			title: 'Website & Deployment',
			shortDescription:
				'Landing page, website bisnis atau UMKM, domain, hosting, deployment, hingga maintenance.',
			details: [
				'Pembuatan landing page & website profil usaha yang cepat',
				'Setup nama domain, hosting, dan sertifikat SSL',
				'Membantu mendeploy website yang sudah jadi agar online',
				'Maintenance rutin dan pembaruan konten dasar'
			],
			whatsappContext: 'web',
			ctaLabel: 'Konsultasi online-kan web'
		}
	] as ServiceItem[],

	audiences: [
		{
			category: 'Individu',
			lead: 'Buat kamu yang laptopnya mendadak rewel, ingin setup Linux, atau kehilangan file penting.',
			items: [
				'Laptop lemot atau mendadak bluescreen / error',
				'Install ulang Windows tanpa kehilangan lisensi/data penting',
				'Ingin beralih ke Linux atau butuh sistem dual boot',
				'Setup lingkungan koding untuk belajar atau kerja',
				'Data di flashdisk / harddisk tidak sengaja terformat'
			]
		},
		{
			category: 'Bisnis & UMKM',
			lead: 'Buat usaha atau kantor kecil yang butuh kehadiran digital dan operasional teknis andal.',
			items: [
				'Website bisnis / UMKM yang rapi dan siap pakai',
				'Membantu deploy website yang sudah dibuat tapi bingung cara online-nya',
				'Setup domain profesional dan email kantor dasar',
				'Maintenance berkala agar website tetap aman dan aktif',
				'Konsultasi kebutuhan sistem atau otomasi kerja sederhana'
			]
		}
	],

	process: [
		{
			number: '01',
			title: 'Ceritakan',
			description:
				'Ceritakan apa yang kamu lihat atau rasakan. "Laptop sering mati sendiri" atau "Flashdisk minta format" sudah cukup bagi kami untuk mulai memeriksa.'
		},
		{
			number: '02',
			title: 'Kita Cek',
			description:
				'Kami pelajari kondisinya terlebih dahulu untuk mengetahui apa yang sebenarnya terjadi dan opsi penanganan yang masuk akal.'
		},
		{
			number: '03',
			title: 'Sepakati',
			description:
				'Setelah solusi jelas, rencana kerja dan estimasi biayanya kita bicarakan terbuka sebelum mulai dikerjakan.'
		},
		{
			number: '04',
			title: 'Beres',
			description:
				'Pekerjaan diselesaikan sesuai kesepakatan dan hasil akhirnya dijelaskan dengan transparan.'
		}
	] as StepItem[],

	recoveryNotice: {
		heading: 'Data penting hilang? Jangan buru-buru utak-atik.',
		lead: 'Kalau file penting tiba-tiba hilang atau storage tidak terbaca, sebisa mungkin hentikan penggunaan perangkat tersebut. Menjalankan laptop terus-menerus atau mencoba software recovery sembarangan berisiko menimpa data lama secara permanen.',
		assurance:
			'NALAR bisa membantu memeriksa kondisi fisik storage dan peluang pemulihan secara objektif sebelum mengambil tindakan lebih lanjut.',
		ctaText: 'Konsultasikan Data Recovery'
	},

	whyNalar: [
		{
			title: 'Berangkat dari kebutuhan',
			description:
				'Kami tidak langsung menawarkan paket atau alat mahal. Kami dengarkan dan pahami dulu kendalanya.'
		},
		{
			title: 'Solusi seperlunya',
			description:
				'Kalau masalahnya sederhana, solusinya tidak akan dibuat rumit atau diada-adakan.'
		},
		{
			title: 'Bahasa manusia',
			description:
				'Komunikasi yang jelas tanpa istilah teknis yang bikin bingung. Penjelasan selalu mudah dipahami.'
		},
		{
			title: 'Transparan & adil',
			description:
				'Lingkup pekerjaan dan estimasi biaya selalu dibicarakan serta disepakati di awal.'
		}
	] as ValueItem[],

	projects: [] as ProjectItem[],

	faq: [
		{
			question: 'Laptop saya mati total, apakah datanya masih bisa diselamatkan?',
			answer:
				'Sangat sering masih bisa. Pada sebagian besar kasus laptop mati total, media penyimpanan data (SSD/harddisk) masih dalam kondisi fisik yang sehat di dalamnya. Kami bantu cek kondisi storage-nya terlebih dahulu dan mencadangkan data pentingmu dengan aman.'
		},
		{
			question: 'Apakah saya harus tahu persis penyebab masalahnya?',
			answer:
				'Nggak perlu. Cukup ceritakan gejala apa yang kamu lihat atau apa yang sedang ingin kamu capai. Kita bantu periksa sama-sama.'
		},
		{
			question: 'Apakah data recovery dijamin 100% berhasil?',
			answer:
				'Tidak selalu. Kemungkinan recovery sangat bergantung pada kondisi fisik perangkat storage dan bagaimana datanya hilang. Karena itu, kami cek kondisinya terlebih dahulu secara objektif.'
		},
		{
			question: 'Bisa pasang Linux tanpa menghapus Windows?',
			answer:
				'Bisa, selama kapasitas dan struktur partisi storage perangkat memungkinkan. Opsi yang umum digunakan adalah dual boot.'
		},
		{
			question: 'Bisa bantu website yang sudah dibuat tapi belum online?',
			answer:
				'Bisa. Kami dapat membantu pengaturan domain, hosting / VPS, SSL, konfigurasi server web, hingga website kamu bisa diakses publik.'
		},
		{
			question: 'Bisa membuat sistem atau aplikasi khusus untuk bisnis saya?',
			answer:
				'Bisa untuk kebutuhan yang terukur. Ceritakan dulu alur kerja atau kendala yang dihadapi, agar kita bisa menilai apakah sistem custom memang solusi yang paling efisien.'
		},
		{
			question: 'Bagaimana jika kendala IT saya tidak ada di daftar layanan di atas?',
			answer:
				'Tetap tanyakan saja. Selama masih dalam ranah komputer, sistem operasi, server, jaringan lokal, atau web, ceritakan kendalamu. Kalau memang di luar kapasitas kami, kami akan katakan terus terang dan merekomendasikan langkah terbaik untukmu.'
		}
	] as FAQItem[],

	finalCta: {
		headline: 'Punya masalah IT? Ceritain aja.',
		subheadline:
			'Kamu nggak harus paham jeroan teknologinya. Cukup ceritakan kendalanya, nanti kita bantu petakan masalahnya dan cari jalan keluar yang masuk akal.',
		primaryAction: 'Chat WhatsApp',
		note: 'Konsultasi awal untuk memahami kebutuhan · Respon ramah & transparan.'
	}
};
