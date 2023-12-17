import cv2
import numpy as np 

img1= cv2.imread('imagedata/1bit1.png')
img2= cv2.imread('imagedata/1bit2.png')

op_and = cv2.bitwise_and(img1, img2)
op_or = cv2.bitwise_or(img1, img2)
op_not = cv2.bitwise_not(img1)
op_xor = cv2.bitwise_xor(img1, img2)


cv2.imshow("Origin 1", img1)
cv2.imshow("Origin 2", img2)
cv2.imshow("AND", op_and)
cv2.imshow("NOT", op_not)
cv2.imshow("OR", op_or)
cv2.imshow("XOR", op_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()
