# Дана сумма вклада и процент вклада, сказать
# через сколько лет сумма вклада увеличится в двое
# (ставка рефинансирования)

# def calculate_deposit(deposit: float | int, percent: float | int, k: float | int) -> int:
#     expected_deposit = deposit * k
#     percent = percent / 100
#     years = 0
#     while deposit < expected_deposit:
#         deposit += deposit * percent
#         deposit = round(deposit, 2)
#         years += 1
#         print(f'{years=} {deposit=}')
#     return years
#
#
# print(calculate_deposit(
#     float(input('deposit: ')),
#     float(input('percent: ')),
#     float(input('k: ')))
# )


# C2H5OH -> {'C': 2, 'H': 6, 'O': 1}
#
# data = {}
# formula = 'C2H5OH'
# formula += '1' if formula[-1].isalpha() else ''
# print(formula)
#
# for i in range(len(formula)):
#     if formula[i].isalpha():
#         if formula[i+1].isdigit():
#             if formula[i] in data:
#                 data[formula[i]] += int(formula[i+1])
#             else:
#                 data[formula[i]] = int(formula[i+1])
#         else:
#             if formula[i] in data:
#                 data[formula[i]] += 1
#             else:
#                 data[formula[i]] = 1
# print(data)
