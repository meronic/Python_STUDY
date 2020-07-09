#자체 보안 프로그램

from tkinter import*
import tkinter.messagebox
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from functools import partial
import sys



def auto_login():

    id_=(id_adress.get())
    pw_=(pw_adress.get())

    lb_r.config(text="로그인 정보를 확인합니다.")

    if (id_ == "hen3633","chobwj"):
        tkinter.messagebox.showinfo("보안1","올바른 아이디 입니다.")
        tkinter.messagebox.showinfo("보안1","비밀번호를 확인합니다.")
        
        if ( pw_ == "you1288" , "tnwls1621"):
            tkinter.messagebox.showinfo("알림","로그인 성공")
            lb_r.config(text="사용자가 확인 되었습니다.")
        else:
            tkinter.messagebox.showinfo("보안2","비밀번호가 틀립니다.")
            tkinter.messagebox.showinfo("보안2","누구냐 너 ")
            lb_r.config(text="비밀번호가 올바르지 않습니다.")

    elif (id_ != "hen3633","chobwj"):
        if (pw_ == "you1288" , "tnwls1621"):
            tkinter.messagebox.showinfo("알림","비밀번호는 맞았는데")
            tkinter.messagebox.showinfo("알림","아이디가 틀립니다.")
            tkinter.messagebox.showinfo("알림","다시 한번 입력해보세요")
            return
        
        tkinter.messagebox.showinfo("알림","아이디가 틀립니다.")
        tkinter.messagebox.showinfo("알림","로그인 실패 누구냐 너 ")    
        lb_r.config(text="침입자가 식별되었습니다")


    return


def exitf():
    sys.exit()


n_window=Tk()
n_window.title("사용자 확인 프로그램")
n_window.geometry("300x150")

title1 = Label(n_window,text="자체 보안 프로그램").grid(row=0,column=1)
title1 = Label(n_window,text="로그인 하세요").grid(row=1,column=1)


#################################################################

id_adress = StringVar()
pw_adress = StringVar()

lb1 = Label(n_window, text="ID : ").grid(row=2, column=0)
lb2 = Label(n_window, text="PW : ").grid(row=3, column=0)

lb_r= Label(n_window)

lb_r.grid(row=7,column=1)


entry_num1 = Entry(n_window,textvariable = id_adress).grid(row=2,column=1)
entry_num2 = Entry(n_window,textvariable = pw_adress, show = "*" ).grid(row=3,column=1)

show_result = partial(auto_login)

lbline=Label(n_window,text=" ").grid(row=4)

btn = Button(n_window,text="로그인", command=auto_login).grid(row=5,column=1)
bte = Button(n_window,text="종료", command=exitf).grid(row=5,column=2)


##b1=Button(text="login",command=auto_login).pack(side="left")
##b2=Button(text="exit",command=exitf).pack(side="left")



n_window.mainloop()

