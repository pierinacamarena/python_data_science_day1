import numpy as np


def is_list_of_lists(var: object) -> bool:
    """
    Check if the variable is a list and all its elements are lists.

    Parameters:
    - var: The variable to check.

    Returns:
    - bool: True if the variable is a list and all its elements are lists,
    False otherwise.
    """
    if not isinstance(var, list):
        return False

    return all(isinstance(element, list) for element in var)


def lists_of_same_size(lst: list) -> bool:
    """
    Check if 'lst' is a 2D list where all inner lists have the same size.

    Parameters:
    - lst: A 2D list or similar iterable.

    Returns:
    - bool: True if all inner lists have the same size, False otherwise.
    """
    try:
        array = np.array(lst)
        if array.dtype == object or array.ndim != 2:
            return False
        return True
    except Exception as error:
        print(error)
        return False


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a list of lists (family) from the 'start' index to the 'end' index,
    ensuring all lists are of the same size.

    Validates input types and conditions before slicing. If validation fails,
    it raises an exception with an error message.
    After slicing, it prints the original and new shapes of the 'family' array.
    Returns the sliced portion as a list of lists.

    Parameters:
    - family (list): A list of lists to slice.
    - start (int): Start index for slicing.
    - end (int): End index for slicing, exclusive.

    Returns:
    - list: A sliced portion of 'family' as a list of lists
    or an empty list on error.

    Raises:
    - ValueError: If 'family' is not a list of lists, if lists in 'family'
    are not of the same size, if 'start' or 'end' are not integers,
    or if the 'end' index is not valid.
    """

    try:
        # Step0 handle errors
        if not is_list_of_lists(family):
            raise ValueError("Error: family must be a list of lists")
        if not lists_of_same_size(family):
            raise ValueError("Error: lists are not of the same size")
        if not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("Error: start and end must be integers")
        if not family[end - 1]:
            raise ValueError("Error: end index not valid")

        # Step 1 Convert list to numpy array
        array_family = np.array(family)

        # Step 2 print shape
        size = np.shape(array_family)
        print(f"My shape is : {size}")

        # Step 3 truncate the list
        sliced_array = array_family[start: end]

        # Step 4 print new shape
        size = np.shape(sliced_array)
        print(f"My new shape is : {size}")

        # Step 5 return the truncated list
        return sliced_array.tolist()

    except Exception as error:
        print(error)
        return []
