import sys
import os
from PIL import Image

#  JPG to PNG convert.py img.py create new 

# grab first and 2nd argument 
img= sys.argv[1]
output_folder= sys.argv[2]
# print(img_folder, output_folder)

# check if new folder exist if not create
# print(os.path.exists(output_folder))
# show error bcz no folders

# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# loop through the img.py and convert into png

# save to the new folder





# I created folder manually
# check if new folder exist if not create
print(os.path.exists('new'))
# # output True


# # loop through the img.py and convert into png
for filename in os.listdir(img):
    img= Image.open(f'{img}{filename}')
    img.save(f'{img}{filename}.png', 'png')
    print('all done')
    
    
    
        # redo exo 