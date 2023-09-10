#Importing Required Modules
import rembg as rb
from PIL import Image

# Store path of the image in the variable input_path
input_path = r"C:\Users\VAIO\Desktop\art\photo_2023-09-10_11-44-02.jpg"
import cv2
import numpy as np
ff=cv2.imread(input_path)
# Store path of the output image in the variable output_path
# output_path = 'E:\C programs\
# 			Remove BackGround\gfgoutput.png'

# # Processing the image
input = Image.open(input_path)

# # Removing the background from the given Image

output = rb.remove(input,bgcolor=[255,255,255,0])
output1=np.array(output)
output1=cv2.cvtColor(output1,cv2.COLOR_RGBA2BGR)
# # print(type(output1))
# output1=cv2.resize(output1,(800,600))
# #output1[np.where((output1==[0,0,0]).all(axis=2))]=[255,255,255]
# # print(output1)
cv2.imshow("nn",cv2.resize(output1,(800,600)))
cv2.waitKey()
cv2.destroyAllWindows()
# #Saving the image in the given path
# import cv2
# output.show()
#output1=cv2.cvtColor(output1,cv2.COLOR_BGR2RGB)
print(output1.shape)
cv2.imwrite(r"C:\Users\VAIO\Desktop\art\1_.jpg",output1)