Здесь представлена работа команды Brooklyn Style(MISIS). 
В составе команды :

Татарников Иван Борисович (Tech Lead, backend developer)

Цыпкин Артем Денисович (full-stack developer)

Святогорова Ксения Евгеньевна (designer, frontend developer)

Куркубет Варвара Михайловна (designer, frontend developer)

Крюкова Екатерина Николаевна (designer, frontend developer)

В этом проекте реализуется биллинговое веб-приложение. 

Большая часть работы написана на языке программирования python, с использованием таких библиотек как django, sqlalchemy, psycopg2

База данных реализована на Postgresql

Дизайн разрабатывался в figma

Мы выбрали именно язык python и библиотеку django потому что они достаточно просты во взаимодействии и при этом имеют большие возможности реализации проектов

База данных содержит две основные таблицы client_data и client, которые содержат следующие столбцы:

client_data:

![image](https://github.com/mllbll/hakaton_dubna/assets/116435228/2deea89a-e1c2-4d0b-b2e8-eb638d2f7dae)

client:

![image](https://github.com/mllbll/hakaton_dubna/assets/116435228/863d32c8-6382-4c61-ae51-32f9f1effb2d)


Наше приложение очень просто для понимания и использования, оно содержит:

главую страницу

![image](https://github.com/mllbll/hakaton_dubna/assets/116435228/e0490648-f01d-4629-bdef-48044357d7ec)

страницу добавления пользователей, которая вызывается путем взаимодействия с кнопкой "добавить пользователя"

![image](https://github.com/mllbll/hakaton_dubna/assets/116435228/6f5e200f-1aa9-47a1-ad7e-b73681d4e39c)

страницу добавления данных о пользователе, которая вызывается путем взаимодействия с кнопкой "изменить данные о пользователе"

![image](https://github.com/mllbll/hakaton_dubna/assets/116435228/cbcad3d1-7043-4e6e-aa0b-50d83d6b3a80)

Так же главная страница содержит кнопку удаления пользователей, описание работы с ней наглядно показано в видео, 

но если описать его кратко то вы должны ввести ФИО в соответствующее поле и после этого нажать на кнопку и подтвердить действие, путем взаимодействия с кнопкой "удалить пользователя"

Особое внимание хоется уделить причине использования sqlalchemy, так как многим это может показаться неуместным.
Мы решили использовать sqlalchemy потому что стандартная ORM django не смогла взаимодействовать с базой данных postgres, по неизвестным причинам, но не смотря на это мы настроили локальное взаимодействие, описанное в видео

Так же неотъемлимой частью любого django проекта являются html,css,js и другие файлы, с ними вы так же можете ознакомится в папке static

База данных, как и сайт располагаются локально, потому что нам не хватило времени перенести их с локального сервера, но мы надеемся что локальное соединение достаточно полно раскроет весь смысл нашего проекта

Мы уделили не очень много времени дизайну сайта, потому что посчитали что создание взаимодействий между  базой данных и сайтом более важными аспектами нашего проекта

