import tkinter
import tkinter.font

def click_btnRun():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    num3 = int(entry3.get())
    num4 = int(entry4.get())
    num5 = int(entry5.get())
    num6 = int(entry6.get())
    num7 = int(entry7.get())
    num8 = int(entry8.get())
    num9 = int(entry9.get())
    num10 = int(entry10.get())
    num11 = int(entry11.get())
    num12 = int(entry12.get())

    num1*=1800 
    num2*=1400 
    num3*=1800 
    num4*=4000 
    num5*=1500 
    num6*=2000
    num7*=500 
    num8*=900
    num9*=800 
    num10*=3500 
    num11*=700 
    num12*=1000
   

    Num1 = num1+num2+num3+num4+num5+num6
    Num2 = num7+num8+num9+num10+num11+num12
    str1 = "오늘 총 매출액은 "+str(Num1-Num2)+"원 입니다."

    label03 = tkinter.Label(root, text=str1, font=("마비옛체",10))
    label03.place(x=50,y=250)

root = tkinter.Tk()
root.title("CU")
root.geometry("670x400")

label1 = tkinter.Label(root, text="캔 커피", font=('마비옛체',10))
label1.place(x=134, y=26)
label2 = tkinter.Label(root, text="삼각김밥", font=('마비옛체',10))
label2.place(x=210, y=26)
label3 = tkinter.Label(root, text="바나나 우유", font=('마비옛체',10))
label3.place(x=282, y=26)
label4 = tkinter.Label(root, text="도시락", font=('마비옛체',10))
label4.place(x=377, y=26)
label5 = tkinter.Label(root, text="콜라", font=('마비옛체',10))
label5.place(x=460, y=26)
label6 = tkinter.Label(root, text="새우깡", font=('마비옛체',10))
label6.place(x=534, y=26)
label01 = tkinter.Label(root, text="판매 수량", font=('마비옛체',10))
label01.place(x=35, y=80)
label02 = tkinter.Label(root, text="구매 수량", font=('마비옛체',10))
label02.place(x=35, y=120)

entry1 = tkinter.Entry(width=7)
entry1.place(x=130, y=80)
entry2 = tkinter.Entry(width=7)
entry2.place(x=210, y=80)
entry3 = tkinter.Entry(width=7)
entry3.place(x=290, y=80)
entry4 = tkinter.Entry(width=7)
entry4.place(x=370, y=80)
entry5 = tkinter.Entry(width=7)
entry5.place(x=450, y=80)
entry6 = tkinter.Entry(width=7)
entry6.place(x=530, y=80)

entry7 = tkinter.Entry(width=7)
entry7.place(x=130, y=120)
entry8 = tkinter.Entry(width=7)
entry8.place(x=210, y=120)
entry9 = tkinter.Entry(width=7)
entry9.place(x=290, y=120)
entry10 = tkinter.Entry(width=7)
entry10.place(x=370, y=120)
entry11 = tkinter.Entry(width=7)
entry11.place(x=450, y=120)
entry12 = tkinter.Entry(width=7)
entry12.place(x=530, y=120)

btnRun = tkinter.Button(root, text="계산", font=("마비옛체",10),command=click_btnRun)
btnRun.place(x=110, y=200,width=450,height=30)

root.mainloop()