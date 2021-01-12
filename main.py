
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]


def extract_full_name(name_list):
    return list(map(lambda n: n["first"] + " " + n["last"], name_list))


print(extract_full_name(names))
