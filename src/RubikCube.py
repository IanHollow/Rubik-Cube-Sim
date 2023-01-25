from Face import Face
import numpy as np

class RubikCube:
    def __init__(self, size: int = 3) -> None:
        self.size = size
        self.faces = [Face(size=size, color=x) for x in range(6)]

    def __eq__(self, other):
        if type(self) == type(other):
            for face, o_face in zip(self.faces, other.faces):
                if face != o_face:
                    return False
            return True
        else:
            return False

    @staticmethod
    def n_to_c(num) -> str:
        #return f' {num} '
        #square = u'\u2588\u2588 '
        color_lookup = {0: 'y', 1: 'b', 2: 'r', 3: 'g', 4: 'o', 5: 'w'}
        if num not in color_lookup:
            raise KeyError(f'num "{num}" is out of range 0 to 5')
        return f' {color_lookup[num]} '

    def turn_x(self, layer:int, clockwise:bool=True) -> None:
        # check layer val
        if not -1 < layer < self.size:
            raise IndexError(f'layer "{layer}" is out of range 0 to {self.size}')

        l = layer
        f = lambda i : self.faces[i].get_face()
        # swap matrix faces 1, 2, 3, 4
        if clockwise:
            f(1)[[l]], f(2)[[l]], f(3)[[l]], f(4)[[l]]  = f(2)[[l]], f(3)[[l]], f(4)[[l]], f(1)[[l]]
        else:
            f(1)[[l]], f(2)[[l]], f(3)[[l]], f(4)[[l]]  = f(4)[[l]], f(1)[[l]], f(2)[[l]], f(3)[[l]]

        # rotate face
        if layer == 0:
            self.faces[l].rotate(clockwise=clockwise, times=1)
        elif layer == self.size-1:
            self.faces[5].rotate(clockwise=(not clockwise), times=1)

    def turn_y(self, layer:int, away:bool=True) -> None:
        # check layer val
        if not -1 < layer < self.size:
            raise IndexError(f'layer "{layer}" is out of range 0 to {self.size}')

        l = layer
        l2 = self.size-1-layer
        f = lambda i : self.faces[i].get_face()
        # swap matrix faces 0, 1, 3, 5
        if away:
            f(0)[:, [l]], f(1)[:, [l2]], f(3)[:, [l]], f(5)[:, [l]]  = f(3)[:, [l]], f(0)[:, [l]], f(5)[:, [l]], f(1)[:, [l2]]
            f(5)[:, [l]] = np.flip(f(5)[:, [l]])
        else:
            f(0)[:, [l]], f(1)[:, [l2]], f(3)[:, [l]], f(5)[:, [l]] = f(1)[:, [l2]], f(5)[:, [l]], f(0)[:, [l]], f(3)[:, [l]]
            f(0)[:, [l]] = np.flip(f(0)[:, [l]])
        f(1)[:, [l2]] = np.flip(f(1)[:, [l2]])


        # rotate face
        if layer == 0:
            self.faces[2].rotate(clockwise=(not away), times=1)
        elif layer == self.size-1:
            self.faces[4].rotate(clockwise=away, times=1)

    def turn_z(self, layer:int, clockwise:bool=True) -> None:
        # check layer val
        if not -1 < layer < self.size:
            raise IndexError(f'layer "{layer}" is out of range 0 to {self.size}')

        l = layer
        l2 = self.size - 1 - layer
        f = lambda i : self.faces[i].get_face()
        ft = lambda i : np.transpose(self.faces[i].get_face())
        # swap matrix faces 0, 2, 4, 5
        if clockwise:
            f(0)[[l2]], f(2)[:, [l2]], f(4)[:, [l]], f(5)[[l]] = ft(2)[[l2]], ft(5)[:, [l]], ft(0)[:, [l2]], ft(4)[[l]]
            f(0)[[l2]] = np.flip(f(0)[[l2]])
            f(5)[[l]] = np.flip(f(5)[[l]])
        else:
            f(0)[[l2]], f(2)[:, [l2]], f(4)[:, [l]], f(5)[[l]] = ft(4)[[l]], ft(0)[:, [l2]], ft(5)[:, [l]], ft(2)[[l2]]
            f(2)[:, [l2]] = np.flip(f(2)[:, [l2]])
            f(4)[:, [l]] = np.flip(f(4)[:, [l]])


        # rotate face
        if layer == 0:
            self.faces[3].rotate(clockwise=clockwise, times=1)
        elif layer == self.size-1:
            self.faces[1].rotate(clockwise=(not clockwise), times=1)

    def __str__(self):
        result = ""
        # Top
        for row in range(self.size):
            result += ' ' * (3 * 3 * 2)
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
            result += ' ' * (3 * 3 * 2)
            for col in range(self.size):
                num = self.faces[5].get_face()[row][col]
                result += self.n_to_c(num)
            result += '\n'
        return result


if __name__ == '__main__':
    cube = RubikCube()
    print(cube)
    cube.turn_z(layer=2, clockwise=False)
    print(cube)
