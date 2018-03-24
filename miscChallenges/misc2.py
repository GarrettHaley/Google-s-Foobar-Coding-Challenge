def answer(xs):
    filter(lambda nonzero: nonzero != 0, xs)
    negativeCount = 0
    negativeValues = []
    for value in xs:
        if (value < 0):
            xs.remove(value)
            negativeValues.append(value)
            negativeCount+=1
    if not(value % 2 == 0):
        negativeValues.remove(max(negativeValues))
    result = reduce(lambda x, y: x*y, negativeValues) + reduce(lambda x, y: x*y, xs)
    return result
