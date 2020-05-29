def max_combination(seq):
    temp = []
    temp.append(max(seq))
    seq.remove(max(seq))
    temp.append(max(seq))
    seq.remove(max(seq))
    return sum(temp)


print(max_combination([1, 7, 3, 1, 3, 5, 4]))


# other solution
'''
def find_max_comb(seq):
    temp = 0
    for i, n in enumerate(seq):
        for v in seq[i + 1:]:
            temp = max(temp, n + v)
    return temp


print(find_max_comb([1, 7, 3, 1, 3, 5, 4]))
'''
