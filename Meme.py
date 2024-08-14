from PIL import Image, ImageDraw, ImageFont

def create_meme(image_path, text, output_path='meme.jpg'):
    """
    Creates a meme by overlaying text on an image and saves it to a file.

    Parameters:
    - image_path: Path to the input image.
    - text: Text to overlay on the image.
    - output_path: Path where the output image will be saved.
    """
    # Open the image file
    image = Image.open(image_path)
    
    # Create an ImageDraw object
    draw = ImageDraw.Draw(image)
    
    # Load a font
    font = ImageFont.load_default()
    
    # Calculate text size and position
    text_width, text_height = draw.textsize(text, font=font)
    width, height = image.size
    position = (width // 2 - text_width // 2, height - text_height - 10)
    
    # Draw the text on the image
    draw.text(position, text, fill="white", font=font)
    
    # Save the image with the text overlay
    image.save(output_path)
    print(f"Meme created and saved to {output_path}")

if __name__ == "__main__":
    # Example usage
    image_path = 'example.jpg'  # Path to your input image
    text = 'This is a meme!'    # Text to overlay
    output_path = 'meme.jpg'    # Path to save the output image
    
    create_meme(image_path, text, output_path)
