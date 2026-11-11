# Problem 4: Count Pairs with Given Sum

n = int(input())
arr = list(map(int, input().split()))
target = int(input())

count = 0

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == target:
            count += 1

print(count)
