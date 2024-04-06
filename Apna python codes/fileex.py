#From a file "nums.txt" containing numbers separated by comma, print the count of even numbers.
count = 0
with open("nums.txt", "r") as f:
    data = f.read()

    nums = data.split(",") #As the data in the file is string format. We need to split each strings and parse/cast them to integers.
    for val in nums:
        if(int(val)%2 == 0): #check if each integer is even or odd.
            count += 1

print(count)