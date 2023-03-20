n = int(input())
grid = []
for i in range(n):
    row = input().split()
    grid.append(row)

count_row = 0
count_col = 0

# đếm số cặp đồng xu cùng hàng
for i in range(n):
    count = grid[i].count('C')
    if count >= 2:
        count_row += count * (count - 1) // 2

# đếm số cặp đồng xu cùng cột
for j in range(n):
    count = 0
    for i in range(n):
        if grid[i][j] == 'C':
            count += 1
    if count >= 2:
        count_col += count * (count - 1) // 2

print(count_row + count_col)
