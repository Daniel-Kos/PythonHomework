name = str
n = 0
def top_left(n, i, j):
    return j < n - 1 - i

def bottom_right(n, i, j):
    return j > n - 1 - i

def top_center_v(n, i, j):
    return i < min(j, n - 1 - j)

def bottom_center_v(n, i, j):
    return i > max(j, n - 1 - j)

def left_center_v(n, i, j):
    return j < min(i, n - 1 - i)

def right_center_v(n, i, j):
    return j > max(i, n - 1 - i)

def cross_corners(n, i, j):
    return (j < n - 1 - i and j < i) or (j > n - 1 - i and j > i)

def diamond_center(n, i, j):
    return not cross_corners(n, i, j) and (i != j and i + j != n - 1)

def below_main_diag(n, i, j):  # lower-left triangle (including diagonal)
    return j < i
def above_main_diag(n, i, j):  # upper-right triangle (including diagonal)
    return j > i

def render(shape_fn, n):
    out = []
    for i in range(n):
        row = ''.join('*' if shape_fn(n, i, j) else ' ' for j in range(n))
        out.append(row)
    return '\n'.join(out)

shapes = {
    "a" : ("top-left (triangle cut by anti-diagonal)", top_left),
    "б" : ("bottom-right (triangle cut by anti-diagonal)", bottom_right),
    "в" : ("top-center V (small triangle pointing down)", top_center_v),
    "г" : ("bottom-center V (small triangle pointing up)", bottom_center_v),
    "д" : ("cross corners (X-like, corners filled toward center)", cross_corners),
    "е" : ("diamond center (center area filled)", diamond_center),
    "ж" : ("left-pointing (triangle in center-left)", left_center_v),
    "з" : ("right-pointing (triangle in center-right)", right_center_v),
    "и" :("below main diagonal (lower-left triangle)", below_main_diag),
    "к" : ("above main diagonal (upper-right triangle)", above_main_diag))
}

interactive_block = '''
if __name__ == "__main__":
    while True:
        print_menu()
        choice = int(input("Enter shape number (0 to exit): "))
        if choice == 0:
            break
        if choice not in shapes:
            print("Bad choice")
            continue
        n = int(input("Enter size n (odd >= 7 recommended): "))
        print(render(shapes[choice][1], n))
'''

if __name__ == "__main__":

    while True:
        print(
        "a — top-left (triangle cut by anti-diagonal)"
        "\nб — bottom-right (triangle cut by anti-diagonal)"
        "\nв — top-center V (small triangle pointing down)"
        "\nг — bottom-center V (small triangle pointing up)"
        "\nд — cross corners (X-like, corners filled toward center)"
        "\nе — diamond center (center area filled)"
        "\nж — left-pointing (triangle in center-left)"
        "\nз — right-pointing (triangle in center-right)"
        "\nи — below main diagonal (lower-left triangle)"
        "\nк — above main diagonal (upper-right triangle)")

        name = str(input())

        if name == "а":
            size = int(input("Enter size:"))
            print(render(top_left, n))
        elif name == "б":
            size = int(input("Enter size:"))
            print(render(bottom_right["б"], n))
        elif name == "в":
            size = int(input("Enter size:"))
            print(render(top_center_v["в"], n))
        elif name == "г":
            size = int(input("Enter size:"))
            print(render(bottom_center_v["г"], n))
        elif name == "д":
            size = int(input("Enter size:"))
            print(render(cross_corners["д"], n))
        elif name == "е":
            size = int(input("Enter size:"))
            print(render(diamond_center["е"], n))
        elif name == "ж":
            size = int(input("Enter size:"))
            print(render(left_center_v["ж"], n))
        elif name == "з":
            size = int(input("Enter size:"))
            print(render(right_center_v["з"], n))
        elif name == "и":
            size = int(input("Enter size:"))
            print(render(below_main_diag["и"], n))
        elif name == "к":
            size = int(input("Enter size:"))
            print(render(above_main_diag["к"], n))
