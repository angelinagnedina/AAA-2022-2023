class Color:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red: int = 0, green: int = 0, blue: int = 0):
        if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
            raise 'Incorrect input'
        self.rgb = (red, green, blue)

    def __repr__(self):
        return (f'{self.START};{self.rgb[0]};{self.rgb[1]};{self.rgb[2]}'
                f'{self.MOD}●{self.END}{self.MOD}')

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.rgb == other.rgb

    def __hash__(self):
        return hash(self.rgb)

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError
        new_rgb = [min(self.rgb[i] + other.rgb[i], 255) for i in range(3)]
        return Color(*new_rgb)

    def __mul__(self, c: float):
        if not 0 <= c <= 1:
            raise ValueError

        cl = -256 * (1 - c)
        F = 259 * (cl + 255)/(255 * (259 - cl))
        new_rgb = (int(F * (col - 128) + 128) for col in self.rgb)
        return Color(*new_rgb)

    def __rmul__(self, c: float):
        return self.__mul__(c)


if __name__ == '__main__':
    orange1 = Color(255, 165, 0)
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]

    assert not (green == red), 'Wrong!'
    assert (orange1 == orange2), 'Wrong!'

    assert red + green == Color(255, 255, 0), 'Wrong!'

    assert len(set(color_list)) == 3, 'Wrong!'

    print(0.5*red)
