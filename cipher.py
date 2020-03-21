chars = {
    "0000": ["О", "Е", "А", 'И', 'Н', 'Т', 'С', 'Р', 'В', 'Л', "К"],
    "0001": ["М", "Д", "П", "У", "Я", "Ы", "Ь", "Г", "З", "Б", "Ч"],
    "0010": ["Й", "Х", "Ж", "Ш", "Ю", "Ч", "Щ", "Э", "Ф", "Ъ", "Ё"],
    "0011": [" ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "0100": [".", ",", "!", "?", ";", ":", "*", "/", "-", "+", "="],
    "1000": ["E", "T", "A", "O", "I", "N", "S", "H", "R", "D", "L"],
    "1001": ["C", 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K'],
    "1010": ["X", "J", "Q", "Z", "n", "'", "[", "]", "{", "}", '"']
}
label: str = '''
   mmm    "           #                    mmmmm  mmmmmm  mmmm     mm  mmm
 m"   " mmm    mmmm   # mm    mmm    m mm  #          #" "   "#   m"#    #
 #        #    #" "#  #"  #  #"  #   #"  " """"mm    m"      m"  #" #    #
 #        #    #   #  #   #  #""""   #          #   m"     m"   #mmm#m   #
  "mmm" mm#mm  ##m#"  #   #  "#mm"   #     "mmm#"  m"    m#mmmm     #  mm#mm
               #
               "'''
# "ПРИВЕТ МИР!": 0001111000000110000011110000010000001100000000110011100000011000000011110000011001001110


def translate_char(char) -> str:
    code: str = ""
    section: str = ""
    for i in chars:
        try:
            code = codes[chars[i].index(char)]
        except:
            continue
        section = i
    return section + code


def detranslate_char(char) -> str:
    section: str = ""
    code: str = ""
    for i in char:
        if len(section) < 4:
            section += i
        else:
            code += i
    if section == "1010" and code == "0111":
        return "\n"
    elif section == "1010" and code == "1001":
        return "\""
    return chars[section][codes.index(code)]


def main():
    print(label)
    flag = True
    inp0: str = ""
    while flag:
        inp0 = input("Шифровать или дешифровать(ш/д): ")

        if inp0.upper() == "Ш":
            inp0 = True
        elif inp0.upper() == "Д":
            inp0 = False
        else:
            print("Ш или Д!")
            continue
        flag = False
    if inp0:
        inp = input("Введите фразу для шифровки: ")
        code: str = ""
        for char in inp:
            code += translate_char(char.upper())
        print(code)
    else:
        inp = input("Введите шифр для расшифровки: ")
        string: str = ""
        i = 1
        tmp: str = ""
        for char in inp:
            tmp += str(char)
            if i == 8:
                string += detranslate_char(tmp)
                i = 0
                tmp = ""
            i += 1
        print(string)


if __name__ == "__main__":
    main()
