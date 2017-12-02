from pymongo import MongoClient


def get_db():
    client = MongoClient('localhost:27017')
    db = client.FoodYummy
    return db

def add_user(table, uid,name, passward):
    table.insert_one({"uid":uid, 
                                "name" : name,
                                "pw":passward})

def add_users(table, info):
    table.insert_many(info)

def get_userByName(table, name):
    return table.find_one({"name":name})

def get_userById(table,uid):
    return table.find_one({"uid":uid})

def add_index(table, index):
    return table.create_index([(index, 1)], unique=True),

def add_friends(table, uid, fuid):
    user = get_userById(table,uid)
    friend = get_userById(table,fuid)
    user["friends"].append(friend)
    table.save(user)

if __name__ == "__main__":

    db = get_db()
    table = db.recipes
    add_index(table,"uid")
    bulk = []
    print (table.index_information())
    bulk.append({"rid": 1, "uid":12,"name":"chicken sandwich", "des":"good taste","time":"", "score":5,"prl":"","f1":"USA","f2":"chicken","f3":"meal"})
    bulk.append({"rid": 2, "uid":11,"name":"fried fish", "des":"good taste!!","time":"", "score":1,"prl":"","f1":"USA","f2":"fish","f3":"meal"})
    bulk.append({"rid": 3, "uid":13,"name":"sushi", "des":"good tastetoo!","time":"", "score":2,"prl":"","f1":"USA","f2":"rice","f3":"meal"})
    bulk.append({"rid": 4, "uid":8,"name":"beef soup", "des":"good sdsataste","time":"", "score":3,"prl":"","f1":"USA","f2":"beef","f3":"meal"})
    bulk.append({"rid": 5, "uid":7,"name":"ice cream", "des":"good taste now!","time":"", "score":5,"prl":"","f1":"USA","f2":"milk","f3":"dessert"})
    
    
    add_users(table,bulk)


