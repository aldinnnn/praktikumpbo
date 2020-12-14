class Bangun_datar:
    __vendor_message = "Ini adalah rahasia"  #atribute
    name = ""
    jari = ""
    luas = ""

    def __init__(self, name):   # method Konstruktor
        print ("Ini adalah constructor")
        self.name = name

    def get_vendor_message(self):  # method
        print (self.__vendor_message)

    def set_jari(self, jari): # method
        self.jari = jari

    def set_luas(self, luas):
        self.luas = luas

bd = Bangun_datar("Objek Lingkaran Pertama")
bd.set_jari(12)
bd.luas = 3.14 * bd.jari * bd.jari
print ("\n%s \nMemiliki jari-jari %s cm \nluas lingkaran adalah %d cm\n" % (bd.name, bd.jari, bd.luas))

bd = Bangun_datar("Objek Lingkaran Kedua")
bd.set_jari(5)
bd.luas = 3.14 * bd.jari * bd.jari
print ("\n%s \nMemiliki jari-jari %s cm \nluas lingkaran adalah %d cm\n" % (bd.name, bd.jari, bd.luas))

bd = Bangun_datar("Objek Lingkaran Ketiga")
bd.set_jari(7)
bd.luas = 3.14 * bd.jari * bd.jari
print ("\n%s \nMemiliki jari-jari %s cm \nluas lingkaran adalah %d cm\n" % (bd.name, bd.jari, bd.luas))
