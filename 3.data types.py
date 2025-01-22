#1concat name
first_name=input()
second_name=input()
delimeter=input()
print(f'{first_name}{delimeter}{second_name}')
#2meters to kilometers
meters=int(input())
kilometers=meters/1000
print(f'{kilometers:.2f}')
#3convert dollar
british_point=int(input())
convert=british_point*1.31
print(f'{convert:.3f}')
#4Next happy year
year = int(input())

while True:
    year += 1
    year_str = str(year)

    if len(set(year_str)) == len(year_str):
        break

print(year)
