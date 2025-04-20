import tkinter
import tkinter.font

# tkinter 기본문 작성
root = tkinter.Tk()
root.title("연습용용")
root.geometry("400x300")

# 좌표 인식 & 출력 위치
def mouseMove(event):
    x = event.x
    y = event.y
    lavelMouse.config(text=str(x)+","+str(y))
    lavelMouse.place(x=0, y=270)

lavelMouse = tkinter.Label(root, text=",", font=('맑은 고딕',10))


lavel1 = tkinter.Label(root, text="으악", font=('맑은 고딕',10))

entry1 = tkinter.Entry(width=10)
entry1.place(x=130, y=26)

# 좌표 출력
root.bind("<Motion>", mouseMove)

root.mainloop()