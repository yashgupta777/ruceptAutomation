# author: Adrian Rosebrock
# date: 14 January 2014
# website: http://www.pyimagesearch.com

# import the necessary packages
import sys

# sys.path.append('/usr/local/lib/python2.7/dist-packages')

import cv2

import numpy as np
from matplotlib import pyplot as plt

print ("For Original Image, Press 1")
print ("For Resized Image, Press 2")
print ("For Rotated Image, Press 3")
print ("For Cropped Image, Press 4")
print ("For Cropped Image, Press 4")
print ("For Cropped Image, Press 4")
print ("For Cropped Image, Press 4")
print ("For Smoothing/Noise Reduction, Press 9")

# load the image and show it
image = cv2.imread("images/jurassic-park-tour-jeep.jpg", cv2.IMREAD_UNCHANGED)
image1 = cv2.imread("images/jurassic-park-tour-jeep-1.jpg", cv2.IMREAD_UNCHANGED)

# grab the dimensions of the image and calculate the center
# of the image
(h, w) = image.shape[:2]
center = (w / 2, h / 2)
print ("shape", image.shape)
print ("center", center)

while True:
    choice = int((input("choice ")))
    
    if choice == 1:
        cv2.imshow("original", image)
        cv2.waitKey(0)
        
        # print the dimensions of the image
        print image.shape
    
    # perform the actual resizing of the image and show it
    if choice == 2:
        # we need to keep in mind aspect ratio so the image does
        # not look skewed or distorted -- therefore, we calculate
        # the ratio of the new image to the old image
        r = 100.0 / image.shape[1]
        dim = np.array((100, int(image.shape[0] * r)))
        
        # current = np.zeros((frameHeight, frameWidth, 3), np.uint8)
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
        cv2.imshow("resized", resized)
        cv2.waitKey(0)
        
        # print the dimensions of the image
        print resized.shape
    
    if choice == 3:
        # rotate the image by 180 degrees
        M = cv2.getRotationMatrix2D(center, 180, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h))
        cv2.imshow("rotated", rotated)
        cv2.waitKey(0)
        
        # print the dimensions of the image
        print rotated.shape
    
    if choice == 4:
        # crop the image using array slices -- it's a NumPy array
        # after all!
        cropped = image[70:170, 440:540]
        cv2.imshow("cropped", cropped)
        cv2.waitKey(0)
        
        # print the dimensions of the image
        print cropped.shape
        
        # # write the cropped image to disk in PNG format
        cv2.imwrite("thumbnail.png", cropped)
    
    if choice == 5:
        height, width, depth = image.shape
        circle_img = np.zeros((height, width), np.uint8)
        cv2.circle(circle_img, (width / 2, height / 2), 180, 1, thickness=-1)
        
        masked_data = cv2.bitwise_and(image, image, mask=circle_img)
        
        cv2.imshow("masked", masked_data)
        cv2.waitKey(0)
    
    if choice == 6:
        res = image + image1
        
        cv2.imshow("addition", res)
        cv2.waitKey(0)
        
        # print the dimensions of the image
        print res.shape
        
        x = np.uint8([250])
        y = np.uint8([10])
        
        print cv2.add(x, y)  # 250+10 = 260 => 255
        # [[255]]
        
        print x
        print y
        print x + y
    
    # if choice == "blend":
    
    if choice == 7:
        edges = cv2.Canny(image, 100, 200)
    
        plt.subplot(121), plt.imshow(image, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    
        plt.show()
        
    if choice == 8:
        BLUE = [255, 0, 0]
    
        img1 = image
    
        replicate = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
        reflect = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT)
        reflect101 = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
        wrap = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_WRAP)
        constant = cv2.copyMakeBorder(img1, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)
    
        plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
        plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
        plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
        plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
        plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
        plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
    
        plt.show()
        
    if choice == 9:
        img = image
    
        kernel = np.ones((5, 5), np.float32) / 25
        dst = cv2.filter2D(img, -1, kernel)

        edges = cv2.Canny(dst, 100, 200)

        plt.subplot(121), plt.imshow(image, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

        plt.show()
    
        # plt.subplot(121), plt.imshow(img), plt.title('Original')
        # plt.xticks([]), plt.yticks([])
        # plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
        # plt.xticks([]), plt.yticks([])
        # plt.show()
    
    
    
    if choice > 10:
        break
    
    cv2.destroyAllWindows()
