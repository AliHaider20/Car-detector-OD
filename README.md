Detecting cars using OpenCV

Problem statement: Detecting cars using OpenCV.
Applications: Survaillance, Unlawful driving. 

Here are the steps taken for the detection.

1. Used OpenCV's MOG2 algorithm to remove background from the image.
2. Creating Region of Interest under which we need to detect the cars.
3. Created mask of ROI and applied Binary Thresholding on top of that so that to only take the white pixels.
4. Detected all the countours from the mask and considered only the ones with area above than 400 to remove the outliers.
5. Displayed the images with bounding boxes with the count.
