
# Image Pixelation Game

This is a simple image pixelation game built using Pygame. The game starts with a large pixelated version of an image. As the mouse moves over the image, the pixels divide into smaller pixels, gradually revealing the image. If the smallest pixels are adjacent to each other, they merge back into a square pixel.

## Features

- Image starts with a large pixelated view.
- Pixels divide into smaller pixels as the mouse moves over them.
- Highlighted pixels temporarily brighten as the mouse passes over them.
- Smallest pixels merge back into square pixels if adjacent.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ImagePixelationGame.git
   cd ImagePixelationGame
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # mac used.
   ```

3. **Install the required packages**:
   ```bash
   pip install pygame
   ```

4. **Place your image** in the project directory and rename it to `some.jpg`.

## Usage

1. **Run the game**:
   ```bash
   python main.py
   ```

2. **Interact with the game**:
   - Move your mouse over the Pygame window to divide the pixels and reveal the image.

## Code Overview

- **main.py**: The main game logic.
  - **Pixel class**: Handles the drawing, division, and merging of pixels.
  - **brighten_color function**: Temporarily brightens a color.
  - **Game loop**: Handles events, updates, and renders the pixels.

## Customization

- **Change the image**: Replace `some.jpg` with any image of your choice.
- **Adjust division speed**: Modify the delay in the `divide` method of the `Pixel` class.
- **Highlight duration**: Adjust the highlight duration in the `update` method of the `Pixel` class.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

