from PIL import Image
import os

def remove_white_background(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return False
        
    try:
        img = Image.open(input_path)
        img = img.convert("RGBA")
        datas = img.getdata()
        
        newData = []
        for item in datas:
            # Change all white (also shades of whites)
            # to transparent
            if item[0] > 200 and item[1] > 200 and item[2] > 200:
                newData.append((255, 255, 255, 0))
            else:
                # Make dark pixels completely black for crispness, or keep original color
                # Since the logo is black, we can keep it as is.
                newData.append(item)
                
        img.putdata(newData)
        img.save(output_path, "PNG")
        print(f"Success! Saved transparent logo to {output_path}")
        return True
    except Exception as e:
        print(f"Failed to process image: {e}")
        return False

if __name__ == "__main__":
    input_img = "images/apple-touch-icon.png"
    output_img = "images/logo-transparent.png"
    
    print(f"Looking for {input_img}...")
    remove_white_background(input_img, output_img)
