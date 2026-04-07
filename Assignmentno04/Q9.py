start = int(input("Enter the Start Number :"))
end = int(input("Enter the end Number :"))
divisor = int(input("Enter the Divisor :"))
print(f"Numbers between {start} and {end} divisible by {divisor}")

for i in range(start,end + 1):
    if (i % divisor == 0):
        print(i)