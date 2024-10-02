# #url = "http://naver.com"
# #url = "http://daum.net"
# #url = "http://google.com"
# url = "http://youtube.com"

# # my_str = url.replace("http://","") #    규칙1
# # #print(my_str)
# # my_str2 = url.replace(".com","") # 규칙1
# # #print(my_str2)

# my_str = url.replace("http://","") #    규칙1
# print(my_str)
# my_str = my_str[:my_str.index(".")] # 규칙2 my_str[0:5] -> 0~5직전까지 (0,1,2,3,4)
# print(my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는 {1}입니다." .format(url, password))










# url = "http://www.pknu.ac.kr"
# my_pw = url.replace("http://www.","")
# print(my_pw)
# my_pw2 = my_pw[:-6]
# print(my_pw2)
# password = my_pw2[:3] + str(len(my_pw2)) + str(my_pw2.count("e")) + "!"
# print("생성된 비밀번호는 : " + password + " 입니다.")


url = "http://www.pknu.ac.kr"
my_pw = url.replace("http://www.","")
print(my_pw)
my_pw = my_pw[:-6]
print(my_pw)
password = my_pw[:3] + str(len(my_pw)) + str(my_pw.count("e")) + "!"
print("생성된 비밀번호는 : " + password + " 입니다.")