class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value: str):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 50, 'M': 1000}
        int_val = 0

        for i in range(len(value)):
            if rom_val[value[i]] > rom_val[value[i-1]]:
                pass
            else:
                int_val += rom_val[value[i]]
