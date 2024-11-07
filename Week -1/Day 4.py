# Comparative operators
# To compare values and give boolean results i.e. True or False
# 1. Equal to (= =)
# 2. Not equal to (!=)
# Greater than (>)
# Lesser than (<)
# Greater than or equal to (>=)
# Less than or equal to (<=)

x = 5
print(x==5)
print(x==4)
print(x<10)
print(x>=3)
print(x>8)

digit=50
if digit>10:
    print("right it is")
else:
    print("wrong it is")
print(" ")

number=20
if number %2==0:   #Modules - it means %2 will divide the actual number and if result i.e. remainder is 0 then answer is 0 or whatever the remainder value
    print("number is even")
else:
    print("number is odd")

# elif is similar to if to give multiple creterias because if cannot be written multiple times
# single condition use if and else
# multiple condition use if, elif and else

# Arithematic operators
a=10
b=40
result=a+b
print(result)
print("addition", result)
multiply=a*b
print(multiply)
divide=b/a
print(divide)

#exponentiation
base=3
exponent=3
rr=base**exponent
print(rr)

j=2
k=3
expo=j**k
print(expo)

upper=33
lower=3
answer=upper%lower
print("module:",answer)

a=13
b=5
ans=13%5      #13 divide by 5 and remainder is 3 i.e. module
print("module:",ans)

score=85
if score>90:
    print("excellent")
else:
          print("good")

marks=60
if marks>90:
     print("excellent")
elif marks>50:
     print("average")
else:
     print("fair")

weather="cloudy"
if weather == "sunny":
     print("lets go to the market")
elif weather =="rainy":
     print("lets stay indoors")
else:
     print("lets check forecast")

a=20
b=6
c=a//b # floor division gives interger output and not the decimal figure
print(c)