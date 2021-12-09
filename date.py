from datetime import datetime, timedelta

# ************************************************************
# Goal #1:
# Format date from string '1/1/2017' to string 'YYYYMMDD HH:mm:ss'
# ************************************************************

my_datetime_str = '1/1/2017'

# The strptime() method:
  # strptime means string parser. 
  # This method will convert a string to datetime object.

  # syntax:
    # time.strptime(string, format)
  
  # parameters: 
    # string − This is the time in string format which would be parsed based on the given format.
    # format − This is the directive which would be used to parse the given string.

parsed_date = datetime.strptime(my_datetime_str, "%m/%d/%Y")

# The strftime() method:
  # strftime means string formatter.
  # This method will format a datetime object to string format.

formatted_date = parsed_date.strftime('%Y%m%d %H:%M:%S')

print('---------------------------------------------------')
print('GOAL #1: Format date from string', my_datetime_str, 'to string YYYYMMDD HH:mm:ss')

# Print the parsed datetime object
print('----------------parsed date------------------------')
print('Type =', type(parsed_date))
print('Type is object? =', isinstance(parsed_date, object))
print('Parsed date:', parsed_date)

# Print the formatted datetime string
print('----------------formatted date---------------------')
print('Type =', type(formatted_date))
print('Type is string? =', isinstance(formatted_date, str))
print('Formatted date:', formatted_date)
print('---------------------------------------------------')

# ************************************************************
# Goal #2:
# Add one day to the formatted date
# ************************************************************

# The variable formatted_date is currently a string, so we need use the parsed_date variable,
# which is a datetime object, which can be added to a timedelta to produce an updated datetime object.

# A timedelta object represents a duration, the difference between two dates or times.
# class datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
# Note: we are only using days here

# create a new variable to hold the amount of time we want to move forward
plus_one_day = timedelta(days=1)

# create a new variable to increment our datetime object by the time identified above
date_plus_one = parsed_date + plus_one_day

# now we format the newly incremented date
formatted_date_plus_one = date_plus_one.strftime('%Y%m%d %H:%M:%S')

print('---------------------------------------------------')
print('GOAL #2: Add one day to the formatted date')

# Print the formatted datetime *PLUS ONE DAY*
print('----------------date plus one----------------------')
print('Formatted date plus one day:', formatted_date_plus_one)
print('---------------------------------------------------')
