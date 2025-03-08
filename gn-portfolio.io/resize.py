from PIL import Image
import os

# Define the file paths of the uploaded images
image_paths = [
    "/Users/gouthami/Downloads/browny-v1.0/assets/images/projects/ecom-fraud.jpg",
    "/Users/gouthami/Downloads/browny-v1.0/assets/images/projects/heart-pred.jpg",
    "/Users/gouthami/Downloads/browny-v1.0/assets/images/projects/mortgage.jpg",
    "/Users/gouthami/Downloads/browny-v1.0/assets/images/projects/nlpfn.jpg"
]

# Target file size in bytes (16 KB)
target_size = 16 * 1024

# Resize and compress images
resized_images = []
for img_path in image_paths:
    with Image.open(img_path) as img:
        # Resize while maintaining aspect ratio
        img = img.convert("RGB")
        img.thumbnail((300, 300))  # Initial resizing to reduce size
        
        # Save with adjusted quality to reach target size
        for quality in range(95, 5, -5):  # Adjust quality in steps
            temp_path = img_path.replace(".jpg", "_resized.jpg")
            img.save(temp_path, "JPEG", quality=quality)
            if os.path.getsize(temp_path) <= target_size:
                resized_images.append(temp_path)
                break

# Return the paths of the resized images
resized_images
