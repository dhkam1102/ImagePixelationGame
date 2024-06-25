import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Load image
image_path = 'we2.jpg'
image = pygame.image.load(image_path)
image = pygame.transform.scale(image, (600, 600))  # Scale the image to a larger size for better visibility

# Set up display
window_width, window_height = 600, 600  # Larger window size
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Image Pixelation Game')

def brighten_color(color, factor=1.5):
    # Brighten the color by multiplying each RGB component by the factor
    r, g, b, *a = color  # Extract RGB, ignore alpha if present
    return (min(255, int(r * factor)), 
            min(255, int(g * factor)), 
            min(255, int(b * factor)), 
            a[0] if a else 255)  # Include alpha if present, otherwise set to 255

class Pixel:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.original_color = color
        self.children = []
        self.highlighted = False
        self.highlight_time = 0
        self.last_division_time = time.time()  # Track last division time

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def divide(self, image):
        current_time = time.time()
        if not self.children and self.radius > 2 and (current_time - self.last_division_time) > 0.2:  # Add delay of 0.5 seconds
            self.last_division_time = current_time
            new_radius = self.radius // 2
            offsets = [(-new_radius, -new_radius), (new_radius, -new_radius), 
                       (-new_radius, new_radius), (new_radius, new_radius)]
            for dx, dy in offsets:
                nx, ny = self.x + dx, self.y + dy
                if 0 <= nx < window_width and 0 <= ny < window_height:
                    color = image.get_at((nx, ny))
                    self.children.append(Pixel(nx, ny, new_radius, color))

    def update(self, mouse_pos, image):
        if (self.x - mouse_pos[0])**2 + (self.y - mouse_pos[1])**2 < self.radius**2:
            if not self.children:
                self.divide(image)
            self.highlighted = True
            self.highlight_time = time.time()
        else:
            if time.time() - self.highlight_time > 0.1:  # Highlight duration: 0.2 seconds
                self.highlighted = False
        
        for child in self.children:
            child.update(mouse_pos, image)

    def render(self, screen):
        if self.highlighted:
            self.color = brighten_color(self.original_color)  # Highlight with brighter color
        else:
            self.color = self.original_color

        if not self.children:
            self.draw(screen)
        else:
            for child in self.children:
                child.render(screen)

# Initial large pixel
initial_pixel = Pixel(window_width // 2, window_height // 2, window_width // 2, (255, 0, 0))  # Start with a large red pixel

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()

    # Clear screen with black background
    screen.fill((0, 0, 0))
    
    # Update and render the pixels
    initial_pixel.update(mouse_pos, image)
    initial_pixel.render(screen)
    
    pygame.display.flip()  # Update display

pygame.quit()
sys.exit()