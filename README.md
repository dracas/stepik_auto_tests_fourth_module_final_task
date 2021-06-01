# stepik_auto_tests_fourth_module_final_task
This repository created for fourth module, for final task. The course: https://stepik.org/course/575/info

Хочу добавить небольшое описание к этому репозиторию и файлам в нем, чтобы было проще мне и людям, которые будут смотреть этот проект. Описание будет обновляться. 

Тестируется сайт: https://selenium1py.pythonanywhere.com/en-gb/#

/pages/ - хранит все страницы проекта;

/pages/base_page.py - храним методы, которые применяются по всему проекту вообще, всё завернуто в класс, чтобы было удобно импортировать;

/pages/locators.py - храним локаторы в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать;

/pages/main_page.py - храним методы, которые связаны с главной страницей сайта, завернутые в класс этой странице. Класс этот — условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py;

/pages/product_page.py - храним методы для страницы товара;

/test_main_page.py - храним сами тест-кейсы, которые будем запускать с помощью pytest;

/test_product_page.py - файл для тест-кейсов, связанных со страницей товара;
