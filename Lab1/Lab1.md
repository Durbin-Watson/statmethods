# Лабораторная работа 1 <<Построение моделей линейной регрессии>> 

Срок сдачи: 15 марта.
Оценка: 20 баллов.
Штраф: 2 балла в неделю.

0. Подготовить исходную выборку на основе данных с kaggle.com или Росстат размером 100 измерений. Разделить выборку на две части - одну для обучения, вторую для тестирования.
1. Найти уравнение линейной регрессии по обучающей выборке. Скрипт считывает данные из файла и выводит на экране уравнение регрессии (Python, numpy, scipi, scilearn-kit).
2. Для полученной регрессионной модели рассчитайте линейный коээфициент коррелляции и среднюю ошибку аппроксимации, оценить статистическую значимость параметров регрессии.
3. Построить график по данным и уравнению с помощью библиотеки (matplotlib, bokeh+d3.js).
4. Построить интерполяционную модель (полиномиальную, сплайн) по обучающей выборке, построить график.
5. Исследовать корреляцию регрессионной и интерполяционных моделей по тестовой выборке.
Сделать вывод о точности исследуемых моделей.

# Вопросы к защите
1. Синтаксис языка программирования Python.
2. Линейная регрессия.
3. Метод наименьших квадратов.
4. Обращение и псевдобращение. Аксимы Мура-Пенроуза.
5. Линейная алгебра: критерий разрешимости СЛАУ, теорема Кронекера-Капелли, ранг (строчный, столбцовый, обычный).


# Рекомендуемые источники

1. Регрессия в Python
https://medium.freecodecamp.org/data-science-with-python-8-ways-to-do-linear-regression-and-measure-their-speed-b5577d75f8b
https://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html
https://github.com/numpy/numpy/blob/v1.14.0/numpy/lib/polynomial.py#L398-L611

2. Интерполяция в Python
https://stackoverflow.com/questions/11851770/spline-interpolation-with-python
https://docs.scipy.org/doc/scipy-0.19.0/reference/generated/scipy.optimize.curve_fit.html
http://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html
https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html


3. Примеры графиков
https://matplotlib.org/gallery/index.html