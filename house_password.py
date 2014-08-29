#! /usr/bin/env python3
'''
http://www.checkio.org/mission/task/house-password/

Since Mar 31 2013
'''

import string


def checkio(data):
    'Return True if password strong and False if not'
    if len(data) < 10:
        return False
    else:
        flags = {'digit': 0, 'upper': 0, 'lower': 0}
        for c in data:
            if c in string.digits:
                flags['digit'] += 1
            elif c in string.ascii_uppercase:
                flags['upper'] += 1
            elif c in string.ascii_lowercase:
                flags['lower'] += 1
        if 0 in flags.values():
            return False
        else:
            return True
            
if __name__ == '__main__':
    assert checkio('A1213pokl')==False, 'First'
    assert checkio('bAse730onE4')==True, 'Second'
    assert checkio('asasasasasasasaas')==False, 'Third'
    assert checkio('QWERTYqwerty')==False, 'Fourth'
    assert checkio('123456123456')==False, 'Fifth'
    assert checkio('QwErTy911poqqqq')==True, 'Sixth'
    print('All ok')
