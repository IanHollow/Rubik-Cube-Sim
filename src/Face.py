import numpy as np


class Face:
    def __init__(self, size: int, color: int):
        if size < 1:
            raise EnvironmentError("Size must be greater than 1")
        self.face = np.full(shape=(size, size), fill_value=color)
        # testing
        #self.face = np.array([x for x in range(size**2)]).reshape(size, size)

    def get_face(self):
        return self.face

    def rotate(self, clockwise: bool = True, times: int = 1) -> None:
        rot_num = (times*(3 if clockwise else 1)) % 4
        self.face = np.rot90(m=self.face, k=rot_num)

    def __str__(self):
        result = ""
        for row in self.face:
            for num in row:
                result += f' {num}{"" if len(str(num)) > 1 else " "}'
            result += '\n'
        return result

    def __eq__(self, other):
        if type(other) == type(self):
            return np.array_equal(self.face, other.face)
        else:
            return False


if __name__ == '__main__':
    face = Face(3, 1)
    print(face)
    face.rotate(clockwise=False, times=1)
    print(face)
