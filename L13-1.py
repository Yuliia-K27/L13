#імпортуємо необхідні пакети рандомізації та створюємо списки int_list, float_list та str_list.
import random

int_list = []
float_list = []
str_list = []

#за допомогою циклу for, заповнюємо списки int_list, float_list та str_list випадковими значеннями.Код створює списки int_list, float_list та str_list, 
#які містять 5000 випадкових цілих чисел у діапазоні від 0 до 1000, 5000 випадкових дійсних чисел у діапазоні від 0.1 до 100.0 та 5000 випадкових рядків
#довжиною від 3 до 10 символів з набору літер англійського алфавіту
for i in range(5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(round(random.uniform(0.1, 100.0), 2))
    str_list.append(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(3, 10))))
