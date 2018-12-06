from PIL import Image
import os


def convert(image_path, gray_path):
    img = Image.open(image_path).convert('L')
    img.save(os.path.join(gray_path, os.path.basename(image_path).split(".")[0] + ".jpg"))

rgb_path = "./JPEGImages"
gray_path = "./GrayImages"

for image_path in os.listdir(rgb_path):
    convert(os.path.join(rgb_path, image_path), gray_path)