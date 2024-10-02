python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index("n",index + 1)
print(index)

print(python.find("Java")) # 원하는 값이 없을 때는 -1
# print(python.index("Java")) # 인덱스로 찾게 되어 그 값이 없을 때는 오류로 나타낸다.
print("hi")

print(python.count("n")) #n이 총 몇 번 나오는지?