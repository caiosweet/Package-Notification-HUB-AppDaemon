## globals.py
import secrets
import random
import re

def get_arg(args, key):
    key = args[key]
    if type(key) is str and key.startswith("secret_"):
        if key in secrets.secret_dict:
            return secrets.secret_dict[key]
        else:
            raise KeyError("Could not find {} in secret_dict".format(key))
    else:
        return key

def get_arg_list(args, key):
    arg_list = []
    if isinstance(args[key], list):
        arg = args[key]
    else:
        arg = (args[key]).split(",")
    for key in arg:
        if type(key) is str and key.startswith("secret_"):
            if key in secrets.secret_dict:
                arg_list.append(secrets.secret_dict[key])
            else:
                raise KeyError("Could not find {} in secret_dict".format(key))
        else:
            arg_list.append(key)
    return arg_list

## from list to plain text
def to_text(data: list)->str:
    return " ".join([str(item) for item in data])

## from text to list
def to_list(self, stringa)->list: 
    return list(stringa.replace(" ", "").split(","))

'''
used to replace special characters ans multiple space in message
'''
def replace_char(text: str, substitutions: dict):
    substrings = sorted(substitutions, key=len, reverse=True)
    regex = re.compile('|'.join(map(re.escape, substrings)))
    return regex.sub(lambda match: substitutions[match.group(0)], text)

def replace_regular(text: str, substitutions: list):
    for old,new in substitutions:
        text = re.sub(old, new, text.strip())
    return text
