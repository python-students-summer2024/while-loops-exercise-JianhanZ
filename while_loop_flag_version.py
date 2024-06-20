
def get_starting_number():
    return int(input("Enter the starting number of bottles: "))

def sing(num_bottles):
    keep_singing = True
    while keep_singing:
        print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.")
        num_bottles -= 1
        if num_bottles == 0:
            keep_singing = False
        print(f"Take one down, pass it around, {num_bottles} bottles of beer on the wall.")
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")
