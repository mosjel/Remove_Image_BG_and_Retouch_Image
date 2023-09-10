from PIL import Image, ImageFilter,ImageEnhance
file_path=r"C:\Users\VAIO\Desktop\art\1_.jpg"
img=Image.open(file_path)
enc_img=img.filter(ImageFilter.DETAIL)
img_enh=ImageEnhance.Color(enc_img)

img_enh=img_enh.enhance(1.15)
img_enh=ImageEnhance.Brightness(img_enh)
img_enh=img_enh.enhance(1.15)
img_enh=ImageEnhance.Contrast(img_enh)
img_enh=img_enh.enhance(1.15)
img_enh.save(r"C:\Users\VAIO\Desktop\art\refined.jpg")
img_enh.show()

