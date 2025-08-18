from PIL import Image, ImageDraw
# Pillow (PIL) — это популярная внешняя библиотека Python для обработки изображений

# создаем новое изображение (500x500 пикселей, цвет — синий)
image = Image.new("RGB", (500, 500), "blue")

# добавляем текст
draw = ImageDraw.Draw(image)
draw.text((50, 50), "Hello, Pillow!", fill="white")

# сохраняем и меняем размер
image.save("demo.jpg")  # исходный файл
resized = image.resize((300, 300))
resized.save("resized_demo.jpg")  # результат

print("Изображение успешно создано и изменено")
