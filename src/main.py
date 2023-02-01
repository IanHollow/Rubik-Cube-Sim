from RubikCube import RubikCube


if __name__ == '__main__':
    size = 2
    correct_cube = RubikCube(size)
    cube = RubikCube(size)
    cube.mix(moves=1000)
    #print(cube)

    move = 1
    in_progress = True

    for i in range(1000000):
        cube.mix(moves=1)
        if i % 10000 == 0:
            print(i)
        if cube == correct_cube:
            print('Done!')
            print(move)
            print(cube)
            in_progress = False

    print(f' eq: {cube.eq_time}')
    print(f'  x: {cube.xyz_time[0]}')
    print(f'  y: {cube.xyz_time[1]}')
    print(f'  z: {cube.xyz_time[2]}')
    print(f'mix: {cube.mix_time[0]-(cube.xyz_time[0][0]+cube.xyz_time[1][0]+cube.xyz_time[2][0])}')
    print(f'moves: {(cube.xyz_time[0][1]+cube.xyz_time[1][1]+cube.xyz_time[2][1])-1000}')

    """
    while in_progress:
        #print(move)
        #print(cube)
        move += 1
        cube.mix(1)
        print(move)
        #print(cube)

        #cube.turn_y(layer=0, away=True)

        #print(move)
        #print(cube)
        #move += 1

        #cube.turn_z(layer=1, clockwise=False)


        #cube.turn_x(layer=1, clockwise=False)

        #cube.turn_x(layer=0, clockwise=True)

        #move += 1
        
        if cube == correct_cube:
            print('Done!')
            print(move)
            print(cube)
            in_progress = False
    """