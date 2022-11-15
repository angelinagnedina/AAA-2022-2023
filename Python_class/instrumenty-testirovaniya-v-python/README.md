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

## Задание 2

Чтобы запустить второй тест - выполните следующую команду

```
python -m pytest tests/parametrize_issue-2.py
```

## Задание 3

Чтобы запустить третий тест - выполните следующую команду

```
python -m unittest -v tests/test_issue-3.py
```

## Задание 4

Чтобы запустить четвёртый тест - выполните следующую команду

```
python -m pytest tests/pytest_issue-4.py
```

## Задание 5

Чтобы запустить пятый тест - выполните следующую команду

```
python -m pytest -q tests/coverage_issue-5.py --cov=what_is_year_now
```

Если хочется запустить с отчётом в виде html, то 

```
python -m pytest -q tests/coverage_issue-5.py --cov=what_is_year_now --cov-report=html
```
