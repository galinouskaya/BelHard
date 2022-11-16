# побитовые операторы
#
# print(bin(10))
# print(bin(14))
# print(bin(10 & 14))
#
# print(bin(10))
# print(bin(14))
# print(bin(10 | 14))
#
#
# print(bin(10))
# print(bin(14))
# print(bin(10 ^ 14))


# print(bin(14))
# print(bin(14>>2))

# аннотация типов при определении переменных и изменении типа данных
# a: int = int(input())
# a += 1
# a: str = str(a)
#
# расширенная типизация до python 3.10
# from typing import List, Tuple, Any, Optional
#
#
# def foo(numbers: List[Any, str]) -> Optional[List[Tuple[int, int]]]:
#     return numbers

# расширенная типизация с python 3.9
# def bar(numbers: list[str, str]) -> list[tuple[int, int]] | None:
#     a: str = numbers[0]
#     return None
#
#
# bar(1234)