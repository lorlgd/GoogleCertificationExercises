import os, sys
from PIL import Image


def fix_format(folder_path):
    if not os.path.isdir(folder_path):
        return f"{folder_path} is not a valid directory. Make sure the parameter send is a folder with the images to process."
    if len(os.listdir(folder_path)) == 0:
        return f"{folder_path} is empty. Finishing execution."
    else:
        images = os.listdir(folder_path)
        for image in images:
            abs_path_image = os.path.join(folder_path, image)
            if not abs_path_image.endswith(".py"):
                im = Image.open(abs_path_image)
                # print(os.path.splitext(abs_path_image)[0])
                im.rotate(0).convert('RGB').resize((128, 128)).save(os.path.join(os.getcwd(), os.path.splitext(image)[0]), "JPEG")
            print("The images were successfully rotated to the right format.")


folder = os.path.join(os.getcwd(), "images")
print(folder)
fix_format(folder)



