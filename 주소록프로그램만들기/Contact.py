class Contact : 
	'''save data'''
	def __init__(self, name, phone_number, e_mail, addr) : 
		self.name = name
		self.phone_number = phone_number
		self.e_mail = e_mail
		self.addr = addr
		
	def print_info(self) :
		print("Name : ", self.name)
		print("Phone number : ", self.phone_number)
		print("E mail : ", self.e_mail)
		print("addr : ", self.addr)


def set_contact() : 
	name = input("name :")
	phone_number = input("phone_number :")
	e_mail = input("e_mail :")
	addr = input("address :")

	contact = Contact(name,phone_number,e_mail,addr)
	return contact

def print_menu() : 
	print("1. 연락처 입력")
	print("2. 연락처 출력")
	print("3. 연락처 삭제")
	print("4. 종료")

	menu = input("번호를 입력해주세요 :")
	return int(menu)

def print_contact(contact_list) :
	if len(contact_list) == 0 :
		print("저장된 데이터가 없습니다.")
	for contact in contact_list :
		contact.print_info()

def delete_contact(contact_list, name) : 
	for i, contact in enumerate(contact_list) : 
		if contact.name == name : 
			del contact_list[i]


## 데이터 저장 함수

def store_contact(contact_list) :
	f = open("contact_db.txt", 'wt', encoding='UTF-8')
	for contact in contact_list : 
		f.write(contact.name + '\n')
		f.write(contact.phone_number + '\n')
		f.write(contact.e_mail + '\n')
		f.write(contact.addr + '\n')
	f.close()

## 데이터를 불러들이는 함수

def load_contact(contact_list) : 
	f = open("contact_db.txt", "rt", encoding = "UTF-8")
	lines = f.readlines()
	num = len(lines)/4
	num = int(num)

	for i in range(num) : 
		name = lines[4*i].rstrip('\n')
		phone_number = lines[4*i+1].rstrip('\n')
		e_mail = lines[4*i+2].rstrip('\n')
		addr = lines[4*i+3].rstrip('\n')

		contact = Contact(name, phone_number, e_mail, addr)
		contact_list.append(contact)

	f.close()





def run() :
	contact_list = [] 
	load_contact(contact_list)
	
	while True : 
		menu = print_menu()
		if menu == 1 : 
			contact = set_contact()
			contact_list.append(contact)
		elif menu == 2 : 
			print_contact(contact_list)
		elif menu == 3 :
			print("연락처를 삭제합니다.")
			name = input("삭제할 이름을 입력해주세요 : ")
			delete_contact(contact_list, name)


		elif menu == 4 :
			store_contact(contact_list)
			break
		print()

if __name__ == '__main__':
	run()
	

