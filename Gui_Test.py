import tkinter
import tkinter.font


root = tkinter.Tk()
root.title("첫 번째 윈도우")
root.geometry("800x600")

def click_btn():
    label1 = tkinter.Label(root, text="서", font=("마비옛체", 20))
    label2 = tkinter.Label(root, text="동", font=("마비옛체", 20))
    label3 = tkinter.Label(root, text="남", font=("마비옛체", 20))
    label4 = tkinter.Label(root, text="북", font=("마비옛체", 20))

    label1.place(x=250, y=200)
    label2.place(x=500, y=200)
    label3.place(x=380, y=300)
    label4.place(x=380, y=100)

    txt = entry.get()
    str1 = txt
    labeltxt= tkinter.Label(root, text=str1, font=("마비옛체", 15))
    labeltxt.place(x=250, y=350)


btn = tkinter.Button(root, text='정말누르시겠습니까?', font=("마비옛체",20), command=click_btn)
btn.place(x=180, y=500, width=400,height=50)

entry =tkinter.Entry(width=5)
entry.place(x=200, y=350)

root.mainloop()