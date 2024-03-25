import tkinter as tk
from tkinter import ttk

#oyun pencereleri oluşturma
player_wind = tk.Tk()
player_wind.title("LORDS OF THE POLYWARPHISM")
player_wind.geometry("450x500+500+100")

matrix_screen = tk.Tk()
matrix_screen.title("LORDS OF THE POLYWARPHISM")
matrix_screen.attributes('-fullscreen', True)


#savaşçılar için sınıf
class Warrior:
    def __init__(self, name, kaynak, can, hedef, hasar, yatay_menzil, dikey_menzil, capraz_menzil):
        self.name = name
        self.kaynak = kaynak
        self.can = can
        self.hedef = hedef
        self.hasar = hasar
        self.yatay_menzil = yatay_menzil
        self.dikey_menzil = dikey_menzil
        self.capraz_menzil = capraz_menzil

    def saglik(self):
        return self.can

    def saldir(self):
        pass


class Muhafiz(Warrior):
#savaşçılar sınıfından miras alınan saldırma özelliği
    def saldir(x, y, cell_size, canvas, i):

        saldiri_yerleri = []
        for i in range(-1, 2):
            x_s = int(x) + i
            for j in range(-1, 2):
                y_s = int(y) + j
                if x_s == x and y_s == y:
                    continue
                if x_s < 0 or y_s < 0:
                    continue
                saldiri_yerleri.append([x_s, y_s])
        for i in oyuncular[i-1].hamleler:
            if i in saldiri_yerleri:
                saldiri_yerleri.remove(i)

        for oyuncu in oyuncular:
            if oyuncu.oyuncu_id != i:
                for yerler in saldiri_yerleri:
                    if yerler in oyuncu.hamleler:
                        oyuncu.hamleler.remove(yerler)
                        sayi = oyuncu.alan
                        sayi -= 1
                        oyuncu.alan = sayi
                        alan = (int(oyuncu.alan) / d_boyut)
                        alani = alan * 100 / 8
                        oyuncu.yuzdelik_alan = alani
                        for svs in oyuncu.savascilar:
                            if svs != []:
                                koordinatlar = svs[1].split("x")
                                xk = int(koordinatlar[0])
                                yk = int(koordinatlar[1])
                                if svs[0] == "Muhafız" and [xk, yk] == yerler:
                                    oyuncu.savascilar.remove(svs)

        Oyun_dunyasi.ozel_renk_liste_fonksiyonu(saldiri_yerleri, cell_size, canvas, "white", "black", ".")



class Okcu(Warrior):
#savaşçılar sınıfından miras alınan saldırma özelliği
    def saldir(x, y, cell_size, canvas, i):
        saldiri_yerleri_okcu = []

        for i in range(1, 3):
            x1 = int(x)
            y1 = int(y)
            saldiri_yerleri_okcu.append([x1, y1 - i])
            saldiri_yerleri_okcu.append([x1, y1 + i])
            saldiri_yerleri_okcu.append([x1 - i, y1])
            saldiri_yerleri_okcu.append([x1 + i, y1])
            saldiri_yerleri_okcu.append([x1 - i, y1 - i])
            saldiri_yerleri_okcu.append([x1 + i, y1 + i])
            saldiri_yerleri_okcu.append([x1 + i, y1 - i])
            saldiri_yerleri_okcu.append([x1 - i, y1 + i])

        for i in oyuncular[i-1].hamleler:
            if i in saldiri_yerleri_okcu:
                saldiri_yerleri_okcu.remove(i)

        for i in saldiri_yerleri_okcu:
            x_s, y_s = i
            if x_s < 0 or y_s < 0:
                saldiri_yerleri_okcu.remove(i)

        for oyuncu in oyuncular:
            if oyuncu.oyuncu_id != i:
                for yerler in saldiri_yerleri_okcu:
                    if yerler in oyuncu.hamleler:
                        oyuncu.hamleler.remove(yerler)
                        sayi = oyuncu.alan
                        sayi -= 1
                        oyuncu.alan = sayi
                        alan = (int(oyuncu.alan) / d_boyut)
                        alani = alan * 100 / 8
                        oyuncu.yuzdelik_alan = alani
                        for svs in oyuncu.savascilar:
                            if svs != []:
                                koordinatlar = svs[1].split("x")
                                xk = int(koordinatlar[0])
                                yk = int(koordinatlar[1])
                                if svs[0] == "Okçu" and [xk, yk] == yerler:
                                    oyuncu.savascilar.remove(svs)


        Oyun_dunyasi.ozel_renk_liste_fonksiyonu(saldiri_yerleri_okcu, cell_size, canvas, "white", "black", ".")

class Topcu(Warrior):
#savaşçılar sınıfından miras alınan saldırma özelliği
    def saldir(x, y, cell_size, canvas, i):
        saldiri_yerleri_topcu = []

        for i in range(1, 3):
            x1 = int(x)
            y1 = int(y)
            saldiri_yerleri_topcu.append([x1, y1 - i])
            saldiri_yerleri_topcu.append([x1, y1 + i])
            saldiri_yerleri_topcu.append([x1 - i, y1])
            saldiri_yerleri_topcu.append([x1 + i, y1])

        for i in oyuncular[i-1].hamleler:
            if i in saldiri_yerleri_topcu:
                saldiri_yerleri_topcu.remove(i)

        for i in saldiri_yerleri_topcu:
            x_s, y_s = i
            if x_s < 0 or y_s < 0:
                saldiri_yerleri_topcu.remove(i)

        for oyuncu in oyuncular:
            if oyuncu.oyuncu_id != i:
                for yerler in saldiri_yerleri_topcu:
                    if yerler in oyuncu.hamleler:
                        oyuncu.hamleler.remove(yerler)
                        sayi = oyuncu.alan
                        sayi -= 1
                        oyuncu.alan = sayi
                        alan = (int(oyuncu.alan) / d_boyut)
                        alani = alan * 100 / 8
                        oyuncu.yuzdelik_alan = alani
                        for svs in oyuncu.savascilar:
                            if svs != []:
                                koordinatlar = svs[1].split("x")
                                xk = int(koordinatlar[0])
                                yk = int(koordinatlar[1])
                                if svs[0] == "Topçu" and [xk, yk] == yerler:
                                    oyuncu.savascilar.remove(svs)

        Oyun_dunyasi.ozel_renk_liste_fonksiyonu(saldiri_yerleri_topcu, cell_size, canvas, "white", "black", ".")

class Atli(Warrior):
    #savaşçılar sınıfından miras alınan saldırma özelliği
    def saldir(x, y, cell_size, canvas, i):
        saldiri_yerleri_atli = []

        for i in range(1, 4):
            x1 = int(x)
            y1 = int(y)
            saldiri_yerleri_atli.append([x1 - i, y1 - i])
            saldiri_yerleri_atli.append([x1 + i, y1 + i])
            saldiri_yerleri_atli.append([x1 + i, y1 - i])
            saldiri_yerleri_atli.append([x1 - i, y1 + i])

        for i in oyuncular[i-1].hamleler:
            if i in saldiri_yerleri_atli:
                saldiri_yerleri_atli.remove(i)

        for i in saldiri_yerleri_atli:
            x_s, y_s = i
            if x_s < 0 or y_s < 0:
                saldiri_yerleri_atli.remove(i)

        for oyuncu in oyuncular:
            if oyuncu.oyuncu_id != i:
                for yerler in saldiri_yerleri_atli:
                    if yerler in oyuncu.hamleler:
                        oyuncu.hamleler.remove(yerler)
                        sayi = oyuncu.alan
                        sayi -= 1
                        oyuncu.alan = sayi
                        alan = (int(oyuncu.alan) / d_boyut)
                        alani = alan * 100 / 8
                        oyuncu.yuzdelik_alan = alani
                        for svs in oyuncu.savascilar:
                            if svs != []:
                                koordinatlar = svs[1].split("x")
                                xk = int(koordinatlar[0])
                                yk = int(koordinatlar[1])
                                if svs[0] == "Atlı" and [xk, yk] == yerler:
                                    oyuncu.savascilar.remove(svs)

        Oyun_dunyasi.ozel_renk_liste_fonksiyonu(saldiri_yerleri_atli, cell_size, canvas, "white", "black", ".")

class Saglikci(Warrior):
    #savaşçılar sınıfından miras alınan saldırma özelliği

    def saldir(x, y, cell_size, canvas, i):
        saldiri_yerleri_saglikci = []

        for i in range(1, 3):
            x1 = int(x)
            y1 = int(y)
            saldiri_yerleri_saglikci.append([x1, y1 - i])
            saldiri_yerleri_saglikci.append([x1, y1 + i])
            saldiri_yerleri_saglikci.append([x1 - i, y1])
            saldiri_yerleri_saglikci.append([x1 + i, y1])
            saldiri_yerleri_saglikci.append([x1 - i, y1 - i])
            saldiri_yerleri_saglikci.append([x1 + i, y1 + i])
            saldiri_yerleri_saglikci.append([x1 + i, y1 - i])
            saldiri_yerleri_saglikci.append([x1 - i, y1 + i])

        for i in oyuncular[i-1].hamleler:
            if i in saldiri_yerleri_saglikci:
                saldiri_yerleri_saglikci.remove(i)

        for i in saldiri_yerleri_saglikci:
            x_s, y_s = i
            if x_s < 0 or y_s < 0:
                saldiri_yerleri_saglikci.remove(i)

        for oyuncu in oyuncular:
            if oyuncu.oyuncu_id != i:
                for yerler in saldiri_yerleri_saglikci:
                    if yerler in oyuncu.hamleler:
                        oyuncu.hamleler.remove(yerler)
                        sayi = oyuncu.alan
                        sayi -= 1
                        oyuncu.alan = sayi
                        alan = (int(oyuncu.alan) / d_boyut)
                        alani = alan * 100 / 8
                        oyuncu.yuzdelik_alan = alani
                        for svs in oyuncu.savascilar:
                            if svs != []:
                                koordinatlar = svs[1].split("x")
                                xk = int(koordinatlar[0])
                                yk = int(koordinatlar[1])
                                if svs[0] == "Sağlıkçı" and [xk, yk] == yerler:
                                    oyuncu.savascilar.remove(svs)


        Oyun_dunyasi.ozel_renk_liste_fonksiyonu(saldiri_yerleri_saglikci, cell_size, canvas, "white", "black", ".")



warriors = [
    Warrior("Muhafız", 10, 80, "Tüm düşmanlar", -20, 1, 1, 1),
    Warrior("Okçu", 20, 30, "En yüksek canlı 3 düşman", -60, 2, 2, 2),
    Warrior("Topçu", 50, 30, "En yüksek canlı 1 düşman", -100, 2, 2, 0),
    Warrior("Atlı", 30, 40, "Menzildeki en pahalı 2 düşman", -30, 0, 0, 3),
    Warrior("Sağlıkçı", 10, 100, "En az canlı 3 dost", 50, 2, 2, 2)
]

#oyuncu bilgileri sınıfı
class Oyuncu:
    def __init__(self, oyuncu_id, kaynak, savascilar, alan, yuzdelik_alan, hamleler, cevre):
        self.oyuncu_id = oyuncu_id
        self.kaynak = kaynak
        self.savascilar = savascilar
        self.alan = alan
        self.yuzdelik_alan = yuzdelik_alan
        self.hamleler = hamleler
        self.cevre = cevre


    def s_cevre_koordinatlari(x, y, i):
        cevre_koordinat = oyuncular[i - 1].cevre

        for i in range(-1, 2):
            x_c = x + i
            for j in range(-1, 2):
                y_c = y + j
                if (x_c, y_c) in cevre_koordinat:
                    continue
                elif x_c < 0 or y_c < 0:
                    continue
                cevre_koordinat.append([x_c, y_c])

        for i in oyuncular[i - 1].hamleler:
            if i in cevre_koordinat:
                cevre_koordinat.remove(i)

        for oyuncu in oyuncular:
            for i in oyuncu.hamleler:
                if i in cevre_koordinat:
                    cevre_koordinat.remove(i)

    #oyuncunun sahip olduğu alanı bulma
    def sahip_olunan_alan(x, y, i):

        oyuncular[i - 1].hamleler.append([x, y])

        deger = oyuncular[i - 1].alan
        deger += 1
        oyuncular[i - 1].alan = deger

        alan = (int(oyuncular[i - 1].alan) / d_boyut)
        alani = alan * 100 / 8
        oyuncular[i - 1].yuzdelik_alan = alani

    #oyuncu kaynaklarını tutma
    def oyuncu_kaynak(savasci_adi,x_entry, y_entry, i, selected_warrior):

        oyuncular[i - 1].savascilar.append([selected_warrior, "{}x{}".format(x_entry, y_entry)])
        for savasci in warriors:
            if savasci.name == savasci_adi:
                harcama = savasci.kaynak

        o_kaynak = oyuncular[i - 1].kaynak
        o_kaynak -= harcama
        oyuncular[i - 1].kaynak = o_kaynak

    #oyuncu bilgi tablosu yazdırma
    def oyuncu_bilgileri(sayi, oyuncular):
        konumy = 0.17

        for i in range(sayi):
            kisi = "Oyuncu " + str(i + 1)

            tablo_frame = tk.Frame(matrix_screen)
            tablo_frame.place(relx=0.11, rely=(konumy), anchor="center")

            tree = ttk.Treeview(tablo_frame, columns=("Kategori", "Bilgi"), show="headings")
            tree.column("Kategori", width=100)  # Kategori sütunu genişliği
            tree.column("Bilgi", width=200)
            tree.heading("Kategori", text=kisi)
            tree.heading("Bilgi", text="Bilgiler")
            tree.pack()

            # Oyuncu bilgilerini tabloya ekle
            tree.insert("", "end", values=("Kaynak", oyuncular[i].kaynak))
            tree.insert("", "end", values=("Alan", oyuncular[i].alan))
            tree.insert("", "end", values=("Yüzdelik Alan", oyuncular[i].yuzdelik_alan))

            konumy += 0.175


oyuncular = [
    Oyuncu(1, 200, [[]], 0, 0, [], []),
    Oyuncu(2, 200, [[]], 0, 0, [], []),
    Oyuncu(3, 200, [[]], 0, 0, [], []),
    Oyuncu(4, 200, [[]], 0, 0, [], [])
]

#dünya boyutu seçim ekranı
def game_place():
    gplace = tk.Label(player_wind, text="Dünya Boyutunu Seçiniz", font=("Times New Roman", 15))
    gplace.place(relx=0.5, rely=0.5, anchor="center")

    place8 = tk.Button(player_wind, text="8x8", command=lambda: Oyun_dunyasi.create_matrix_screen(8), width=10,
                       height=1)
    place8.place(relx=0.5, rely=0.6, anchor="center")

    place16 = tk.Button(player_wind, text="16x16", command=lambda: Oyun_dunyasi.create_matrix_screen(16), width=10,
                        height=1)
    place16.place(relx=0.5, rely=0.7, anchor="center")

    place24 = tk.Button(player_wind, text="24x24", command=lambda: Oyun_dunyasi.create_matrix_screen(24), width=10,
                        height=1)
    place24.place(relx=0.5, rely=0.8, anchor="center")

    place32 = tk.Button(player_wind, text="32x32", command=lambda: Oyun_dunyasi.create_matrix_screen(32), width=10,
                        height=1)
    place32.place(relx=0.5, rely=0.9, anchor="center")

#oyuncu sayısı seçim ekranı
game_name = tk.Label(player_wind, text="LORDS OF THE \n POLYWARPHISM", font=("Times New Roman", 25))
game_name.place(relx=0.5, rely=0.3, anchor="center")

pl1button = tk.Button(player_wind, text="1 player", command=lambda: Oyun_dunyasi.player_count(1), width=10, height=1)
pl1button.place(relx=0.5, rely=0.5, anchor="center")

pl2button = tk.Button(player_wind, text="2 player", command=lambda: Oyun_dunyasi.player_count(2), width=10, height=1)
pl2button.place(relx=0.5, rely=0.6, anchor="center")

pl3button = tk.Button(player_wind, text="3 player", command=lambda: Oyun_dunyasi.player_count(3), width=10, height=1)
pl3button.place(relx=0.5, rely=0.7, anchor="center")

pl4button = tk.Button(player_wind, text="4 player", command=lambda: Oyun_dunyasi.player_count(4), width=10, height=1)
pl4button.place(relx=0.5, rely=0.8, anchor="center")


class Oyun_dunyasi:

    #oyuncu sayısını tutma
    def player_count(count):
        global oyuncu_sayisi
        oyuncu_sayisi = int(count)
        Oyuncu.oyuncu_bilgileri(oyuncu_sayisi, oyuncular)

        buttons = [pl1button, pl2button, pl3button, pl4button]
        for b in buttons:
            b.destroy()
        game_place()

    #oyun kuralları sekmesi
    def show_help():
        global show_help
        help_window = tk.Tk()
        help_window.title("Yardım ve Bilgilendirme")
        help_window.geometry("800x300+600+300")

        help_text = """
        Oyun Kuralları:
        - Oyun 8x8, 16x16, 24x24 veya 32x32 boyutlarında bir dünya üzerinde oynanır.
        - Her oyuncu sırayla savaşçılarını dünyaya yerleştirir.
        - Savaşçılarınızı dünyaya yerleştirirken, rakiplerinizin savaşçılarını göz önünde bulundurun.
        - Savaşçılarınızın özelliklerini ve saldırı yeteneklerini dikkate alın.
        - Savaşçılarınızı stratejik olarak yerleştirerek rakiplerinizi yenmeye çalışın.

        İyi eğlenceler!
        """

        help_label = tk.Label(help_window, text=help_text, justify="left",font=("Times New Roman", 14), padx=10, pady=10)
        help_label.pack()

        help_window.mainloop()

    #onayla butonu işlemleri
    def onayla_buton_fonksiyonu(savasci_secim_pencere, x_entry, y_entry, selected_warrior, i):

        sayi = oyuncu_sayisi

        savasci_secim_pencere.destroy()
        Oyuncu.oyuncu_bilgileri(sayi, oyuncular)

        if i > int(oyuncu_sayisi):
            i = 1
            Oyun_dunyasi.savasci_secim_ekrani2(i)
        else:
            Oyun_dunyasi.savasci_secim_ekrani(i)

    #2. onayla butonu işlemleri
    def onayla_buton_fonksiyonu2(savasci_secim_pencere2, x_entry, y_entry, selected_warrior, i):

        sayi = oyuncu_sayisi

        savasci_secim_pencere2.destroy()
        Oyuncu.oyuncu_bilgileri(sayi, oyuncular)

        if i > int(oyuncu_sayisi):
            i = 1

        # İkinci oyuncunun seçimlerini yapması için pencereyi aç
        Oyun_dunyasi.savasci_secim_ekrani2(i)

    #savaşçı seçim ekranı oluşturma
    def savasci_secim_ekrani(i):

        i_2 = int(i)

        oyuncu_sayi = int(oyuncu_sayisi)
        global renkler
        renkler = ["black", "red", "#ffc0c0", "green", "#90EE90", "blue", "#ADD8E6", "#CCCC00", "#FFFFE0"]

        savasci_secim_pencere = tk.Tk()
        savasci_secim_pencere.geometry("330x700+1195+10")
        savasci_secim_pencere.title("Savaşçı Seçimi - Oyuncu {}".format(i))

        warrior_label = tk.Label(savasci_secim_pencere, text="Savaşçı Seçimi - Oyuncu {}".format(i),
                                 font=("Times New Roman", 15))
        warrior_label.place(relx=0.5, rely=0.1, anchor="center")

        # Savaşçı seçimi için dropdown menü
        selected_warrior = tk.StringVar(savasci_secim_pencere)
        warrior_names = [warrior.name for warrior in warriors]
        selected_warrior.set(warrior_names[0])  # Başlangıçta ilk savaşçı seçili

        warrior_menu = tk.OptionMenu(savasci_secim_pencere, selected_warrior, *warrior_names)
        warrior_menu.place(relx=0.5, rely=0.2, anchor="center")

        # Koordinat girişi için Entry widget'ları
        x_label = tk.Label(savasci_secim_pencere, text="X Koordinatı:")
        x_label.place(relx=0.5, rely=0.3, anchor="center")
        x_entry = tk.Entry(savasci_secim_pencere)
        x_entry.place(relx=0.5, rely=0.35, anchor="center")

        y_label = tk.Label(savasci_secim_pencere, text="Y Koordinatı:")
        y_label.place(relx=0.5, rely=0.4, anchor="center")
        y_entry = tk.Entry(savasci_secim_pencere)
        y_entry.place(relx=0.5, rely=0.45, anchor="center")

        # Kaynak bilgisi
        kaynak_bilgi_label = tk.Label(savasci_secim_pencere, text="Mevcut Kaynak: {}".format(oyuncular[i - 1].kaynak))
        kaynak_bilgi_label.place(relx=0.5, rely=0.5, anchor="center")

        konumlandir_button = tk.Button(savasci_secim_pencere, text="Konumlandır", font=("Times New Roman", 12),
                                       command=lambda: Oyun_dunyasi.guncelleme(
                                           int(x_entry.get()), int(y_entry.get()), int(cell_size), canvas,
                                           renkler[(2 * i) - 1],
                                           renkler[(2 * i)], selected_warrior.get()[0] + str(i), i_2,
                                           selected_warrior.get()))
        konumlandir_button.place(relx=0.5, rely=0.63, anchor="center")

        # Pas geçme butonu
        pass_button = tk.Button(savasci_secim_pencere, text="Pas Geç", font=("Times New Roman", 12))
        # command=lambda: Oyuncu.pass_turn(oyuncu, savaşçı_seçim_pencere))
        pass_button.place(relx=0.3, rely=0.7, anchor="center")

        # Onayla butonu
        confirm_button = tk.Button(savasci_secim_pencere, text="Onayla", font=("Times New Roman", 12),
                                   command=lambda: Oyun_dunyasi.onayla_buton_fonksiyonu(savasci_secim_pencere,
                                                                                        x_entry.get(),
                                                                                        y_entry.get(), selected_warrior,
                                                                                        i + 1))

        confirm_button.place(relx=0.7, rely=0.7, anchor="center")

        saldiri_label = tk.Label(savasci_secim_pencere, text="Saldırı Seç", font=("Times New Roman", 12))
        saldiri_label.place(relx=0.5, rely=0.75, anchor="center")

        saldiri_secim = tk.StringVar(savasci_secim_pencere)
        oyuncu_s = oyuncular[i - 1]
        savasci_secim = oyuncu_s.savascilar
        saldiri_secim.set(savasci_secim[0])

        saldiri_menu = tk.OptionMenu(savasci_secim_pencere, saldiri_secim, *savasci_secim)
        saldiri_menu.place(relx=0.5, rely=0.8, anchor="center")

        savasci_secim_pencere.mainloop()

    def savasci_secim_ekrani2(i):

        i_2 = int(i)

        oyuncu_sayi = int(oyuncu_sayisi)
        global renkler
        renkler = ["black", "red", "#ffc0c0", "green", "#90EE90", "blue", "#ADD8E6", "#CCCC00", "#FFFFE0"]

        savasci_secim_pencere2 = tk.Tk()
        savasci_secim_pencere2.geometry("330x700+1195+10")
        savasci_secim_pencere2.title("Savaşçı Seçimi - Oyuncu {}".format(i))

        warrior_label2 = tk.Label(savasci_secim_pencere2, text="Savaşçı Seçimi - Oyuncu {}".format(i),
                                  font=("Times New Roman", 15))
        warrior_label2.place(relx=0.5, rely=0.1, anchor="center")

        # Savaşçı seçimi için dropdown menü
        selected_warrior2 = tk.StringVar(savasci_secim_pencere2)
        warrior_names2 = [warrior.name for warrior in warriors]
        selected_warrior2.set(warrior_names2[0])  # Başlangıçta ilk savaşçı seçili

        warrior_menu2 = tk.OptionMenu(savasci_secim_pencere2, selected_warrior2, *warrior_names2)
        warrior_menu2.place(relx=0.5, rely=0.2, anchor="center")

        # Koordinat girişi için Entry widget'ları
        xy_label = tk.Label(savasci_secim_pencere2, text="X-Y Koordinatı:")
        xy_label.place(relx=0.5, rely=0.3, anchor="center")

        xy_entry2 = tk.StringVar(savasci_secim_pencere2)
        xy_liste = oyuncular[i - 1]
        xy_list2 = xy_liste.cevre
        xy_entry2.set(xy_list2[0])

        xy_menu2 = tk.OptionMenu(savasci_secim_pencere2, xy_entry2, *xy_list2)
        xy_menu2.place(relx=0.5, rely=0.35, anchor="center")
        secilmis_k = xy_entry2.get()
        koordinat2 = secilmis_k[1:-1]
        x_entry2, y_entry2 = koordinat2.split(',')

        # Kaynak bilgisi
        kaynak_bilgi_label2 = tk.Label(savasci_secim_pencere2, text="Mevcut Kaynak: {}".format(oyuncular[i - 1].kaynak))
        kaynak_bilgi_label2.place(relx=0.5, rely=0.4, anchor="center")

        konumlandir_button2 = tk.Button(savasci_secim_pencere2, text="Konumlandır", font=("Times New Roman", 12),
                                        command=lambda: Oyun_dunyasi.guncelleme(
                                            int((xy_entry2.get()[1:-1].split(','))[0]),
                                            int((xy_entry2.get()[1:-1].split(','))[1]),
                                            int(cell_size), canvas, renkler[(2 * i) - 1],
                                            renkler[(2 * i)], selected_warrior2.get()[0] + str(i), i_2,
                                            selected_warrior2.get()))
        konumlandir_button2.place(relx=0.5, rely=0.5, anchor="center")

        # Pas geçme butonu
        pass_button2 = tk.Button(savasci_secim_pencere2, text="Pas Geç", font=("Times New Roman", 12))
        # command=lambda: Oyuncu.pass_turn(oyuncu, savaşçı_seçim_pencere))
        pass_button2.place(relx=0.3, rely=0.6, anchor="center")

        # Onayla butonu
        confirm_button2 = tk.Button(savasci_secim_pencere2, text="Onayla", font=("Times New Roman", 12),
                                    command=lambda: Oyun_dunyasi.onayla_buton_fonksiyonu2(savasci_secim_pencere2,
                                                                                          int((xy_entry2.get()[
                                                                                               1:-1].split(','))[0]),
                                                                                          int((xy_entry2.get()[
                                                                                               1:-1].split(','))[1]),
                                                                                          selected_warrior2, i + 1))

        confirm_button2.place(relx=0.7, rely=0.6, anchor="center")

        saldiri_label2 = tk.Label(savasci_secim_pencere2, text="Saldırı Seç", font=("Times New Roman", 12))
        saldiri_label2.place(relx=0.5, rely=0.7, anchor="center")

        saldiri_secim2 = tk.StringVar(savasci_secim_pencere2)
        oyuncu_s2 = oyuncular[i - 1]
        savasci_secim2 = oyuncu_s2.savascilar
        saldiri_secim2.set(savasci_secim2[0])

        saldiri_menu2 = tk.OptionMenu(savasci_secim_pencere2, saldiri_secim2, *savasci_secim2)
        saldiri_menu2.place(relx=0.5, rely=0.75, anchor="center")

        saldiri_button2 = tk.Button(savasci_secim_pencere2, text="Saldır!", font=("Times New Roman", 12),
                                    command=lambda: Oyun_dunyasi.saldiri_yonetimi(saldiri_secim2.get(),
                                                                                  (saldiri_secim2.get().split(' '))[1],
                                                                                  (saldiri_secim2.get().split(' '))[1],
                                                                                  int(cell_size), canvas, i))

        saldiri_button2.place(relx=0.5, rely=0.82, anchor="center")

        savasci_secim_pencere2.mainloop()

    def saldiri_yonetimi(savasci, x, y, cell, canvas, i):
        x1 = int(x.split("x")[0][1:])
        y1 = int(y.split("x")[1][0])
        savasci_a = (savasci.split(" "))[0][2:-2]
        if savasci_a == 'Muhafız':
            Muhafiz.saldir(x1, y1, cell_size, canvas,i)
        elif savasci_a == 'Okçu':
            Okcu.saldir(x1, y1, cell_size, canvas, i)
        elif savasci_a == 'Topçu':
            Topcu.saldir(x1, y1, cell_size, canvas, i)
        elif savasci_a == 'Atlı':
            Atli.saldir(x1, y1, cell_size, canvas, i)
        elif savasci_a == 'Sağlıkçı':
            Saglikci.saldir(x1, y1, cell_size, canvas, i)

    def guncelleme(x_ent, y_ent, cell_s, canv, renk1, renk2, warrior_basharfi, i, savasci_adi):
        Oyun_dunyasi.ozel_renk_boyama_fonksiyonu(x_ent, y_ent, cell_s, canv, renk1, renk2, warrior_basharfi)
        Oyuncu.sahip_olunan_alan(x_ent, y_ent, i)
        Oyuncu.oyuncu_kaynak(savasci_adi,x_ent, y_ent, i, savasci_adi)
        Oyuncu.s_cevre_koordinatlari(x_ent, y_ent, i)

    @staticmethod
    def create_matrix_screen(boyut):
        player_wind.destroy()
        global d_boyut
        d_boyut = int(boyut)

        global cell_size
        global canvas

        cell_size = min(matrix_screen.winfo_screenwidth() // boyut, matrix_screen.winfo_screenheight() // boyut)
        canvas = tk.Canvas(matrix_screen, bg="black", width=boyut * cell_size, height=boyut * cell_size)
        canvas.pack()

        # Matrisi satır ve sütunlara ayırarak küçük kutucukları oluştur
        for i in range(boyut + 1):
            x = i * cell_size
            canvas.create_line(x, 0, x, boyut * cell_size, fill="white")
            y = i * cell_size
            canvas.create_line(0, y, boyut * cell_size, y, fill="white")

        for i in range(boyut):
            for j in range(boyut):
                x1, y1 = i * cell_size, j * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
                canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=".", fill="white")

        # Yardım ve bilgilendirme butonu
        help_button = tk.Button(matrix_screen, text="Yardım ve Bilgilendirme", font=("Times New Roman", 12),
                                        command=Oyun_dunyasi.show_help, width=18, height=2)
        help_button.place(relx=0.1, rely=0.95, anchor="center")

        # Ekranı kapatma tuşu ekleyin
        close_button = tk.Button(matrix_screen, text="Kapat", font=("Times New Roman", 15),
                                 command=matrix_screen.destroy,
                                 width=15, height=2)
        close_button.place(relx=0.9, rely=0.88, anchor="center")

        # Oyun_dunyasi.ozel_renk_liste_fonksiyonu(cevre_koordinat, cell_size, canvas, renkler[0], renkler[1], ".")

        baslat_buton = tk.Button(matrix_screen, text="Oyunu Başlat",font=("Times New Roman", 13),
                                 command=lambda: Oyun_dunyasi.savasci_secim_ekrani(1), width=20, height=2)
        baslat_buton.place(relx=0.1, rely=0.87, anchor="center")

        matrix_screen.mainloop()

    def hata_mesaji():
        hata_penceresi = tk.Tk()
        hata_penceresi.title("HATA")
        hata_penceresi.geometry("300x100+700+400")

        hata_label = tk.Label(hata_penceresi,
                              text="Seçtiğiniz Koordinatlar \n savaşçı yerleştimek için \n uygun değil!",
                              font=("Times New Roman", 12))
        hata_label.place(relx=0.5, rely=0.3, anchor="center")

    @staticmethod
    def ozel_renk_boyama_fonksiyonu(x, y, cell_size, canvas, rnk, rnk2, savasci):
        liste = ["red", "#ffc0c0", "green", "#90EE90", "blue", "#ADD8E6", "#CCCC00", "#FFFFE0"]
        liste.remove(rnk)
        liste.remove(rnk2)
        x1, y1 = x * cell_size, y * cell_size
        x2, y2 = x1 + cell_size, y1 + cell_size

        if canvas.itemcget(canvas.find_closest((x1 + x2) / 2, (y1 + y2) / 2), "fill") in liste:
            Oyun_dunyasi.hata_mesaji()
            return

        canvas.create_rectangle(x1, y1, x2, y2, outline="white", fill=rnk2)
        metin = savasci
        text_x, text_y = (x1 + x2) // 2, (y1 + y2) // 2
        canvas.create_text(text_x, text_y, text=metin, font=("Times New Roman", 12), fill=rnk)

    def ozel_renk_liste_fonksiyonu(koordinat_listesi, cell_size, canvas, rnk, rnk2, savasci):
        for koordinat in koordinat_listesi:
            x, y = koordinat
            x1, y1 = x * cell_size, y * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            canvas.create_rectangle(x1, y1, x2, y2, outline="white", fill=rnk2)
            metin = savasci
            text_x, text_y = (x1 + x2) // 2, (y1 + y2) // 2
            canvas.create_text(text_x, text_y, text=metin, font=("Times New Roman", 12), fill=rnk)


player_wind.mainloop()
