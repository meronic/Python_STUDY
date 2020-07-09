def fibonacci(n):
	n = int(n)
	zero = 0
	one = 1
	two = 1
	if n == 0 : 
		return 0

	elif n == 1 : 
		return one

	elif n == 2 :
		return two

	else : 
		return fibonacci(n-2) + fibonacci(n-1)

#######################################################

def factorial(n):
	if not isinstance(n, int) or n < 0 :
		return None

	if n == 1 :
		return 1;

	else : 
		return n*factorial(n-1)

##########################################################

print("fibonacci sequence searcher");
n = int(input("enter an integer : "))

for i in range(1,n+1):
	print(fibonacci(i), end =" ")





class Person:
	def __init__(self, name, age, address):
		self.hello = 'Hello People'
		self.name = name;
		self.age = age;
		self.address = address;

	def greeting(self):
		print("{0}, my name is {1}, i am {2}old, my address = {3}".format(self.hello, self.name, self.age, self.address))




seyu = Person('seyu', 26, 'hell')

seyu.greeting()



class Person2:
	def __init__(self, *args):
		self.hello = 'Hello People'
		self.name = args[0]
		self.age = args[1]
		self.address = args[2]

	def greeting(self):
		print("{0}, my name is {1}, i am {2}old, my address = {3}".format(self.hello, self.name, self.age, self.address))




seyu = Person('seyu', 26, 'hell')

seyu.greeting()
################3

class Person3:
	def __init__(self, name, age, address, wallet):
		self.hello = 'Hello world';
		self.name = name;
		self.age = age;
		self.address = address;
		self.__wallet = wallet;


	def pay(self, amount):
		self.__wallet -= amount

		print("The remaining money is {} won".format(self.__wallet))

	def greeting(self):
		print(self.hello)


seyu = Person('seyu', 26, 'suncheon seomyeon', 30000)


seyu.greeting();

seyu.pay(2345);

print(seyu.name)
print(seyu.age)
print(seyu.address)
print(seyu.__wallet)



class Knight:
	def __init__(self, **kwargs):
		self.health = kwargs['health']
		self.mana = kwargs['mana']
		self.armor = kwargs['armor']

	def slash(self):
		print("베기!!!!!")



class Annie:
	def __init__(self, **kwargs):
		self.hello = 'hi my name is Annie'
		self.health = kwargs['health']
		self.mana = kwargs['mana']
		self.armor = kwargs['armor']
		self.level = kwargs['level']
		self.ap = kwargs['ap']
		self.ad = kwargs['ad']

	def tibber(self):
		print("Summon Tibber!!!!")
		self.demage = (self.ap)*(0.65) + (400)
		print(self.demage)

	def greeting(self):
		print(self.hello)




x = Annie(health = 300, mana = 500, level = 18, armor = 30, ap = 300, ad = 30)


x.greeting();

x.tibber();

################3

class Person:
	''' 가방이랑 가방에 넣는 기능입니다.'''
	def __init__(self):
		self.bag = []

	def put_bag(self, stuff):
		self.bag.append(stuff)




seyu = Person();
sujin = Person();

sujin.put_bag('money')

seyu.put_bag('key')

print(seyu.bag)

print(sujin.bag)


########################################################
class Person:
	count =0

'''캐릭터 생성 갯수 카운팅 클래스 '''
	def __init__(self):
		Person.count += 1



	@classmethod
	def print_count(cls):
		print("{}명 생성되었습니다.".format(cls.count))





x = Person()
y = Person()
z = Person()
i = Person()

Person.print_count()



######################################3

class Person:

	def __init__(self):
		pass

	def greeting(self):
		print('안녕하세요?')



class Student(Person):

	def greeting(self):
		super().greeting() ## method overriding function.
		## 원래 기능을 유지하면서 새로운 기능을 덧 붙일때 사용.
		print("i am going to ignore you.")





a = Student()

a.greeting();

#########################





###피보나치 동적 
import time
start = time.time()

cache = [0 for i in range(100001)]
cache[1] = 1

for i in range(2, 100001) : 
	cache[i] = cache[i-1] + cache[i-2]


first = 2 

while True : 

	result = str(cache[first])
	if len(result) == 1000 : 
		print(result)
		print("length : ",len(result))
		print(first)
		break

	first += 1


print(time.time() - start)

