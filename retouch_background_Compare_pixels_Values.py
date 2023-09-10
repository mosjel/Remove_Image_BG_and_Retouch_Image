#Importing Required Modules
from rembg import remove
from PIL import Image

# Store path of the image in the variable input_path
input_path = r"C:\Users\VAIO\Desktop\art\IMG_5459.jpg"
import cv2
import numpy as np
ff=cv2.imread(input_path)
print(type (ff))
# Store path of the output image in the variable output_path
# output_path = 'E:\C programs\
# 			Remove BackGround\gfgoutput.png'

# # Processing the image
input = Image.open(input_path)

# # Removing the background from the given Image

output = remove(input)
input=np.array(input)
output1=np.array(output)
output1=cv2.cvtColor(output1,cv2.COLOR_RGBA2BGR)
input=cv2.cvtColor(input,cv2.COLOR_RGBA2BGR)
# print(type(output1))
output1=cv2.resize(output1,(800,600))
input=cv2.resize(input,(800,600))
output1[np.where((output1=!input).all(axis=2))]=[255,255,255]
# print(output1)
cv2.imshow("nn",output1)
cv2.waitKey()
cv2.destroyAllWindows()
# #Saving the image in the given path
# import cv2
# output.show()
output1=cv2.cvtColor(output1,cv2.COLOR_BGR2RGB)
output1=Image.fromarray(output1)
output1.save(r"C:\Users\VAIO\Desktop\art\1.jpg")