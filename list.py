st = input("Enter X and Y")
X, Y = [int(x) for x in st.split(',')]
lst = [[0 for col in range(Y)] for row in range(X)]

for row in range(X):
    for col in range(Y):
        lst[row][col] = row*col
for row in range(X):
    print(lst[row])