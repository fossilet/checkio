#! /usr/bin/env python3

'''http://www.checkio.org/mission/task/info/cipher-map/python-3/

Since Mar 31 2013
'''

def checkio(input_data):
    'Return password of given cipher map'
    #1. Get the last four characters
    #2. Rotate 90 degrees counterclockwise
    #3. Get the last but four character
    #......
    

if __name__ == '__main__':
    assert checkio([[
    'X...',
    '..X.',
    'X..X',
    '....'],[
    'itdf',
    'gdce',
    'aton',
    'qrdi']]) == 'icantforgetiddqd', 'First'

    assert checkio( [[
    '....',
    'X..X',
    '.X..',
    '...X'],[
    'xhwc',
    'rsqx',
    'xqzz',
    'fyzr']]) == 'rxqrwsfzxqxzhczy', 'Second'
    print('All ok')
