n = int(input("Enter number of students: "))
results = []

for i in range(n):
    print(f"Student {i+1}:")
    marks = [float(input(f" Subject {j+1}: ")) for j in range(5)]
    percentage = sum(marks) / 5
    results.append(percentage)

print("\nPercentages:", results)
print("Class Average:", sum(results) / n)