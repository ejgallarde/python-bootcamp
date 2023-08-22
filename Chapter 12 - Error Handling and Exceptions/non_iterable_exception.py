class NonIterableError(TypeError):
    def __init__(self, obj):
        super().__init__(f"'{type(obj).__name__}' object is not iterable")


def concatenate_lists(list1, list2):
    if not isinstance(list1, list):
        raise NonIterableError(list1)
    if not isinstance(list2, list):
        raise NonIterableError(list2)
    return list1 + list2


# Example usage
list1 = [1, 2, 3]
list2 = 4  # This is not iterable
try:
    concatenated = concatenate_lists(list1, list2)
except NonIterableError as e:
    print(f"Custom Exception: {e}")
