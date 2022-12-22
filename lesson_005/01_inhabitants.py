# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from room_1 import folks as f1, module_name as m1
from room_2 import folks as f2, module_name as m2

print('В комнате', m1, 'живут:', ', '.join(f1))
print('В комнате', m2, 'живут:', ', '.join(f2))
