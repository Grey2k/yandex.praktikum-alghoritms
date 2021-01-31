def leap_year(year: int) -> bool:
    """
    Function returns True if year is a leap, False otherwise

    :param int year: Year to check leap or not
    :return: bool
    """

    if not isinstance(year, int):
        TypeError("Year must be an int type")

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    return year % 4 == 0
