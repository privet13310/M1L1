meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное"
            }
while True:
    word = input("Введите непонятное слово (большими буквами!): ").upper()
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("не найдено")
