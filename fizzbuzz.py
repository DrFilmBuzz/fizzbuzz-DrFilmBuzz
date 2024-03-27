# Fizzbuzz Assignment by Wesley Gift
# Printing numbers 1 to 100
for num in range (1, 101):
    # Is num divisible by 3 and 5?
    if num % 3 == 0 and num % 5 == 0:
        # If so, print "Fizzbuzz"
        print("Fizzbuzz")
        continue
    # Is num divisible by 3 only?
    elif num % 3 == 0:
        # If so, print "Fizz"
        print("Fizz")
        continue
    # Is num divisible by 5 only?
    elif num % 5 == 0:
        # If so, print "Buzz"
        print("Buzz")
        continue
    # If num is NOT divisible by 3 or 5, print num
    print(num)
    
