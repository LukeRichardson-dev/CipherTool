class Context:

    @property
    def key(self):
        ...

class VerticalLayer:

    def __init__(self, context):

        self.context = context

    def apply(self, text):

        return text

class HorizontalLayer:

    def __init__(self, context):

        self.context = context

    def apply(self, char):

        return char

  