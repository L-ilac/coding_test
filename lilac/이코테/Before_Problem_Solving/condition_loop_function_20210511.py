# Logical Operators of python -> and, or , not (&& || ! 안씀)

# Extra operators -> in , not in
-> 여러개의 데이터를 담는 자료형 안에 특정 값이 존재하는지 안하는지 확인하는 연산자(list, tuple, dict, string, etc.)

pass: 조건문의 값이 참이어도 아무것도 처리하고 싶지 않을 때 씀.

# 조건부 표현식 (Conditional Expression)
Ex. result = "Success" if score >= 80 else "Fail"
	  -> 조건문을 만족하면 Success 저장, 실패시 Fail 저장

    result2 = [i for i in a if i not in remove_set] 
		-> "a안에 있는 i 중에 뒤에 if 조건문을 만족하는 애들만 넣겠다!"


	# result = [표현식 + 반복분 + 조건문] 1. 반복문에 해당되는 횟수와 변수에 대하여 2. 조건문을 만족하는 변수만 3. 표현식에 대입하여 나온 값으로 리스트에 저장.

# Loop
range(시작 값, 끝 값 + 1) Ex. range(1,10) -> 1~9 까지
range(특정값) -> 0 ~ 특정값 -1

for i in range(?) 혹은 for i in DATA_SET(list, tuple, string, etc.)

# Function

def funcname(args):
	# code
	return return_value

함수를 호출하는 과정에서 파라미터의 변수를 지정해서 인자를 넘겨줄 수 있다.
Ex. add(a=8, b=2) 와 add(b=2, a=8)는 동일한 호출

함수 안에서 함수 밖의 변수 데이터를 변경해야하는 경우, 함수 안에서 global 키워드로 함수 밖의 변수를 지정하면, 해당 함수에서는 지역변수를 만들지않고, 함수 바깥에 선언된 변수를 바로 참조하게됌.