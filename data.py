var1 = "나는 Fghiting을 공부 중입니다"
var2 = "파이썬"

var3 = var1+var2
var4 = var2+var1

str1Len = len(var1)
str2Len = len(var2)



print("두 문자열 길이의 차이는 "+str(str1Len-str2Len)+"입니다.")

var5 = var1.upper()
print(var5)

var6 = var1.lower()
print(var6)

var7 = """
간장공장공장장은 강공장장이고
된장공장공장장은 장공장장이다
"""
numThang = var7.count("장",0)

print(numThang)


