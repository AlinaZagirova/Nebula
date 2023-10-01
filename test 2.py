import os
import git

# Получаем текущую директорию, где находится исполняемый файл
current_directory = os.path.dirname(os.path.abspath(__file__))

# Имя папки, которое мы хотим создать
folder_name = "test"

# Создаем папку с уникальным именем, добавляя индекс, если папка уже существует
index = 1
new_folder_name = folder_name

while os.path.exists(os.path.join(current_directory, new_folder_name)):
    index += 1
    new_folder_name = f"{folder_name}_{index}"

# Создаем новую папку
new_folder_path = os.path.join(current_directory, new_folder_name)
os.mkdir(new_folder_path)

# Переменная new_folder_path содержит путь к созданной папке
print(f"Создана папка: {new_folder_path}")

# URL вашего репозитория GitHub
github_repo_url = 'https://github.com/AlinaZagirova/Nebula.git'

# Клонирование репозитория GitHub в созданную папку
repo = git.Repo.clone_from(github_repo_url, new_folder_path)

print(f"Репозиторий склонирован в {new_folder_path}")





