with open ("myascii.txt",encoding="utf-8") as fin:
    for line in fin:
        for char in line:
            if char == " ":
                save = 'std::cout << " ";'

            if char == "█":
                save = 'std::cout << (char)219;'

            if char == "▓":
                save = 'std::cout << (char)178;'

            if char == "▄":
                save = 'std::cout << (char)220;'

            if char == "▀":
                save = 'std::cout << (char)223;'

            if char == "▒":
                save = 'std::cout << (char)177;'

            if char == "░":
                save = 'std::cout << (char)176;'

            if char == "▐▌":
                save = 'std::cout << (char)219;'

            elif char == "\n":
                save = 'std::cout << "" << endl;'
                
            with open("code.txt", "a+", encoding="utf-8") as file_object:
                        file_object.seek(0)
                        data = file_object.read(100)
                        if len(data) > 0 :
                            file_object.write("\n")
                        file_object.write(save)
print("Data Saved\n")
