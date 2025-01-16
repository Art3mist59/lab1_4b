

def count_common_elements(*lists):
    if not lists:
        return 0

    # Преобразуем первый список в множество
    common_elements = set(lists[0])

    # Пересекаем с остальными списками
    for lst in lists[1:]:
        common_elements.intersection_update(lst)

    return len(common_elements)