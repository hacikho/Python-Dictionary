_dict = {'ID': [{'type': 'Custom_Budget_ID', '_value_1': '124520 2021 Forecast'}]}
print(_dict.get("ID"))

print(_dict.get("ID")[0])

print((_dict.get("ID")[0]).get("_value_1"))