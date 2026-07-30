from PIL import Image, ImageDraw
import os

img_path = 'images/logo-transparent.png'
out_path = 'images/favicon-circle.png'

if not os.path.exists(img_path):
    print(f"Error: {img_path} not found.")
    exit(1)

img = Image.open(img_path).convert("RGBA")
w, h = img.size

# Make circle 30% larger for nice padding
circle_size = int(max(w, h) * 1.3)

bg = Image.new("RGBA", (circle_size, circle_size), (255, 255, 255, 0))
draw = ImageDraw.Draw(bg)
# Draw the white circle
draw.ellipse((0, 0, circle_size-1, circle_size-1), fill=(255, 255, 255, 255))

# Center the logo
offset = ((circle_size - w) // 2, (circle_size - h) // 2)
bg.paste(img, offset, img)

# Save as PNG
bg.save(out_path)
print(f"Success! Saved to {out_path}")
