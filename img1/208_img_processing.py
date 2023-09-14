# key developer fundamentals
# Pillow help us to manipulate img in python
# 209_210


from PIL import Image,ImageFilter
                        # pillow gives us img filters
# img= Image.open('./img/pikachu.jpg')
# print(img)
# output    <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x640 at 0x26399AEF050> 



# print(img.format)       #output    JPEG
# print(img.size)           #         (640, 640)
# print(img.mode)           #          coloring is in RGB

# print(dir(img))



# filter the img
img= Image.open('./img/pikachu.jpg')
filtered_img= img.filter(ImageFilter.BLUR)
# img is blurry
# filtered_img= img.filter(ImageFilter.SMOOTH)
# img is clear, smooth
# filtered_img= img.filter(ImageFilter.SHARPEN)
# filtered_img.save('blur.png', 'png')
# it creates a new file 'blur.png'
# png support these img filter


# filtered_img= img.convert('L')
# great scale

# filtered_img.show()
# when run it display the img

# filtered_img.rotate(90)
# filtered_img.save('grey.png', 'png')
# img turn into grey

# crooked=filtered_img.rotate(90)
# crooked.save('grey.png', 'png')
# img rotate 90°


# resize=filtered_img.resize((100,100))
# resize.save('grey.png', 'png')
# img resize


# crop
box=((100,100,400,400))
region= filtered_img.crop(box)
region.save('grey.png', 'png')
# img cropped 






