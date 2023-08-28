# write your code here
favorite_animal = ['dog', 'cat','monkey', 'rabbit']
print(favorite_animal)

print(favorite_animal[1])
favorite_animal.remove('monkey')
favorite_animal.append('deer')
for i in favorite_animal:
    print('i love', i)
numbers = [1, 2, 3, 4, 5]
numbers_sum = 0
for oneNum in numbers:
    numbers_sum += oneNum 
print(f'the total is: {numbers_sum}')