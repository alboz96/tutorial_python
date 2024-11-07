# Read the coordinates of the first and second squares
r1 = int(input())  # Row of the first square
c1 = int(input())  # Column of the first square
r2 = int(input())  # Row of the second square
c2 = int(input())  # Column of the second square

# Check if the queen can move in one move
if r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
    print("YES")
else:
    print("NO")