# 1print() 함수의 서삭

print("안녕하세요")

print("100")  # 문자 100
print("%d" % 100)  # 숫자 100

print("100+100")
print("%d" % (100+100))

# 오류 예시

"""print("%d" % (100, 200)) -> %d 하나인데 숫자가 두 개
print("%d %d" % (100)) -> %d 두 개인데 숫자가 한 개

중간의 %는 왼쪽 서식과 오른쪽 값을 구분해주는 역할

숫자는 콤마로 구분하기"""

print("%d %d" % (100, 200))
print("%d" % (100))


# 2 print() 함수를 사용한 다양한출력

print("%d / %d = %d" % (100, 200, 0.5))
print("%d / %d = %f" % (100, 200, 0.5))  # 0.500000 뒤에 딸린 게 너무 많다. 이거 없애는 방법
print("%d / %d = %5.1f" % (100, 200, 0.5))

# 3 print() 함수를 사용한 깔끔한 출력
print("%d" % 123)
print("%5d" % 123)
print("%05d" % 123)

print("%f" % 123.45)
print("%7.1f" % 123.45)
print("%7.3f" % 123.45)

print("%s" % "Python")
print("%10s" % "Python")

# 데이터 서식 지정

print("%d %5d %05d" % (123, 123, 123))
print("{0:d} {1:5d} {2:05d}".format(123, 123, 123))
# {} 안의 0, 1, 2는 format 안의 값 중에서 0번째, 1번째, 2번째에 대응한다는 의미이다. %d에서 %를 떼고 d로 표시한다.

print("{2:d} {1:d} {0:d}".format(100, 200, 300))

print("한 행입니다. 또 한 행입니다.")
print("한 행입니다. \n또 한 행입니다.")  # \n은 이스케이프 문자 또는 서식 문자라고 한다.
print("한 행입니다. \t또 한 행입니다.")
print("한 행입니다. \b또 한 행입니다.")
print("한 행입니다. \\또 한 행입니다.")
print("한 행입니다. \'또 한 행입니다.")
print("한 행입니다. \"또 한 행입니다.")
print("한 행입니다. \n또 한 행입니다.\n그리고 또 한 행입니다.")

print("\n줄바꿈\n연습 ")
print("\t탭키\t연습")
print("글자가\"강조\"되는 효과1")
print("글자가\'강조\'되는 효과2")
print("\\\\\\ 역슬래시 세 개 출력")
print(r"\n \t \" \\를 그대로 출력")
print("\n \t \" \\를 그대로 출력")

#[프로그램 1]의 완성

print("    *    ")
print("   ***   ")
print("  *****  ")
print(" ******* ")
print("*********")
print(" ******* ")
print("  *****  ")
print("   ***   ")
print("    *    ")

#self study 3-1
print("*********")
print(" ******* ")
print("  *****  ")
print("   ***   ")
print("    *    ")
print("   ***   ")
print("  *****  ")
print(" ******* ")
print("*********")