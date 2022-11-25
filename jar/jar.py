class Jar:

    def __init__(self, capacity=12):
        """Initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can
            fit in the cookie jar.

        :param capacity: int
        """

        if capacity < 0:
            raise ValueError

    def __str__(self):
        """Return a string with n 🍪 cookies, where n is the number of cookies in the jar

        :return: string of 🍪s
        """
        ...

    def deposit(self, n):
        """Add n cookies to the cookie jar.

        :param n: integer
        """

        size += n
        # Raise a ValueError if adding that many cookies would exceed the jar's capacity.
        ...

    def withdraw(self, n):
        """Remove n cookies from the cookie jar.

        :param n: integer
        """

        # Raise a ValueError if there aren't enough cookies in the cookie jar.
        ...

    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        return self.size


jar = Jar(capacity=10)
print(str(Jar))
print(jar.capacity)
print(jar.size)
