import json


def data_load(file_path):
    with open(file_path, encoding='utf-8') as json_file:
        return json.loads(json_file.read())


# Создает словарь {'id': 'value'} из Values
def values_map(obj, val_dict={}):
    if 'values' in obj.keys():
        for row in obj['values']:
            id_from_values = row.get('id')
            val_from_values = row.get('value')
            val_dict[id_from_values] = val_from_values
        return val_dict


# Создает словарь {'id': 'title'} из Structure
def title_map(obj, title_dict=None):
    if title_dict is not None:
        title_dict = title_dict
    else:
        title_dict = dict()
    if isinstance(obj, dict):
        if 'id' in obj and 'title' in obj:
            title_dict[obj['id']] = obj['title']

        for param in obj.get('params', list()):
            title_map(param, title_dict)

        for value in obj.get('values', list()):
            title_map(value, title_dict)

        return title_dict


# Ищет 'id' в структуре, проверяет есть ли найденный 'id' в ключах в словаре из values
# если есть, то проверяет есть ли значение в словаре с title из структуры
def swap(obj, values, title):
    if isinstance(obj, dict):
        if 'id' in obj:
            if obj['id'] in values.keys():
                if values[obj['id']] in title:
                    obj['value'] = (title.get(values[obj['id']]))
                else:
                    obj['value'] = values[obj['id']]
        for param in obj.get('params', list()):
            swap(param, values, title)
        for value in obj.get('values', list()):
            swap(value, values, title)
    return obj


try:
    # data_structure = data_load('TestcaseStructure.json')
    data_structure = data_load('ValidTestcaseStructure.json')
    # data_values = data_load('Values.json')
    data_values = data_load('ValidValues.json')
except json.JSONDecodeError:
    error_dict = {'error': {'message': 'Входные файлы некорректны'}}
    with open('result\\error.json', 'w') as outerror:
        json.dump(error_dict, outerror, indent=2, ensure_ascii=False)

else:
    title = title_map(data_structure)
    values = values_map(data_values)
    update = swap(data_structure, values, title)
    with open('result\\StructureWithValues.json', 'w') as outfile:
        outfile.write(json.dumps(update, indent=2, ensure_ascii=False))
