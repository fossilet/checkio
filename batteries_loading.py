#! /usr/bin/env python3

'''http://www.checkio.org/mission/task/batteries-loading/

Since Mar 31 2013
'''

from itertools import combinations


def checkio(stones):
    '''minimal possible weight difference between stone piles
    '''
    # XXX: This is O(2^n*n^3)*O(combinations(n, r))!!!
    total = len(stones)
    st = stones[:]
    diffs = []
    for i in range(total + 1):
        for comb in combinations(stones, i):
            st = stones[:]
            for j in comb:
                st.remove(j)
            print(comb, tuple(st))
            diffs.append(abs(sum(comb) - sum(st)))
    return min(diffs)


def checkio(stones):
    pass

if __name__ == '__main__':
    #assert checkio([10,10]) == 0, 'First, with equal weights'
    #assert checkio([10]) == 10, 'Second, with a single stone'
    #assert checkio([5, 8, 13, 27, 14]) == 3, 'Third'
    #assert checkio([5,5,6,5]) == 1, 'Fourth'
    #assert checkio([12, 30, 30, 32, 42, 49]) == 9, 'Fifth'
    #assert checkio([1, 1, 1, 3]) == 0, "Six"
    stones = [3, 7, 2, 1]
    print(checkio(stones))
    print ('All is ok')
