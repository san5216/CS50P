class Jar:

    def __init__(self, capacity=12):
        """Initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can
            fit in the cookie jar.

        :param capacity: int
        """
        self.capacity = capacity
        self._size = 0
        ...
        # self.size = ""
        # self.capacity = capacity

    def __str__(self):
        """Return a string with n 🍪 cookies, where n is the number of cookies in the jar

        :return: string of 🍪s
        """
        return "🍪" * self.size

    def deposit(self, n):
        """Add n cookies to the cookie jar.

        :param n: integer
        """
        self.size += n
        return self.size


    def withdraw(self, n):
        """Remove n cookies from the cookie jar.

        :param n: integer
        """
        self.size -= n
        return self.size



    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError

        if self.capacity < size:
            raise ValueError

        self._size = size


def main():
    jar = Jar(capacity=10)
    jar.deposit(3)
    print(f"capacity: {jar.capacity}")
    print(f"size: {jar.size}")
    print(str(jar))
    jar.withdraw(3)
    print(f"capacity: {jar.capacity}")
    print(f"size: {jar.size}")
    print(str(jar))
    jar.withdraw(4)
    print(f"capacity: {jar.capacity}")
    print(f"size: {jar.size}")
    print(str(jar))

if __name__ == '__main__':
    main()
