def is_leap_year(year: int) -> bool:
    return bool(not year % 4 and (year % 100 or not year % 400))
