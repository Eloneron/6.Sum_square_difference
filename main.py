"""
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

sum_of_squares = 0
sum = 0

# sum of squares
for x in range(1,101):
    sum_of_squares += x**2

# square of sum
for y in range(1,101):
    sum += y

square_of_sum = sum**2

# difference
difference = square_of_sum - sum_of_squares

print(f'Answer: {difference}')
