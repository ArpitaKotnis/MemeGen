from PIL import Image, ImageDraw, ImageFont

def create_meme(image_path, text, output_path='meme.jpg'):
   
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    text_width, text_height = draw.textsize(text, font=font)
    width, height = image.size
    position = (width // 2 - text_width // 2, height - text_height - 10)
    draw.text(position, text, fill="white", font=font)
    
   
    image.save(output_path)
    print(f"Meme created and saved to {output_path}")

if __name__ == "__main__":
    # Example usage
    image_path = 'example.jpg'  # Path to your input image
    text = 'This is a meme!'    # Text to overlay
    output_path = 'meme.jpg'    # Path to save the output image
    
    create_meme(image_path, text, output_path)
