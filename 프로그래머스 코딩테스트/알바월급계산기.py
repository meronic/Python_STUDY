# 알바 월급 계산기
import calendar
month_pay = 0

def pay_calculator(month) : 
	global month_pay
	global year

	pay = 7400
	hour = 8

	#그 월에 있는 일의 개수 구하기

	
	find_day = 13

	monthrange = calendar.monthrange(year,month) # 2020년의 6월의 일 개수를 튜플로 반환
	count_day = monthrange[1] # 그 월의 일의 개수
	day = calendar.weekday(year,month,find_day) # 그 년도 월 일의 요일 구하기

	count_t = 0
	count_f = 0
	count_s = 0

	for i in range(1,count_day+1) : 
		day = calendar.weekday(year,month,i) # 그 년도 월 일의 요일 구하기
		if day == 0 :
			day_k = '월요일'
		elif day == 1 : 
			day_k = '화요일'
		elif day == 2 : 
			day_k = '수요일'
		elif day == 3 : 
			day_k = '목요일'
			count_t += 1
			#print(month,"월 ",i,"일은",day_k,"입니다." )
		elif day == 4 : 
			day_k = '금요일'
			count_f += 1
			#print(month,"월 ",i,"일은",day_k,"입니다." )
		elif day == 5 : 
			day_k = '토요일'
			count_s += 1
			#print(month,"월 ",i,"일은",day_k,"입니다." )
		elif day == 6 : 
			pass

	print(month,"월에서 목요일은 ", count_t,"번 있습니다.")
	print(month,"월에서 금요일은 ", count_f,"번 있습니다.")
	print(month,"월에서 토요일은 ", count_s,"번 있습니다.")

	sum_count = count_t + count_f + count_s
	month_pay = sum_count*hour*pay

	print("시급 %d원 받으면서 하루 %d시간을 일할 때" %(pay, hour))
	print("%d월에 일하는 날은 총 %d번이고 한달 월급은 %d 원 입니다." %(month,sum_count,month_pay))
	return month_pay

total = 0
year = int(input("년도를 입력해주세요 : "))
m_start = int(input("몇월부터 계산할까요? : "))
m_end = int(input("몇월까지 계산할까요? : "))

#시작

print("\n%d년도 %d월부터 %d월까지의 월급을 계산합니다. \n" %(year, m_start, m_end))

for i in range(m_start,m_end+1) : 
	pay_calculator(i)
	total += month_pay
	print("")

total_dot = format(total,',')
print("%d년도 %d월부터 %d월까지 받을 수 있는 돈은 총 [ %s ]원 입니다." %(year, m_start, m_end, total_dot))


