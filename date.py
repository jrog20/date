from datetime import datetime

# format date from string '1/1/2017' to 'YYYYMMDD HH:mm:ss'
my_datetime_str = '1/1/2017'
my_formatted_date = datetime.strptime(my_datetime_str, "%m/%d/%Y").strftime('%Y%m%d %H:%M:%S')

# Print the formatted datetime
print('my formatted date:', my_formatted_date)

# The strptime() method:
  # strptime means string parser. 
  # This method will convert a string to datetime object.

  # syntax:
    # time.strptime(string, format)
  
  # parameters: 
    # string − This is the time in string format which would be parsed based on the given format.
    # format − This is the directive which would be used to parse the given string.

# The strftime() method:
  # strftime means string formatter.
  # This method will format a datetime object to string format.
