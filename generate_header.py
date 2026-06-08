import base64

image_path = r"d:\projects\Fork Projects\harshsingh07i\hero_image.jpeg"
svg_path = r"d:\projects\Fork Projects\harshsingh07i\header_new.svg"

with open(image_path, "rb") as f:
    b64_data = base64.b64encode(f.read()).decode("utf-8")

svg_content = f"""<svg width="1000" height="400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="blur">
      <feGaussianBlur stdDeviation="3" />
    </filter>
  </defs>

  <!-- Background Image with Cover sizing -->
  <image href="data:image/jpeg;base64,{b64_data}" x="0" y="0" width="1000" height="400" preserveAspectRatio="xMidYMid slice" />
  
  <!-- Dark Overlay to make text pop -->
  <rect x="0" y="0" width="1000" height="400" fill="black" fill-opacity="0.6" />

  <!-- Main Title -->
  <text x="500" y="200" font-family="'Courier New', Courier, monospace" font-size="65" font-weight="bold" fill="#D4AF37" text-anchor="middle" letter-spacing="4">HARSH SINGH</text>
  
  <!-- Subtitle -->
  <text x="500" y="260" font-family="'Segoe UI', Arial, sans-serif" font-size="22" font-weight="300" fill="#ffffff" text-anchor="middle" letter-spacing="2">SOFTWARE WIZARD • BACKEND ALCHEMIST • CODE SORCERER</text>
  
  <!-- Magical divider -->
  <path d="M 300 290 L 700 290" stroke="#740001" stroke-width="2" stroke-linecap="round" />
  <path d="M 400 295 L 600 295" stroke="#D4AF37" stroke-width="2" stroke-linecap="round" />

</svg>"""

with open(svg_path, "w", encoding="utf-8") as f:
    f.write(svg_content)

print("Generated header.svg successfully!")
