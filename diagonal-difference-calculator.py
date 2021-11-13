from random import randint


def create_matrix(matrix, n):
    for row in range(0,n):
        matrix.append([])
        for col in range(0,n):
            value = randint(1,20)
            matrix[row].append(value)


def display_greid(matrix):
    n = len(matrix)
    for row in range(0,n):
        st="| "
        for col in range(0,n):
            if matrix[row][col] < 10:
                st = st + str(matrix[row][col]) + "  | "
            else:
                st = st + str(matrix[row][col]) + " | "
        print(st)


def diff(matrix):
    l = len(matrix)
    x = []
    y = []

    for i in range(0,l):
        x.append(matrix[i][i])
    for p in range(0, l):
        y.append(matrix[p][(l-1)-p])
    z = sum((x)) - sum((y))
    return z


def sum_of_corners(marix):
    l = len(marix)
    corners = [marix[0][0],
               marix[-1][0],
               marix[0][-1],
               marix[-1][-1]]
    total = sum(corners)
    return total


def average_value(matrix):
    row_total = []
    for row in matrix:
        row_total.append(sum(row))
    grand_total = sum(row_total)
    return round(grand_total/len(matrix), 4)


for v in range(1):
    matrixx = []
    # n = int(input("Enter a number for matrix: "))
    create_matrix(matrixx, 3)
    display_greid(matrixx)
    a = diff(matrixx)
    print(f"Diffrence is {a}")
    sum_is = sum_of_corners(matrixx)
    print(f"Sum of all corners {sum_is} ")
    average_val = average_value(matrixx)
    print(f"Average value is {average_val}")