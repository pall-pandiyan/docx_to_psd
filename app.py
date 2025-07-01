# from docx import Document
# from PIL import Image, ImageDraw
# # import psd_tools
# # from psd_tools.api import Layer


# # Step 1: Convert .docx to an image
# def docx_to_image(docx_path, image_path):
#     doc = Document(docx_path)
#     # Create an image from the text (this is a simplified example)
#     text = "\n".join([para.text for para in doc.paragraphs])
#     img = Image.new("RGB", (800, 600), color=(255, 255, 255))
#     d = ImageDraw.Draw(img)
#     d.text((10, 10), text, fill=(0, 0, 0))
#     img.save(image_path)


# Step 2: Convert image to .psd
# def image_to_psd(image_path, psd_path):
#     # Load the image
#     image = Image.open(image_path)

#     # Create a new PSD file with the same size as the image
#     psd = psd_tools.api.psd_image.PSDImage.new(mode="RGB", size=image.size)

#     # Create a new layer from the image
#     layer = Layer.frompil(image.convert("RGBA"))  # Convert to RGBA if needed

#     # Append the layer to the PSD
#     psd.append(layer)

#     # Save the PSD file
#     psd.save(psd_path)


# Usage
# docx_to_image("file.docx", "output_image.png")
# image_to_psd("output_image.png", "output_file.psd")

from image_to_psd.processor import process_image

image_path = "output_image.png"
result = process_image(
    image_path,
    method_type=1,
    bandwidth=10,
    is_dynamic=1,
    num_colors=50,
    save_layers=True,
)
print(f"{result=}")
