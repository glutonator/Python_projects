
def ewakuacja (lista_osob, liczba_klatek_schodowych, liczba_osob_w_rzedzie, tempo_schodzenia ):
    odst_czas = 1
    out = list()
    temp = liczba_osob_w_rzedzie * liczba_klatek_schodowych
    lista_osob_rev = list(lista_osob)
    lista_osob_rev.reverse()
    czas_od_pocz =0    
    for x in lista_osob_rev:
        out.append(czas_od_pocz)        
        liczba_krokow_do_opusz_pietra =0
        #liczba krokow potrzbna do opuszczenia pietra
        for y in range(0,x,temp):
            liczba_krokow_do_opusz_pietra+=1
        czas_od_pocz+=liczba_krokow_do_opusz_pietra*odst_czas+tempo_schodzenia
    out.reverse()
    return out
    





lista_osob = [5, 10, 15]
liczba_klatek_schodowych = 2
liczba_osob_w_rzedzie = 1
tempo_schodzenia = 30

ewakuacja(
    lista_osob=lista_osob,
    liczba_klatek_schodowych=liczba_klatek_schodowych,
    liczba_osob_w_rzedzie=liczba_osob_w_rzedzie,
    tempo_schodzenia=tempo_schodzenia
)

assert [73, 38, 0] == ewakuacja(
    lista_osob=lista_osob,
    liczba_klatek_schodowych=liczba_klatek_schodowych,
    liczba_osob_w_rzedzie=liczba_osob_w_rzedzie,
    tempo_schodzenia=tempo_schodzenia
)