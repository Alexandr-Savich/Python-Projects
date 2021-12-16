class Color:
    def __init__(self, r, g, b):
        self.red_level = r
        self.green_level = g
        self.blue_level = b

    def __repr__(self):
        END = '\033[0'
        START = '\033[1;38;2'
        MOD = 'm'
        return f'{START};{self.red_level};{self.green_level};{self.blue_level}{MOD}●{END}{MOD}'

    def __eq__(self, other):
        if not isinstance(other, Color):
            raise TypeError("Other must be the type of color")
        if self.red_level == other.red_level and self.green_level == other.green_level and self.blue_level == other.blue_level:
            return True
        else:
            return False

    def __add__(self, other):
        if not isinstance(other, Color):
            raise TypeError("Other must be the type of color")
        return Color(min(255, other.red_level + self.red_level), min(255, other.green_level + self.green_level),
                     min(255, other.blue_level + self.blue_level))

    def __hash__(self):
        return hash((self.red_level,
                     self.green_level,
                     self.blue_level))

    def __mul__(self, other):
        return Color(self.red_level,
                     self.green_level,
                     self.blue_level)

    def _contrast(self, c, value):
        cl = (-256) * (1 - c)
        f = (259 * (cl + 259)) / (255 * (259 - cl))
        l = f * (value - 128) + 128
        return int(l)
    
    
if __name__ == '__main__':
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange1 = Color(255, 165, 0)
    orange2 = Color(255, 165, 0)
    color_list = [red, green, orange1, orange2]
    print(set(color_list))
