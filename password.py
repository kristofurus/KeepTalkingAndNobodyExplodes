passwords = ["alarm", "apacz", "arena", "babka", "cecha",
             "ekipa", "fajka", "farma", "głowa", "hańba",
             "larwa", "laska", "macka", "obiad", "palec",
             "palma", "pegaz", "robak", "scena", "skrót",
             "smoła", "smycz", "tafla", "teren", "toast",
             "torba", "trasa", "twarz", "walka", "wełna",
             "wnęka", "zakaz", "zwiad", "znicz", "żniwa"]

character = 0
available_passwords = passwords

for _ in range(5):
    letters = input("enter letters: ")
    letters = letters.lower().split()
    print(letters)
    tmp = []
    for i in range(len(letters)):
        for password in available_passwords:
            if letters[i] == password[character]:
                tmp.append(password)
    available_passwords = tmp
    print(available_passwords)
    if len(available_passwords) <= 1:
        break
    character += 1
