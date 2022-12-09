from PIL import Image
cat_img = Image.open(r'C:\Users\czx\Desktop\photo\1111.png')
face_crop_img = cat_img.crop((1600, 160, 1750, 350))
face_crop_img.save( r'C:\Users\czx\Desktop\photo\3333.png')
