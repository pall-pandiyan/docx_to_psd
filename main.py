from docx import Document
from PIL import Image, ImageDraw
# import psd_tools


# Step 1: Convert .docx to an image
def docx_to_image(docx_path, image_path):
    doc = Document(docx_path)
    # Create an image from the text (this is a simplified example)
    # You may need to render the text properly
    text = "\n".join([para.text for para in doc.paragraphs])
    img = Image.new("RGB", (800, 600), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    d.text((10, 10), text, fill=(0, 0, 0))
    img.save(image_path)


# Step 2: Convert image to .psd
# def image_to_psd(image_path, psd_path):
#     # Load the image
#     image = Image.open(image_path)
#     # Create a new PSD file
#     psd = psd_tools.PSDImage.new()
#     psd.append(image)
#     psd.save(psd_path)


def main():
    # Usage
    docx_to_image("sample.docx", "output_image.png")
    # image_to_psd("output_image.png", "output_file.psd")


if __name__ == "__main__":
    main()
