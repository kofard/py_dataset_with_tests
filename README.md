# Clean Python Algorithms Dataset (293 Samples) / Очищенный датасет алгоритмов на Python (293 образца)

[English](#english) | [Русский](#русский)

---

## English

### Overview
A curated, self-contained dataset of **293 clean Python programs** paired with isolated `pytest` verification suites. Each sample has been filtered to rely strictly on the Python Standard Library (`stdlib`), formatted according to PEP 8, and verified via automated test execution.

This dataset is designed for research in **source code analysis, static metrics extraction, code obfuscation, and machine learning on code** (e.g., pairwise ranking of obfuscation levels, AST/CFG structural transformations, and semantic equivalence verification).

### Dataset Structure
The dataset is organized into one directory with 293 directories (`001` – `293`), each containing an isolated code-test pair:

```text
dataset/
│	├── 001/
│	│   ├── clean.py
│	│   └── tests.py
│	├── 002/
│	│   ├── clean.py
│	│   └── tests.py
...
├── pytest.ini
├── .gitignore
├── README.md
└── LICENSE.md
```

* **`clean.py`**: Standalone algorithmic module free of external third-party dependencies (`numpy`, `pandas`, etc.) and free of inline `doctest` or `__main__` execution blocks to prevent static feature contamination.
* **`tests.py`**: Independent verification script that dynamically loads the local `clean.py` via `importlib.util.spec_from_file_location` (preventing `sys.modules` caching collisions during batch test runs) and asserts functional equivalence.

### Data Sources & Preprocessing Pipeline
The samples were collected, filtered, and standardized from two open-source repositories:
1. **[TheAlgorithms/Python](https://github.com/TheAlgorithms/Python)** (MIT License):
   * Filtered for standalone scripts using only Python standard library modules (`sys.stdlib_module_names`).
   * Inline `doctest` blocks (`>>>`) were extracted via `doctest.DocTestParser` and converted into standalone `assert` statements inside `tests.py`.
   * Narrative docstrings, type annotations, and developer comments were preserved while stripping `__main__` blocks.
2. **[google-research/mbpp](https://github.com/google-research/google-research/tree/master/mbpp)** (`sanitized-mbpp.json`, Apache License 2.0):
   * Filtered by Source Lines of Code (SLOC) and control-flow complexity (`if`, `for`, `while`).
   * Task descriptions (`prompt`) were embedded as module-level docstrings, PEP 484 type hints were inferred via runtime profiling (`sys.setprofile`), and code was normalized via AST unparsing.

### Quick Start (Running Verification Tests)
To verify all 293 samples in parallel without module namespace collisions:

```bash
pip install pytest pytest-xdist pytest-timeout pytest-json-report
pytest
```

### Licensing & Attribution
The dataset curation scripts, structure, and documentation are provided under the **MIT License**. Individual code samples retain their original upstream licenses (**MIT** for samples derived from *TheAlgorithms/Python* and **Apache License 2.0** for samples derived from *google-research/mbpp*). See [LICENSE.md](LICENSE.md) for full details, summary translations, and license texts.

---

## Русский

### Описание
Очищенный набор данных из **293 автономных программ на Python**, снабженных изолированными модулями тестирования `pytest`. Все образцы отфильтрованы на предмет отсутствия сторонних зависимостей (используется только стандартная библиотека Python), приведены к стандарту PEP 8 и проверены автоматическим прогоном тестов.

Датасет предназначен для исследований в области **статического анализа кода, извлечения структурных метрик, обфускации программ и машинного обучения на исходном коде** (например, обучение моделей попарного ранжирования уровней обфускации, трансформация AST/CFG и верификация семантической эквивалентности).

### Структура датасета
Датасет состоит из одной директории, в которой расположено 293 директори (`001` – `293`), каждая из которых содержит пару файлов:

```text
dataset/
│	├── 001/
│	│   ├── clean.py      
│	│   └── tests.py 
│	├── 002/
│	│   ├── clean.py
│	│   └── tests.py
...
├── pytest.ini
├── .gitignore
├── README.md
└── LICENSE.md
```

* **`clean.py`**: Автономный алгоритмический модуль без внешних библиотек (`numpy`, `pandas` и др.). Из файлов удалены встроенные `doctest`-примеры и блоки `if __name__ == "__main__":`, чтобы исключить искажение структурных метрик (Хальстеда, МакКейба, глубины AST) при анализе.
* **`tests.py`**: Независимый тестовый модуль, который динамически подгружает локальный `clean.py` через `importlib.util.spec_from_file_location` (исключая коллизии кэша `sys.modules` при массовом параллельном запуске) и проверяет корректность работы алгоритма.

### Источники данных и пайплайн подготовки
Исходные программы собраны, отфильтрованы и унифицированы из двух открытых репозиториев:
1. **[TheAlgorithms/Python](https://github.com/TheAlgorithms/Python)** (лицензия MIT):
   * Отобраны скрипты, использующие исключительно стандартную библиотеку Python (`sys.stdlib_module_names`).
   * Встроенные `doctest`-проверки (`>>>`) извлечены с помощью `doctest.DocTestParser` и преобразованы в `assert`-выражения внутри `tests.py`.
   * Сохранены текстовые описания в `docstring`, аннотации типов и комментарии разработчиков; удалены блоки `__main__`.
2. **[google-research/mbpp](https://github.com/google-research/google-research/tree/master/mbpp)** (`sanitized-mbpp.json`, лицензия Apache License 2.0):
   * Выполнена фильтрация по числу непустых строк кода (SLOC) и наличию операторов управления потоком (`if`, `for`, `while`).
   * Описания задач (`prompt`) интегрированы в `docstring` модуля, аннотации типов (PEP 484) восстановлены динамическим профилированием (`sys.setprofile`), а форматирование нормализовано через AST.

### Быстрый запуск тестов
Для параллельной проверки всех 293 образцов выполните:

```bash
pip install pytest pytest-xdist pytest-timeout pytest-json-report
pytest
```

### Лицензирование и авторские права
Структура датасета, скрипты подготовки и документация распространяются под лицензией **MIT**. Исходный код внутри директорий `001-293` сохраняет лицензии первоисточников (**MIT** для программ из *TheAlgorithms/Python* и **Apache License 2.0** для программ из *google-research/mbpp*). Подробные условия, перевод сути лицензий и их полные тексты приведены в файле [LICENSE.md](LICENSE.md).