import json


INPUT_FILE = "input.csv"


def csv_to_list_dict(file, newline='\n', separ=',') -> list[dict]:
    total = []
    with open(file, 'r') as input_f:  # не могу убрать /n
        strings = [line.replace(newline, '').split(separ) for line in input_f]
        for i in range(1, len(strings)):
            dict_ = dict(zip(strings[0], strings[i]))
            total.append(dict_)
    return total


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
# я плакал пока делал оцените
