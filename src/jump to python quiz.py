def q1() : 
	a = 'a:b:c:d'

	b = a.split(':')

	c = '#'.join(b)

	print(c, type(c))


def q2() :

	a = {'A':90, 'B':80}

	a['C'] = 70

	print(a)
	print(a['C'])


def q4() :
	a = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
	b = []
	sum = 0

	for i in range(len(a)) : 

		if a[i] >= 50 :
			sum += a[i]
			b.append(a[i])





	print('scores of over 50 : ', b)
	print('sum of over 50 scores : ', sum)

def q5() :
	number = int(input("enter an inter : "))

	def fibonnaci(number) : 

		if number < 1 : 
			return 0

		elif number == 1 : 
			return 1

		elif number == 2: 
			return 1

		else : 
			return fibonnaci(number-2) + fibonnaci(number-1)

	for i in range(number) :
		print(fibonnaci(i), end = ' ')


def q6() : 
	numbers = list(map(int, input("enter an integer : ").split(',')))
	sum = 0
	for i in range(len(numbers)) : 
		sum += numbers[i]

	print(numbers, "is total scores : ", sum)



def q7() : 
	number = int(input("enter an integer by Multiplication table : "))
	print('%d Multiplication is : '%(number), end = '')
	for i in range(1,10) :
		print(number*i, end=' ')



def q9() :
	with open('sample.txt', 'r') as file : 
		lines = file.readlines()

		

	sum = 0

	for i in range(len(lines)) : 
		lines[i] = int(lines[i])
		sum += lines[i]


	with open('result.txt', 'w') as f :
		f.write(str(sum))


def q10() : 
	class Calculater : 
		def __init__(self, numbers) : 
			self.numbers = numbers

		def sum(self) : 
			result = 0
			for i in range(len(self.numbers)) : 
				result += int(self.numbers[i])

			return result

		def avg(self) : 
			result = self.sum()

			return result/len(self.numbers) 

	cal1 = Calculater([1,2,3,4,5])

	print(cal1.sum())
	print(cal1.avg())

	cal2 = Calculater([6,7,8,9,10])

	print(cal2.sum())
	print(cal2.avg())




def q13() : 

	numbers = list(map(int, input("enter an integer : ")))

	for i in range(len(numbers)) :

		if numbers[i-1] % 2 == 0 and numbers[i] % 2 != 0 :
			print(numbers[i], end = '')
		if numbers[i-1] % 2 != 0 and numbers[i] % 2 == 0 :
			print(numbers[i], end = '')
		if numbers[i-1] % 2 == 0 and numbers[i] % 2 == 0 :
			print('*' + str(numbers[i]), end = '')
		if numbers[i-1] % 2 != 0 and numbers[i] % 2 != 0 :
			print('-' + str(numbers[i]), end = '')





