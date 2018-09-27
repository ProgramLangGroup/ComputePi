class Pie:
    def __init__(self, name, last):
        self.first = name
        self.last = last

    @property
    def fullname(self):
        return "%s %s" % (self.first, self.last)

    @fullname.setter
    def fullname(self, value):
        # this is much more complicated in real life
        first, last = value.split(" ", 1)
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        del self.first
        del self.last
