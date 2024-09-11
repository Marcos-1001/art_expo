from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import sys

from PIL import Image

def increase_dpi(input_image_path, output_image_path, new_dpi):
    # Open the image file
    img = Image.open(input_image_path)
    
    # Save the image with the new DPI
    img.save(output_image_path, dpi=(new_dpi, new_dpi))
    print(f"DPI increased to {new_dpi} and saved to {output_image_path}")



def image_to_pdf(image_path, pdf_path, dpi=300, padding=10):
    # Open the image file
    with Image.open(image_path) as img:
        # Get image dimensions
        width, height = img.size

        # Calculate the size in points (1 point = 1/72 inch)
        # High DPI setting: 1 inch = 300 points
        width_in_points = (width / dpi) * 72
        height_in_points = (height / dpi) * 72

        # Add padding
        padding_in_points = padding * 7200 //2 / dpi
        pdf_width = width_in_points + 2 * padding_in_points
        pdf_height = height_in_points + 2 * padding_in_points

        # Create a PDF canvas
        c = canvas.Canvas(pdf_path, pagesize=(pdf_width, pdf_height))

        # Draw the image on the canvas with padding
        c.drawImage(image_path, padding_in_points, padding_in_points, width_in_points, height_in_points)

        # Save the PDF file
        c.save()

if __name__ == "__main__":

    # Example usage
    input_image_path = "l_system.png"
    output_image_path = "l_system_dpi.jpg"
    new_dpi = 300

    increase_dpi(input_image_path, output_image_path, new_dpi)


