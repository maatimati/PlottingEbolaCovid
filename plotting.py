#----------#----------#----------#----------#----------#----------#
#          Codice usato per graficare i dati di Ebola e           #
#                        Covid nella ricerca:                     #
#   "Studio del grafico probabile del coronavirus e dell'ebola    #
#                  tramite modello SIS e SIR"                     #
#                                                                 #
#                  Autore: Matilde Albonetti                      #
#----------#----------#----------#----------#----------#----------#

import matplotlib.pyplot as plt

r = 0
rCovid = 'M'
rEbola = 'M'
ch = 'Y'

#Sono stati considerati i dati Covid dal mese di Gennaio 2021
giorniCovid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

casiCovid = [141358, 61046, 68052, 170844, 189109, 219441, 108304, 197552,
15659, 101762, 220532, 196224, 184615, 186253, 180426, 149512, 83403, 228179,
192320, 188797, 197106, 171263, 138860, 77696, 186740, 167206, 155697, 143898,
137147, 104065, 57715]

mortiCovid = [111, 133, 140, 259, 231, 198, 223, 184, 157, 227, 294, 313, 316,
360, 308, 248, 287, 434, 380, 385, 373, 333, 227, 352, 468, 426, 389, 378, 377,
235, 349]

#Sono stati considerati i dati ebola dal periodo 2014-2015
giorniEbola = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
 61, 62, 63, 64, 65]

mortiEbola = [244, 134, 722, 427, 196, 340, 212, 194, 330, 317, 673, 527, 318,
381, 230, 39, 260, 200, 142, 29, 0, 45, 322, 1809, 160, 211, 79, 191, 257, 296,
125, 77, 121, 84, 76, 55, 53, 29, 45, 61, 97, 57, 12, 28, 29, 64, 21, 51, 129, 1,
85, 21, 23, 8, 19, 17, 2, 9, 10, 7, 7, 21, 6, 1, 59]

casiEbola = [613, 306, 1178, 835, 399, 771, 428, 529, 541, 259, 1344, 661, 797,
1210, 584, 206, 1047, 830, 226, 3562, 205, 720, 3454, 423, 493, 553, 326, 260, 638,
454, 142, 233, 113, 152, 127, 69, 68, 108, 45, 84, 76, 44, 85, 160, 71, 54, 36, 84,
45, 39, 25, 2, 10, 13, 5, 6, 40, 6, 28, 5, 16, 11, 17, 0, 86]

while True:
    print("\nQuesto programma mostra i grafici di casi e morti sia da Covid che da Ebola, rispettivamente dal periodo di Gennaio 2021 e dal periodo 2014-2015. \nInserire: \n1 - Grafici Covid \n2 - Grafici Ebola")
    r = int(input())
    match(r):
        case 1:
            print("\nE' stato scelto Covid. \nInserire M per ottenere il grafico dei morti oppure C per ottenere il grafico dei casi: ")
            rCovid = input()
            while True:
                if rCovid == 'M' or rCovid == 'm':
                    plt.title("Morti Covid")
                    plt.xlabel("Giorni")
                    plt.ylabel("Persone")
                    plt.plot(giorniCovid, mortiCovid)
                    plt.show()
                    break
                elif rCovid == 'C' or rCovid == 'c':
                    plt.title("Casi Covid")
                    plt.xlabel("Giorni")
                    plt.ylabel("Persone")
                    plt.plot(giorniCovid, casiCovid)
                    plt.show()
                    break
                else:
                    print("\nE' stato inserito un valore non valido. Inserire M per ottenere il grafico dei morti oppure C per ottenere il grafico dei casi: ")
                    rCovid = input()
        case 2:
            print("\nE' stato scelto Ebola. \nInserire M per ottenere il grafico dei morti, C per ottenere il grafico dei casi, T per il grafico sia dei morti che dei casi: ")
            rEbola = input()
            while True:
                if rEbola == 'M' or rEbola == 'm':
                    plt.title("Morti Ebola")
                    plt.xlabel("Giorni")
                    plt.ylabel("Persone")
                    plt.plot(giorniEbola, mortiEbola)
                    plt.show()
                    break
                elif rEbola == 'C' or rEbola == 'c':
                    plt.title("Casi Ebola")
                    plt.xlabel("Giorni")
                    plt.ylabel("Persone")
                    plt.plot(giorniEbola, casiEbola)
                    plt.show()
                    break
                elif rEbola == 'T' or rEbola == 't':
                    plt.title("Ebola")
                    plt.xlabel("Giorni")
                    plt.ylabel("Persone")
                    plt.plot(giorniEbola, casiEbola, "-b", label = "Casi")
                    plt.plot(giorniEbola, mortiEbola, "-r", label = "Morti")
                    plt.legend(loc="upper right")
                    plt.show()
                    break
                else:
                    print("\nE' stato inserito un valore non valido. Inserire M per ottenere il grafico dei morti oppure C per ottenere il grafico dei casi: ")
                    rEbola = input()
        case _:
            print("\nE' stato inserito un valore non valido.")
    ch = input("\nVuole rieseguire il programma? (Y/N): ")
    if ch == 'N' or ch == 'n':
        print("Grazie di aver usato il programma :]")
        break
