
def get_starting_number():
    return int(input("Enter the starting number of bottles: "))

def sing(num_bottles):
    for i in range(num_bottles, 0, -1):
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down, pass it around, {i - 1} bottles of beer on the wall.")
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")
