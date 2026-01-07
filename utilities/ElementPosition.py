class ElementPosition:
    def is_element_visible_in_viewport(driver, element):
        rect = element.rect  # Прямоугольник элемента (x, y, ширина, высота)
        window_width = driver.execute_script('return document.documentElement.clientWidth')
        window_height = driver.execute_script('return document.documentElement.clientHeight')
        scroll_top = driver.execute_script('return window.scrollY')  # Текущая позиция вертикальной прокрутки
        scroll_left = driver.execute_script('return window.scrollX')  # Текущая позиция горизонтальной прокрутки

        # Вычисляем границы окна браузера
        top_bound = scroll_top
        bottom_bound = scroll_top + window_height
        left_bound = scroll_left
        right_bound = scroll_left + window_width

        # Координаты элемента относительно окна браузера
        element_top = rect["y"]
        element_bottom = rect["y"] + rect["height"]
        element_left = rect["x"]
        element_right = rect["x"] + rect["width"]

        # Проверяем, пересекается ли элемент с окном браузера
        return (
                element_top >= top_bound and element_bottom <= bottom_bound and
                element_left >= left_bound and element_right <= right_bound
        )