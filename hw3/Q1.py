import re

validRegex = re.compile(r"(^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$)")
invalidRegex = re.compile(r"(^(.+)@(.+)$)")


def sort_valid_emails(file):
    """
    This function checks whether there is an email address with the regex we implemented above.
    If it fits the regex, it will append it to the valid list, if it's not, we will check whether it looks like an email
    and if it, we will append it to the invalid list.

    :param file: file that contains email addresses
    :return: Valid emails list, Invalid emails list
    """
    with open(file) as f:
        lines = f.readlines()
        validemail = []
        invalidemail = []
        for line in lines:
            split_line = line.split()
            for split in split_line:
                if re.fullmatch(validRegex, split):
                    validemail.append(split)
                elif re.fullmatch(invalidRegex, split):
                    invalidemail.append(split)
    return f'Valid emails: {validemail} "\nInvalid emails: {invalidemail}'


if __name__ == '__main__':
    print(sort_valid_emails("email_check.txt"))
