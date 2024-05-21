import os
from pdf2image import convert_from_path

def process_pdf(pdf_path):
    # Path to pdftoppm (update this path to your local installation)
    poppler_path = r"D:\\Programs\\poppler-24.02.0\\Library\\bin"

    # Add poppler_path to system PATH for the duration of this function
    os.environ["PATH"] += os.pathsep + poppler_path

    # Convert PDF to images
    images = convert_from_path(pdf_path)
    image_folder = os.path.join(os.path.dirname(pdf_path), 'images')
    os.makedirs(image_folder, exist_ok=True)

    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(image_folder, f"{os.path.basename(pdf_path).replace('.pdf', '')}_{i+1}.png")
        image.save(image_path, 'PNG')
        image_paths.append(image_path)

    return image_paths
