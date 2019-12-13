from PIL import  Image,ImageFilter

im=Image.open('kk.jpg')
im2=im.filter(ImageFilter.EMBOSS)
im2.save('4.jpg','jpeg')