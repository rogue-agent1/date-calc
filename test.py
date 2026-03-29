from date_calc import is_leap, days_in_month, day_of_week, add_days, diff_days, date_range
assert is_leap(2000) and is_leap(2024) and not is_leap(1900) and not is_leap(2023)
assert days_in_month(2024, 2) == 29
assert days_in_month(2023, 2) == 28
assert day_of_week(2026, 3, 29) == "Sun"
assert add_days(2026, 1, 1, 365) == (2027, 1, 1)
assert add_days(2024, 2, 28, 1) == (2024, 2, 29)
assert diff_days(2026, 1, 1, 2026, 12, 31) == 364
r = date_range(2026, 3, 28, 2026, 3, 30)
assert len(r) == 3
print("date_calc tests passed")
