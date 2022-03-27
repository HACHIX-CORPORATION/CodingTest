def get_pair(numbers, target):
    pair = [[x, y] for x in numbers for y in numbers if x + y == target]
    for _ in pair:
        if _[0] == _[1]:
            pair.remove(_)

    if pair:
        return pair
    else:
        return None


def get_pair_half_sum(numbers):
    result = [[x, y] for x in numbers for y in numbers if
              (x + y) * 2 == sum(numbers)]
    for _ in result:
        if _[0] == _[1]:
            result.remove(_)

    if result:
        return result
    else:
        return None


if __name__ == '__main__':
    l = [11, 2, 5, 9, 10, 3]
    t = 12
    print(get_pair(l, t))

    l = [11, 2, 5, 9, 10, 3]
    print(get_pair_half_sum(l))
