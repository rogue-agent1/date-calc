#!/usr/bin/env python3
"""Date calculation utilities. Zero dependencies."""

def is_leap(y): return y%4==0 and (y%100!=0 or y%400==0)
def days_in_month(y, m):
    return [0,31,29 if is_leap(y) else 28,31,30,31,30,31,31,30,31,30,31][m]
def days_in_year(y): return 366 if is_leap(y) else 365

def date_to_days(y, m, d):
    days = 0
    for yr in range(1, y): days += days_in_year(yr)
    for mo in range(1, m): days += days_in_month(y, mo)
    return days + d

def days_to_date(total):
    y = 1
    while total > days_in_year(y): total -= days_in_year(y); y += 1
    m = 1
    while total > days_in_month(y, m): total -= days_in_month(y, m); m += 1
    return y, m, total

def day_of_week(y, m, d):
    names = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    return names[(date_to_days(y, m, d) - 1) % 7]

def add_days(y, m, d, n):
    return days_to_date(date_to_days(y, m, d) + n)

def diff_days(y1, m1, d1, y2, m2, d2):
    return date_to_days(y2, m2, d2) - date_to_days(y1, m1, d1)

def date_range(y1, m1, d1, y2, m2, d2):
    start = date_to_days(y1, m1, d1); end = date_to_days(y2, m2, d2)
    return [days_to_date(d) for d in range(start, end + 1)]

if __name__ == "__main__":
    print(f"2026-03-29 is a {day_of_week(2026,3,29)}")
    print(f"30 days from now: {add_days(2026,3,29,30)}")
