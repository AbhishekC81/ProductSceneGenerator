# Product Scene Generator

This project is designed to generate a visually appealing scene for e-commerce products using an input image and a descriptive prompt. It removes the background from the product image, creates a canvas for scene generation, creates a mask, and finally produces an image and a video showcasing the product in the text-conditioned scene using Stable Diffusion. 

## How to Use

### Step 1: Install Requirements

Make sure you have all the required libraries installed. You can do this by running:

```bash
pip install -r requirements.txt
```

### Step 2: Run the Pipeline

To run the pipeline, use the following command:

```bash
python run.py --image Examples/cooking_pot.jpg --text-prompt "product in a kitchen used in meal generation"
```

## Example Result

### Input Image
![Input Image](Examples/cooking_pot.jpg)

### Text Prompt
*"Product in a kitchen used in meal generation"*

### Scene
![Scene Output](Results/cooking_pot_20241005_002321/scene.jpg)

### Video
![Video Output](Results/cooking_pot_20241005_002321/video.mp4)

You can view other generations in the [Results](Results) folder.
