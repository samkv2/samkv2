import random

width = 800
height = 200
font_size = 20
cols = width // font_size
chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"

svg_header = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">
  <style>
    .bg {{ fill: #000; }}
    .matrix-text {{
      font-family: monospace;
      font-size: {font_size}px;
      font-weight: bold;
    }}
    .glow {{
      filter: drop-shadow(0 0 5px #0F0);
    }}
    @keyframes fall {{
      0% {{ transform: translateY(-100%); opacity: 1; fill: #0F0; }}
      50% {{ fill: #00FF00; }}
      100% {{ transform: translateY({height + 100}px); opacity: 0; fill: #003300; }}
    }}
  </style>
  <rect width="100%" height="100%" class="bg" />
'''

svg_body = ""

for i in range(cols):
    x = i * font_size
    # generate a column of random characters
    num_chars = random.randint(10, 25)
    
    col_str = ""
    for j in range(num_chars):
        c = random.choice(chars)
        col_str += f'<tspan x="{x}" dy="{font_size}">{c}</tspan>'
        
    delay = random.uniform(0, 5)
    duration = random.uniform(3, 8)
    
    # CSS animations on SVG elements are supported in modern browsers
    svg_body += f'''
  <g style="animation: fall {duration}s linear {delay}s infinite;">
    <text class="matrix-text glow" x="{x}" y="0">{col_str}</text>
  </g>'''

svg_footer = "</svg>"

with open("matrix.svg", "w") as f:
    f.write(svg_header + svg_body + svg_footer)
