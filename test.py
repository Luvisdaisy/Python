import numpy as np
import cv2

# 打开摄像头
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()

    if not ret:
        break

    # 将图像从 BGR 转换为 HSV 颜色空间
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 定义红色、蓝色和绿色的颜色范围
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])

    # 创建颜色掩码
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    # 使用掩码提取红色、蓝色和绿色的物体
    red_res = cv2.bitwise_and(frame, frame, mask=red_mask)
    blue_res = cv2.bitwise_and(frame, frame, mask=blue_mask)
    green_res = cv2.bitwise_and(frame, frame, mask=green_mask)

    # 合并结果
    result = cv2.add(cv2.add(red_res, blue_res), green_res)

    # 显示原始帧和提取的颜色物体
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Red Objects", red_res)
    cv2.imshow("Blue Objects", blue_res)
    cv2.imshow("Green Objects", green_res)
    cv2.imshow("Result", result)

    if cv2.waitKey(1) == ord("q"):
        break

# 释放摄像头并关闭窗口
capture.release()
cv2.destroyAllWindows()
