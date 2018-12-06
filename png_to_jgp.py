from PIL import Image

def png_to_jpg(png):
    im = Image.open(png)
    rgb_im = im.convert('RGB')
    rgb_im.save(png.replace("pos","jpg").replace("png","jpg"))

if __name__ == '__main__':
    with open("Train/pos.lst") as f:
        for png_file in f.readlines():
            png_to_jpg(png_file.replace("\n",""))



