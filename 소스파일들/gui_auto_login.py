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

    lb_r.config(text="웹정보서비스에 접속합니다.")

    tkinter.messagebox.showinfo("알림","자동으로 로그인합니다.")
    
    driver = webdriver.Chrome()

    url = 'https://intra.wku.ac.kr'

    driver.get(url)  #대학교 웹정보 서비스 홈페이지 접속

    action = ActionChains(driver)


    driver.find_element_by_css_selector('#userid').send_keys(id_)
    driver.find_element_by_css_selector('#passwd').send_keys(pw_)
    driver.find_element_by_css_selector('#passwd').send_keys(Keys.ENTER)

    return

##def show_result(lb_r,n1,n2):
##    num1 = (n1.get())
##    num2 = (n2.get())
##    result = int(num1)+int(num2)
##    lb_r.config(text="result = %d" %result)
##    return
##    

def exitf():
    sys.exit()


n_window=Tk()
n_window.title("auto login")
n_window.geometry("250x100")

label=Label(n_window,text="웹 정보서비스 접속 프로그램").grid(row=0,column=1)

#################################################################

id_adress = StringVar()
pw_adress = StringVar()

lb1 = Label(n_window, text="ID : ").grid(row=1, column=0)
lb2 = Label(n_window, text="PW : ").grid(row=2, column=0)

lb_r= Label(n_window)

lb_r.grid(row=7,column=1)


entry_num1 = Entry(n_window,textvariable = id_adress).grid(row=1,column=1)
entry_num2 = Entry(n_window,textvariable = pw_adress, show = "*" ).grid(row=2,column=1)

show_result = partial(auto_login)

btn = Button(n_window,text="로그인", command=auto_login).grid(row=3,column=1)
bte = Button(n_window,text="종료",command=exitf).grid(row=3,column=2)

##b1=Button(text="login",command=auto_login).pack(side="left")
##b2=Button(text="exit",command=exitf).pack(side="left")



n_window.mainloop()

