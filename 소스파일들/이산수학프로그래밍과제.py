from tkinter import *
from tkinter import ttk

root = Tk()
root.title("이산수학 과제 프로그램")
root.geometry('300x320')
root.resizable(False, False)

#######클릭했을때 함수 실행##################

def click() : 
	# strs = entry1.get()
	# cl = int(strs)
	# cl2 = strs2.get()
	# result_label.configure(text = "your age : " + str(cl) + "\n" + "your gen : " + cl2)
	# print(cl, type(cl))
	# print(strs, type(strs))


	result = 0

	strs = entry1.get()

	#other_number = [2,3,4,5,6,7,8,9]

	n = strs

	if n.count('.') == 0 :
		n_list = str(n)

		for i, digit in enumerate(n_list) : 
			result += int(digit)*pow(2, len(n_list)-1-i)

		
		result_label.configure(text = "result : " + str(result))
		return 0

	elif n.count('.') == 1 : 
		n_list = str(n).split(".")

		front_list = n_list[0]
		point_list = n_list[1]

		for i, digit in enumerate(front_list) : 
			result += int(digit)*pow(2,len(front_list)-1-i)

		for i, digit in enumerate(point_list) : 
			result += int(digit)*pow(2,-(i+1))


		result_label.configure(text = "result : " + str(result))
		return 0


	else : 

		return "2진수가 아닙니다."


##################################################################

def set_input(event) : 
	entry1.delete(0,20)

######변수 저장#####################################
strs = StringVar()
strs2 = StringVar()
###################################################
lbl = Label(root, text = "진법 변환 프로그램", pady = 8)
lbl.grid(row = 0, column = 0)

lbtext = Label(root, text = "임의의 2진수를 입력받아 지정한 진수로 변환하며\n실수범위도 변환 가능합니다.", justify = "left", relief = "ridge", padx = 3, pady = 5)
lbtext.grid(row = 1, column = 0)

#맨 위 프레임###############################################

first_frame = ttk.LabelFrame(root, text = "2진수를 입력해주세요.")
first_frame.grid(row = 2, column = 0, padx = 15, pady = 10)

# combx1 = ttk.Combobox(first_frame, textvariable = strs, width = 7)
# combx1['value'] = ('16진법', '10진법', '8진법', '2진법')
# combx1.current(1)
# combx1.grid(row = 1, column = 0, padx = 5, pady = 10)

entry1 = Entry(first_frame, width = 35)
entry1.insert(0,"변환할 숫자를 입력해주세요.")
entry1.bind("<Button-1>", set_input)
entry1.grid(row = 1, column = 0, padx = 10, pady = 10)


#두번째 프레임###############################################

second_frame = ttk.LabelFrame(root, text = "Second Frame" , relief = 'ridge')
second_frame.grid(row = 3, column = 0, padx = 15, pady = 0)

combx2 = ttk.Combobox(second_frame, textvariable = strs2, width = 7)
combx2['value'] = ('16진법', '10진법', '8진법', '2진법')
combx2.current(3)
combx2.grid(row = 1, column = 0, padx = 15, pady = 10)

lbl2 = Label(second_frame, text = "으로")
lbl2.grid(row = 1, column = 1, padx = 0)

btn = Button(second_frame, text = "변환", command = click, width = 15, height = 1)
btn.grid(row = 1, column = 2, padx = 10)

#결과 프레임###############################################

result_frame = ttk.LabelFrame(root, text = "Result Frame")
result_frame.grid(row = 4, column = 0, padx = 10)

result_label = Label(result_frame, text = "imformation", font = "NanumGothic 11")
result_label.grid(row = 5, column = 1, padx = 50, pady = 10)

#인적사항###############################################

lbInfo = Label(root, text = "20162908 유명현")
lbInfo.grid(row = 7, column = 0)




################################################
################################################
################################################
root.mainloop()