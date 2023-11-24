#moduły oraz ich importowanie (biblioteka)

import random #korzystanie z biblioteki
print(random.randint(1, 10))

from random import randint
print(randint(1, 10))

from math import pi
print(pi)

from math import sqrt as pierwiastek
print(pierwiastek(16))
print(int(pierwiastek(16)))