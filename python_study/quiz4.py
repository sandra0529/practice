# from random import *

# first = randint[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(first)
# shuffle(first)
# print(first)
# print(sample,(first, 1))

# from random import *
# first = (list(range(1,21)))
# #print(first)
# #shuffle(first)
# #print(first)
# #print(sample(first,4))
# print("치킨 당첨자 :" ,sample(first,4)[0] )
# print("커피 당첨자 :" ,sample(first,4)[1:])

# from random import *
# first = (list(range(1,21)))
# print(first)
# shuffle(first)
# print(first)
# print(sample(first,3))
# print(sample(first,1))
# # print("치킨 당첨자 :" ,sample(first,4)[0] )
# # print("커피 당첨자 :" ,sample(first,4)[1:])

# import random

# # 1부터 20까지의 숫자를 랜덤으로 중복 없이 뽑기
# random_numbers = random.sample(range(1, 21), 20)

# print(random_numbers)


import random

# 1부터 20까지의 숫자를 랜덤으로 중복 없이 뽑기
numbers = list(range(1, 21))

# 1개를 먼저 뽑기
first_pick = random.choice(numbers)
print("치킨 당첨자 :", first_pick)

# 뽑은 숫자를 제외한 나머지에서 3개를 추가로 뽑기
numbers.remove(first_pick)
additional_picks = random.sample(numbers, 3)

print("커피 당첨자 :", additional_picks)

from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst,1))

from random import *
users =list(range(1,21))
print(type(users))
print(users)
shuffle(users)
print(users)
winners = sample(users, 4)
print("--당첨자 발표--")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하합니다--")