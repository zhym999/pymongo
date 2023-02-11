import time,re
from pymongo import MongoClient



client = MongoClient('mongodb://localhost:27017/')

db_nosql= client['nosql']
col_publics=db_nosql['publics']
col_M=db_nosql['movies']
col_U=db_nosql['user']


#1
# for x1 in col_publics.find({'type':'Book'}):
#     print(x1)

# 2
# for x2 in col_publics.find( {'year':{'$gte':2011}}):
#     print(x2)
# 3
# for x3 in col_publics.find({'type':'Book','year':{'$gte':2014}}):
#     print(x3)
#4
# for x4 in col_publics.find({'authors':'Toru Ishida'}):
#     print(x4)
# 5
# for x5 in col_publics.distinct('publisher'):
#     print(x5)
# 6
# for x6 in col_publics.distinct('authors'):
#     print(x6)
# 7
# for x7 in col_publics.find({'authors':'Toru Ishida'}).sort('title' ,1):
#     print(x7)
# 8
# x8 = col_publics.count_documents({'authors':'Toru Ishida'})
# print(x8)
# 9
# x9 = col_publics.count_documents({'year':{'$gte':2011}})
# print(x9)
# for x9 in col_publics.aggregate([
#     {'$group':{
#         '_id':'$type',
#         'count':{'$sum':1}
#     }}
# ]):
#      print(x9)
# 10
# x10= col_publics.count_documents({'authors':'Toru Ishida'})
# print(x10)
# 11
# for x11 in col_publics.aggregate([
#         {'$group':{
#             '_id':'$authors',
#             'count':{'$sum':1}
#         }},
#         {'$sort':{'count':1}}
# ]):
#     print(x11)

# Q1 ,Q2
# q1=col_U.count_documents({})
# qq= col_publics.count_documents({})
# q2= col_M.count_documents({})
# print(q1,qq ,q2)

# Q3
# for q3 in col_U.aggregate([
#     {'$project':{'_id': 1 ,'name':1,'occupation':1}},
#     {'$match' : {'name':'Clifford Johnathan'}}
# ]):
#     print(q3)

# Q4
# for q4 in  col_U.find({'age':{'$gte':18,'$lte':30}}):
#     print(q4)

# Q5
# for q5 in col_U.find({'$or':[
#     {'occupation':'artis'},
#     {'occupation':'scientist'}]}):
#     print(q5)

# Q6
# for q6 in col_U.aggregate([
#     {'$limit':10},
#     {'$sort':{'age':-1}},
#     {'$match':{'gender':'F'}}
# ]):
#     print(q6)



# Q7

# for q7 in col_U.distinct('occupation'):
#     print(q7)



# Q8
# doc={
#     # "_id": 6041,
#   "name": "zhu yiming",
#   "gender": "M",
#   "age": 23,
#   "occupation": "student"
# }
# q8 = col_U.insert_one(doc)
# for x in col_U.find({"name": "zhu yiming"}):
#     print(x)


# Q9
# time=time.asctime()         #import time!!
# t= {'time':time}
# q9 =  col_M.update_one({}, {'$set':t})
# print((q9))

# Q10
# col_M.delete_one({})


# Q11
# col_U.update_many(
#     {'occupation':'programmer'},
#     {'$set':{
#         'occupation':'developer'
#     }}
# )

# Q12
#
# condition = { "$or": [
#     {'title':{'$regex':'199'}},
#     {'title':{'$regex':'198'}},
#     {'title':{'$regex':'200'}},
# ] }
# q12= col_M.count_documents(condition)
# print(q12)

# Q13
# condition = { "$or": [
#     {'title':{'$regex':'1992'}},
#     {'title':{'$regex':'1989'}},
#     {'title':{'$regex':'1988'}},
#     {'title': {'$regex': '1991'}},
#     {'title': {'$regex': '1987'}},
#     {'title': {'$regex': '1986'}},
#     {'title': {'$regex': '1990'}},
#     {'title': {'$regex': '1985'}},
#     {'title': {'$regex': '1984'}},
# ] }
# q13 = col_M.count_documents(condition)
# print(q13)

# Q14
# q14 = col_M.count_documents(
#     {'genres':{'$regex':"Thriller"}}
# )
# print(q14)

# Q15
# q15 = col_M.count_documents(
#     {'genres':{'$regex':"Musical|Romance"}}
# )
#
# print(q15)

# Q16
# n=1
# for x in col_M.aggregate([
#         {'$project':{
#             '_id':0,
#             'title':1
#         }}
# ]):
#     values = str(x.values())
#     year = values[-8:]
#     year1 = year[:4]
#     print(year1)
#     title = str(values[:-9])
#     title1 =title[14:]
#     print(title1)
#     col_M.update_one(
#         {'_id':n},
#         {'$set':{'title':title1,'year':year1}}
#     )
#     n=n+1

# Q17
# n=1
# for x in col_M.aggregate([
#         {'$project':{
#             '_id':0,
#             'genres':1
#         }}
# ]):
#     values = x.get('genres')
#     m1 = values.split('|')
#     col_M.update_one(
#              {'_id':n},
#              {'$set':{'genres':m1}})
#     n=n+1



# Q18
# for q18 in col_U.find({'movies':{ '$elemMatch': 1196 }}):
#     print(q18)

# filter_find = {'movies': {'$elemMatch': {'movieid': 1196}}}
# x = col_U.count_documents(filter_find)
# print(x)

# Q19
# filter_find1 ={'movies': {'$elemMatch':{'movieid':260,'movieid':1196,'movieid':1210}} }
# q20 = col_U.count_documents(filter_find1)
# print(q20)

# Q20
# filter={'movies':{'$size':48}}
# q21 = col_U.count_documents(filter)
# print(q21)


# Q21*****
# try:
#     i=6040
#     for x in col_U.aggregate([
#             {'$project':{
#                 '_id':0,
#                 'movies':1
#             }}
#     ]):
#         n = len(x.get('movies'))
#
#         col_U.update_one(
#                 {'_id':i},
#                 {'$set':{'num_ratings':n}}
#             )
#         i=i-1
# except:print('e')


# Q22

# try:
#     n=0
#     for rets in col_U.find().where('this.movies.length>90'):
#         n+=1
#         print(rets)
#
# except: print(n)

# Q23
# n=0
# dt = "2001-01-01"
# timeArray = time.strptime(dt, "%Y-%m-%d")
# timestamp = time.mktime(timeArray)
# for x in col_U.find({'movies.timestamp':{'$gt':timestamp}}):
#     # print(x)
#     n=n+1
#
# print(n)



# Q24
# for x in col_U.aggregate([
#     {'$match':{'name':'Jayson Brad'}},
#     {'$project':{
#         '_id':0,
#         'movies':1
#     }}
# ]):
#     q = x.get('movies')
#     q24 =q[-3:]
#     print(q24)


# Q25
# for x in col_U.find(
#         {'name':'Tracy Edward','movies.movieid':1210},
#         {'movies':{'$elemMatch':{'movieid':1210}}}
# ):
#     print(x)



# Q26
#Il manque un espace dans le titre de la question！！！！
# for x2 in col_M.aggregate([
#     {'$match':{ 'title':'Untouchables, The '}},
#     {'$project':{'_id':1}}
#
# ]):
#      id=x2.get('_id')
# n=0
# for q26 in col_U.find(
#         {'movies.movieid':id},
#         {'movies':{'$elemMatch':{'rating':5}}}
# ):
#     n=n+1
# print(n)

# Q27
# col_U.update_one(
#     {'name':'Barry Erin'},
#     {'$push':{'movies':
#          {'movieid':14,'rating':4,'timestamp':int(time.time())}}
#
#      }
# )

# Q28

# col_U.delete_one({'name':'Marquis Billie','movies.movieid':1311})

# Q29

# col_M.update_one(
#     {'title':'Cinderella '},
#     {'$set':{'genres':'Animation|Children‘s|Musical'}}
# )


