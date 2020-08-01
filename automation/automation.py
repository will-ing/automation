import re


def stringify_file(file):
    """
    Turns a txt file in to a string.

    Args:
        file (.txt): file with txt extension

    Returns:
        str: Returns a string of a file
    """
    with open(file, "r") as f:
        return f.read().lower()


def get_email(file):
    """
    Get the emails from a document. Removes duplicates by converting to dict.

    Args:
        file (.txt): file with txt extension

    Returns:
        list: Returns a list of strings with emails
    """
    opened = stringify_file(file)
    emails = re.findall(r'\S+@\S+', opened)
    emails = list(dict.fromkeys(emails))
    return emails


def get_phone_numbers(file):
    """
    Gets phone numbers from a document

    REF: http://www.learningaboutelectronics.com/Articles/How-to-match-a-phone-number-in-Python-using-regular-expressions.php

    Args:
        file (.txt): file with txt extension. Removes duplicates by converting to dict

    Returns:
        list: Returns a list of strings with phone numbers
    """
    opened = stringify_file(file)
    regex = r'(\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s *\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}|\d{10})'
    phone_numbers = re.findall(regex, opened)
    phone_numbers = list(dict.fromkeys(phone_numbers))
    return phone_numbers


def store_info(info, file):
    """
    Stores data in to a file sorted in ascending order

    Args:
        info (list): list of data you want to write
        file (.txt): file with txt extension that you want to write to.
    """
    info.sort()
    list_format = stringify_file(file).split('\n')

    with open(file, "a+") as f:
        for i in info:
            if i in list_format:
                return False
            else:
                f.write(i + '\n')


email_data = get_email('assets/potential-contacts.txt')

phone_data = get_phone_numbers('assets/potential-contacts.txt')

store_info(email_data, 'assets/emails.txt')
store_info(phone_data, 'assets/phone_numbers.txt')
