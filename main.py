
import csv
import json


with open("data/books.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    books = list(reader)


with open("data/users.json", "r", encoding="utf-8") as file:
    users = json.load(file)


result = []

for user in users:
    new_user = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"],
        "books": []
    }

    result.append(new_user)


for index, book in enumerate(books):
    new_book = {
        "title": book["Title"],
        "author": book["Author"],
        "pages": int(book["Pages"]),
        "genre": book["Genre"]
    }

    user_index = index % len(result)

    result[user_index]["books"].append(new_book)


with open("result.json", "w", encoding="utf-8") as file:
    json.dump(result, file, indent=4, ensure_ascii=False)

print("Файл result.json создан")
