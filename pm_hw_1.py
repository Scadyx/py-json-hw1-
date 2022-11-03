import json
from datetime import datetime
from math import floor
from collections import defaultdict


if __name__ == '__main__':
    file_path = '.\\data.jsonl'

    with open(file_path, 'r') as fin:
        data = [json.loads(line) for line in fin]

    for dct in data:
        dct['time_created'] = datetime.fromtimestamp(dct['time_created'])

    seen = set()
    unique_data = []
    for dct in data:
        if (dct['name'], dct['time_created']) not in seen:
            seen.add((dct['name'], dct['time_created']))
            unique_data.append(dct)

    ages = []
    for dct in unique_data:
        if dct.get('age'):
            ages.append(dct['age'])

    mean_age = floor(sum(ages) / len(ages))

    for dct in unique_data:
        if not dct.get('age'):
            dct['age'] = mean_age

    gender_dict = defaultdict(int)
    last_name_dict = defaultdict(int)
    city_dict = defaultdict(int)

    for dct in unique_data:
        if dct.get('gender'):
            gender_dict[dct['gender']] += 1
        if dct.get('last_name'):
            last_name_dict[dct['last_name']] += 1
        if dct.get('city'):
            city_dict[dct['city']] += 1

    most_common_gender = max(gender_dict, key=gender_dict.get)
    most_common_last_name = max(last_name_dict, key=last_name_dict.get)
    most_common_city = max(city_dict, key=city_dict.get)

    for dct in unique_data:
        if not dct.get('gender'):
            dct['gender'] = most_common_gender
        if not dct.get('last_name'):
            dct['last_name'] = most_common_last_name
        if not dct.get('city'):
            dct['city'] = most_common_city
        if not dct.get('premium'):
            dct['premium'] = None
        if not dct.get('ip'):
            dct['ip'] = None
        if not dct.get('birth_day'):
            dct['birth_day'] = None

    for dct in unique_data:
        f_name = dct['time_created'].strftime("%Y-%m-%d") + '.jsonl'
        dct['time_created'] = int(round(dct['time_created'].timestamp()))
        with open(f_name,'a') as f:
            json.dump(dct, f)
            f.write('\n')







