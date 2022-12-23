
from lesson_005.district.central_street import central_folks_both_houses
from lesson_005.district.soviet_street import soviet_folks_both_houses

def both_streets_folks():
    return ', '.join(central_folks_both_houses()), ', '.join(soviet_folks_both_houses())