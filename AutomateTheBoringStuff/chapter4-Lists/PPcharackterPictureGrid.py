#Character Picture Grid


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#Objective is to rotate the grid clockwise 90 degrees
#output should be:
#..OO.OO..
#.OOOOOOO.
#.OOOOOOO.
#..OOOOO..
#...OOO...
#....O....

for x in range(6):
    for y in range(9):
        print(grid[y][x], end='')
    print()

# For this project, we have to use a nested loop
# The first loop will iterate through each column in the grid. However,
# You also don't want to change columns until you've finished each row.
# So you nest a loop inside the first one. Since there are 6 columns and 9
# rows, you will have both loops at a range of 6 and 9, respectively.
# Your print will include both variables, [i] and [j] as well as
# a sep='' so you don't print a new line. This one is difficult, it may
# take you some trial and error.




