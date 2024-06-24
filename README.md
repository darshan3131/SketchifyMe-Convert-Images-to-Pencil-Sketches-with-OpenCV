# SketchifyMe-Convert-Images-to-Pencil-Sketches-with-OpenCV
SketchifyMe is a Python application that transforms your images into beautiful pencil sketches using OpenCV. This project provides a simple yet powerful tool to create artistic sketches from your photos. Perfect for both beginners and advanced users interested in image processing and computer vision.

# SketchifyMe: Convert Images to Pencil Sketches with OpenCV

SketchifyMe is a Python-based application designed to transform your images into stunning pencil sketches. Utilizing the power of OpenCV, this project offers an easy-to-use solution for creating artistic renditions of your photos. Whether you're a beginner looking to learn more about image processing or an advanced user seeking a reliable tool for creating sketches, SketchifyMe has you covered.

## Features

- **Simple and Intuitive**: Easily convert images to pencil sketches with minimal code.
- **High-Quality Output**: Produces detailed and aesthetically pleasing sketches.
- **OpenCV Powered**: Leverages the capabilities of OpenCV for image processing.
- **Customizable**: Adjust the parameters to tweak the sketching effect to your preference.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/SketchifyMe.git
    cd SketchifyMe
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place your input image in the project directory.

2. Run the script:
    ```bash
    python img_to_sketch.py
    ```

3. The sketched image will be saved in the specified output path.

## Example

Here's an example of how to use SketchifyMe:

```python
import cv2
import os

def image_to_sketch(image_path, output_path):
    # Check if the input image exists
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' does not exist.")
        return

    img = cv2.imread(image_path)
    if img is None:
        print("Error: Could not open or find the image.")
        return

    # Converting to gray scale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Applying Gaussian blur
    blurred_img = cv2.GaussianBlur(gray_img, (21, 21), 0)
    inverted_blurred_img = cv2.bitwise_not(blurred_img)
    sketch_img = cv2.divide(gray_img, inverted_blurred_img, scale=256.0)

    # Ensure the directory exists
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the results
    success = cv2.imwrite(output_path, sketch_img)
    if success:
        print(f"Saved the sketch at {output_path}")
    else:
        print(f"Error: Could not write the image to {output_path}")

    return output_path

if __name__ == "__main__":
    input_image_path = "/path/to/your/input_image.png"
    output_image_path = "/path/to/save/sketch_image.png"
    image_to_sketch(input_image_path, output_image_path)
