class FileUitls:
    def write(txt, file_path):
        f = open(file_path, mode='w', encoding='utf-8')
        f.write(txt)
        f.close()

    def reade(file_path):
        f = open(file_path, mode='r', encoding='utf-8')
        txt = f.read()
        f.close()
        return txt

    def reade_lines(file_path):
        f = open(file_path, mode='r', encoding='utf-8')
        lines = f.readlines()
        f.close()
        return lines

    def append(txt, file_path):
        f = open(file_path, mode='a', encoding='utf-8')
        f.write(txt)
        f.close()