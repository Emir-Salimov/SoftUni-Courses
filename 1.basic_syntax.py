#1.number_definier
number=float(input())

if number==0:
    print("zero")
elif number>0:
    if number<1:
        print('small positive')
    elif number>1000000:
        print('large positive')
    else:
        print('positive')
else:
    if abs(number)<1:
        print('small negative')
    elif abs(number)>1000000:
        print('large negative')
    else:
        print('negative')
#2.The_largest_one
first_num=int(input())
second_num=int(input())
third_num=int(input())
if first_num>second_num and first_num>third_num:
    print(first_num)
elif second_num>first_num and second_num>third_num:
    print(second_num)
else:
    print(third_num)
#3.word.reverse
word=input()

for i in range(len(word)-1,-1,-1):
    print(word[i] , end="")
#4.odd or even
n=int(input())

for _ in range(n):
    number=int(input())

    if number%2 !=0:
        print(f'{number} is odd!')
        break
else:
    print('All numbers are even.')
#5.num 1 to 100
number=float(input())

while number<1 or number>100:
    number=float(input())
print(f"The number {number} is between 1 and 100")
# while True:
#     number=float(input())
#     if number>1 and number<100:
#         break
# print(f"The number {number} is between 1 and 100.")
#6.shopping
budget=int(input())
while True:
    command=input()
    if command=="End":
        if budget>0:
            print("You bought everything needed.")

        break
    else:
        price=int(command)
        if budget>=price:
            budget-=price
        else:
            print("You went in overdraft!" )
            break
#7.patterns
number=int(input())

for i in  range (1 , number+1):
    print('*'*i)
    #for _ in range(0,i):
        #print('*' , end='')
    #print()
for i in range (number-1 ,0 , -1):
    print('*'*i)
    # for j in range(0,i):
    #     print('*' , end='')
    # print()
