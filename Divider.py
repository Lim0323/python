import tkinter
import tkinter.font

# 버튼 클릭하면 실행하는 함수
def click_btnRun():
    # 값 입력 (글자라 숫자로 변경 필요)
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    
    # 라벨 넣을 문자열
    str1 = ""+str(num1)+"을(를) "+str(num2)+"(으)로 나눈 몫은 "+str(num1//num2)+"입니다."
    str2 = ""+str(num1)+"을(를) "+str(num2)+"(으)로 나눈 나머지는 "+str(num1%num2)+"입니다."

    # 라벨 위치
    label3 = tkinter.Label(root, text=str1, font=("마비옛체",10))
    label3.place(x=25,y=125)

    label3 = tkinter.Label(root, text=str2, font=("마비옛체",10))
    label3.place(x=25,y=152)

root = tkinter.Tk()
root.title("산술연산자")
root.geometry("400x300")

label1 = tkinter.Label(root, text="나눠 지는 수", font=('마비옛체',10))
label1.place(x=25, y=25)

label2 = tkinter.Label(root, text="나누는 수", font=('마비옛체',10))
label2.place(x=35, y=77)

# 값 입력 받을 위치
entry1 = tkinter.Entry(width=10)
entry1.place(x=130, y=26)

entry2 = tkinter.Entry(width=10)
entry2.place(x=130, y=78)

btnRun = tkinter.Button(root, text="계산", font=("마비옛체",10),command=click_btnRun)
btnRun.place(x=234, y=25,width=70,height=77)

root.mainloop()