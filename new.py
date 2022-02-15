import random
import string

for i in range(0, 6):
    reverse = ''.join(random.choices(string.ascii_letters + string.digits, k = 32))
    print(reverse)