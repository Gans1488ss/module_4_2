def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    print(inner_function()) # 3 - здесь ничего не возвращает

print(inner_function()) # ЗДЕСЬ НЕ РАБОТАЕТ! (ошибка)


print(test_function()) # Здесь - работает :-)