from RubikCube import RubikCube

# Simulation

if __name__ == '__main__':
    size = 3
    correct_cube = RubikCube(size)
    cube = RubikCube(size)

    move_set = 0
    in_progress = True
    while in_progress:
        cube.turn_y(layer=0, away=True)

        cube.turn_z(layer=1, clockwise=False)

        #cube.turn_x(layer=1, clockwise=False)

        #cube.turn_x(layer=0, clockwise=True)

        move_set += 1
        print(move_set)
        if cube == correct_cube:
            print('Done!')
            print(move_set)
            in_progress = False