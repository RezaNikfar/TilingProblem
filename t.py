
# Tiling Project    Reza Nikfar

import turtle
import random


def putNumber(s, p):
    global number

    number = number + 1
    arr[s][p] = number
    arr[s + 1][p] = number
    arr[s][p + 1] = number
    arr[s + 1][p + 1] = number


# -------------------------------------------------
def getColor(n,x,y):
    for i in range(n):
        color[i] = [random.randrange(1, 255, 1) / 255, random.randrange(1, 255, 1) / 255,
                    random.randrange(1, 255, 1) / 255]

    color[arr[x][y]] = [1, 1, 1]


# -------------------------------------------------
def draw(n):
    #windows = turtle.Screen();
    turtle.speed(9)
    turtle.penup()
    turtle.goto(-320, 280)
    turtle.pendown()

    for i in range(n):
        for j in range(n):
            turtle.fillcolor(color[arr[i][j]])
            turtle.begin_fill()
            for k in range(4):
                turtle.forward(40)
                turtle.left(90)

            turtle.goto(-320 + 40 * (j+1), 280 - 40 * i)
            turtle.end_fill()
        turtle.penup()
        turtle.goto(-320, 280 - 40 * (i + 1))
        turtle.pendown()


# ------------------------------------------------
def solve(n, x, y, s, p):
    f = arr[x][y]
    if n == 2:
        putNumber(s, p)
        arr[x][y] = f
        return

    mid_x = int(s + (n / 2) - 1)
    mid_y = int(p + (n / 2) - 1)
    putNumber(mid_x, mid_y)

    if x <= mid_x and y <= mid_y:
        arr[mid_x][mid_y] = 0
        arr[x][y] = f
        solve(int(n / 2), x, y, s, p)
        solve(int(n / 2), mid_x + 1, mid_y, mid_x + 1, p)
        solve(int(n / 2), mid_x, mid_y + 1, s, mid_y + 1)
        solve(int(n / 2), mid_x + 1, mid_y + 1, mid_x + 1, mid_y + 1)
    elif x > mid_x and y <= mid_y:
        arr[mid_x + 1][mid_y] = 0
        arr[x][y] = f
        solve(int(n / 2), x, y, mid_x + 1, p)
        solve(int(n / 2), mid_x, mid_y, s, p)
        solve(int(n / 2), mid_x, mid_y + 1, s, mid_y + 1)
        solve(int(n / 2), mid_x + 1, mid_y + 1, mid_x + 1, mid_y + 1)
    elif x <= mid_x and y > mid_y:
        arr[mid_x][mid_y + 1] = 0
        arr[x][y] = f
        solve(int(n / 2), x, y, s, mid_y + 1)
        solve(int(n / 2), mid_x, mid_y, s, p)
        solve(int(n / 2), mid_x + 1, mid_y, mid_x + 1, p)
        solve(int(n / 2), mid_x + 1, mid_y + 1, mid_x + 1, mid_y + 1)
    elif x > mid_x and y > mid_y:
        arr[mid_x + 1][mid_y + 1] = 0
        arr[x][y] = f

        solve(int(n / 2), mid_x, mid_y, s, p)
        solve(int(n / 2), mid_x, mid_y + 1, s, mid_y + 1)
        solve(int(n / 2), mid_x + 1, mid_y, mid_x + 1, p)
        solve(int(n / 2), x, y, mid_x + 1, mid_y + 1)


# --------------------------------------------------------
number = 0

n = input("Enter the dimension :")
n = int(n)
rows, cols = (n, n)
arr = [[0 for i in range(cols)] for j in range(rows)]
color = [[0 for i in range(3)] for j in range(n * n)]
x = input("Enter the x of mising mosiac : ")

y = input("Enter the y of mising mosaic : ")

x = int(x)
y = int(y)

arr[x][y] = 0
solve(n, x, y, 0, 0)
i = 0
j = 0
# arr1 = [[2,3,4,5],[6,7,8,9]]
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print("\n")
getColor(n * n,x,y)
draw(n)

