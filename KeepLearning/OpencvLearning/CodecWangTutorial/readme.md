# OpenCV学习记录

跟随CodecWang的教程进行学习

https://codec.wang/docs/opencv/

### 2023.9.16

完成基础篇01-03

### 2023.9.17

完成基础篇04-06

1. 图像操作

   ```python
   px=imge[100,90]
   # 获取某一通道,x=0,1,2(b,r,g)
   px_c=img[100,90,x]

   # 截取
   face=img[100:200,115:188]

   ```
2. 颜色追踪

   ```python
       # 1.捕获视频中的一帧
       ret, frame = capture.read()

       # 2.从 BGR 转换到 HSV
       hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

       # 3.inRange()：介于 lower/upper 之间的为白色，其余黑色
       mask = cv2.inRange(hsv, lower_blue, upper_blue)

       # 4.只保留原图中的蓝色部分
       res = cv2.bitwise_and(frame, frame, mask=mask)
   ```
3. 阈值分割

   ```python
   # 固定阈值
   ret, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

   # 自适应阈值
   th2 = cv2.adaptiveThreshold(
       img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)
   th3 = cv2.adaptiveThreshold(
       img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 17, 6)

   # Otsu 阈值法
   ret2,th2=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

   # 先进行高斯滤波，再使用 Otsu 阈值法
   blur = cv2.GaussianBlur(img, (5, 5), 0)
   ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
   ```
