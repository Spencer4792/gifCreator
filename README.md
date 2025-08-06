# Simple GIF Creator 🎬

A script to turn your photos into a gif with a simple command!

## What it does

Drop your images in a folder, run the script, and get an animated GIF. Perfect for:
- Photo slideshows
- Animation sequences  
- Step-by-step tutorials
- Before/after comparisons
- Any series of images you feel like animating for whatever reason

## Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

## Quick Setup

### 1. Download the Script

```bash
git clone https://github.com/Spencer4792/gifCreator.git
cd gifCreator
```

### 2. Set up the Environment

**On Mac/Linux:**
```bash
python3 -m venv gif_env
source gif_env/bin/activate
pip install Pillow
```

**On Windows:**
```bash
python -m venv gif_env
gif_env\Scripts\activate
pip install Pillow
```

### 3. Test It Out

If you use my sample folder, the command will be:
```bash
python gifCreator.py sampleImages
```
It should create a file called animation.gif

## How to Use

### Basic Usage (Just like above)

Put your images in a folder and run:
```bash
python gifCreator.py sample_folder_name
```

This creates an `animation.gif` with the default settings that I set (500ms per frame).

### Custom Options

```bash
python gifCreator.py my_photos -o vacation.gif -d 800 -l 3
```

**Options:**
- `-o` or `--output` - Name your GIF file (default: `animation.gif`)
- `-d` or `--duration` - Milliseconds per frame (default: `500`)  
- `-l` or `--loop` - Number of loops, 0 = infinite (default: `0`)

## Examples

### Photo Slideshow
```bash
# Slow slideshow - 1 second per photo
python gifCreator.py vacation_pics -o slideshow.gif -d 1000
```

### Fast Animation
```bash
# Quick animation - like a flipbook
python gifCreator.py drawing_frames -o flipbook.gif -d 100
```

### Logo Sequence  
```bash
# Medium speed with 5 loops
python gifCreator.py logo_steps -o logo_reveal.gif -d 300 -l 5
```

## Tips for the Best Results

### Image Preparation
- **Consistent naming**: Use `image001.jpg`, `image002.jpg`, etc. for proper ordering
- **Similar dimensions**: Images work best when they're already the same size
- **Supported formats**: PNG, JPG, JPEG, BMP, GIF

### Animation Settings
- **Slideshow**: 800-2000ms per frame
- **Smooth animation**: 50-200ms per frame  
- **Photo sequence**: 300-800ms per frame

### File Size Tips
- More frames = larger file
- Longer duration = same file size (just slower)
- Large image dimensions = much larger file
- Consider resizing images before running the script

## What the Script Does

1. **Finds your images** - Looks for PNG, JPG, JPEG, BMP, and GIF files
2. **Sorts them** - Alphabetical order (image1.jpg before image10.jpg)
3. **Loads and converts** - Makes sure they're all compatible
4. **Resizes if needed** - Matches everything to the first image's size
5. **Creates your GIF** - With optimization to keep file size reasonable
6. **Shows progress** - So you know what's happening!

## Sample Output

```
🎬 GIF Creator
📁 Source folder: my_photos
📄 Output file: slideshow.gif
==================================================
📁 Found 8 images:
   • photo001.jpg
   • photo002.jpg
   • photo003.jpg
   ...

🔄 Loading images...
   ✅ Loaded 1/8: photo001.jpg
   ✅ Loaded 2/8: photo002.jpg
   ...

📐 Image dimensions: 1920x1080
🔧 Resizing images to match first image...

🎬 Creating GIF...
✅ GIF created successfully!
   📄 File: slideshow.gif
   📊 Size: 2.3 MB
   ⏱️  Duration per frame: 500ms
   🔄 Frames: 8

🎉 Done! Your GIF is ready to use.
```

## Troubleshooting

### "No images found"
- Check that your folder path is correct
- Make sure images have supported extensions (.png, .jpg, .jpeg, .bmp, .gif)
- Verify the folder isn't empty

### "Command not found: python"
Try using `python3` instead:
```bash
python3 gifCreator.py my_photos
```

### Virtual Environment Issues
Make sure you've activated it:
```bash
source gif_env/bin/activate  # Mac/Linux
gif_env\Scripts\activate     # Windows
```

### Large File Sizes
- Resize your images first (try 800x600 or smaller)
- Reduce the number of frames
- Use fewer colors in your original images

### Images in Wrong Order
Name your files with leading zeros:
- ✅ Good: `image001.jpg`, `image002.jpg`, `image010.jpg`
- ❌ Bad: `image1.jpg`, `image2.jpg`, `image10.jpg` (10 will process before 2 here which isn't ideal, that's why the 0's are important)

## Project Structure

```
gifCreator/
├── gifCreator.py       # The main script
├── README.md           # This file
├── requirements.txt    # Dependencies
└── sampleImages        # Sample images (Some images I provided as an example)
```

## Advanced Usage

### Batch Processing Multiple Folders
```bash
# Process multiple vacation folders
for folder in vacation_*; do
    python gifCreator.py "$folder" -o "${folder}.gif" -d 1000
done
```

### Different Speeds for Different Content
```bash
# Fast for drawings/animations
python gifCreator.py drawings -o animation.gif -d 100

# Medium for step-by-step tutorials  
python gifCreator.py tutorial_steps -o howto.gif -d 400

# Slow for photo slideshows
python gifCreator.py photos -o memories.gif -d 1500
```

## Contributing

Found a bug? Have an idea? Hate something?
1. Fork this repository
2. Make your changes
3. Submit a pull request

## License

MIT License - feel free to use this for any project!

---
