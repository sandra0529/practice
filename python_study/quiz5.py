#Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
#50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

#조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
#조건2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

#(출력문 예제)
#[0] 1번째 손님 (소요시간 : 15분)
#[ ] 2번째 손님 (소요시간: 50분)
#[0] 3번째 손님 (소요시간: 5분)
#...
#[0] 50번째 손님 (소요시간: 16분)

#총 탑승 승객 : 2분

# from random import *
# number = 0 #탑승 승객
# for i in range(1, 51):
#     time = randrange(5,51)
#     if 5<= time <=15:
#         number += 1
#         print("[0]{0}번째 손님(소요시간:{1}분)".format(i,time))
#     else:
#         print("[ ]{0}번째 손님(소요시간:{1}분)".format(i,time))

# print("총 탑승 승객 : {0}분".format(number))

from random import sample
time = range(5,51)
time2 = sample(time,1)
print(time2)

print(round(35.2388,2)) #반올림
