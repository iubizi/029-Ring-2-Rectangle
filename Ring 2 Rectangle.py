import gc
gc.enable()

import cv2
import numpy as np

####################
# 图像显示函数
####################

def imshow(string='imshow', name=None):
    cv2.imshow(string, name)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

####################
# 圆环变长方形
####################
 
def cir2rec(img, circle_center, radius, radius_width):
    
    rec_img = np.zeros( (radius_width, int(2*radius*np.pi), 3),
                          dtype='uint8' )
    
    for row in range(0, rec_img.shape[0]):
        for col in range(0, rec_img.shape[1]):
            
            theta = np.pi*2 / rec_img.shape[1] * (col+1) # + origin_theta
            rho = radius - row - 1
            p_x = int(circle_center[0] + rho*np.sin(theta)+0.5) - 1
            p_y = int(circle_center[1] - rho*np.cos(theta)+0.5) - 1
            
            rec_img[row, col, :] = img[p_y, p_x, :]
            
    return rec_img
'''
img = cv2.imread('img.png')
cir2rec_img = cir2rec(img, (400,400), 400, 166) # 圆心，外径，边宽度
# imshow('cir2rec_img', cir2rec_img)

# 保存
cv2.imwrite('cir2rec.png', cir2rec_img)
'''


####################
# 长方形变圆环
####################

def rec2cir(img):
    
    h,w,_ = img.shape
    
    radius = w / (np.pi*2)
    cir_img = np.zeros((int(2*radius)+1, int(2*radius)+1, 3), dtype='uint8')
    circle_center = ((int(2*radius)+1)//2, (int(2*radius)+1)//2)
    
    for row in np.arange(0, img.shape[0], 0.5):
        for col in np.arange(0, img.shape[1], 0.5):
            
            rho = radius - row - 1
            theta = (col+1)*(np.pi*2) / img.shape[1] # + origin_theta
            p_x = int(circle_center[0] + rho*np.sin(theta) + 0.5)
            p_y = int(circle_center[1] - rho*np.cos(theta) - 0.5)
            cir_img[p_y, p_x, :] = img[int(row), int(col), :]

    # 采用插值方案
    # 模糊不太行
    # cir_img = cv2.blur(cir_img, (3, 3))
    
    return cir_img
 
img = cv2.imread('cir2rec.png')
rec2cir_img = rec2cir(img)
# imshow('rec2cir_img', rec2cir_img)

# 保存
cv2.imwrite('rec2cir.png', rec2cir_img)
