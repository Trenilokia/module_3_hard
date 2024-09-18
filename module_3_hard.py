data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(data_structure):
    if isinstance(data_structure, int):
        return data_structure
    elif isinstance(data_structure, str):
        return len(data_structure)
    elif isinstance(data_structure, list):
        return sum([calculate_structure_sum(item) for item in data_structure])
    elif isinstance(data_structure, tuple):
        return sum([calculate_structure_sum(item) for item in data_structure])
    elif isinstance(data_structure, dict):
        return sum([calculate_structure_sum(item) for item in data_structure.values()])
    else:
        return 0



result = calculate_structure_sum(data_structure)
print(result)