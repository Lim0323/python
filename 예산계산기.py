import tkinter
import tkinter.font

# tkinter 기본문 작성
root = tkinter.Tk()
root.title("예산 계산기")
root.geometry("400x300")

label1 = tkinter.Label(root, text="월요일", font=('마비옛체',10))
label1.place(x=25, y=25)

label2 = tkinter.Label(root, text="다른 날", font=('마비옛체',10))
label2.place(x=25, y=77)

entry1 = tkinter.Entry(width=10)
entry1.place(x=130, y=26)

btn = tkinter.Button(root,text="계산",font=('마비옛체',10))
btn.pack()

root.mainloop()