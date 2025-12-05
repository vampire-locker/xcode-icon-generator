# Batch Resize Icon for Xcode

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

[中文文档](README_CN.md) | English

A Python tool that automatically generates all required iOS/iPadOS app icon sizes from a single 1024×1024 source image.

## Features

- 🚀 **One Command Generation**: Generate all 13 icon sizes required by Xcode
- ✅ **Xcode Ready**: Automatically creates `Contents.json` configuration file
- 🔍 **Input Validation**: Checks image format, size, and transparency
- 🎨 **Auto Downscaling**: Optionally downscale high-resolution images (>1024px) to 1024×1024
- 📦 **Zero Configuration**: Works out of the box with sensible defaults
- 💻 **CLI & Interactive**: Supports both command-line arguments and interactive mode

## Generated Icon Sizes

The tool generates the following sizes required for iOS and iPadOS:

| Size (px)    | Usage                                    |
| ------------ | ---------------------------------------- |
| 20, 40, 60   | iPhone Notification, Settings, Spotlight |
| 29, 58, 87   | iPhone Settings                          |
| 80, 120, 180 | iPhone App Icon                          |
| 76, 152      | iPad App Icon                            |
| 167          | iPad Pro App Icon                        |
| 1024         | App Store                                |

## Requirements

- Python 3.6 or higher
- Pillow (PIL) 10.0.0+

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/BatchResizePicForXcode.git
cd BatchResizePicForXcode
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Interactive Mode

Simply run the script and follow the prompts:

```bash
python batch_resize_icon.py
```

### Command Line Mode

```bash
# Basic usage
python batch_resize_icon.py icon_1024.png

# Specify custom output directory
python batch_resize_icon.py icon_1024.png -o MyAppIcon.appiconset

# Auto-downscale high-resolution images (e.g., 2048x2048 to 1024x1024)
python batch_resize_icon.py icon_2048.png --auto-scale

# Custom icon filename prefix (generates: icon_20.png, icon_29.png, etc.)
python batch_resize_icon.py icon_1024.png --prefix icon_

# Enable verbose output
python batch_resize_icon.py icon_1024.png -v
```

### Command Line Options

| Option                | Description                                                                    |
| --------------------- | ------------------------------------------------------------------------------ |
| `input_image`         | Path to source image (preferably 1024×1024 PNG)                                |
| `-o, --output DIR`    | Custom output directory name                                                   |
| `-a, --auto-scale`    | Automatically downscale images larger than 1024×1024 (upscaling not supported) |
| `-p, --prefix PREFIX` | Custom prefix for icon filenames (default: "\_")                               |
| `-v, --verbose`       | Enable verbose output                                                          |
| `--version`           | Show version information                                                       |
| `-h, --help`          | Show help message                                                              |

## Best Practices

For optimal results, your source image should be:

- **1024×1024 pixels** - Required size for App Store
- **PNG format** - Supports transparency
- **Transparent background** - iOS icon standard
- **Square aspect ratio** - Required by iOS

## Output

The tool creates a folder (e.g., `AppIcon.appiconset_1234567890`) containing:

- 13 PNG files with all required icon sizes (default names: `_20.png`, `_29.png`, etc., or custom with `--prefix`)
- `Contents.json` - Xcode configuration file

You can drag the entire folder directly into your Xcode project's Assets.xcassets.

## Example

```bash
$ python batch_resize_icon.py my_icon_1024.png
INFO: Output directory: /path/to/AppIcon.appiconset_1701234567
INFO: Starting icon generation...
INFO: Successfully generated 13/13 icons
INFO: Generated: Contents.json

✓ All icons generated successfully!
Output location: /path/to/AppIcon.appiconset_1701234567

You can now drag the 'AppIcon.appiconset_1701234567' folder into Xcode.
```

## How to Use in Xcode

1. Run the tool to generate icons
2. Open your Xcode project
3. Navigate to `Assets.xcassets`
4. Delete the existing `AppIcon` asset (if any)
5. Drag the generated `.appiconset` folder into Assets.xcassets
6. Rename it to `AppIcon` if needed

## Troubleshooting

### "Image must be 1024x1024" or size error

- **If your image is larger than 1024×1024**: Use `--auto-scale` to automatically downscale it:
  ```bash
  python batch_resize_icon.py large_icon_2048.png --auto-scale
  ```
- **If your image is smaller than 1024×1024**: You must use a higher quality source image. Upscaling will produce blurry icons that may fail App Store review. Please create or obtain a proper 1024×1024 source image.

### "Unsupported format"

The tool only supports PNG, JPG, and JPEG formats. Convert your image first.

### "Image doesn't have transparency"

This is a warning, not an error. iOS icons typically use transparent backgrounds, but you can proceed if your design requires a solid background.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### Version 2.0 (2025)

- Complete refactor with modern Python practices
- Added command-line argument support
- Added input validation and error handling
- Fixed deprecated PIL API usage
- **Improved auto-scaling feature**: Now only allows downscaling from high-resolution images (>1024px) to prevent blurry icons from upscaling
- Improved logging and user feedback
- Added comprehensive documentation

### Version 1.0 (2018)

- Initial release
- Basic icon generation functionality

## Author

Original Author: vampire-locker (2018)
Refactored: 2025

## Acknowledgments

- Built with [Pillow (PIL)](https://python-pillow.org/)
- Icon size requirements based on [Apple's Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)

---

If you find this tool helpful, please consider giving it a ⭐️ on GitHub!
