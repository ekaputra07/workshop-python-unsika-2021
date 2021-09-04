# Module = file yang terdapat kode Python di dalamnya (builtin | custom)

# 1. mengimport module dengan `import`
# import datetime
# print(datetime.datetime.now())


# 2. Mengimport module dengan `from x import`
# from datetime import datetime
# print(datetime.now())

# 3. Mengimport module dengan `from x import *`
# from datetime import *
# print(datetime.now())

# 4. Mengimport module dengan `from x import x, y, z`
from datetime import datetime, timedelta
print(datetime.now())

# 5. Membuat module sendiri
# import module_umur
# u = module_umur.umur(1990)
# print(u)

from module_umur import umur
u = umur(1990)
print(u)