numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = int(input("Please enter a number to find from the list: "))
l= 0
u = len(numbers) - 1

while l <= u:
    mid = (l + u) // 2
    if numbers[mid] == x:
        print(f"{x} found at index {mid}")
        l = u + 1

    elif x > numbers[mid]:
        l = numbers[mid] + 1
    else:
        u = numbers[mid] - 1

else:
    print(f"{x} not found in sequence")