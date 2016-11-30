num = int(input('Enter a number to find out if it a prime number'))

if num > 1:
    #iteration within the given range
    for i in range(2,num):
        if num % i == 0:
#eliminate number less or equal than one since prime number start from two
else:
    print num, 'is not prime number'
