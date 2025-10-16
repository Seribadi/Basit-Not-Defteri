def note_app():
    while True:
        print("1. Not Ekle\n2. Notları Oku\n3. Çıkış")
        choice = input("Seçiminiz (1-3): ")
        
        if choice == "1":
            note = input("Notunuzu girin: ")
            with open("notes.txt", "a") as file:
                file.write(note + "\n")
            print("Not kaydedildi!")
        elif choice == "2":
            try:
                with open("notes.txt", "r") as file:
                    print("Notlarınız:")
                    print(file.read())
            except FileNotFoundError:
                print("Henüz not yok!")
        elif choice == "3":
            break
        else:
            print("Geçersiz seçim!")

note_app()
