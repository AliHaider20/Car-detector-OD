import cv2

cap = cv2.VideoCapture("Traffic.mp4")
od = cv2.createBackgroundSubtractorMOG2(history=25, varThreshold=80 )


while True:
    detections = [] # Storing the coordinates of the detetion

    ret, frame = cap.read()
    if not ret:
        break 

    frame = cv2.resize(frame, (1000, 1000))
    roi = frame[350:, 95:900]
    roi_x, roi_y, _ = roi.shape

    # Object Detection
    mask = od.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    count = 0
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 400:
            x, y, w, h = cv2.boundingRect(cnt)
            detections.append([x, y, w, h, count])
            count+=1

    for i in range(len(detections)):
        x, y, w, h, count = detections[i]
        cv2.rectangle(frame, (roi_x, roi_y), (roi_x+200, roi_y+200), (0, 255, 0), 3)
        cv2.putText(roi, str(count), (x, y-15), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
        cv2.rectangle(roi, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()