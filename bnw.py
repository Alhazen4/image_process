import cv2 as cv

init_img = cv.imread("lena.png")
cv.imshow("Original img", init_img);

gray_img = cv.cvtColor(init_img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray img", gray_img)

(thresh, bnw) = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)
cv.imshow("Black and White",bnw)

cv.waitKey(0)
cv.destroyAllWindows()