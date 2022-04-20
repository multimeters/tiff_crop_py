#!/usr/bin/python  
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

left_top_x=0
left_top_y=0
left_bo_x=0
left_bo_y=0
right_top_x=0
right_top_y=0
right_bo_x=0
right_bo_y=0
mymap = mpimg.imread('map.tif') # 输入文件的名字
print(mymap.shape) #(512, 512, 3)
print(mymap.shape[0])
break2=False
left_top_find_flag=False
right_top_find_flag=False
left_bo_find_flag=False
right_bo_find_flag=False

for row in range(mymap.shape[0]):
    if break2==True:
        break
    for col in range(mymap.shape[1]):
        if mymap[row][col][3] !=0 and left_top_find_flag==False:
            left_top_find_flag=True
            left_top_x=row
            left_top_y=col
            print ('左上x: %s' % left_top_x)
            print ('左上y: %s' % left_top_y)
            #break2=True
            #break
        if mymap[row][col][3]==0 and left_top_find_flag==True and right_top_find_flag==False:
            right_top_find_flag=True
            right_top_x=row
            right_top_y=col-1
            print ('右上x: %s' % right_top_x)
            print ('右上y: %s' % right_top_y)
            break2=True
            break

break2=False
for row in range(mymap.shape[0]-1,-1,-1):
    if break2==True:
        break
    for col in range(mymap.shape[1]):
        if mymap[row][col][3] !=0 and left_bo_find_flag==False:
            left_bo_find_flag=True
            left_bo_x=row
            left_bo_y=col
            print ('左下x: %s' % left_bo_x)
            print ('左下y: %s' % left_bo_y)
            #break2=True
            #break
        if mymap[row][col][3]==0 and left_bo_find_flag==True and right_bo_find_flag==False:
            right_bo_find_flag=True
            right_bo_x=row
            right_bo_y=col-1
            print ('右下x: %s' % right_bo_x)
            print ('右下y: %s' % right_bo_y)
            break2=True
            break


img = cv2.imread('map.tif')#输入文件的名字
print(img.shape)
cropped = img[left_top_x:left_bo_x,left_top_y:right_top_y]  # 裁剪坐标为[y0:y1, x0:x1]
cv2.imwrite('map2.tif', cropped)#输出文件的名字



plt.imshow(cropped) # 显示图片
plt.axis('on') # 不显示坐标轴
plt.show()
