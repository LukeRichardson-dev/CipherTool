from models.layer import Context, Layer

def inv_mod(a, m):

    for b in range(m):

        res = a * b % m
        if res == 1:
            return b

class AffineKeyContext:

    def __init__(self, a, b):
        self.a, self.b = a, b

    @property
    def key(self):
        return self.a, self.b

class Affine(Layer):

    @staticmethod
    def shift(char, a, b):
        x = ord(char.upper()) - 65

        return chr(((x - b) * inv_mod(a, 26)) % 26 + 65)

    def apply(self, text, context: Context):
        a, b = context.key

        new = ""
        for char in text:

            if 0 <= ord(char) - 65 < 26:

                new += self.shift(char, a, b)
                continue
                
            new += char

        return new, context