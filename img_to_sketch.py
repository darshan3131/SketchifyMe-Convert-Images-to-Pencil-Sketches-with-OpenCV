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
    input_image_path = "#path"
    output_image_path = "#path"
    image_to_sketch(input_image_path, output_image_path)