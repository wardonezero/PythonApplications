from collections.abc import Iterable


# chunk_generator(iterable, size)
#  Yield successive size-sized chunks from an iterable.
def chunkGenerator(iterable, size: int):
    if not isinstance(iterable, Iterable):
        raise TypeError(f"{type(iterable)} object is not iterable")
    if len(iterable) < 1:
        raise TypeError("chunkGenerator() of empty iterable")

    if not isinstance(size, int):
        raise TypeError(f"{type(size)} object is not int")

    if size < 1:
        raise ValueError("chunk size must be greater than 0")

    if len(iterable) < size or len(iterable) % size != 0:
        raise ValueError("Not enough elements in iterable to fill chunks")

    if size > len(iterable):
        raise ValueError("chunk size must be less than or equal to iterable size")

    for i in range(0, len(iterable), size):
        yield tuple(iterable[i : i + size])


print(list(chunkGenerator([1, 2, 3, 4, 5, 6, 7, 8], 2)))


# Write a generator function transpose_rows(matrix) that takes a 2D matrix (list of lists) and yields one row at a time from its transposed version.
def transposeRows(matrix):
    if not isinstance(matrix, list):
        raise TypeError(f"{type(matrix)} object is not list")

    if not matrix:
        raise TypeError("transposeRows() of empty matrix")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("transposeRows() of non-list matrix")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("transposeRows() of non-rectangular matrix")

    for i in range(len(matrix[0])):
        yield [matrix[j][i] for j in range(len(matrix))]


matrix = [[1, 2, 3], [4, 5, 6]]

print(list(transposeRows(matrix)))

# Create a generator function repeat_element(element, times) that yields the given element a specified number of times. Test this generator with different inputs.
def repeatElement(element,times:int):
    if not isinstance(times, int):
        raise TypeError(f"{type(times)} object is not int")
    if times < 1:
        raise ValueError("times must be greater than 0")
    while times > 0:
        yield element
        times -= 1


#sliding_window(iterable, window_size)
# Yield a sliding window of the given size from the iterable.
# Example: sliding_window([1,2,3,4], 3) → yields (1,2,3), (2,3,4)

def slidingWindow(iterable, windowSize: int):
    if not isinstance(iterable, Iterable):
        raise TypeError(f"{type(iterable)} object is not iterable")
    if len(iterable) < 1:
        raise TypeError("slidingWindow() of empty iterable")

    if not isinstance(windowSize, int):
        raise TypeError(f"{type(windowSize)} object is not int")

    if windowSize < 1:
        raise ValueError("window size must be greater than 0")

    if windowSize > len(iterable):
        raise ValueError("window size must be less than or equal to iterable size")

    for i in range(len(iterable) - windowSize + 1):
        yield tuple(iterable[i : i + windowSize])
        
print(list(slidingWindow([1, 2, 3, 4], 3)))