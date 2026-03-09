def function_name(search: str, status: bool, *args: tuple, **kwargs: dict) -> list[int] | str:
    """
    Функция обрабатывает аргументы в зависимости от search и status.

    :param search: "args" или "kwargs"
    :param status: True или False для args
    :param args: позиционные аргументы
    :param kwargs: ключевые аргументы
    :return: список чисел или строка
    """
    result: list[int] = []
    result_2: str = ""
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += ("Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")