

print("Hello world line - 1")
print("Hello world line - 2")

#lesson 3-4
a = "mr vasya pupkin"
b = "mrs valera"

print(a.title())
print(b.upper())
#lesson 5
a = "..//../test/..//.."
b=a.strip(".")
b=b.strip("/")

c=b.strip(".")
c=c.strip("/")
print(c)

#lesson 6
a = 2
b = 12

print(a*b)

#lesson 7

for x in range (10, 100, 2):
    print("Number X =" + " " + str(x))

z=1
while True:
    z=z+1
    print(z)
    if z==1000:
        break

#lesson 8 - 9

cities = ['New York', 'Moscow', 'new dehli', 'Toronto', 'simferopol']
print(cities[0])
for x in range(0 , len(cities), 1):
    print(cities[x])
    if cities[x] == 'new dehli':
        cities[x] = cities[x].title()
cities.insert(3, 'Feodosiya')
cities.append('Kramatorsk')
cities.append('Kiev')
print(cities)

cities.remove('Moscow')
del cities[-3]
cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)
print("----------------------------------9--------------------------------")
for x in cities:
    print(x.upper())
print("===================================================================")
c = max(cities)
print(c)
c = min(cities)
print(c)
my_cities = cities[1:3]
print(my_cities)

#lesson 10
print("---------- lesson 10 ------------")
x=16
if x <= 4:
    print("Yes, you are baby")
elif x>4 and x<=18:
    print("You are kid")
else:
    print("No, you are adult")

ua_cities = ['Kiev', 'Kramatorsk']
for x in cities:
    if x in ua_cities:
        print(x + " is a UA cities")
    else:
        print(x + " is not a UA cities")

#lesson 11 - 12
print("-----------lesson 11 and 12-------------")

enemy = {
    'loc_x': 180,
    'loc_y': 200,
    'name': 'mudilo',
    'color': 'green',
    'health': 100
}

print(enemy)
print(enemy['name'])
print(str(enemy['loc_x']))
enemy['rank'] = 'Admiral'
print(enemy)

all_enemies = []
print("+++++++++++++++++++++++++++++++++++++++++++++++++")
for x in range(1, 10):
    all_enemies.append(enemy)
n=0
for xx in all_enemies:
    n=n+1
    print("Enemy "+str(n))
    print(xx)
    print("\n")
print("+++++++++++++++++++++++++++++++++++++++++++++++++")
print(all_enemies[2]['name'])

#lesson 13 user input from keyboard
print("---------------lesson 13-------------------")

name = input("Please enter your name:\n\n")
print("\tYour name = "+name)



while True:
    pas = input("please input password:\n")
    if pas == "password":
        break
    else:
        print("Wrong password!")

print("OK!")

#lesson 14-15 function
print("------------lesson 14-15--------------")
def summa_age(x,y,name):
    z=x+y
    print(name + " , your age is: "+ str(z))

def fact(x):
    z=1
    for x in range(1,x+1,1):
       z=z*x
    return z

summa_age(12,21,"Kirill")

n=fact(3)
print(str(n))
