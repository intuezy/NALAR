#!/usr/bin/env python3
"""
NALAR Brand Logo Generator
Generates high-resolution transparent and badge PNGs and SVGs for NALAR:
1. nalar-mark-shadow (App icon / Avatar with signature blue shadow)
2. nalar-mark-badge (Minimalist dark rounded badge)
3. nalar-mark-transparent-dark (Standalone pixel N on transparent canvas)
4. nalar-mark-transparent-light (Standalone white pixel N on transparent canvas)
5. nalar-logo-horizontal-dark (Official full horizontal lockup for light backgrounds)
6. nalar-logo-horizontal-light (Official full horizontal lockup for dark backgrounds)
7. nalar-logo-with-tagline (Horizontal lockup with official tagline)
"""

import os
import shutil
import subprocess

OUTPUT_DIR = "static/brand"
ARTIFACT_DIR = "/home/devtective/.gemini/antigravity-cli/brain/4234e72a-1d70-49fb-9c52-2d0512ccbf2e"

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(ARTIFACT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. Badge with Accent Shadow (512x512 & 1024x1024)
# -------------------------------------------------------------
def svg_badge_with_shadow(size=512):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="{size}" height="{size}">
  <!-- Accent Brutalist Hard Shadow -->
  <rect x="74" y="74" width="380" height="380" rx="76" fill="#1754CF" />
  <!-- Main Dark Badge -->
  <rect x="58" y="58" width="380" height="380" rx="76" fill="#151618" />
  
  <!-- 16-bit Pixel N Graphic -->
  <g transform="translate(122, 122) scale(15.75)" shape-rendering="crispEdges">
    <path d="M2 2h3v12H2V2zm9 0h3v12h-3V2zM5 5h2v2H5V5zm2 2h2v2H7V7zm2 2h2v2H9V9z" fill="#FAF9F6" />
    <rect x="12" y="11" width="3" height="3" fill="#1754CF" />
  </g>
</svg>'''

# -------------------------------------------------------------
# 2. Clean Badge without Shadow (Square avatar/icon)
# -------------------------------------------------------------
def svg_badge_clean(size=512):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="{size}" height="{size}">
  <rect x="48" y="48" width="416" height="416" rx="84" fill="#151618" />
  <g transform="translate(118, 118) scale(17.25)" shape-rendering="crispEdges">
    <path d="M2 2h3v12H2V2zm9 0h3v12h-3V2zM5 5h2v2H5V5zm2 2h2v2H7V7zm2 2h2v2H9V9z" fill="#FAF9F6" />
    <rect x="12" y="11" width="3" height="3" fill="#1754CF" />
  </g>
</svg>'''

# -------------------------------------------------------------
# 3. Transparent Pixel Mark (Dark and Light)
# -------------------------------------------------------------
def svg_pixel_transparent(color="#151618", size=512):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="{size}" height="{size}">
  <g transform="translate(48, 48) scale(26)" shape-rendering="crispEdges">
    <path d="M2 2h3v12H2V2zm9 0h3v12h-3V2zM5 5h2v2H5V5zm2 2h2v2H7V7zm2 2h2v2H9V9z" fill="{color}" />
    <rect x="12" y="11" width="3" height="3" fill="#1754CF" />
  </g>
</svg>'''

# -------------------------------------------------------------
# 4. Horizontal Logo Lockup (Dark text on Transparent)
# -------------------------------------------------------------
def svg_horizontal_dark(width=1600, height=440):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 440" width="{width}" height="{height}">
  <!-- Badge Icon on Left -->
  <g transform="translate(60, 60)">
    <!-- Shadow -->
    <rect x="14" y="14" width="300" height="300" rx="60" fill="#1754CF" />
    <!-- Badge -->
    <rect x="0" y="0" width="300" height="300" rx="60" fill="#151618" />
    <g transform="translate(45, 45) scale(13.125)" shape-rendering="crispEdges">
      <path d="M2 2h3v12H2V2zm9 0h3v12h-3V2zM5 5h2v2H5V5zm2 2h2v2H7V7zm2 2h2v2H9V9z" fill="#FAF9F6" />
      <rect x="12" y="11" width="3" height="3" fill="#1754CF" />
    </g>
  </g>

  <!-- NALAR Wordmark -->
  <text x="430" y="278" font-family="Inter, -apple-system, sans-serif" font-weight="900" font-size="220" letter-spacing="-6" fill="#151618">NALAR</text>
</svg>'''

# -------------------------------------------------------------
# 5. Horizontal Logo Lockup (Light/White text on Transparent)
# -------------------------------------------------------------
def svg_horizontal_light(width=1600, height=440):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 440" width="{width}" height="{height}">
  <!-- Badge Icon on Left -->
  <g transform="translate(60, 60)">
    <!-- Shadow -->
    <rect x="14" y="14" width="300" height="300" rx="60" fill="#1754CF" />
    <!-- Badge -->
    <rect x="0" y="0" width="300" height="300" rx="60" fill="#151618" stroke="#323438" stroke-width="4" />
    <g transform="translate(45, 45) scale(13.125)" shape-rendering="crispEdges">
      <path d="M2 2h3v12H2V2zm9 0h3v12h-3V2zM5 5h2v2H5V5zm2 2h2v2H7V7zm2 2h2v2H9V9z" fill="#FAF9F6" />
      <rect x="12" y="11" width="3" height="3" fill="#1754CF" />
    </g>
  </g>

  <!-- NALAR Wordmark in Off-White -->
  <text x="430" y="278" font-family="Inter, -apple-system, sans-serif" font-weight="900" font-size="220" letter-spacing="-6" fill="#FAF9F6">NALAR</text>
</svg>'''

# -------------------------------------------------------------
# 6. Horizontal Logo with Tagline
# -------------------------------------------------------------
def svg_horizontal_tagline(width=1800, height=480):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1800 480" width="{width}" height="{height}">
  <!-- Badge Icon on Left -->
  <g transform="translate(60, 80)">
    <rect x="14" y="14" width="300" height="300" rx="60" fill="#1754CF" />
    <rect x="0" y="0" width="300" height="300" rx="60" fill="#151618" />
    <g transform="translate(45, 45) scale(13.125)" shape-rendering="crispEdges">
      <path d="M2 2h3v12H2V2zm9 0h3v12h-3V2zM5 5h2v2H5V5zm2 2h2v2H7V7zm2 2h2v2H9V9z" fill="#FAF9F6" />
      <rect x="12" y="11" width="3" height="3" fill="#1754CF" />
    </g>
  </g>

  <!-- NALAR Wordmark -->
  <text x="430" y="250" font-family="Inter, -apple-system, sans-serif" font-weight="900" font-size="180" letter-spacing="-5" fill="#151618">NALAR</text>
  <!-- Tagline -->
  <text x="435" y="340" font-family="Inter, -apple-system, sans-serif" font-weight="600" font-size="52" letter-spacing="-0.5" fill="#585960">Ada Masalah, Ada NALAR.</text>
</svg>'''

def render_svg_and_png(svg_content, filename_base, scale=1):
    svg_path = os.path.join(OUTPUT_DIR, f"{filename_base}.svg")
    png_path = os.path.join(OUTPUT_DIR, f"{filename_base}.png")
    
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
        
    cmd = [
        "resvg",
        "--sans-serif-family", "Inter",
    ]
    if scale > 1:
        cmd.extend(["-z", str(scale)])
    cmd.extend([svg_path, png_path])
    subprocess.run(cmd, check=True)
    
    # Copy to artifact dir for instant accessibility in UI
    artifact_png = os.path.join(ARTIFACT_DIR, f"{filename_base}.png")
    shutil.copy2(png_path, artifact_png)
    print(f"  Generated: {png_path} ({os.path.getsize(png_path) // 1024} KB)")

def main():
    print("Generating official NALAR Brand Logos...")
    
    # 1. Badge with signature blue shadow
    render_svg_and_png(svg_badge_with_shadow(512), "nalar-mark-shadow-512")
    render_svg_and_png(svg_badge_with_shadow(1024), "nalar-mark-shadow-1024")
    
    # 2. Clean badge (no shadow)
    render_svg_and_png(svg_badge_clean(512), "nalar-mark-badge-512")
    render_svg_and_png(svg_badge_clean(1024), "nalar-mark-badge-1024")
    
    # 3. Transparent pixel mark (pure icon mark)
    render_svg_and_png(svg_pixel_transparent("#151618", 512), "nalar-mark-transparent-dark")
    render_svg_and_png(svg_pixel_transparent("#FAF9F6", 512), "nalar-mark-transparent-light")
    
    # 4. Horizontal logo lockups (Dark & Light)
    render_svg_and_png(svg_horizontal_dark(1600, 440), "nalar-logo-horizontal-dark")
    render_svg_and_png(svg_horizontal_light(1600, 440), "nalar-logo-horizontal-light")
    
    # 5. Horizontal logo with tagline
    render_svg_and_png(svg_horizontal_tagline(1800, 480), "nalar-logo-with-tagline")
    
    print("✅ All NALAR logo PNG and SVG assets generated successfully!")

if __name__ == "__main__":
    main()
