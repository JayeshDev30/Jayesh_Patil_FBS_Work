start = int(input("Enter the Start Number :"))
end = int(input("Enter the end Number"))

print(f"Numbers between {start} and {end} divisible by 7 and 5:")

for i in range(start,end + 1):
    if (i % 7 == 0 and i % 5 == 0):
        print(i)