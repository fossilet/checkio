#! /usr/bin/python3

'''http://www.checkio.org/mission/task/info/speechmodule/

Since Mar 30 2013
'''

FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
        "eight", "nine"] 
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety"]
HUNDRED = "hundred"


def _rest(x):
    if x == 0:
        return ''
    elif x in range(20):
        return (FIRST_TEN + SECOND_TEN)[x]
    else:
        tens, rst = x // 10, x % 10
        return OTHER_TENS[tens - 2] + ' ' +  \
                (FIRST_TEN[rst] if rst > 0  else '')

def _hundreds(x):
    return FIRST_TEN[x] + ' ' + HUNDRED + ' ' if x > 0 else ''


def checkio(x):
    assert 0 <= x <= 999
    if x == 0:
        return FIRST_TEN[x]
    else:
        hundreds, rst = x // 100, x % 100
        return (_hundreds(hundreds) + _rest(rst)).strip()


if __name__ == '__main__':
    for i in range(0, 1000):
        print(i, checkio(i))

    assert checkio(4) == 'four', "First"
    assert checkio(13) == 'thirteen', '13'
    assert checkio(133) == 'one hundred thirty three', "Second"
    assert checkio(12)=='twelve', "Third"
    assert checkio(101)=='one hundred one', "Fifth"
    assert checkio(212)=="two hundred twelve", "Sixth"
    assert checkio(40)=='forty', "Seventh, forty - it is correct"
    print('All ok')
