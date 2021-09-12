# 변수
first_name = 'earl'
last_name = 'gray'

print(first_name + last_name + '2')

# 리스트
a_list = ['사과', '감', '배']
b_list = ['영희', '철수', ['사과', '감']]

print(b_list[2][0])

a_list.append('수박')

print(a_list)

# 딕셔너리
a_dict = {'name': 'bob', 'age': 24}

a_dict['fruits'] = a_list

print(a_dict)

# 조건문
age = 24

if age > 20:
    print('성인입니다')
else:
    print('청소년입니다.')

# 반복문
fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']

people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for fruit in fruits:
    print(fruit)

for person in people:
    print(person['name'])

# Split

myemail = "sparta@naver.com"

result = myemail.split('@')

print(result[0])

# replace

result = myemail.replace('naver', 'gmail')

print(result)

name = 1
