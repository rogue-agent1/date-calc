#!/usr/bin/env python3
"""Date arithmetic calculator."""
from datetime import date, timedelta

def add_days(d, n):
    return d + timedelta(days=n)

def diff_days(d1, d2):
    return (d2 - d1).days

def add_business_days(d, n, holidays=None):
    holidays = set(holidays or [])
    direction = 1 if n >= 0 else -1
    remaining = abs(n)
    current = d
    while remaining > 0:
        current += timedelta(days=direction)
        if current.weekday() < 5 and current not in holidays:
            remaining -= 1
    return current

def business_days_between(d1, d2, holidays=None):
    holidays = set(holidays or [])
    count = 0
    current = min(d1, d2) + timedelta(days=1)
    end = max(d1, d2)
    while current <= end:
        if current.weekday() < 5 and current not in holidays:
            count += 1
        current += timedelta(days=1)
    return count

def is_weekend(d):
    return d.weekday() >= 5

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month in (1,3,5,7,8,10,12): return 31
    if month in (4,6,9,11): return 30
    return 29 if is_leap_year(year) else 28

def age(birthdate, as_of=None):
    if as_of is None: as_of = date.today()
    years = as_of.year - birthdate.year
    if (as_of.month, as_of.day) < (birthdate.month, birthdate.day):
        years -= 1
    return years

if __name__ == "__main__":
    today = date.today()
    print(f"Today: {today}")
    print(f"+10 business days: {add_business_days(today, 10)}")

def test():
    d = date(2026, 3, 29)
    assert add_days(d, 5) == date(2026, 4, 3)
    assert diff_days(date(2026, 1, 1), date(2026, 12, 31)) == 364
    # Business days
    mon = date(2026, 3, 23)  # Monday
    assert add_business_days(mon, 5) == date(2026, 3, 30)
    assert business_days_between(mon, date(2026, 3, 27)) == 4
    # Weekend
    assert is_weekend(date(2026, 3, 28))  # Saturday
    assert not is_weekend(date(2026, 3, 23))  # Monday
    # Leap year
    assert is_leap_year(2024) and not is_leap_year(2023)
    assert is_leap_year(2000) and not is_leap_year(1900)
    assert days_in_month(2024, 2) == 29
    assert days_in_month(2023, 2) == 28
    # Age
    assert age(date(2000, 6, 15), date(2026, 3, 29)) == 25
    print("  date_calc: ALL TESTS PASSED")
