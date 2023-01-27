# Program to display calendar of the given month and year

# importing calendar module
import calendar

y = int(input(Enter year:))  # year
m = int(input(Enter month:))    # month

# display the calendar
print(calendar.month(y, m))
