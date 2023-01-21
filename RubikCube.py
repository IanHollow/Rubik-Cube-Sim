import numpy as np


class RubikCube:
    def __init__(self, size=3) -> None:
        self.size = size
        self.color_lookup = {0: ' ', 1: 'y', 2: 'b', 3: 'r', 4: 'g', 5: 'o', 6: 'w'}

        self.rubik_cube = np.array([np.array([0] * 4 * size) for _ in range(3 * size)])

        for i in range(size, 2 * size):
            for j in range(len(self.rubik_cube[i])):
                self.rubik_cube[i][j] = j // size + 2

        for i in range(0, size):
            for j in range(2 * size, 3 * size):
                self.rubik_cube[i][j] = -2  # supposed to be 1

        for i in range(2 * size, 3 * size):
            for j in range(2 * size, 3 * size):
                self.rubik_cube[i][j] = -1  # supposed to be 6

    def print_cube(self):
        count = 1
        count2 = 1
        print()
        top_index_row = "i |"
        for i in range(self.size * 4):
            top_index_row += f' {i}{" " if len(str(i)) == 1 else ""}'
        print(top_index_row)
        print("-" * (self.size * 4 * 3 + 3))
        for i in range(len(self.rubik_cube)):
            row = self.rubik_cube[i]
            view_row = f"{i}{' ' if len(str(i)) == 1 else ''}|"
            for j in range(len(row)):
                """color = self.color_lookup[self.rubik_cube[i][j]]
                if color == 'y':
                    color = count
                    count += 1
                if color == 'w':
                    color = count2
                    count2 += 1
                view_row += f' {color} '
                """
                # temp testing
                if self.rubik_cube[i][j] == -2:
                    self.rubik_cube[i][j] = count
                    count += 1

                if self.rubik_cube[i][j] == -1:
                    self.rubik_cube[i][j] = count2
                    count2 += 1
                num = self.rubik_cube[i][j]
                view_row += f' {num if num != 0 else " "}{"" if len(str(num)) == 2 else " "}'
            print(view_row)
        print()

    def turn_layer(self, layer: int, clock_wise: bool = True):
        # check in range
        if layer > self.size or layer < 1:
            raise IndexError("Out of Layer Range")

        # Save cube values that will overridden
        lower, upper = (0 if clock_wise else self.size * 3), (self.size if clock_wise else self.size * 4)
        temp = self.rubik_cube[self.size + layer - 1][lower:upper].copy()

        # main rotation
        if clock_wise:
            for i in range(0, self.size * 4 - self.size):
                self.rubik_cube[self.size + layer - 1][i] = self.rubik_cube[self.size + layer - 1][i + self.size]
        else:
            for i in range(self.size * 4 - (self.size + 1), -1, -1):
                self.rubik_cube[self.size + layer - 1][i + self.size] = self.rubik_cube[self.size + layer - 1][i]

        # Uses saved values to overwrite the end values
        for i, num in enumerate(temp):
            shift = self.size * 3 if clock_wise else 3
            self.rubik_cube[self.size + layer - 1][i + shift] = num

        # check if top or bottom for rotation
        if layer == 1:
            # check direction of top rotation
            if clock_wise:
                # Save TR
                top_right = self.rubik_cube[0][self.size * 2 + 1:self.size * 3].copy()

                # left_top = (range(0, self.size - 1), self.rubik_cube[j][self.size * 2])

                # Overwrite TR with LT
                for i, j in zip(range(self.size * 3 - 1, self.size * 2, -1), range(0, self.size - 1)):
                    self.rubik_cube[0][i] = self.rubik_cube[j][self.size * 2]

                # Overwrite LT with BL
                for i, j in zip(range(0, self.size - 1), range(self.size * 2, self.size * 3 - 1)):
                    self.rubik_cube[i][self.size * 2] = self.rubik_cube[self.size - 1][j]

                print(list())
                # Overwrite BL with RB
                for i, j in zip(range(self.size * 3 - 2, self.size * 2 - 1, -1), range(1, self.size)):  
                    self.rubik_cube[self.size - 1][i] = self.rubik_cube[j][self.size * 3 - 1]

                # Overwrite RB with TR
                for i, j in zip(range(1, self.size), top_right):
                    self.rubik_cube[i][self.size * 3 - 1] = j

            else:

                # Save TL
                temp = self.rubik_cube[0][self.size * 2:self.size * 3 - 1].copy()

                # Overwrite TR with RB
                for i, j in zip(range(self.size * 2 + 1, self.size * 2 - 1, -1), range(0, self.size - 1)):
                    self.rubik_cube[0][i] = self.rubik_cube[j][self.size * 2]

                # Overwrite RB with BL

                # Overwrite BL with LT

                # Overwrite LT with TL

        elif layer == self.size:
            pass


if __name__ == '__main__':
    cube = RubikCube(4)
    cube.print_cube()
    cube.turn_layer(1)
    cube.print_cube()
