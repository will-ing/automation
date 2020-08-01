import re


def stringify_file(file):
    with open(file, "r") as f:
        return f.read().lower()


def get_email(file):
    opened = stringify_file(file)
    emails = re.findall(r'\S+@\S+', opened)
    return emails


def get_phone_numbers(file):
    """
    Gets phone numbers from a document

    REF: http://www.learningaboutelectronics.com/Articles/How-to-match-a-phone-number-in-Python-using-regular-expressions.php

    Args:
        file ([type]): [description]

    Returns:
        [type]: [description]
    """
    opened = stringify_file(file)
    regex = r'(\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s *\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}|\d{10})'
    phone_numbers = re.findall(regex, opened)
    return phone_numbers


def store_info(info, file):
    info.sort()
    with open(file, "w+") as f:
        for i in info:
            f.write(i + '\n')


email_data = get_email('assets/potential-contacts.txt')

phone_data = get_phone_numbers('assets/potential-contacts.txt')

store_info(email_data, 'assets/emails.txt')
store_info(phone_data, 'assets/phone_numbers.txt')
