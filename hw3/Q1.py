import re

validRegex = re.compile(r"(^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$)")
invalidRegex = re.compile(r"(^(.+)@(.+)$)")


# Q1
def sort_valid_emails(file):
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
