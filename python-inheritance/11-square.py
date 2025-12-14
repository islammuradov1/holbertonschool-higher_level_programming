class Square(__import__('9-rectangle').Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
