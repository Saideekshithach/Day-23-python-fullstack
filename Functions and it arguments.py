#keyword arguments
'''def check(id,name,mailid):
    id=10
    name="pooja"
    mailid="pooja@codegnan.com"
    print(id,name,mailid)
check(id="id",name="name",mailid="mailid")'''

'''def check1(id,name,mailid):
    print(id,name,mailid)
check1(id="id",name="name",mailid="mailid")
check1(id=20,name="ganesh",mailid="g@gmail.com")
check1(id=30,name="deekshi",mailid="s@gmail.com")
check1(40,"thoshith","t@gmail.com")
check1("pavan","p@gmail.com",50)
check1(name="manikanta",mailid="m@gmail.com",id=60)'''
'''
def check1(id,name,mailid):
    name=input()
    mailid=input()
    id=int(input())
    print(id,mailid,name)
check1(id="id",name="name",mailid="mailid")
'''
'''
def emp(name,designation,salary):
    print(name,designation,salary)
emp(name="name",designation="designation",salary="salary")
emp(name="Deekshi",designation="clerk",salary=10000)
emp("Sai","chemist",25000)
emp(designation="software developer",name="Sakshi",salary=30000)
name=input()
designation=input()
salary=int(input())
emp(name,designation,salary)'''

#default arguments
'''
def grocery(item,price):
    print("item is %s"%item)
    print("price is %.2f"%price)
grocery("sugar",100)

def grocery(item="dhal",price=200):
    print("item is %s"%item)
    print("price is %d" %price)
grocery()

def grocery(item,price=400):
    print("item is %s"%item)
    print("price is %d"%price)
grocery("ghee")

def grocery(item="bread",price=80):#non default arg follows default arguements
    print("item is %s"%item)
    print("price is %d"%price)
grocery(60)
'''
def bakery(cake,quantity,price):
    print("cake is %s"%cake)
    print("quantity is %s"%quantity)
    print("price is %d"%price)
bakery("chocolate","2kgs",800)

def bakery(cake="strawberry",quantity="1kg",price=300):
    print("cake is %s"%cake)
    print("quantity is %s"%quantity)
    print("price is %d"%price)
bakery()

def bakery(cake,quantity="3kgs",price=1000):
    print("cake is %s"%cake)
    print("quantity is %s"%quantity)
    print("price is %d"%price)
bakery("chocolate")

'''def bakery(cake="butterscortch",quantity,price)
    print("cake is %s"%cake)
    print("quantity is %s"%quantity)
    print("price is %d"%price)
bakery("2kgs",800)'''


def bakery(cake,quantity="3kgs",price=1000):
    return cake,quantity,price
print(bakery("pineapple"))


