# Wargaming
В репозитории представлено решение тестовых заданий для компании Wargaming.

Предварительные настройки:

Если в системе отсутствует **chromedriver**, установить его по следующей инструкции:

- Установить браузер **Google Chrome** при необходимости
- Узнать версию **Google Chrome** на странице `chrome://settings/help`
- Найти соответствующую версию **chromedriver** на [сайте](https://sites.google.com/chromium.org/driver/downloads)
- Скачать архив в соответствии с операционной системой
- Распаковать архив

Для ubuntu, macOS:

- Переместить распакованный файл в директорию `/usr/local/bin/`
- Настроить доступ и права файла для ubuntu
```
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod +x /usr/local/bin/chromedriver
```


Для windows:
- Создать на диске `C:` папку `chromedriver`
- Положить разархивированный файл **chromedriver.exe** в папку `C:\chromedriver`
- Добавить в системную переменную **PATH** папку `C:\chromedriver`

Добавление в **PATH**:
- Открыть настройки системы
- Открыть вкладку **About**, а затем **System info**
- Выбрать **Advanced system settings**
- Выбрать **Environment Variables**
- Кликнуть два раза на строчке **Path** в **System variables**
- Нажать кнопку **New**
- Ввести в новую строку путь к **chromedriver** — `C:\chromedriver`
- Нажать **Enter**

Более подробная информация о добавлении в **PATH** для разных версий windows описана
[здесь](https://www.computerhope.com/issues/ch000549.htm)

- Создать и активировать виртуальное окружение

1. Ввести в терминал следующую команду, если не установлен соответствующий пакет для ubuntu:
   ``` 
   sudo apt install python3-venv
   ```
2. Открыть корневую папку проекта и ввести в терминал:

   Для ubuntu, macOS
   ```
   python3 -m venv имя_окружения
   ```
   Для windows
   ```
   python -m venv имя_окружения
   ```
   
3. Активировать виртуальное окружение:

   Для ubuntu и macOS

   ```
   source имя_окружения/bin/activate
   ```
   Для windows
   ```
   имя_окружения\Scripts\activate.bat
   ```
4. Установить зависимости из файла requirements.txt

   Ввести в терминал:
   ```
   pip install -r requirements.txt
   ```

При возникновении ошибок с активацией виртуальной среды попробовать пересоздать виртуальную среду

При возникновении ошибок с установкой зависимостей попробовать обновить менеджер пакетов pip

1. Задание с pytest:

   - Запустить pytest в терминале следующей командой:
    ```
    pytest path_to_dir_task_with_pytest
    ```
    где path_to_dir_task_with_pytest - абсолютный путь до директории `task_with_pytest/`

    Или 

   - Запустить конфигурацию через **PyCharm**, указав директорию `task_with_pytest/` как **Working directory**

2. Задание с ООП:

   - Запустить pytest в терминале следующей командой:
    ```
    pytest path_to_dir_task_with_oop
    ```
    где path_to_dir_task_with_oop - абсолютный путь до директории `task_with_oop/`

    Или 

   - Запустить конфигурацию через **PyCharm**, указав директорию `task_with_oop/` как **Working directory**

3. Задание с алгоритмами:
   - Открыть директорию `task_with_algorithms/`
   ```
    cd task_with_algorithms/
    ```
   - Запустить файл `search_the_shortest_path.py` на исполнение с помощью python3 для ubuntu, macOS:

    ```
    python3 search_the_shortest_path.py
    ```
   с помощью python для windows:
    ```
    python search_the_shortest_path.py
    ```

    Или

   - Открыть файл  `search_the_shortest_path.py`
   - Запустить исполнение из среды разработки
