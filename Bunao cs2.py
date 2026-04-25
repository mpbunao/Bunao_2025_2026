# Ask user for input
age = int(input("Hi there! Please enter your age: "))

# Initialize sum variable
total_sum = 0

# Loop from 1 to age (inclusive)
for i in range(1, age + 1):
    total_sum += i

# Display result
print(f"The sum of all numbers from 1 to {age} is: {total_sum}")
