import img2pdf
from PIL import Image
import os


def imgs_to_pdf(img_path_list, output_path):
    with open(output_path, "wb") as f:
        f.write(img2pdf.convert(img_path_list))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    img_path_list = ['./imgs/1.jpg', './imgs/2.jpg']
    output_path = 'out.pdf'
    imgs_to_pdf(img_path_list, output_path)

