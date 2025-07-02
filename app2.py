from docx2pdf import convert
import os
from pdf2image import convert_from_path
from wand.image import Image as WandImage
import os
import platform
import subprocess

def docx_to_pdf(docx_path, pdf_path):
    system = platform.system()
    print(f"Converting {docx_path} to PDF on {system}...")

    output_dir = os.path.dirname(pdf_path)

    if system == "Windows":
        from docx2pdf import convert
        convert(docx_path, output_dir)
    elif system == "Linux" or system == "Darwin":  
        cmd = [
            "libreoffice",
            "--headless",
            "--convert-to", "pdf",
            "--outdir", output_dir,
            docx_path
        ]
        subprocess.run(cmd, check=True)
    else:
        raise NotImplementedError(f"Unsupported OS: {system}")

    print(f"Saved PDF to {pdf_path}")

def pdf_to_png(pdf_path, output_prefix, dpi=200):
    print(f"Converting PDF {pdf_path} to PNG images...")
    pages = convert_from_path(pdf_path, dpi=dpi)
    png_files = []
    for i, page in enumerate(pages):
        output_path = f"{output_prefix}_page_{i + 1}.png"
        page.save(output_path, "PNG")
        png_files.append(output_path)
        print(f"Saved {output_path}")
    return png_files


def png_to_psd(png_path, psd_path):
    print(f"Converting {png_path} to PSD...")
    with WandImage(filename=png_path) as img:
        img.format = "psd"
        img.save(filename=psd_path)
    print(f"Saved PSD as {psd_path}")


def main():
    docx_path = "sample2.docx"
    pdf_path = os.path.splitext(docx_path)[0] + ".pdf"
    png_prefix = "output"

    docx_to_pdf(docx_path, pdf_path)

    png_files = pdf_to_png(pdf_path, png_prefix, dpi=300)

    for png_file in png_files:
        psd_file = os.path.splitext(png_file)[0] + ".psd"
        png_to_psd(png_file, psd_file)


if __name__ == "__main__":
    main()

