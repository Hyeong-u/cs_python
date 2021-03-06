n = 0 # 요일 구하기를 위해 설정된 변수 n의 값 초기화

#년도를 입력 받는다.
print ("년도를 입력하십시오. \n년도 : ", end='')
year = int(input())

#년도가 1 이상의 정수만 입력받도록 한다.
while(year < 1):
    print ("입력한 년도를 확인하십시오. 년도는 1 이상의 정수만 입력할 수 있습니다.")
    print ("년도를 입력하십시오. \n년도 : ", end='')
    year = int(input())
    
#월을 입력 받는다.
print ("월을 입력하십시오. \n월 : ", end='')
month = int(input())

#월이 1이상 12이하의 정수만 입력받도록 한다.
while(month < 1 or month > 12):
    print ("입력한 월을 확인하십시오. 월은 1과 12사이의 정수만 입력할 수 있습니다.")
    print ("월을 입력하십시오. \n월 : ", end='')
    month = int(input())


#일을 입력 받는다.
print ("일을 입력하십시오. \n일 : ", end='')
day = int(input())
#입력 받은 월에 따라 입력 받은 일의 범위를 제한한다.
if year%400 == 0 or ( year%4 == 0 and year%100 != 0):
    if month == 4 or month == 6 or month == 9 or month == 11:
        while (day < 1 or day > 30):
            print("해당 월은 1일부터 30일까지 있습니다.")
            print("일을 입력하십시오. \n일 : ", end='')
            day = int(input())
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        while (day < 1 or day > 31):
            print("해당 월은 1일부터 31일까지 있습니다.")
            print("일을 입력하십시오. \n일 : ", end='')
            day = int(input())
    elif month == 2:
        while (day < 1 or day > 29):
            print("해당 월은 1일부터 29일까지 있습니다.")
            print("일을 입력하십시오. \n일 : ", end='')
            day = int(input())
else:
    if month == 4 or month == 6 or month == 9 or month == 11:
        while (day < 1 or day > 30):
            print("해당 월은 1일부터 30일까지 있습니다.")
            print("일을 입력하십시오. \n일 : ", end='')
            day = int(input())
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        while (day < 1 or day > 31):
            print("해당 월은 1일부터 31일까지 있습니다.")
            print("일을 입력하십시오. \n일 : ", end='')
            day = int(input())
    elif month == 2:
        while (day < 1 or day > 28):
            print("해당 월은 1일부터 28일까지 있습니다.")
            print("일을 입력하십시오. \n일 : ", end='')
            day = int(input())

#for문을 이용하여 윤년은 366일을 평년은 365일을 더한다. [1, 2, ..., year-1]
for i in range(1, year):
    if i%400 == 0 or ( i%4 == 0 and i%100 != 0):
        n = n + 366
    else:
        n = n + 365

   
#for문을 이용하여 입력받은 월의 전월까지의 일수를 더한다. [1, 2, ..., month-1]
Month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
LeapMonth = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
if year%400 == 0 or ( year%4 == 0 and year%100 != 0):
    for i in range(1, month):
        n += Leapmonth[i]
else:
    for i in range(1, month):
        n += Month[i]

#최종적으로 입력받은 일수를 더한다.
n = n + day


#if문을 이용하여 나머지에 따라 요일을 결정해서 출력한다.
dayofweek = ['일', '월', '화', '수', '목', '금', '토']
print("%d년 %d월 %d일은 %s요일입니다."%(year, month, day, dayofweek[n%7]))

