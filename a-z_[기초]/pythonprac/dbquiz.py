from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


# - (1) 영화제목 '매트릭스'의 평점을 가져오기

rating = db.movies.find_one({'title':'매트릭스'},{'id':False})
point = rating['star']
print(point)

# - (2) '매트릭스'의 평점과 같은 평점의 영화 제목들을 가져오기

list = db.movies.find({'star':point},{'id':False})
for movie in list:
    print(movie['title'])

# - (3) 매트릭스 영화의 평점을 0으로 만들기

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})






# # 저장 - 예시
# doc = {'name':'jane','age':21}
# db.users.insert_one(doc)

# # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# same_ages = list(db.users.find({'age':21},{'_id':False}))
# for person in same_ages:
#     print(person)

# 한 개 찾기 - 예시
# user = db.users.find_one({'name':'bobby'},{'_id':False})
# print(user['age'])

 # 바꾸기 - 예시
# db.users.update_one({'name':'jogn'},{'$set':{'name':'john'}})
# db.users.update_many({'name':'bobby'},{'$set':{'age':19}})

# # 지우기 - 예시
# db.users.delete_one({'name':'bobby'})

