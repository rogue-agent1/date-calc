#!/usr/bin/env python3
"""date_calc - Date arithmetic: add/subtract days, diff, weekday, leap year."""
import sys

def is_leap(y): return y%4==0 and (y%100!=0 or y%400==0)
def days_in_month(y, m):
    return [0,31,29 if is_leap(y) else 28,31,30,31,30,31,31,30,31,30,31][m]
def days_in_year(y): return 366 if is_leap(y) else 365

def to_days(y, m, d):
    """Days from year 1."""
    total = 0
    for yr in range(1, y): total += days_in_year(yr)
    for mo in range(1, m): total += days_in_month(y, mo)
    return total + d

def from_days(n):
    y = 1
    while True:
        dy = days_in_year(y)
        if n <= dy: break
        n -= dy; y += 1
    m = 1
    while True:
        dm = days_in_month(y, m)
        if n <= dm: break
        n -= dm; m += 1
    return y, m, n

def add_days(y, m, d, delta):
    return from_days(to_days(y, m, d) + delta)

def diff_days(y1,m1,d1, y2,m2,d2):
    return to_days(y2,m2,d2) - to_days(y1,m1,d1)

def weekday(y, m, d):
    """0=Mon, 6=Sun (Zeller-like via day count)."""
    return (to_days(y, m, d) - 1) % 7  # year 1 jan 1 = Monday

def test():
    assert is_leap(2000) and is_leap(2024) and not is_leap(1900) and not is_leap(2023)
    assert days_in_month(2024, 2) == 29
    assert days_in_month(2023, 2) == 28
    assert diff_days(2024,1,1, 2024,12,31) == 365
    assert diff_days(2023,1,1, 2023,12,31) == 364
    assert add_days(2024,2,28, 1) == (2024, 2, 29)
    assert add_days(2024,2,29, 1) == (2024, 3, 1)
    assert add_days(2024,12,31, 1) == (2025, 1, 1)
    # 2024-01-01 is Monday
    assert weekday(2024, 1, 1) == 0
    print("date_calc: all tests passed")

if __name__ == "__main__":
    test() if "--test" in sys.argv else print("Usage: date_calc.py --test")
