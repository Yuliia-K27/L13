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
    
import random
import timeit

int_list = []
float_list = []
str_list = []

#щоб обрахувати середній час роботи алгоритму сортування, використаємо функцію timeit() з модуля timeit.
#застосуємо функцію sort_and_time() до кожного з трьох списків int_list, float_list та str_list, та використаємо вбудований метод сортування Python sorted(). 
#результат - середній час роботи алгоритму сортування для кожного списку, який виводиться на екран.
def sort_and_time(list_to_sort, sort_func, num_iter):
    total_time = 0
    for i in range(num_iter):
        start_time = timeit.default_timer()
        sorted_list = sort_func(list_to_sort)
        end_time = timeit.default_timer()
        total_time += end_time - start_time
    return total_time / num_iter

int_sorted_time = sort_and_time(int_list, sorted, 100)
float_sorted_time = sort_and_time(float_list, sorted, 100)
str_sorted_time = sort_and_time(str_list, sorted, 100)

print(f"Average time to sort int_list: {int_sorted_time:.5f} seconds")
print(f"Average time to sort float_list: {float_sorted_time:.5f} seconds")
print(f"Average time to sort str_list: {str_sorted_time:.5f} seconds")
    
