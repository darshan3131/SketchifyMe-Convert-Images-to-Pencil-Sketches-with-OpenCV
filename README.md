# SketchifyMe - Convert Images to Pencil Sketches with OpenCV ✏️

![Before and After](example/before-after.jpg)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-green?logo=opencv)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**SketchifyMe** is a lightweight, easy-to-use Python application that transforms any photo into a stunning **hand-drawn pencil sketch** using **OpenCV**. Ideal for digital artists, photographers, beginners learning computer vision, or anyone who loves artistic image effects.

## ✨ Features

- One-click conversion from photo → realistic pencil sketch
- High-quality artistic output using the classic Dodge & Burn technique
- Fully customizable blur and blending parameters
- Simple, clean, and well-commented code – perfect for learning
- No external APIs or internet required
- Cross-platform (Windows, macOS, Linux)

## 🖼️ Example Output

| Original                          | Pencil Sketch                       |
|-----------------------------------|-------------------------------------|
| ![Original](example/original.jpg) | ![Sketch](example/sketch.jpg)       |

> *Side-by-side comparison (collage)*  
> ![Before and After Collage](example/before-after.jpg)

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/SketchifyMe.git
cd SketchifyMe
```

### 2. Install Dependencies
```bash
pip install opencv-python numpy
```

### 3. Run the Sketch Converter
```bash
python img_to_sketch.py --input your_photo.jpg --output output/sketch.jpg
```

#### Optional Command-Line Arguments
```bash
--input   Path to input image (required)
--output  Path to save sketch (default: output/sketch.jpg)
--blur    Gaussian blur kernel size (default: 21)
--scale   Division scale factor (default: 256.0)
```

## 💻 Core Transformation (How It Works)

```python
grey     = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred  = cv2.GaussianBlur(grey, (21, 21), 0)
inverted = cv2.bitwise_not(blurred)
sketch   = cv2.divide(grey, inverted, scale=256.0)
```

This classic technique blends a blurred inverted grayscale image with the original grayscale to simulate pencil shading.

## 📁 Project Structure

```
SketchifyMe/
├── img_to_sketch.py          # Main script (with argparse support)
├── example/
│   ├── original.jpg
│   ├── sketch.jpg
│   └── before-after.jpg      # Optional collage
├── output/                   # Generated sketches are saved here
├── requirements.txt
└── README.md
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to:
- Report bugs or suggest enhancements
- Submit pull requests (e.g., GUI version, batch processing, additional filters)

## ⭐ Show Your Support

If this project was useful to you, please give it a star ⭐ — it motivates further development!

## 📄 License

Released under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---
Transform your photos into art with just one command. Enjoy sketching! ✏️
