# n! = 1 X 2 X 3 X ..... X n
# 5! = 1 X 2 X 3 X 4 X 5

num = int(input("Enter the number here : "))
sum = 0
for i in range(1,9):
    sum = sum +i
print(f"The sum of {num} is {sum}")