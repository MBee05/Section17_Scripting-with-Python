from PIL import Image,ImageFilter

img= Image.open('./img/astro.jpg')
# print(img.size)

# (5611, 5339)

new_img=img.resize((300,200))
new_img.save('astronaute.jpg')
# when we change the size of the img then the ration changes and img not clear 
# if want to keep the ration then have to do 

# new_img=img.thumbnail((300,200))
# new_img.save('astronaute.jpg')
# output    error


img.thumbnail((400,400))
img.save('astronaute.jpg')
# output    img has the thumbnail and it keep the ration

print(img.size)
# (400, 381)

