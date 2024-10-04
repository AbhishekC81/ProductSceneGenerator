import argparse
import os
import time
from pathlib import Path
from datetime import datetime
from src.remove_background import remove_background
from src.create_image_canvas import create_image_canvas
from src.generate_mask import create_mask
from src.create_scene_pipeline import create_scene_pipeline
from src.generate_scene import generate_scene
from src.create_video_pipeline import create_video_pipeline
from src.generate_video import generate_video


def main():
    """
    Main function to generate a product video from an input image and a text prompt.

    This function:
    1. Parses command-line arguments for image path and text prompt.
    2. Creates an output directory based on the image name and current timestamp.
    3. Calls functions to remove the background from the image, generate a mask,
       create a scene, and generate a video from the scene.
    4. Prints a success message upon completion.

    Usage:
        python run.py --image <path_to_image> --text-prompt "<description_of_scene>"
    """
    try:
        # Parse command-line arguments
        parser = argparse.ArgumentParser(description="Generate product video from image and text prompt.")
        parser.add_argument("--image", required=True, help="Path to the input image file.")
        parser.add_argument("--text-prompt", required=True, help="Text prompt for scene generation.")
        args = parser.parse_args()

        # Extract image name and create output directory
        image_name = Path(args.image).stem  # Get the file name without extension
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Create a timestamp
        output_path = f"Results/{image_name}_{timestamp}"  # Create output path as a string
        os.makedirs(output_path, exist_ok=True)  # Create the output directory

        # Step 1: Remove background
        no_bg_path = remove_background(args.image, output_path)

        # Step 2: Generate mask
        canvas = create_image_canvas(no_bg_path)
        print("Image Canvas Created Successfully!")
        mask = create_mask(canvas)
        print("Mask Created Successfully!")

        # Step 3: Create scene pipeline
        scene_pipeline = create_scene_pipeline()
        print("Scene Generation Pipeline Created Successfully!")

        # Step 4: Generate scene
        scene = generate_scene(args.text_prompt, canvas, mask, output_path)
        print("Scene Generated Successfully!")

        # Step 5: Create video pipeline
        video_pipeline = create_video_pipeline()
        print("Video Generation Pipeline Created Successfully!")

        # Step 6: Generate video
        generate_video(video_pipeline, scene, output_path)
        print("Video Generated Successfully!")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}. Please check if the image file exists and try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please check the input parameters.")


if __name__ == "__main__":
    main()
