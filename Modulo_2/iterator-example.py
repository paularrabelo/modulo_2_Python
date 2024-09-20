#forma simples de fazer, utilizando o "for"

my_list = [1,2,3,4,5]

for num in my_list:
    print(num)

#forma utilizando o iter, com o next

iter_example = iter(my_list)


print(next(iter_example))
print(next(iter_example))
print(next(iter_example))
print(next(iter_example))
print(next(iter_example))


#forma utilizando o "while" com o next do iter
try:
    while True:
        print(next(iter_example))
except StopIteration as e:
    pass