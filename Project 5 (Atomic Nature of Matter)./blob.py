import stdio


# A data type to represent a blob.
class Blob:
    # Constructs an empty blob.
    #  Instance variables:
    #  x-coordinate of center of mass, _x (float)
    #  y-coordinate of center of mass, _y (float)
    #  Number of pixels, _pixels (int)
    def __init__(self):
        #  Initialize the instance variables appropriately.
        self._x = 0.0  # x-coordinate of center of mass
        self._y = 0.0  # y-coordinate of center of mass
        self._pixels = 0  # number of pixels

# Adds pixel (x, y) to this blob.
    def add(self, x, y):
        # to update the center of mass of blob b
        x_cord = self._x * self._pixels
        y_cord = self._y * self._pixels
        #  Use the idea of running average1
        self._x = (x_cord + x) / (self._pixels+1)
        self._y = (y_cord + y) / (self._pixels+1)

        #  Increment the number of pixels in blob b by 1
        self._pixels += 1

    # Returns the mass of this blob, ie, the number of pixels in it.
    def mass(self):
        return self._pixels

    # Returns the Euclidean distance between the center of mass of this blob and the center of
    # mass of the other blob.
    def distanceTo(self, other):
        return ((self._x - other._x) ** 2 + (self._y - other._y) ** 2) ** 0.5

    # Returns a string representation of this blob.
    def __str__(self):
        return '%d (%.4f, %.4f)' % (self._pixels, self._x, self._y)


# Unit tests the data type (DO NOT EDIT).
def _main():
    a = Blob()
    a.add(0, 0)
    b = Blob()
    while not stdio.isEmpty():
        x = stdio.readFloat()
        y = stdio.readFloat()
        b.add(x, y)
    stdio.writeln('a          = ' + str(a))
    stdio.writeln('b          = ' + str(b))
    stdio.writeln('dist(a, b) = ' + str(a.distanceTo(b)))


if __name__ == '__main__':

    _main()
