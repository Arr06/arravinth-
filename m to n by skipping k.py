m, n, k = map(int, input("Enter values for M, N, and K separated by space: ").split())

for num in range(m, n+1, k+1):
    print(num, end=" ")
