input_file = "input_1.txt"

def parse_data(input_file):
    data = []
    with open(input_file, "r") as file:
        meta_data = file.readline().split(" ")
        b = int(meta_data[0])
        r = int(meta_data[1])
        m = int(meta_data[2])
        obr1 = [int(x) for x in file.readline().split(" ")]
        obr2 = [int(x) for x in file.readline().split(" ")]

    #print(n, k, l, data)
    return b, r, m, obr1, obr2

def can_picture_fit(zostatok,obr):
    for i in range(len(zostatok)):
        if zostatok[i] < obr[i]:
            return False
    return True

def substract(zostatok,obr):
    novy_zostatok = []
    for i in range(len(zostatok)):
        hodnota = zostatok[i] - obr[i]
        novy_zostatok.append(hodnota)
    return novy_zostatok

def traversetree(zostatok, obr1, obr2):
    if can_picture_fit(zostatok,obr1):
        pass


b, r, m, obr1, obr2 = parse_data(input_file)
zostatok = [b,r,m]


