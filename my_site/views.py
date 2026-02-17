from django.shortcuts import render


def calc_page(request):
    result = None

    if request.method == 'POST':
        try:
            # Считываем как float, чтобы поддерживать ввод дробных чисел
            n1 = float(request.POST.get('num1'))
            n2 = float(request.POST.get('num2'))
            op = request.POST.get('op')

            # Считаем
            if op == '+':
                val = n1 + n2
            elif op == '-':
                val = n1 - n2
            elif op == '*':
                val = n1 * n2
            elif op == '/':
                val = n1 / n2 if n2 != 0 else "Деление на 0"
            else:
                val = "Ошибка"

            # ЛОГИКА ФОРМАТИРОВАНИЯ
            # Если val это число, а не текст ошибки
            if isinstance(val, (int, float)):
                # Если число целое (например 17.0 == 17)
                if val == int(val):
                    result = int(val)  # Убираем .0 (будет 17)
                else:
                    result = val  # Оставляем дробь (будет 17.5)
            else:
                result = val  # Если это текст ошибки

        except:
            result = "Ошибка ввода"

    return render(request, 'index.html', {'result': result})