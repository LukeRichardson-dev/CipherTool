class Context:

    @property
    def key(self):
        ...

class Layer:

    def apply(self, text, context):

        return text, context