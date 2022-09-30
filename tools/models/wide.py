from .layer import VerticalLayer

class WideLayer(VerticalLayer):

    def __init__(self, context, horizontal):

        self.horizontal = horizontal
        super().__init__(context)

    def apply(self, text, *, transform = lambda x: decode(x)):
        result = [self.horizontal.apply(letter) for letter in text]

      return encode(result)


            

    