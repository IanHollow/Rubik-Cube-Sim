from Face import Face
import numpy as np
from colorama import Fore
from random import randint
import time


class RubikCube:
    def __init__(self, size: int = 3) -> None:
        self.size = size
        self.faces = [Face(size=size, color=x) for x in range(6)]
        self.eq_time = np.zeros(2)
        self.xyz_time = np.zeros(6).reshape((3, 2))
        self.mix_time = np.zeros(2)

    def __eq__(self, other):
        start = time.perf_counter()
        if type(self) == type(other):
            for face, o_face in zip(self.faces, other.faces):
                if face != o_face:
                    return False
            end = time.perf_counter()
            self.eq_time[0] += (end - start)
            self.eq_time[1] += 1
            return True
        else:
            end = time.perf_counter()
            self.eq_time[0] += (end - start)
            self.eq_time[1] += 1
            return False

    @staticmethod
    def n_to_c(num) -> str:
        #return f' {num} '
        square = u'\u2588\u2588 '
        color_lookup = {0: Fore.YELLOW + square, 1: Fore.BLUE + square, 2: Fore.RED + square, 3: Fore.GREEN + square,
                        4: Fore.MAGENTA + square, 5: Fore.WHITE + square}
        if num not in color_lookup:
            raise KeyError(f'num "{num}" is out of range 0 to 5')
        return f'{color_lookup[num]}'

    def turn_x(self, layer: int, clockwise: bool = True) -> None:
        start = time.perf_counter()
        # check layer val
        if not -1 < layer < self.size:
            raise IndexError(
                f'layer "{layer}" is out of range 0 to {self.size}')

        l = layer
        def f(i): return self.faces[i].get_face()
        # swap matrix faces 1, 2, 3, 4
        if clockwise:
            f(1)[[l]], f(2)[[l]], f(3)[[l]], f(4)[[l]] = f(
                2)[[l]], f(3)[[l]], f(4)[[l]], f(1)[[l]]
        else:
            f(1)[[l]], f(2)[[l]], f(3)[[l]], f(4)[[l]] = f(
                4)[[l]], f(1)[[l]], f(2)[[l]], f(3)[[l]]

        # rotate face
        if layer == 0:
            self.faces[l].rotate(clockwise=clockwise, times=1)
        elif layer == self.size - 1:
            self.faces[5].rotate(clockwise=(not clockwise), times=1)

        end = time.perf_counter()
        self.xyz_time[0][0] += (end - start)
        self.xyz_time[0][1] += 1

    def turn_y(self, layer: int, away: bool = True) -> None:
        start = time.perf_counter()
        # check layer val
        if not -1 < layer < self.size:
            raise IndexError(
                f'layer "{layer}" is out of range 0 to {self.size}')

        l = layer
        l2 = self.size - 1 - layer
        def f(i): return self.faces[i].get_face()
        # swap matrix faces 0, 1, 3, 5
        if away:
            f(0)[:, [l]], f(1)[:, [l2]], f(3)[:, [l]], f(5)[:, [l]] = f(3)[
                :, [l]], np.flip(f(0)[:, [l]]), f(5)[:, [l]], np.flip(f(1)[:, [l2]])
        else:
            f(0)[:, [l]], f(1)[:, [l2]], f(3)[:, [l]], f(5)[:, [l]] = np.flip(
                f(1)[:, [l2]]), np.flip(f(5)[:, [l]]), f(0)[:, [l]], f(3)[:, [l]]

        # rotate face
        if layer == 0:
            self.faces[2].rotate(clockwise=(not away), times=1)
        elif layer == self.size - 1:
            self.faces[4].rotate(clockwise=away, times=1)

        end = time.perf_counter()
        self.xyz_time[1][0] += (end - start)
        self.xyz_time[1][1] += 1

    def turn_z(self, layer: int, clockwise: bool = True) -> None:
        start = time.perf_counter()
        # check layer val
        if not -1 < layer < self.size:
            raise IndexError(
                f'layer "{layer}" is out of range 0 to {self.size}')

        l = layer
        l2 = self.size - 1 - layer
        def f(i): return self.faces[i].get_face()
        def ft(i): return np.transpose(self.faces[i].get_face())
        # swap matrix faces 0, 2, 4, 5
        if clockwise:
            f(0)[[l2]], f(2)[:, [l2]], f(4)[:, [l]], f(5)[[l]] = np.flip(
                ft(2)[[l2]]), ft(5)[:, [l]], ft(0)[:, [l2]], np.flip(ft(4)[[l]])
        else:
            f(0)[[l2]], f(2)[:, [l2]], f(4)[:, [l]], f(5)[[l]] = ft(4)[
                [l]], np.flip(ft(0)[:, [l2]]), np.flip(ft(5)[:, [l]]), ft(2)[[l2]]

        # rotate face
        if layer == 0:
            self.faces[3].rotate(clockwise=clockwise, times=1)
        elif layer == self.size - 1:
            self.faces[1].rotate(clockwise=(not clockwise), times=1)

        end = time.perf_counter()
        self.xyz_time[2][0] += (end - start)
        self.xyz_time[2][1] += 1

    def mix(self, moves: int):
        start = time.perf_counter()
        if moves < 0:
            raise Exception(f'moves "{moves}" has to be positive')

        for _ in range(moves):
            direction = randint(1, 3)
            if direction == 1:
                layer = randint(0, self.size-1)
                rot = True if randint(1, 2) == 1 else False
                self.turn_x(layer=layer, clockwise=rot)
            elif direction == 2:
                layer = randint(0, self.size - 1)
                rot = True if randint(1, 2) == 1 else False
                self.turn_y(layer=layer, away=rot)
            else:
                layer = randint(0, self.size - 1)
                rot = True if randint(1, 2) == 1 else False
                self.turn_z(layer=layer, clockwise=rot)

        end = time.perf_counter()
        self.mix_time[0] += (end - start)
        self.mix_time[1] += 1

    def __str__(self):
        result = ""
        # Top
        for row in range(self.size):
            result += ' ' * (3 * self.size * 2)
            for col in range(self.size):
                num = self.faces[0].get_face()[row][col]
                result += self.n_to_c(num)
            result += '\n'
        # Middle
        for row in range(self.size):
            for face in range(1, 5):
                for col in range(self.size):
                    num = self.faces[face].get_face()[row][col]
                    result += self.n_to_c(num)
            result += '\n'
        # Bottom
        for row in range(self.size):
            result += ' ' * (3 * self.size * 2)
            for col in range(self.size):
                num = self.faces[5].get_face()[row][col]
                result += self.n_to_c(num)
            result += '\n'
        result += '\n'
        return result


if __name__ == '__main__':
    cube = RubikCube()
    print(cube)
    cube.turn_z(layer=2, clockwise=False)
    print(cube)
