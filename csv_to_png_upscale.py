'''
Script to visualize odd values in pascal's triangle.
pascal_data.csv contains odd values marked '1' and even values marked '0'.
'''
from PIL import Image

def generate_image_from_csv(csv_file, output_image):
    with open(csv_file, 'r') as file:
        lines = file.readlines()
    
    # Calculate image dimensions based on CSV dimensions
    width = len(lines[0].strip().split(',')) * 4
    height = len(lines) * 4
    
    # Create a new image
    img = Image.new('RGB', (width, height))
    pixels = img.load()
    
    # Map values to colors
    for y, line in enumerate(lines):
        values = line.strip().split(',')
        for x, value in enumerate(values):
            color = (255, 0, 0) if value == '1.00' else (0, 0, 0)  # Red for 1.00, Black otherwise
            # Fill a 4x4 block with the same color
            for i in range(4):
                for j in range(4):
                    pixels[x*4 + i, y*4 + j] = color
    
    # Save the image
    img.save(output_image)
    print(f"Image saved as {output_image}")

# Example usage
csv_file = 'pascal_data.csv'
output_image = 'output-scaled.png'
generate_image_from_csv(csv_file, output_image)
