def print_row(size, star_count):
    for row in range(size - star_count):
        print(" ", end="")
    for row in range(1, star_count):
        print("*", end=" ")
    print("*")


n = int(input())
for star in range(1, n):
    print_row(n, star)
for star in range(n, 0, -1):
    print_row(n, star)
