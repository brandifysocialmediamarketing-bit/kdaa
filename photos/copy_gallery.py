import os
import shutil

src_dir = r"d:\brandify\photos"
dst_dir = r"C:\Users\parth\.gemini\antigravity\brain\314e81fb-b648-4b48-8535-f097477dde65\browser"

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

files = os.listdir(src_dir)
html_content = """<!DOCTYPE html>
<html>
<head>
<title>Photo Gallery</title>
<style>
  body { font-family: sans-serif; background: #f0f0f0; margin: 20px; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; }
  .card { background: white; padding: 10px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); text-align: center; }
  img { max-width: 100%; height: auto; max-height: 250px; object-fit: contain; display: block; margin: 0 auto 10px; }
  .filename { font-size: 12px; word-break: break-all; font-weight: bold; }
</style>
</head>
<body>
<h1>Gallery</h1>
<div class="grid">
"""

for f in files:
    if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')) and not f.startswith('gallery') and not f.startswith('generate') and not f.startswith('copy'):
        src_path = os.path.join(src_dir, f)
        dst_path = os.path.join(dst_dir, f)
        shutil.copy2(src_path, dst_path)
        html_content += f"""  <div class="card">
    <img src="{f}" />
    <div class="filename">{f}</div>
  </div>
"""

html_content += """</div>
</body>
</html>
"""

with open(os.path.join(dst_dir, "gallery.html"), "w", encoding="utf-8") as fh:
    fh.write(html_content)

print("Gallery copied and generated successfully in the allowed folder!")
