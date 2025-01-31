from dateutil import parser
import logging as log


# I have tried it with all possible extracted scenarios, it's working perfect.
def convert_date(input_date_str, desired_format="%d-%m-%Y"):
    try:
        parsed_date = parser.parse(input_date_str, dayfirst=True)

        formatted_date = parsed_date.strftime(desired_format)
        return formatted_date
    except ValueError as e:
        log.error(f"Error parsing date: {e}")
        return input_date_str


input_date = "12-23-2024"
# input_date = "26.08.2024"

result = convert_date(input_date, desired_format="%d/%m/%Y")
print(result)
