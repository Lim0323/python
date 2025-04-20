import tkinter
import random

root = tkinter.Tk()
root.title("캔버스 만들기")

# 좌표 인식 & 출력 위치
def mouseMove(event):
    x = event.x
    y = event.y
    lavelMouse.config(text=str(x)+","+str(y))
    lavelMouse.pack()

lavelMouse = tkinter.Label(root, text=",", font=('맑은 고딕',10))

# 좌표 출력
root.bind("<Motion>", mouseMove)

# 캔버스 생성
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

# 이미지 생성
bgimg = tkinter.PhotoImage(file= "miko.png")
canvas.create_image(400, 300, image = bgimg)

def click_btnRun():
    label1["text"] =  random.choice(["대길", "중길", "소길", "흉", "대흉"])

label1 = tkinter.Label(root, text="???", font=('맑은 고딕',30), fg="black")
label1.place(x=450, y=100,width=250,height=250)

btnRun = tkinter.Button(root, text="제비뽑기", font=('맑은 고딕',10), fg = "purple",command=click_btnRun)
btnRun.place(x=450, y=450,width=250,height=30)

root.mainloop()