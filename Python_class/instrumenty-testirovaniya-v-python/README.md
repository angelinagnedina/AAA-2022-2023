# Инструкция

Все тесты будут запускаться из директории **instrumenty-testirovaniya-v-python**, чтобы перейти в неё - запустите команду

```
cd Python_class/instrumenty-testirovaniya-v-python
```

## Задание 1

Чтобы запустить первый тест - выполните следующую команду

```
python -m doctest -v -o=ELLIPSIS -o=NORMALIZE_WHITESPACE -f=tests/doctest_issue-1.py
```

Брала 2 теста - первый хорошо отрабатывает, второй выдаёт ошибку.

## Задание 2

Чтобы запустить второй тест - выполните следующую команду

```
python -m pytest tests/parametrize_issue-2.py
```

Проверяла на 3 примерах, на первых 2 тест отрабатывает отлично, на последнем тесте падает - так и задумано. Этот тест подсвечивает, что decode не справляется с расстановкой пробелов.

## Задание 3

Чтобы запустить третий тест - выполните следующую команду

```
python -m unittest -v tests/test_issue-3.py
```

Брала 4 тестовых примера, использовала методы проверки **assertEqual, assertCountEqual, assertTupleEqual**. В третьем примере перехватывала исключение при помощи **try / except** (тест выполнялся, но в консоль выводится сообщение, что что-то не в порядке).

## Задание 4

Чтобы запустить четвёртый тест - выполните следующую команду

```
python -m pytest tests/pytest_issue-4.py
```

Взяла 4 теста - на третьем перехватываю **AssertionError** с помощью **with pytest.raises(AssertionError)**.

## Задание 5

Чтобы запустить пятый тест - выполните следующую команду

```
python -m pytest -q tests/coverage_issue-5.py --cov=what_is_year_now
```

Если хочется запустить с отчётом в виде html, то 

```
python -m pytest -q tests/coverage_issue-5.py --cov=what_is_year_now --cov-report=html
```

Тестируется 3 кейса: даты в формате YMD/DMY/произвольный формат (я брала D@M@Y). В последнем случае поднимается **ValueError**, который я ловлю конструкцией **try / except**.
