class RectCorrectError(Exception):
    pass

def isCorrectRect(rect):
    (x1, y1), (x2, y2) = rect
    return x1 < x2 and y1 < y2

def isCollisionRect(rect1, rect2):
    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некоректный")
    if not isCorrectRect(rect2):
        raise RectCorrectError("2й прямоугольник некоректный")
    
    x1_min, y1_min = rect1[0]
    x1_max, y1_max = rect1[1]
    x2_min, y2_min = rect2[0]
    x2_max, y2_max = rect2[1]

    if x1_max <= x2_min or x2_max <= x1_min or y1_max <= y2_min or y2_max <= y1_min:
        return False
    else:
        return True

def intersectionAreaRect(rect1, rect2):
    if not isCorrectRect(rect1):
        raise ValueError("1й прямоугольник некорректный")
    if not isCorrectRect(rect2):
        raise ValueError("2й прямоугольник некорректный")
    
    x1_min, y1_min = rect1[0]
    x1_max, y1_max = rect1[1]
    x2_min, y2_min = rect2[0]
    x2_max, y2_max = rect2[1]
    
    x_left = max(x1_min, x2_min)
    x_right = min(x1_max, x2_max)
    y_bottom = max(y1_min, y2_min)
    y_top = min(y1_max, y2_max)
    
    if x_left < x_right and y_bottom < y_top:
        area = (x_right - x_left) * (y_top - y_bottom)
        return area
    else:
        return 0

def intersectionAreaMultiRect(rectangles):
    if not rectangles:
        return 0

    for i, rect in enumerate(rectangles, start=1):
        if not isCorrectRect(rect):
            raise RectCorrectError(f"{i}й прямоугольник некоректный")

    (x_min, y_min), (x_max, y_max) = rectangles[0]

    for rect in rectangles[1:]:
        (x1, y1), (x2, y2) = rect
        x_min = max(x_min, x1)
        y_min = max(y_min, y1)
        x_max = min(x_max, x2)
        y_max = min(y_max, y2)

        if x_min >= x_max or y_min >= y_max:
            return 0
        
    return (x_max - x_min) * (y_max - y_min)