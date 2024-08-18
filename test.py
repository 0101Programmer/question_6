class Figure:
    SIDES_COUNT = 0

    def __init__(self, filled, r, g, b, *args, sides=None, color=None):
        if filled == 1 or filled == 0:
            self.filled = bool(filled)
        else:
            self.filled = True
        if color is None:
            color = [r, g, b]
            self.__color = color
        if sides is None:
            if len(args) == self.SIDES_COUNT:
                self.__sides = args
            else:
                self.__sides = [self.SIDES_COUNT] * self.SIDES_COUNT

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
            print(f'Цвет ({r},{g},{b}) корректен')
        else:
            print('Цвет некорректен')

    def get_is_valid_color(self, r, g, b):
        return self.__is_valid_color(r, g, b)

    def __is_valid_sides(self, *args):
        if len(args) == len(self.__sides):
            for i in args:
                if i > 0 and i % 1 == 0:
                    i += 1
                    continue
                else:
                    return False
            return True
        else:
            return False

    def get_is_valid_sides(self, *args):
        return self.__is_valid_sides(*args)

    def set_color(self, r, g, b):
        if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b
        else:
            print('Невозможно сменить цвет')

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.SIDES_COUNT:
            self.__sides = new_sides


class Cube(Figure):
    SIDES_COUNT = 12

    def __init__(self, filled, r, g, b, *args):
        super().__init__(filled, r, g, b, *args)
        new_args = []
        x = 1
        if len(args) == self.SIDES_COUNT:
            for i in args:
                n = args[x]
                if i == n:
                    new_args.append(i)
                    if x < (len(args) - 1):
                        x += 1
                    self.set_sides(new_args)
                else:
                    right_side = [self.SIDES_COUNT] * self.SIDES_COUNT
                    self.set_sides(right_side)
                    break
        else:
            right_side = [self.SIDES_COUNT] * self.SIDES_COUNT
            self.set_sides(right_side)


cu = Cube(0, 55, 66, 188, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
# cu.set_sides(55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55)
print(cu.get_sides())
cu1 = Cube(0, 55, 66, 188, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
print(cu.get_sides())

