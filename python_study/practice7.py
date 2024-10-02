# 7-1 함수

def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

# 전달값과 반환값

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
    return balance + money

def withdraw (balance, money):
    if balance >= money: 
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))

def withdraw_nigth(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 1000)
#balance = withdraw(balance, 2000)
#balance = withdraw(balance, 500)
commission, balance = withdraw_nigth(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))

#7-3기본값

# 
def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
          .format(name, age, main_lang))
    
#profile("유재석", 20, "파이썬")
#profile("김태호", 25, "자바")

#같은 학교 학년 같은 반 같은 수업

#def profile(name, age=17, main_lang="파이썬"):
#    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
#          .format(name, age, main_lang))
    
#profile("유재석")
#profile("김태호")

#7-4 키워드값 
#def profile(name, age, main_lang):
#    print(name, age, main_lang)

#profile(name="유재석", main_lang="파이썬", age=20)
#profile(main_lang="자바", age=25, name="김태호")

# 7-5 가변인자 
#def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#    print(lang1, lang2, lang3, lang4, lang5)

#profile("유재석", 20, "Pyton", "Java", "C", "C++", "C#")
#profile("김태호", 25, "Kotlin", "Swift", "", "", "")

def profile(name, age, *language): #가변인자
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Pyton", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")

#7-6 지역변수와 전역변수

#gun = 10

#def checkpoint(soldiers):
#    global gun
#    gun = gun - soldiers
#    print("[함수 내]남은 총 : {0}".format(gun))

#print("전체 총 : {0}".format(gun))
#checkpoint(2)
#print("남은 총 : {0}".format(gun))

gun = 10

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내]남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun,2)
print("남은 총 : {0}".format(gun))

# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else : 
#         return height * heigth * 21

# height = 175
# gender = "여자"
# weight = round(std_weight(height/100, gender),2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))


