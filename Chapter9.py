#Problem 1
from graphics import *
import time
import math

def main():
    height = float(input("Enter the initial height in meters: "))

    if height <= 0:
        print("Height must be greater than zero.")
        return

    win = GraphWin("Three Bouncing Balls", 600, 500)
    win.setCoords(0, 0, 10, height * 1.2)

    radius = height * 0.025
    gravity = 9.8

    # Each ball stores its graphics object, velocity, and bounce height.
    balls = []

    positions = [2, 5, 8]
    colors = ["red", "blue", "green"]

    for i in range(3):
        ball = Circle(Point(positions[i], height - radius), radius)
        ball.setFill(colors[i])
        ball.draw(win)

        balls.append([ball, 0, height])

    Line(Point(0, 0), Point(10, 0)).draw(win)

    active = [True, True, True]
    time_step = 0.02

    while True:
        running = False

        for i in range(3):
            if active[i]:
                running = True

                ball = balls[i][0]
                velocity = balls[i][1]
                bounce_height = balls[i][2]

                velocity = velocity - gravity * time_step
                ball.move(0, velocity * time_step)

                center_y = ball.getCenter().getY()

                if center_y <= radius:
                    ball.move(0, radius - center_y)

                    bounce_height = bounce_height * 0.60

                    if bounce_height < 0.001:
                        active[i] = False
                    else:
                        velocity = math.sqrt(
                            2 * gravity * bounce_height
                        )

                balls[i][1] = velocity
                balls[i][2] = bounce_height

        if not running:
            break

        time.sleep(time_step)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()

#Problem 2
checkerboard = (
    ("A", "B", "C", "D", "E"),
    ("F", "G", "H", "I", "K"),
    ("L", "M", "N", "O", "P"),
    ("Q", "R", "S", "T", "U"),
    ("V", "W", "X", "Y", "Z")
)

def locateLetter(letter):
    letter = letter.upper()

    if letter == "J":
        letter = "I"

    for row in range(5):
        for col in range(5):
            if checkerboard[row][col] == letter:
                return (row, col)

    return None

def encode(message):
    code = []

    for letter in message.upper():
        if letter.isalpha():
            position = locateLetter(letter)

            if position != None:
                code.append(position)

    return code

def decode(code):
    message = ""

    for position in code:
        row, col = position
        message = message + checkerboard[row][col]

    return message

def main():
    message = input("Enter a message to encode: ")

    encoded = encode(message)
    print("Encoded message:", encoded)

    decoded = decode(encoded)
    print("Decoded message:", decoded)

if __name__ == "__main__":
    main()

#Problem 3
def createGrid(message, keyword):
    columns = len(keyword)
    rows = (len(message) + columns - 1) // columns

    message = message.upper().replace(" ", "")
    message = message.ljust(rows * columns, "X")

    grid = []

    position = 0

    for row in range(rows):
        current_row = []

        for col in range(columns):
            current_row.append(message[position])
            position = position + 1

        grid.append(current_row)

    return grid

def getColumnOrder(keyword):
    order = []

    for col in range(len(keyword)):
        order.append((keyword[col], col))

    order.sort()

    return [item[1] for item in order]

def encrypt(message, keyword):
    grid = createGrid(message, keyword)
    column_order = getColumnOrder(keyword)

    ciphertext = ""

    for col in column_order:
        for row in range(len(grid)):
            ciphertext = ciphertext + grid[row][col]

    return ciphertext

def decrypt(ciphertext, keyword):
    columns = len(keyword)
    rows = len(ciphertext) // columns

    grid = [[""] * columns for row in range(rows)]

    column_order = getColumnOrder(keyword)
    position = 0

    for col in column_order:
        for row in range(rows):
            grid[row][col] = ciphertext[position]
            position = position + 1

    message = ""

    for row in range(rows):
        for col in range(columns):
            message = message + grid[row][col]

    return message.rstrip("X")

def main():
    message = input("Enter the message: ")
    keyword = input("Enter the keyword: ").upper()

    encrypted = encrypt(message, keyword)
    print("Encrypted message:", encrypted)

    decrypted = decrypt(encrypted, keyword)
    print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()

#Problem 4
def createGrid(message):
    rows = 5
    columns = 6

    message = message.upper().replace(" ", "")
    message = message.ljust(rows * columns, "X")

    grid = []
    position = 0

    for row in range(rows):
        current_row = []

        for col in range(columns):
            current_row.append(message[position])
            position = position + 1

        grid.append(current_row)

    return grid

def createPath():
    path = []

    top = 0
    bottom = 4
    left = 0
    right = 5

    while top <= bottom and left <= right:

        for col in range(left, right + 1):
            path.append((top, col))
        top = top + 1

        for row in range(top, bottom + 1):
            path.append((row, right))
        right = right - 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                path.append((bottom, col))
            bottom = bottom - 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                path.append((row, left))
            left = left + 1

    return path

def encrypt(message):
    grid = createGrid(message)
    path = createPath()

    ciphertext = ""

    for row, col in path:
        ciphertext = ciphertext + grid[row][col]

    return ciphertext

def decrypt(ciphertext):
    grid = [[""] * 6 for row in range(5)]
    path = createPath()

    position = 0

    for row, col in reversed(path):
        grid[row][col] = ciphertext[::-1][position]
        position = position + 1

    message = ""

    for row in range(5):
        for col in range(6):
            message = message + grid[row][col]

    return message.rstrip("X")

def main():
    message = input("Enter the message: ")

    encrypted = encrypt(message)
    print("Encrypted message:", encrypted)

    decrypted = decrypt(encrypted)
    print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()

#Prblem 5
def createGrid(message, rows, columns):
    message = message.upper().replace(" ", "")
    message = message.ljust(rows * columns, "X")

    grid = []
    position = 0

    for row in range(rows):
        current_row = []

        for col in range(columns):
            current_row.append(message[position])
            position = position + 1

        grid.append(current_row)

    return grid

def getColumnOrder(keyword):
    order = []

    for col in range(len(keyword)):
        order.append((keyword[col], col))

    order.sort()

    return [item[1] for item in order]

def createPath(rows, columns):
    path = []

    top = 0
    bottom = rows - 1
    left = 0
    right = columns - 1

    while top <= bottom and left <= right:

        for col in range(left, right + 1):
            path.append((top, col))
        top = top + 1

        for row in range(top, bottom + 1):
            path.append((row, right))
        right = right - 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                path.append((bottom, col))
            bottom = bottom - 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                path.append((row, left))
            left = left + 1

    return path

def encrypt(message, keyword, rows, columns):
    grid = createGrid(message, rows, columns)
    column_order = getColumnOrder(keyword)
    path = createPath(rows, columns)

    ciphertext = ""

    for row, col in path:
        actual_col = column_order[col]
        ciphertext = ciphertext + grid[row][actual_col]

    return ciphertext

def decrypt(ciphertext, keyword, rows, columns):
    grid = [[""] * columns for row in range(rows)]

    column_order = getColumnOrder(keyword)
    path = createPath(rows, columns)

    position = 0

    for row, col in reversed(path):
        actual_col = column_order[col]
        grid[row][actual_col] = ciphertext[::-1][position]
        position = position + 1

    message = ""

    for row in range(rows):
        for col in range(columns):
            message = message + grid[row][col]

    return message.rstrip("X")

def main():
    message = input("Enter the message: ")
    keyword = input("Enter the keyword: ").upper()

    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

    if len(keyword) != columns:
        print("The keyword length must match the number of columns.")
        return

    if rows <= 0 or columns <= 0:
        print("Grid dimensions must be greater than zero.")
        return

    encrypted = encrypt(message, keyword, rows, columns)
    print("Encrypted message:", encrypted)

    decrypted = decrypt(encrypted, keyword, rows, columns)
    print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
