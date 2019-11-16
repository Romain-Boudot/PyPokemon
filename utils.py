def tupleAddition(tuples):
    sameLen = True
    FirstTupleLen = len(tuples[0])
    for i in range(1, len(tuples)):
        if len(tuples[i]) != FirstTupleLen: sameLen = False
    if sameLen:
        returnTuple = tuple()
        for i in range(0, FirstTupleLen):
            _sum = 0
            for _tuple in tuples: _sum += _tuple[i]
            returnTuple += (_sum,)
        return returnTuple