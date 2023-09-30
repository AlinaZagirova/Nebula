import cv2
import dlib
import numpy as np

# Загрузка изображений
image = cv2.imread('test_image.jpg')  # Загрузите ваше изображение
reference_image = cv2.imread('reference_image.jpg')  # Загрузите эталонное изображение

# Создание объекта для детекции лица с использованием dlib
detector = dlib.get_frontal_face_detector()

  # Вычисление степени сходства (например, среднего расстояния между ключевыми точками)
    similarity = np.mean(np.linalg.norm(landmarks_image - landmarks_reference, axis=1))

# Создание объекта для извлечения ключевых точек лица с использованием dlib
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')  # Загрузите файл модели с ключевыми точками

# Детекция лица на тестовом изображении
faces = detector(image)



    # Преобразование ключевых точек в массивы numpy
    landmarks_image = np.array([[p.x, p.y] for p in landmarks_image.parts()])
    landmarks_reference = np.array([[p.x, p.y] for p in landmarks_reference.parts()])

    # Вычисление степени сходства (например, среднего расстояния между ключевыми точками)
    similarity = np.mean(np.linalg.norm(landmarks_image - landmarks_reference, axis=1))

    # Вывод степени сходства
    print(f'Процент схожести: {similarity:.2f}%')

else:
    print('Лицо не обнаружено на изображении.')

# Отображение изображений с выделенными ключевыми точками (для визуализации)
cv2.imshow('Test Image', image)
cv2.imshow('Reference Image', reference_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
