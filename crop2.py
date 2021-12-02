import cv2

img = cv2.imread("")

roi = cv2.selectROI(img)

img_cropped = img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

cv2.imshow("Cropped", img_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
