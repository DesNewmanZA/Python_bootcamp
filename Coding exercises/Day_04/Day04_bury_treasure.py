# Blank map template
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]

# Initialize and ask for input
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ") 

# Process input into a column and row
column = position[0].lower()
col_pos = ['a', 'b', 'c'].index(column)
row_pos = int(position[1])-1

# Hide the treasure
map[row_pos][col_pos] = "X" 

# Output results
print(f"{line1}\n{line2}\n{line3}")