#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Batch Resize Icon for Xcode
Generate all required iOS/iPadOS app icon sizes from a single 1024x1024 image.

Author: vampire
Updated: 2025
License: MIT
"""

import os
import sys
import argparse
import shutil
import logging
from pathlib import Path
from typing import List, Tuple, Optional
from PIL import Image

# Import the Contents.json template
from xcode_contents_json import CONTENTS_JSON_TEMPLATE


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)


class IconResizer:
    """
    A tool to generate iOS app icons in all required sizes from a single source image.
    """

    # All required icon sizes for iOS/iPadOS
    ICON_SIZES = [20, 29, 40, 58, 60, 76, 80, 87, 120, 152, 167, 180, 1024]

    # Supported image formats
    SUPPORTED_FORMATS = {'.png', '.jpg', '.jpeg'}

    # Required source image size
    SOURCE_SIZE = 1024

    def __init__(self, source_image_path: str, output_dir: Optional[str] = None,
                 auto_scale: bool = False, verbose: bool = False):
        """
        Initialize the IconResizer.

        Args:
            source_image_path: Path to the source image (preferably 1024x1024)
            output_dir: Custom output directory (optional)
            auto_scale: Automatically scale non-1024 images to 1024
            verbose: Enable verbose logging
        """
        self.source_path = Path(source_image_path).resolve()
        self.output_dir = output_dir
        self.auto_scale = auto_scale

        if verbose:
            logger.setLevel(logging.DEBUG)

        # Validate input
        self._validate_input()

        # Set output directory
        self._set_output_directory()

    def _validate_input(self) -> None:
        """Validate the input image file."""
        # Check if file exists
        if not self.source_path.exists():
            raise FileNotFoundError(f"Source image not found: {self.source_path}")

        # Check if it's a file
        if not self.source_path.is_file():
            raise ValueError(f"Path is not a file: {self.source_path}")

        # Check file format
        if self.source_path.suffix.lower() not in self.SUPPORTED_FORMATS:
            raise ValueError(
                f"Unsupported format: {self.source_path.suffix}. "
                f"Supported formats: {', '.join(self.SUPPORTED_FORMATS)}"
            )

        # Validate image and size
        try:
            with Image.open(self.source_path) as img:
                width, height = img.size

                # Check if image is square
                if width != height:
                    raise ValueError(
                        f"Image must be square. Current size: {width}x{height}"
                    )

                # Check if image is 1024x1024 or can be scaled
                if width != self.SOURCE_SIZE:
                    if width < self.SOURCE_SIZE:
                        # Upscaling is not allowed - will produce blurry icons
                        raise ValueError(
                            f"Image size is {width}x{height}, which is smaller than required "
                            f"{self.SOURCE_SIZE}x{self.SOURCE_SIZE}. "
                            f"Upscaling small images will result in blurry icons and may fail App Store review. "
                            f"Please use a high-quality source image of at least {self.SOURCE_SIZE}x{self.SOURCE_SIZE}."
                        )
                    else:
                        # Downscaling is allowed with --auto-scale flag
                        if self.auto_scale:
                            logger.info(
                                f"Image size is {width}x{height}, will be downscaled to "
                                f"{self.SOURCE_SIZE}x{self.SOURCE_SIZE}"
                            )
                        else:
                            raise ValueError(
                                f"Image size is {width}x{height}, larger than required "
                                f"{self.SOURCE_SIZE}x{self.SOURCE_SIZE}. "
                                f"Use --auto-scale to automatically downscale to {self.SOURCE_SIZE}x{self.SOURCE_SIZE}."
                            )

                # Check if image has transparency (recommended for iOS icons)
                if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                    logger.debug("Image has transparency channel")
                else:
                    logger.warning(
                        "Image doesn't have transparency. "
                        "iOS icons typically require transparent backgrounds."
                    )

        except Exception as e:
            raise ValueError(f"Failed to open image: {e}")

    def _set_output_directory(self) -> None:
        """Set and create the output directory."""
        if self.output_dir:
            self.output_path = Path(self.output_dir).resolve()
        else:
            # Create directory name with timestamp
            import time
            timestamp = int(time.time())
            dir_name = f"AppIcon.appiconset_{timestamp}"
            self.output_path = self.source_path.parent / dir_name

        # Create directory
        try:
            self.output_path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Output directory: {self.output_path}")
        except Exception as e:
            raise IOError(f"Failed to create output directory: {e}")

    def _prepare_source_image(self) -> Image.Image:
        """
        Load and prepare the source image.

        Returns:
            PIL Image object ready for resizing
        """
        img = Image.open(self.source_path)

        # Convert to RGBA if needed
        if img.mode != 'RGBA':
            img = img.convert('RGBA')

        # Downscale to 1024x1024 if needed (only downscaling is allowed)
        if img.size[0] != self.SOURCE_SIZE and self.auto_scale:
            if img.size[0] > self.SOURCE_SIZE:
                logger.info(f"Downscaling image from {img.size[0]}x{img.size[1]} to {self.SOURCE_SIZE}x{self.SOURCE_SIZE}")
                img = img.resize(
                    (self.SOURCE_SIZE, self.SOURCE_SIZE),
                    Image.Resampling.LANCZOS
                )
            else:
                # This should never happen due to validation, but added as safety check
                raise ValueError(
                    f"Cannot upscale image from {img.size[0]}x{img.size[1]} to {self.SOURCE_SIZE}x{self.SOURCE_SIZE}. "
                    f"Upscaling will result in blurry icons."
                )

        return img

    def generate_icons(self) -> None:
        """Generate all required icon sizes."""
        logger.info("Starting icon generation...")

        # Prepare source image
        source_img = self._prepare_source_image()

        # Generate each size
        generated_count = 0
        for size in self.ICON_SIZES:
            try:
                output_filename = f"_{size}.png"
                output_path = self.output_path / output_filename

                # Resize image
                if size == self.SOURCE_SIZE:
                    # No need to resize 1024x1024
                    resized_img = source_img
                else:
                    resized_img = source_img.resize(
                        (size, size),
                        Image.Resampling.LANCZOS
                    )

                # Save as PNG
                resized_img.save(output_path, 'PNG', optimize=True)
                logger.debug(f"Generated: {output_filename}")
                generated_count += 1

            except Exception as e:
                logger.error(f"Failed to generate {size}x{size} icon: {e}")

        # Close source image
        source_img.close()

        logger.info(f"Successfully generated {generated_count}/{len(self.ICON_SIZES)} icons")

    def generate_contents_json(self) -> None:
        """Generate the Contents.json file required by Xcode."""
        contents_path = self.output_path / "Contents.json"

        try:
            with open(contents_path, 'w', encoding='utf-8') as f:
                f.write(CONTENTS_JSON_TEMPLATE)
            logger.info(f"Generated: Contents.json")
        except Exception as e:
            logger.error(f"Failed to generate Contents.json: {e}")
            raise

    def run(self) -> None:
        """Execute the complete icon generation process."""
        try:
            self.generate_icons()
            self.generate_contents_json()
            logger.info(f"\n✓ All icons generated successfully!")
            logger.info(f"Output location: {self.output_path}")
            logger.info(f"\nYou can now drag the '{self.output_path.name}' folder into Xcode.")
        except Exception as e:
            logger.error(f"Icon generation failed: {e}")
            raise


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Generate iOS/iPadOS app icons in all required sizes from a single image.',
        epilog='Example: python batch_resize_icon.py icon_1024.png -o MyAppIcon.appiconset'
    )

    parser.add_argument(
        'input_image',
        nargs='?',
        help='Path to the source image (preferably 1024x1024 PNG with transparency)'
    )

    parser.add_argument(
        '-o', '--output',
        dest='output_dir',
        help='Custom output directory name'
    )

    parser.add_argument(
        '-a', '--auto-scale',
        action='store_true',
        help='Automatically downscale images larger than 1024x1024 (upscaling is not supported)'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )

    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 2.0'
    )

    return parser.parse_args()


def main() -> int:
    """Main entry point."""
    args = parse_arguments()

    # If no input image provided, prompt user
    if not args.input_image:
        print("Batch Resize Icon for Xcode")
        print("=" * 50)
        print("\nPlease enter the path to your 1024x1024 icon image:")
        print("(Supported formats: PNG, JPG, JPEG)")
        input_path = input("\nPath: ").strip()

        if not input_path:
            logger.error("No input file provided")
            return 1

        args.input_image = input_path

    try:
        # Create resizer and run
        resizer = IconResizer(
            source_image_path=args.input_image,
            output_dir=args.output_dir,
            auto_scale=args.auto_scale,
            verbose=args.verbose
        )
        resizer.run()
        return 0

    except KeyboardInterrupt:
        logger.info("\nOperation cancelled by user")
        return 130

    except Exception as e:
        logger.error(f"Error: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
