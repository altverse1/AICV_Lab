import cv2

def imgdisplay(img, strr=" "):
    cv2.imshow(strr, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def imgprocess(img): 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgdisplay(img, "Original Image")
    imgdisplay(gray, "Greyed Image")

def vidprocess(vid_path):
    vid = cv2.VideoCapture(vid_path)
    while vid.isOpened():
        ret, frame = vid.read()  
        if not ret:
            break
        frame = cv2.resize(frame, (300, 300))
        cv2.imshow("Video", frame)
        if cv2.waitKey(250) & 0xFF == ord('q'):
            break
    vid.release()  
    cv2.destroyAllWindows()  

if __name__ == '__main__':
    x = int(input("Input 1 for image and 2 for video:: "))
    if x == 1:
        img_path = "imagedata\gumball.jpeg"
        image = cv2.imread(img_path)
        imgprocess(image)
    elif x == 2:
        vid_path = 'imagedata\meme.mp4'
        vidprocess(vid_path)
    else:
        print("Invalid Input")
