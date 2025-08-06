#!/usr/bin/env python3
"""
Simple GIF Creator - Create animated GIFs from a folder of images
"""

import argparse
import os
import glob
from PIL import Image, ImageOps

def create_gif(image_folder, output_name="animation.gif", duration=500, loop=0):
    """
    Create an animated GIF from images in a folder
    
    Args:
        image_folder: Path to folder containing images
        output_name: Name of output GIF file
        duration: Duration of each frame in milliseconds
        loop: Number of loops (0 = infinite)
    """
    
    # Find all image files
    extensions = ['*.png', '*.jpg', '*.jpeg', '*.bmp', '*.gif']
    image_files = []
    
    for ext in extensions:
        image_files.extend(glob.glob(os.path.join(image_folder, ext)))
        image_files.extend(glob.glob(os.path.join(image_folder, ext.upper())))
    
    if not image_files:
        print(f"❌ No images found in '{image_folder}'")
        print("   Make sure your folder contains .png, .jpg, .jpeg, .bmp, or .gif files")
        return False
    
    # Sort files naturally (so image1.jpg comes before image10.jpg)
    image_files.sort()
    
    print(f"📁 Found {len(image_files)} images:")
    for img_path in image_files:
        print(f"   • {os.path.basename(img_path)}")
    
    # Load images
    images = []
    print(f"\n🔄 Loading images...")
    
    for i, img_path in enumerate(image_files, 1):
        try:
            img = Image.open(img_path)
            
            # Automatically fix orientation based on EXIF data
            # This handles photos taken with phones/cameras
            try:
                img = ImageOps.exif_transpose(img)
            except Exception:
                # If orientation correction fails, continue with original image
                pass
            
            # Convert to RGB for GIF compatibility
            if img.mode != 'RGB':
                img = img.convert('RGB')
            images.append(img)
            print(f"   ✅ Loaded {i}/{len(image_files)}: {os.path.basename(img_path)}")
        except Exception as e:
            print(f"   ❌ Error loading {os.path.basename(img_path)}: {e}")
    
    if not images:
        print("❌ No valid images could be loaded")
        return False
    
    # Get the size of the first image as reference
    width, height = images[0].size
    print(f"\n📐 Image dimensions: {width}x{height}")
    
    # Resize all images to match the first one (if needed)
    print(f"🔧 Resizing images to match first image...")
    resized_images = []
    
    for i, img in enumerate(images):
        if img.size != (width, height):
            img = img.resize((width, height), Image.Resampling.LANCZOS)
            print(f"   📏 Resized image {i+1}")
        resized_images.append(img)
    
    # Create the GIF
    print(f"\n🎬 Creating GIF...")
    try:
        resized_images[0].save(
            output_name,
            save_all=True,
            append_images=resized_images[1:],
            duration=duration,
            loop=loop,
            optimize=True
        )
        
        # Get file size
        file_size = os.path.getsize(output_name)
        if file_size > 1024 * 1024:
            size_str = f"{file_size / (1024 * 1024):.1f} MB"
        else:
            size_str = f"{file_size / 1024:.1f} KB"
        
        print(f"✅ GIF created successfully!")
        print(f"   📄 File: {output_name}")
        print(f"   📊 Size: {size_str}")
        print(f"   ⏱️  Duration per frame: {duration}ms")
        print(f"   🔄 Frames: {len(resized_images)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating GIF: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="Create animated GIFs from a folder of images",
        epilog="Example: python gif_creator.py my_photos -o vacation.gif -d 800"
    )
    
    parser.add_argument(
        'folder', 
        help='Folder containing images (png, jpg, jpeg, bmp, gif)'
    )
    
    parser.add_argument(
        '-o', '--output', 
        default='animation.gif',
        help='Output GIF filename (default: animation.gif)'
    )
    
    parser.add_argument(
        '-d', '--duration', 
        type=int, 
        default=500,
        help='Duration per frame in milliseconds (default: 500)'
    )
    
    parser.add_argument(
        '-l', '--loop', 
        type=int, 
        default=0,
        help='Number of loops, 0 = infinite (default: 0)'
    )
    
    args = parser.parse_args()
    
    # Check if folder exists
    if not os.path.exists(args.folder):
        print(f"❌ Folder '{args.folder}' not found")
        return
    
    if not os.path.isdir(args.folder):
        print(f"❌ '{args.folder}' is not a directory")
        return
    
    print(f"🎬 GIF Creator")
    print(f"📁 Source folder: {args.folder}")
    print(f"📄 Output file: {args.output}")
    print("=" * 50)
    
    # Create the GIF
    success = create_gif(args.folder, args.output, args.duration, args.loop)
    
    if success:
        print(f"\n🎉 Done! Your GIF is ready to use.")
    else:
        print(f"\n💥 Something went wrong. Please check the errors above.")

if __name__ == "__main__":
    main()