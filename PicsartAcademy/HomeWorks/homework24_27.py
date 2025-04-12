# 24/27

from collections.abc import Iterable
from functools import reduce

# 1. Implementing filter


def customFilter(function, iterable):
    if not hasattr(iterable, "__iter__"):
        raise TypeError(f"{type(iterable)} object is not iterable")
    if not callable(function) and function is not None:
        raise TypeError(f"{type(function)} object is not callable")
    if function == None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]


# 2. Implementing map


def customMap(function, *iterables):
    if not callable(function):
        raise TypeError(f"{type(function)} object is not callable")
    for iterable in iterables:
        if not isinstance(iterable, Iterable):
            raise TypeError(f"{type(iterable)} object is not iterable")
    minLen = len(min(iterables, key=len))
    for i in range(minLen):
        yield function(*[iterable[i] for iterable in iterables])


# 3. Implementing zip


def customZip(*iterables):
    for iterable in iterables:
        if not isinstance(iterable, Iterable):
            raise TypeError(f"{type(iterable)} object is not iterable")
    minLen = min(len(iterable) for iterable in iterables)
    for i in range(minLen):
        yield tuple([iterable[i] for iterable in iterables])


# 4. Implementing reduce


def customReduce(function, iterable, initial=None):
    if not callable(function):
        raise TypeError(f"{type(function)} object is not callable")
    if not isinstance(iterable, Iterable):
        raise TypeError(f"{type(iterable)} object is not iterable")
    if len(iterable) < 1:
        raise TypeError("customReduce() of empty iterable with no initial value")
    if initial is None:
        start, result = 1, iterable[0]
    else:
        start, result = 0, initial
    while start < len(iterable):
        result = function(result, iterable[start])
        start += 1
    return result


# 5. Implementing enumerate


def customEnumerate(iterable, start=0):
    if not isinstance(iterable, Iterable):
        raise TypeError(f"{type(iterable)} object is not iterable")
    if not isinstance(start, int):
        raise TypeError(f"{type(start)} object is not int")
    for i in iterable:
        yield start, iterable[start]
        start += 1


if __name__ == "__main__":
    print(" filter", tuple(filter(None, "abc")))
    print("Cfilter", customFilter(None, "abc"))
    print(" map", tuple(map(lambda x, y: x + y, "abc", "123")))
    print("Cmap", tuple(customMap(lambda x, y: x + y, "abc", "123")))
    print(" zip", tuple(zip("abc", "123")))
    print("Czip", tuple(customZip("abc", "123")))
    print(" reduce", reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6]))
    print("Creduce", customReduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
    print(" enumerate", tuple(enumerate("abc")))
    print(" enumerate", tuple(enumerate("abc", -1)))
    print("Cenumerate", tuple(customEnumerate("abc")))
    print("Cenumerate", tuple(customEnumerate("abc", -1)))
