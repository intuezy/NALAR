#!/usr/bin/env python3
"""
NALAR Minimalist Flyer Generator
Strict minimalist, typography-first, poster-style promotional flyer.
Deliverables:
1. flyer/nalar-flyer-a4.svg
2. flyer/nalar-flyer-a4.png (2480x3508 at 300 DPI)
3. flyer/nalar-flyer-a4.pdf (Print-ready document)
4. flyer/nalar-flyer-instagram.svg
5. flyer/nalar-flyer-instagram.png (1080x1350 px, 4:5 ratio)
Mirrored to static/flyer/
"""

import os
import subprocess
import qrcode
from PIL import Image

WHATSAPP_NUMBER = "0882-4534-7836"
WHATSAPP_URL = "https://wa.me/6288245347836"
WEBSITE_DOMAIN = "nalar.intuezy.my.id"

def generate_qr_svg_paths(url, x, y, size, fill_color="#151618"):
    """Generates crisp SVG rect elements for a scannable QR code."""
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=1,
        border=0,
    )
    qr.add_data(url)
    qr.make(fit=True)
    matrix = qr.get_matrix()
    n = len(matrix)
    cell_size = size / n

    rects = []
    for r in range(n):
        for c in range(n):
            if matrix[r][c]:
                rx = x + c * cell_size
                ry = y + r * cell_size
                rects.append(
                    f'<rect x="{rx:.2f}" y="{ry:.2f}" width="{cell_size + 0.1:.2f}" height="{cell_size + 0.1:.2f}" fill="{fill_color}" shape-rendering="crispEdges" />'
                )
    return "\n    ".join(rects)

def get_pixel_logo_svg(size=40):
    """Generates the official NALAR 16-bit Pixel N logo mark."""
    scale = size / 20.0
    return f'''<g shape-rendering="crispEdges">
      <rect width="{size}" height="{size}" rx="4" fill="#151618" />
      <g transform="translate({scale*2:.1f}, {scale*2:.1f}) scale({scale:.2f})" fill="#FAF9F6">
        <path d="M2 2h3v12H2V2zm9 0h3v12h-3V2zM5 5h2v2H5V5zm2 2h2v2H7V7zm2 2h2v2H9V9z" />
        <rect x="12" y="11" width="3" height="3" fill="#1754CF" />
      </g>
    </g>'''

def get_pixel_icon_svg(name, size=24, color="#151618"):
    """Generates bespoke 16-bit pixel icons for services."""
    scale = size / 16.0
    if name == 'computer':
        content = f'''<path d="M1 2h14v9H1V2zm2 2v5h10V4H3z" fill="{color}" />
        <path d="M6 12h4v1H6v-1zm-3 2h10v1H3v-1z" fill="{color}" />
        <rect x="4" y="5" width="2" height="2" fill="#1754CF" />
        <rect x="7" y="5" width="4" height="1" fill="{color}" />
        <rect x="7" y="7" width="2" height="1" fill="{color}" />'''
    elif name == 'recovery':
        content = f'''<path d="M2 2h12v12H2V2zm2 2v8h8V4H4z" fill="{color}" />
        <rect x="6" y="5" width="4" height="4" fill="{color}" />
        <rect x="7" y="6" width="2" height="2" fill="#FAF9F6" />
        <rect x="5" y="10" width="2" height="1" fill="#1754CF" />
        <rect x="9" y="10" width="2" height="1" fill="#1754CF" />'''
    elif name == 'linux':
        content = f'''<path d="M1 2h14v12H1V2zm2 2v8h10V4H3z" fill="{color}" />
        <path d="M4 6h2v1H4V6zm2 1h2v1H6V7zm-2 1h2v1H4V8z" fill="{color}" />
        <rect x="9" y="8" width="3" height="1" fill="#1754CF" />'''
    else:  # web
        content = f'''<path d="M1 2h14v12H1V2zm2 2v8h10V4H3z" fill="{color}" />
        <rect x="3" y="3" width="1" height="1" fill="{color}" />
        <rect x="5" y="3" width="1" height="1" fill="{color}" />
        <rect x="7" y="3" width="1" height="1" fill="{color}" />
        <path d="M5 6h1v4H5V6zm5 0h1v4h-1V6zm-3 1h2v1H7V7zm0 2h2v1H7V9z" fill="#1754CF" />'''

    return f'''<g transform="scale({scale:.2f})" shape-rendering="crispEdges">
      {content}
    </g>'''

def generate_full_pixel_background(width, height, is_instagram=False):
    """
    Generates an authentic 16-bit pixel art full-canvas background.
    Covers sky (clouds, satellite, tower, stars), mid hardware (circuits, IC chips, server racks),
    and base infrastructure (isometric CAD floor, conduit cables).
    All base coordinates are defined in canonical 1240x1754 space and scaled automatically.
    """
    sy = height / 1754.0
    sx = width / 1240.0

    rects = []
    def r(x, y, w, h, col):
        rects.append(f'<rect x="{x*sx:.1f}" y="{y*sy:.1f}" width="{w*sx:.1f}" height="{h*sy:.1f}" fill="{col}" shape-rendering="crispEdges" />')

    # Grid Pattern (24px repeating 2x2 dot)
    pat_id = "pixelGrid_ig" if is_instagram else "pixelGrid_a4"
    pattern = f'''<defs>
      <pattern id="{pat_id}" width="24" height="24" patternUnits="userSpaceOnUse">
        <rect x="0" y="0" width="2" height="2" fill="#EAE7DD" />
      </pattern>
    </defs>
    <rect width="{width}" height="{height}" fill="#FAF9F6" />
    <rect width="{width}" height="{height}" fill="url(#{pat_id})" />'''

    # 1. Pixel Clouds in Upper Sky (Stepped pixel blocks in #EAE7DC / #DFDBD0)
    # Cloud A (Center-Left)
    r(320, 50, 150, 12, '#EAE7DC')
    r(340, 38, 110, 12, '#EAE7DC')
    r(370, 28, 60, 10, '#EAE7DC')
    r(320, 62, 150, 4, '#DFDBD0')

    # Cloud B (Center-Right)
    r(580, 70, 180, 14, '#EAE7DC')
    r(610, 56, 120, 14, '#EAE7DC')
    r(640, 44, 60, 12, '#EAE7DC')
    r(580, 84, 180, 4, '#DFDBD0')

    # 2. Pixel Satellite in Orbit (top right)
    sat_x, sat_y = 880, 54
    r(sat_x, sat_y, 16, 16, '#D4D0C4')
    r(sat_x - 24, sat_y + 2, 20, 12, '#C8DAFB')
    r(sat_x + 20, sat_y + 2, 20, 12, '#C8DAFB')
    r(sat_x - 14, sat_y + 2, 2, 12, '#1754CF')
    r(sat_x + 30, sat_y + 2, 2, 12, '#1754CF')
    r(sat_x + 6, sat_y - 8, 4, 8, '#9CA3AF')
    r(sat_x + 6, sat_y - 12, 4, 4, '#1754CF')

    # 3. Communications Transmission Tower on Far Right Margin (outside content width)
    tow_x = 1240 - 42
    for ty in range(130, 500, 16):
        r(tow_x - 10, ty, 20, 2, '#DFDBD0')
        r(tow_x - 10, ty, 3, 16, '#D4D0C4')
        r(tow_x + 7, ty, 3, 16, '#D4D0C4')
        r(tow_x - 6, ty + 4, 12, 2, '#EAE7DC')
    r(tow_x - 2, 110, 4, 20, '#9CA3AF')
    r(tow_x - 4, 102, 8, 8, '#1754CF')
    r(tow_x - 16, 94, 4, 4, '#CADBFB')
    r(tow_x + 12, 94, 4, 4, '#CADBFB')
    r(tow_x - 24, 86, 4, 4, '#DCE7FC')
    r(tow_x + 20, 86, 4, 4, '#DCE7FC')

    # 4. Pixel Stars & Twinkles in Negative Sky Space
    star_coords = [
        (220, 50), (490, 40), (790, 80), (840, 30), (1050, 60),
        (260, 150), (450, 130), (740, 150), (1110, 140), (60, 200)
    ]
    for scx, scy in star_coords:
        r(scx, scy - 4, 4, 12, '#CADBFB')
        r(scx - 4, scy, 12, 4, '#CADBFB')
        r(scx, scy, 4, 4, '#1754CF')

    # 5. Server Cabinet Rack Silhouette (Placed in Hero Negative Space, upper right: y: 220 to 510)
    rack_x, rack_y = 900, 220
    rack_w, rack_h = 130, 280
    r(rack_x, rack_y, rack_w, rack_h, '#ECEAE1')
    r(rack_x + 4, rack_y + 4, rack_w - 8, rack_h - 8, '#F2F0E8')
    for shi in range(6):
        shy = rack_y + 10 + shi * 44
        r(rack_x + 8, shy, rack_w - 16, 34, '#E5E2D8')
        r(rack_x + 16, shy + 6, 40, 4, '#D4D0C4')
        r(rack_x + 16, shy + 14, 40, 4, '#D4D0C4')
        r(rack_x + 16, shy + 22, 24, 3, '#D4D0C4')
        # Status LEDs
        r(rack_x + rack_w - 32, shy + 8, 5, 5, '#22C55E')
        r(rack_x + rack_w - 22, shy + 8, 5, 5, '#1754CF')
        r(rack_x + rack_w - 32, shy + 18, 4, 4, '#1754CF')

    # 6. Microchip Package (16-BIT IC Processor) in Hero Space (x: 770, y: 350)
    chip_x, chip_y = 770, 350
    r(chip_x, chip_y, 48, 48, '#E4E1D6')
    r(chip_x + 4, chip_y + 4, 40, 40, '#DCD9CE')
    r(chip_x + 14, chip_y + 14, 20, 20, '#CADBFB')
    r(chip_x + 18, chip_y + 18, 12, 12, '#1754CF')
    for p in range(5):
        r(chip_x + 6 + p * 8, chip_y - 6, 4, 6, '#CADBFB')
        r(chip_x + 6 + p * 8, chip_y + 48, 4, 6, '#CADBFB')
        r(chip_x - 6, chip_y + 6 + p * 8, 6, 4, '#CADBFB')
        r(chip_x + 48, chip_y + 6 + p * 8, 6, 4, '#CADBFB')

    # Traces linking chip to rack and margin
    r(chip_x + 48, chip_y + 22, rack_x - chip_x - 48, 3, '#E0DDD2')
    r(chip_x + 22, chip_y - 30, 3, 30, '#E0DDD2')
    for st in range(8):
        r(chip_x + 22 + st * 3, chip_y - 30 - st * 3, 3, 3, '#E0DDD2')
    r(chip_x + 46, chip_y - 54, 60, 3, '#E0DDD2')
    r(chip_x + 106, chip_y - 56, 6, 6, '#1754CF')

    # 7. Motherboard Traces in Margin Gutters (Keeps service text crystal clear)
    # Left Margin Circuit Spine (outside content)
    r(38, 340, 3, 480, '#E0DDD2')
    for my_node in [360, 480, 600, 720]:
        r(35, my_node, 9, 9, '#CADBFB')
        r(37, my_node + 2, 5, 5, '#1754CF')
    # Dogleg into lower area
    for st in range(12):
        r(38 + st * 3, 820 + st * 3, 3, 3, '#E0DDD2')
    r(74, 856, 3, 260, '#E0DDD2')
    r(71, 1116, 9, 9, '#CADBFB')
    r(73, 1118, 5, 5, '#1754CF')

    # Parallel Data Bus in Far Right Margin (outside content)
    for bi, bx in enumerate([1240 - 32, 1240 - 24, 1240 - 16]):
        r(bx, 540, 2, 560, '#E2DFD4')
        for sy_node in [614, 730, 846, 962, 1078]:
            r(bx - 2, sy_node, 6, 3, '#D4D0C4')
            if bi == 1:
                r(bx, sy_node + 0.5, 2, 2, '#1754CF')

    # 8. Isometric Floor Grid Topography at Bottom (Y: 1320 to 1680)
    for ly in range(1320, 1680, 56):
        for step in range(0, 1240, 10):
            py = ly + (step // 5) * 2
            if py < 1700:
                r(step, py, 4, 2, '#EFECE2')

    # 9. Stepped Cable Trunk / Conduit running across very bottom (below footer text)
    trunk_y = 1754 - 28
    r(36, trunk_y, 1240 - 72, 5, '#DFDBD0')
    r(36, trunk_y + 6, 1240 - 72, 3, '#E5E2D7')
    for cx in range(60, 1240 - 60, 90):
        r(cx, trunk_y - 2, 7, 14, '#CADBFB')
        r(cx + 1.5, trunk_y, 4, 10, '#1754CF')

    # 10. Outer Ruler Ticks along Margins
    for ty in range(40, 1754 - 40, 40):
        r(10, ty, 5, 2, '#DFDBD0')
        r(1240 - 15, ty, 5, 2, '#DFDBD0')
    for tx in range(40, 1240 - 40, 40):
        r(tx, 10, 2, 5, '#DFDBD0')
        r(tx, 1754 - 15, 2, 5, '#DFDBD0')

    # 11. 4 Corner Registration Crosses
    for cx, cy in [(32, 32), (1240 - 36, 32), (32, 1754 - 36), (1240 - 36, 1754 - 36)]:
        r(cx + 4, cy, 3, 11, '#C5C2B6')
        r(cx, cy + 4, 11, 3, '#C5C2B6')

    return pattern + f'''<g id="pixelBackground" shape-rendering="crispEdges">
      {''.join(rects)}
    </g>'''

def build_a4_minimalist_svg():
    width = 1240
    height = 1754
    left = 96
    right = 1144
    content_width = right - left

    # CTA group is translated to (left, 1220)
    qr_size = 144
    qr_local_x = content_width - qr_size - 12
    qr_local_y = 44
    qr_svg = generate_qr_svg_paths(WHATSAPP_URL, qr_local_x, qr_local_y, qr_size, "#151618")

    # Pixel Logo
    pixel_logo = get_pixel_logo_svg(42)

    # Full Pixel Art Background
    pixel_bg = generate_full_pixel_background(width, height, is_instagram=False)

    # Pixel Service Icons
    icon_comp = get_pixel_icon_svg('computer', 26)
    icon_rec = get_pixel_icon_svg('recovery', 26)
    icon_linux = get_pixel_icon_svg('linux', 26)
    icon_web = get_pixel_icon_svg('web', 26)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      text {{
        font-family: 'Plus Jakarta Sans', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
      }}
      .sans {{
        font-family: 'Plus Jakarta Sans', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
      }}
      .mono {{
        font-family: 'Cascadia Mono', 'DejaVu Sans Mono', ui-monospace, monospace;
      }}
    </style>
  </defs>

  <!-- Full-Canvas 16-bit Pixel Art Background -->
  {pixel_bg}

  <!-- 1. HEADER (Official Pixel Logo + Minimalist Wordmark) -->
  <g transform="translate({left}, 84)">
    {pixel_logo}
    <text x="56" y="31" class="sans" font-size="30" font-weight="800" fill="#151618" letter-spacing="-0.5">NALAR</text>
  </g>

  <!-- 2. HEADLINE & VALUE PROPOSITION (Direct & Spacious) -->
  <g transform="translate({left}, 224)">
    <!-- Main Brand Statement with Pixel Terminal Cursor -->
    <text x="0" y="44" class="sans" font-size="68" font-weight="800" fill="#151618" letter-spacing="-2">Ada Masalah,</text>
    <text x="0" y="122" class="sans" font-size="68" font-weight="800" fill="#151618" letter-spacing="-2">Ada NALAR<tspan fill="#1754CF">.</tspan></text>
    <rect x="428" y="74" width="16" height="50" fill="#1754CF" shape-rendering="crispEdges" />

    <!-- Direct & Immediate Description (No redundancy) -->
    <g transform="translate(0, 196)">
      <text x="0" y="0" class="sans" font-size="21.5" font-weight="500" fill="#4B5563" letter-spacing="-0.2">Bantu menyelesaikan masalah komputer, data, Linux, server,</text>
      <text x="0" y="34" class="sans" font-size="21.5" font-weight="500" fill="#4B5563" letter-spacing="-0.2">dan website untuk individu maupun bisnis.</text>
    </g>
  </g>

  <!-- 3. SERVICES (4 Editorial Rows with Concise Descriptions) -->
  <g transform="translate({left}, 596)">
    <!-- Section Label -->
    <text x="0" y="0" class="mono" font-size="11.5" font-weight="600" fill="#71717A" letter-spacing="2">LAYANAN UTAMA</text>

    <!-- Row 1: Komputer -->
    <g transform="translate(0, 24)">
      <line x1="0" y1="0" x2="{content_width}" y2="0" stroke="#E5E4DE" stroke-width="1.2" />
      <text x="0" y="60" class="mono" font-size="15" font-weight="600" fill="#1754CF">01</text>
      <g transform="translate(44, 36)">{icon_comp}</g>
      <text x="86" y="60" class="sans" font-size="28" font-weight="700" fill="#151618" letter-spacing="-0.4">Komputer</text>
      <text x="{content_width}" y="60" text-anchor="end" class="sans" font-size="18.5" font-weight="500" fill="#52525B">Setup, install &amp; troubleshooting</text>
    </g>

    <!-- Row 2: Data Recovery -->
    <g transform="translate(0, 130)">
      <line x1="0" y1="0" x2="{content_width}" y2="0" stroke="#E5E4DE" stroke-width="1.2" />
      <text x="0" y="60" class="mono" font-size="15" font-weight="600" fill="#1754CF">02</text>
      <g transform="translate(44, 36)">{icon_rec}</g>
      <text x="86" y="60" class="sans" font-size="28" font-weight="700" fill="#151618" letter-spacing="-0.4">Data Recovery</text>
      <text x="{content_width}" y="60" text-anchor="end" class="sans" font-size="18.5" font-weight="500" fill="#52525B">Pemulihan data</text>
    </g>

    <!-- Row 3: Linux & Server -->
    <g transform="translate(0, 236)">
      <line x1="0" y1="0" x2="{content_width}" y2="0" stroke="#E5E4DE" stroke-width="1.2" />
      <text x="0" y="60" class="mono" font-size="15" font-weight="600" fill="#1754CF">03</text>
      <g transform="translate(44, 36)">{icon_linux}</g>
      <text x="86" y="60" class="sans" font-size="28" font-weight="700" fill="#151618" letter-spacing="-0.4">Linux &amp; Server</text>
      <text x="{content_width}" y="60" text-anchor="end" class="sans" font-size="18.5" font-weight="500" fill="#52525B">Setup Linux, VPS &amp; server</text>
    </g>

    <!-- Row 4: Web -->
    <g transform="translate(0, 342)">
      <line x1="0" y1="0" x2="{content_width}" y2="0" stroke="#E5E4DE" stroke-width="1.2" />
      <text x="0" y="60" class="mono" font-size="15" font-weight="600" fill="#1754CF">04</text>
      <g transform="translate(44, 36)">{icon_web}</g>
      <text x="86" y="60" class="sans" font-size="28" font-weight="700" fill="#151618" letter-spacing="-0.4">Web</text>
      <text x="{content_width}" y="60" text-anchor="end" class="sans" font-size="18.5" font-weight="500" fill="#52525B">Website &amp; landing page</text>
      <line x1="0" y1="102" x2="{content_width}" y2="102" stroke="#E5E4DE" stroke-width="1.2" />
    </g>
  </g>

  <!-- 4. CALL TO ACTION (Clear, Conversational & Obvious) -->
  <g transform="translate({left}, 1216)">
    <!-- Hairline Separator -->
    <line x1="0" y1="0" x2="{content_width}" y2="0" stroke="#E5E4DE" stroke-width="1.2" />

    <!-- Left Column: Conversational Invitation -->
    <g transform="translate(0, 48)">
      <!-- Eyebrow -->
      <text x="0" y="0" class="mono" font-size="12" font-weight="700" fill="#1754CF" letter-spacing="2">&gt; KONSULTASI</text>

      <!-- Action Prompt -->
      <text x="0" y="46" class="sans" font-size="46" font-weight="800" fill="#151618" letter-spacing="-1">Punya masalah IT?</text>
      <text x="0" y="100" class="sans" font-size="46" font-weight="800" fill="#151618" letter-spacing="-1">Ceritain aja.</text>

      <!-- Clear, Trustworthy Reassurance -->
      <g transform="translate(0, 154)">
        <text x="0" y="0" class="sans" font-size="17" font-weight="500" fill="#52525B" letter-spacing="-0.1">Nggak perlu paham istilah teknis. Ceritakan masalahnya lewat WhatsApp,</text>
        <text x="0" y="28" class="sans" font-size="17" font-weight="500" fill="#52525B" letter-spacing="-0.1">kita cek dulu apa yang bisa dilakukan.</text>
      </g>

      <!-- Direct Contact Details -->
      <g transform="translate(0, 240)">
        <text x="0" y="0" class="mono" font-size="11" font-weight="600" fill="#71717A" letter-spacing="1">WHATSAPP</text>
        <text x="0" y="30" class="mono" font-size="25" font-weight="800" fill="#151618" letter-spacing="0.5">{WHATSAPP_NUMBER}</text>

        <text x="270" y="0" class="mono" font-size="11" font-weight="600" fill="#71717A" letter-spacing="1">WEBSITE</text>
        <text x="270" y="30" class="mono" font-size="17" font-weight="600" fill="#1754CF">{WEBSITE_DOMAIN}</text>
      </g>
    </g>

    <!-- Right Column: Clean Vector Scannable QR Code -->
    <g transform="translate(0, 0)">
      <!-- Framing box with pixel-sharp edge -->
      <rect x="{qr_local_x - 14}" y="{qr_local_y - 14}" width="{qr_size + 28}" height="{qr_size + 28}" rx="4" fill="#FFFFFF" stroke="#E5E4DE" stroke-width="1.2" />
      {qr_svg}
      <text x="{qr_local_x + qr_size / 2}" y="{qr_local_y + qr_size + 28}" text-anchor="middle" class="mono" font-size="11" font-weight="600" fill="#71717A" letter-spacing="0.5">Scan untuk WhatsApp</text>
    </g>
  </g>
</svg>'''
    return svg

def build_instagram_minimalist_svg():
    width = 1080
    height = 1350
    left = 72
    right = 1008
    content_width = right - left

    # QR Code inside CTA group translated to (left, 940)
    qr_size = 124
    qr_local_x = content_width - qr_size - 10
    qr_local_y = 44
    qr_svg = generate_qr_svg_paths(WHATSAPP_URL, qr_local_x, qr_local_y, qr_size, "#151618")

    # Pixel Logo
    pixel_logo = get_pixel_logo_svg(36)

    # Full Pixel Art Background adapted for Instagram
    pixel_bg = generate_full_pixel_background(width, height, is_instagram=True)

    # Pixel Service Icons
    icon_comp = get_pixel_icon_svg('computer', 24)
    icon_rec = get_pixel_icon_svg('recovery', 24)
    icon_linux = get_pixel_icon_svg('linux', 24)
    icon_web = get_pixel_icon_svg('web', 24)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      text {{
        font-family: 'Plus Jakarta Sans', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
      }}
      .sans {{
        font-family: 'Plus Jakarta Sans', system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
      }}
      .mono {{
        font-family: 'Cascadia Mono', 'DejaVu Sans Mono', ui-monospace, monospace;
      }}
    </style>
  </defs>

  <!-- Full-Canvas 16-bit Pixel Art Background -->
  {pixel_bg}

  <!-- 1. HEADER (Official Pixel Logo + Minimalist Wordmark) -->
  <g transform="translate({left}, 68)">
    {pixel_logo}
    <text x="48" y="27" class="sans" font-size="26" font-weight="800" fill="#151618" letter-spacing="-0.5">NALAR</text>
  </g>

  <!-- 2. HEADLINE & VALUE PROP (Direct & Spacious) -->
  <g transform="translate({left}, 176)">
    <text x="0" y="36" class="sans" font-size="52" font-weight="800" fill="#151618" letter-spacing="-1.8">Ada Masalah,</text>
    <text x="0" y="96" class="sans" font-size="52" font-weight="800" fill="#151618" letter-spacing="-1.8">Ada NALAR<tspan fill="#1754CF">.</tspan></text>
    <rect x="330" y="60" width="13" height="38" fill="#1754CF" shape-rendering="crispEdges" />

    <g transform="translate(0, 154)">
      <text x="0" y="0" class="sans" font-size="17.5" font-weight="500" fill="#4B5563" letter-spacing="-0.2">Bantu menyelesaikan masalah komputer, data, Linux, server,</text>
      <text x="0" y="28" class="sans" font-size="17.5" font-weight="500" fill="#4B5563" letter-spacing="-0.2">dan website untuk individu maupun bisnis.</text>
    </g>
  </g>

  <!-- 3. SERVICES (4 Editorial Rows with Concise Descriptions) -->
  <g transform="translate({left}, 500)">
    <text x="0" y="0" class="mono" font-size="11" font-weight="600" fill="#71717A" letter-spacing="2">LAYANAN UTAMA</text>

    <!-- Row 1: Komputer -->
    <g transform="translate(0, 20)">
      <line x1="0" y1="0" x2="{content_width}" y2="0" stroke="#E5E4DE" stroke-width="1.2" />
      <text x="0" y="52" class="mono" font-size="14" font-weight="600" fill="#1754CF">01</text>
      <g transform="translate(38, 32)">{icon_comp}</g>
      <text x="76" y="52" class="sans" font-size="24" font-weight="700" fill="#151618">Komputer</text>
      <text x="{content_width}" y="52" text-anchor="end" class="sans" font-size="16" font-weight="500" fill="#52525B">Setup, install &amp; troubleshooting</text>
    </g>

    <!-- Row 2: Data Recovery -->
    <g transform="translate(0, 110)">
      <line x1="0" y1="0" x2="{content_width}" y2="0" stroke="#E5E4DE" stroke-width="1.2" />
      <text x="0" y="52" class="mono" font-size="14" font-weight="600" fill="#1754CF">02</text>
      <g transform="translate(38, 32)">{icon_rec}</g>
      <text x="76" y="52" class="sans" font-size="24" font-weight="700" fill="#151618">Data Recovery</text>
      <text x="{content_width}" y="52" text-anchor="end" class="sans" font-size="16" font-weight="500" fill="#52525B">Pemulihan data</text>
    </g>

    <!-- Row 3: Linux & Server -->
    <g transform="translate(0, 200)">
      <line x1="0" y1="0" x2="{content_width}" y2="0" stroke="#E5E4DE" stroke-width="1.2" />
      <text x="0" y="52" class="mono" font-size="14" font-weight="600" fill="#1754CF">03</text>
      <g transform="translate(38, 32)">{icon_linux}</g>
      <text x="76" y="52" class="sans" font-size="24" font-weight="700" fill="#151618">Linux &amp; Server</text>
      <text x="{content_width}" y="52" text-anchor="end" class="sans" font-size="16" font-weight="500" fill="#52525B">Setup Linux, VPS &amp; server</text>
    </g>

    <!-- Row 4: Web -->
    <g transform="translate(0, 290)">
      <line x1="0" y1="0" x2="{content_width}" y2="0" stroke="#E5E4DE" stroke-width="1.2" />
      <text x="0" y="52" class="mono" font-size="14" font-weight="600" fill="#1754CF">04</text>
      <g transform="translate(38, 32)">{icon_web}</g>
      <text x="76" y="52" class="sans" font-size="24" font-weight="700" fill="#151618">Web</text>
      <text x="{content_width}" y="52" text-anchor="end" class="sans" font-size="16" font-weight="500" fill="#52525B">Website &amp; landing page</text>
      <line x1="0" y1="90" x2="{content_width}" y2="90" stroke="#E5E4DE" stroke-width="1.2" />
    </g>
  </g>

  <!-- 4. CALL TO ACTION (Clear, Conversational & Obvious) -->
  <g transform="translate({left}, 950)">
    <line x1="0" y1="0" x2="{content_width}" y2="0" stroke="#E5E4DE" stroke-width="1.2" />

    <g transform="translate(0, 42)">
      <text x="0" y="0" class="mono" font-size="11" font-weight="700" fill="#1754CF" letter-spacing="2">&gt; KONSULTASI</text>

      <text x="0" y="40" class="sans" font-size="38" font-weight="800" fill="#151618" letter-spacing="-0.8">Punya masalah IT?</text>
      <text x="0" y="84" class="sans" font-size="38" font-weight="800" fill="#151618" letter-spacing="-0.8">Ceritain aja.</text>

      <g transform="translate(0, 130)">
        <text x="0" y="0" class="sans" font-size="15" font-weight="500" fill="#52525B">Nggak perlu paham istilah teknis. Ceritakan masalahnya</text>
        <text x="0" y="24" class="sans" font-size="15" font-weight="500" fill="#52525B">lewat WhatsApp, kita cek dulu apa yang bisa dilakukan.</text>
      </g>

      <g transform="translate(0, 206)">
        <text x="0" y="0" class="mono" font-size="10.5" font-weight="600" fill="#71717A" letter-spacing="1">WHATSAPP</text>
        <text x="0" y="26" class="mono" font-size="22" font-weight="800" fill="#151618">{WHATSAPP_NUMBER}</text>

        <text x="240" y="0" class="mono" font-size="10.5" font-weight="600" fill="#71717A" letter-spacing="1">WEBSITE</text>
        <text x="240" y="26" class="mono" font-size="15" font-weight="600" fill="#1754CF">{WEBSITE_DOMAIN}</text>
      </g>
    </g>

    <!-- QR Code Box -->
    <g transform="translate(0, 0)">
      <rect x="{qr_local_x - 12}" y="{qr_local_y - 12}" width="{qr_size + 24}" height="{qr_size + 24}" rx="4" fill="#FFFFFF" stroke="#E5E4DE" stroke-width="1.2" />
      {qr_svg}
      <text x="{qr_local_x + qr_size / 2}" y="{qr_local_y + qr_size + 24}" text-anchor="middle" class="mono" font-size="10" font-weight="600" fill="#71717A">Scan untuk WhatsApp</text>
    </g>
  </g>
</svg>'''
    return svg

def main():
    os.makedirs("flyer", exist_ok=True)
    os.makedirs("static/flyer", exist_ok=True)

    print("1. Generating Minimalist A4 SVG...")
    a4_svg = build_a4_minimalist_svg()
    a4_svg_path = "flyer/nalar-flyer-a4.svg"
    with open(a4_svg_path, "w", encoding="utf-8") as f:
        f.write(a4_svg)
    with open("static/flyer/nalar-flyer-a4.svg", "w", encoding="utf-8") as f:
        f.write(a4_svg)

    print("2. Generating Minimalist Instagram SVG...")
    ig_svg = build_instagram_minimalist_svg()
    ig_svg_path = "flyer/nalar-flyer-instagram.svg"
    with open(ig_svg_path, "w", encoding="utf-8") as f:
        f.write(ig_svg)
    with open("static/flyer/nalar-flyer-instagram.svg", "w", encoding="utf-8") as f:
        f.write(ig_svg)

    print("3. Rendering A4 PNG (2480x3508 at 300 DPI) using resvg...")
    a4_png_path = "flyer/nalar-flyer-a4.png"
    subprocess.run([
        "resvg",
        "-z", "2",
        "--sans-serif-family", "Plus Jakarta Sans",
        "--monospace-family", "Cascadia Mono",
        a4_svg_path,
        a4_png_path
    ], check=True)
    subprocess.run(["cp", a4_png_path, "static/flyer/nalar-flyer-a4.png"], check=True)

    print("4. Rendering Instagram PNG (1080x1350) using resvg...")
    ig_png_path = "flyer/nalar-flyer-instagram.png"
    subprocess.run([
        "resvg",
        "--sans-serif-family", "Plus Jakarta Sans",
        "--monospace-family", "Cascadia Mono",
        ig_svg_path,
        ig_png_path
    ], check=True)
    subprocess.run(["cp", ig_png_path, "static/flyer/nalar-flyer-instagram.png"], check=True)

    print("5. Generating High-Res A4 Print PDF from 300 DPI render...")
    a4_pdf_path = "flyer/nalar-flyer-a4.pdf"
    with Image.open(a4_png_path) as im:
        rgb_im = im.convert("RGB")
        rgb_im.save(a4_pdf_path, "PDF", resolution=300.0)
    subprocess.run(["cp", a4_pdf_path, "static/flyer/nalar-flyer-a4.pdf"], check=True)

    print("✅ Minimalist flyer assets generated successfully:")
    for path in [a4_svg_path, a4_png_path, a4_pdf_path, ig_svg_path, ig_png_path]:
        size_kb = os.path.getsize(path) / 1024
        print(f"  - {path} ({size_kb:.1f} KB)")

if __name__ == "__main__":
    main()
