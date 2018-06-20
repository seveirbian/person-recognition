# Recognition Client
# 
# @Author: Bian
# @Abstract: Recognition Client gets pictures from Camera Server, 
# detects them and hightlights the detected persons.
# @Date: 2018.06.20

from darkflow.net.build import TFNet
import cv2
from io import BytesIO
import time
import requests
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import numpy as np
import sys

def recognition():
    global server_addr
    global pic_num

    r = requests.get("http://"+server_addr+"/image.jpg")
    curr_img = Image.open(BytesIO(r.content))
    curr_img_cv2 = cv2.cvtColor(np.array(curr_img), cv2.COLOR_RGB2BGR)

    result = tfnet.return_predict(curr_img_cv2)
    print(result)
    curr_img.save('darkflow/recognitions/face%i.jpg' %pic_num)
    print('running again')
    pic_name = 'darkflow/recognitions/face%i.jpg' %pic_num
    pic_num += 1
    draw(pic_name, result)
    return pic_name
    

def draw(pic_name, result):
    curr_img = Image.open(pic_name).convert('RGB')

    draw = ImageDraw.Draw(curr_img)
    for det in result:
        if det['label'] == 'person':
            draw.rectangle([det['topleft']['x'], det['topleft']['y'], 
                        det['bottomright']['x'], det['bottomright']['y']],
                       outline=(255, 0, 0))
            draw.text([det['topleft']['x'], det['topleft']['y'] - 13], det['label'], fill=(255, 255, 255))
    
    curr_img.save(pic_name)


def window():
    global label
    
    main_window = tk.Tk()

    width = 300
    height = 200

    main_window.title("Face recognition")
    main_window.resizable(False, False)
    
    open_jpg = Image.open('darkflow/recognitions/face0.jpg')
    bm0 = ImageTk.PhotoImage(image=open_jpg)
    label = tk.Label(main_window, image=bm0)
    label.pack(fill='both')

    def changeImage():
        global pic_name, open_jpg, bm, label
        # get the recognition result
        pic_name = recognition()

        open_jpg = Image.open(pic_name)
        bm = ImageTk.PhotoImage(image=open_jpg)
        label.configure(image=bm)
        label.after(100, changeImage)

    label.after(100, changeImage)
    main_window.mainloop()
        

if __name__ == "__main__":
    # import model and load weights
    global server_addr
    global pic_num
    pic_num = 0

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("you should only input on argv: server_addr,\nlike: 192.168.1.1:5000\n")
        sys.exit()
    server_addr = sys.argv[1]

    options = {"model": "darkflow/cfg/tiny-yolo-voc.cfg", "load": "darkflow/bin/tiny-yolo-voc.weights", "threshold": 0.1}
    tfnet = TFNet(options)

    window()
