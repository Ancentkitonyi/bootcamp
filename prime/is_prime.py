def is_prime(num):
    if type(num) == int:
    	if num > 1:
        	#iteration within the given range
        	for i in range(2,num):
        	    if num % i == 0:
        	        return False
        	        break
        	else:
        	    return 'is a prime number'
    	#eliminate number less or equal than one since prime number start from two
    	else:
        	return False
    else:
    	return False
num = input('Enter a number to find prime numbers')
prime_generator = filter(is_prime, range(2, num))
print prime_generator
