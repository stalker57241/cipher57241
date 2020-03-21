import json


class Cipher(object):
    codes = []
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
    def load_codes(self, f):
        self.codes = []
        with open(f, "r") as file:
            data = json.load(file)
            self.codes = data["codes"]
        file.close()
        return self.codes

    def translate_char(self, char) -> str:
        code: str = ""
        section: str = ""
        for i in self.chars:
            try:
                code = self.codes[self.chars[i].index(char)]
            except:
                continue
            section = i
        return section + code

    def detranslate_char(self, char) -> str:
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
        print(section + code)
        return self.chars[section][self.codes.index(code)]

    def translate(self, msg):
        code: str = ""
        for char in msg:
            code += self.translate_char(char.upper())
        return code

    def detranslate(self, msg):
        string: str = ""
        i = 1
        tmp: str = ""
        for char in msg:
            tmp += str(char)
            if i == 8:
                string += self.detranslate_char(tmp)
                i = 0
                tmp = ""
            i += 1
        return string
