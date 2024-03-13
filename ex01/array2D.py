import numpy as np


def is_list_of_lists(var: object) -> bool:
    """
    Check if the variable is a list and all its elements are lists.

    Parameters:
    - var: The variable to check.

    Returns:
    - bool: True if the variable is a list and all its elements are lists, False otherwise.
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
    except:
        return False

def slice_me(family: list, start: int, end: int) -> list:

    try:
        #Step handle errors
        if not is_list_of_lists(family):
            raise ValueError("Error: family must be a list of lists")
        if not lists_of_same_size(family):
            raise ValueError("Error: lists are not of the same size")
        if not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("Error: start and end must be integers")
        if not family[end - 1]:
            raise ValueError("Error: end index not valid")
    
        #convert list to numpy array
        array_family = np.array(family)
        
        #Step 1 print shape
        size = np.shape(array_family)
        print(f"My shape is : {size}")

        #Step 2 truncate the list
        sliced_array = array_family[start : end]
        
        #Step 3 print new shape
        size = np.shape(sliced_array)
        print(f"My new shape is : {size}")
        
        return sliced_array.tolist()

        #Step 4 return the truncated list

    except Exception as error:
        print(error)
        return []