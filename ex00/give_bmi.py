def all_integers_or_floats(lst) -> bool:
    """Check if all items in the list are integers or floats."""
    return all((isinstance(item, int)
                or isinstance(item, float)) for item in lst)


def all_values_are_positive(lst: list) -> bool:
    """Check if all items in the list are positive."""
    return all(item > 0 for item in lst)


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate and return a list of BMI values for
    corresponding heights and weights.

    Args:
        height (list[int | float]): A list of heights in meters.
        weight (list[int | float]): A list of weights in kilograms.

    Returns:
        list[int | float]: A list of BMI values
        calculated using the formula weight/(height^2).

    Raises:
        ValueError: If the number of heights and weights do not match,
        if any height or weight
        is not a positive number,
        or if they are not of type int or float.
    """
    try:
        if len(height) != len(weight):
            raise ValueError("Error: invalid number of weights or heights")

        if not all_integers_or_floats(height + weight):
            raise ValueError("Error: height and weight must be "
                             "integers or floats")

        if not all_values_are_positive(height + weight):
            raise ValueError("Error: the values of height or "
                             "weight must be positive")

        bmis = [w / h ** 2 for h, w in zip(height, weight)]
        return bmis

    except Exception as error:
        print(error)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Determine whether each BMI value in the list exceeds a specified limit.

    Args:
        bmi (list[int | float]): A list of BMI values.
        limit (int): The threshold BMI value to compare against.

    Returns:
        list[bool]: A list of boolean values indicating
        whether each BMI exceeds the limit.

    Raises:
        ValueError: If any BMI value or the limit is not a positive number,
        or if they are not of the correct type
        (BMI values should be int or float, limit should be int).
    """
    try:
        if not isinstance(limit, int) or limit <= 0:
            raise ValueError("Error: limit must be a positive integer")

        if not all_integers_or_floats(bmi):
            raise ValueError("Error: Bmi's must be integers or floats")

        if not all_values_are_positive(bmi):
            raise ValueError("Error: the values of bmis must be positive")

        return [b > limit for b in bmi]

    except Exception as error:
        print(error)
        return []
