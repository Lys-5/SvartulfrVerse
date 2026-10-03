import os
import random
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_polaroid(input_path, output_path, caption="", tilt_angle=None):
    """
    Takes an input image and turns it into a tilted polaroid with a transparent background.
    """
    try:
        # Load the original image
        img = Image.open(input_path).convert("RGBA")
        
        # Determine base sizes (e.g., scale to a standard width if too large)
        target_width = 400
        w_percent = (target_width / float(img.size[0]))
        h_size = int((float(img.size[1]) * float(w_percent)))
        img = img.resize((target_width, h_size), Image.Resampling.LANCZOS)
        
        # Polaroid dimensions
        border_sides = 20
        border_top = 20
        border_bottom = 80
        
        pol_w = img.width + border_sides * 2
        pol_h = img.height + border_top + border_bottom
        
        # Create white polaroid base
        polaroid = Image.new("RGBA", (pol_w, pol_h), (255, 255, 255, 255))
        
        # Paste the photo onto the base
        polaroid.paste(img, (border_sides, border_top))
        
        # Add a subtle inner shadow or border line (optional)
        draw = ImageDraw.Draw(polaroid)
        draw.rectangle(
            [border_sides-1, border_top-1, border_sides+img.width, border_top+img.height],
            outline=(200, 200, 200, 255)
        )
        
        # Add caption (if provided)
        if caption:
            # Try to load a generic font or fallback
            try:
                # Use a handwriting-like font if available, else default
                font = ImageFont.truetype("segoeprb.ttf", 24) # Segoe Print on Windows
            except:
                font = ImageFont.load_default()
            
            # Calculate text size using textbbox
            bbox = draw.textbbox((0, 0), caption, font=font)
            text_w = bbox[2] - bbox[0]
            text_h = bbox[3] - bbox[1]
            
            text_x = (pol_w - text_w) / 2
            text_y = pol_h - border_bottom + (border_bottom - text_h) / 2 - 10
            
            # Draw text (black/dark gray)
            draw.text((text_x, text_y), caption, fill=(30, 30, 30, 255), font=font)
            
        # Add drop shadow to the polaroid
        # Create a slightly larger canvas for the shadow
        shadow_padding = 20
        shadow_w = pol_w + shadow_padding * 2
        shadow_h = pol_h + shadow_padding * 2
        
        shadow = Image.new("RGBA", (shadow_w, shadow_h), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow)
        
        # Draw a black rectangle where the polaroid will go
        shadow_draw.rectangle(
            [shadow_padding, shadow_padding, shadow_padding + pol_w, shadow_padding + pol_h],
            fill=(0, 0, 0, 80) # 80 alpha for subtle shadow
        )
        
        # Blur the shadow
        shadow = shadow.filter(ImageFilter.GaussianBlur(10))
        
        # Paste the polaroid onto the shadow
        shadow.paste(polaroid, (shadow_padding, shadow_padding), polaroid)
        polaroid = shadow
        
        # Tilt the polaroid
        if tilt_angle is None:
            tilt_angle = random.uniform(-4, 4)
            
        # Rotate with expand=True to not clip corners
        polaroid = polaroid.rotate(tilt_angle, resample=Image.Resampling.BICUBIC, expand=True)
        
        # Save output
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        polaroid.save(output_path, "PNG")
        print(f"Saved polaroid to {output_path}")
        return output_path
        
    except Exception as e:
        print(f"Error processing {input_path}: {e}")
        return None

if __name__ == "__main__":
    # Test with one of the user's uploaded images
    input_dir = r"C:\Users\mande\.gemini\antigravity\brain\6d865937-2f87-455c-98d9-b64003916b56\.user_uploaded"
    test_img = os.path.join(input_dir, "media_1790998280657.webp")
    out_img = r"d:\SvartulfrVerse\asset\polaroids\test_polaroid.png"
    
    create_polaroid(test_img, out_img, caption="Test", tilt_angle=-3)
