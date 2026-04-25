# CS2_Section_Surname_2QFunWithNumbers.py

# Variable for input
age = int(input("Hi there! Please enter your age: "))

# Variable for accumulating the sum
total_sum = 0

# Loop from 1 up to the user's age
for number in range(1, age + 1):
    total_sum += number

# Display the result
print("The sum of all numbers from 1 to", age, "is:", total_sum)
