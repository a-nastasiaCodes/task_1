def filter_numbers(numbers, threshold=0, greater=True):
    result = []
    if greater:
        for i in numbers:
            if i > threshold:
                result.append(i)
        return result
    for i in numbers:
        if i < threshold:
            result.append(i)
    return result
