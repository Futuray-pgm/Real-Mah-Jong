from random import randint
import plaquettes

def fin(garder_jeton, jeton=0)  :
    if garder_jeton == "oui" :
        print("Aller a fin")
    elif garder_jeton == "non" :
        print("ne pas aller a fin")

class gagner :
    def pan(jeton, ordi_num) :
        if ordi_num == "est" :
            for num in range(len(plaquette_est)) :
                if plaquette_est[num] == jeton and num in plaquette_est:
                    plaquette_est.remove(num)
            for _ in range(3) :
                plaquette_pans_est.append(jeton)
        fin("non")
    
    def show(jeton, ordi_num, verif_show) :
        if ordi_num == "est" :
            plaquette_pans_est.append(jeton)
            plaquette_pans_est.append(plaquette_est[verif_show[0]])
            plaquette_est.pop(verif_show[0])
            plaquette_pans_est.append(plaquette_est[verif_show[1]])
            plaquette_est.pop(verif_show[1])
        fin("non")
    
    def prendre(jeton, ordi_num, verif_show) :
        if ordi_num == "est" :
            ok = True
            while ok :
                num = randint(0, len(plaquette_est))
                if num not in verif_show :
                    ok = False
            plaquette_est.pop(num)
            plaquette_est.append(jeton)
        fin("non")
    
    def jeter(jeton) :
        jeton_pioche = jeton

def algo_ia(jeton, ordi_num) :
    #Choix du bon ordi = ORDI_NUM.
    nombre = 0
    verif_show = []
    if ordi_num == "est" :
            #Recherche de pion pareil a JETON dans la plaquette_est.
            for num in range(len(plaquette_est)) :
                try :
                    pareil = plaquette_est.index(jeton, num-1, num)
                    pareil = True
                except ValueError :
                    pareil = False
                if pareil == True :
                    nombre = nombre + 1
                if nombre == 2 :
                    break
            if nombre == 2 :
                #PAN
                gagner.pan(jeton, ordi_num)
            else :
                #Recherche de pion +0.1/-0.1 a JETON dans la plaquette_est.
                presque = jeton - 0.1
                nombre = 0
                for _ in range(2) :
                    num = 0
                    for num in range(len(plaquette_est)) :
                        try :
                            pareil = plaquette_est.index(presque, num-1, num)
                            pareil = True
                        except ValueError :
                           pareil = False
                        if pareil == True :
                            nombre = nombre + 1
                            verif_show.append(plaquette_est.index(presque, num-1, num))
                        if nombre == 2 :
                            break
                    if nombre == 2 :
                        # show
                        gagner.show(jeton, ordi_num, verif_show)
                        break
                    presque = jeton + 0.1
                
                if nombre <= 1 :
                    #Recherche de pion +0.2/-0.2 a JETON dans la plaquette_est.
                    presque = (jeton * 10 - 2) / 10
                    for _ in range(2) :
                        num = 0
                        for num in range(len(plaquette_est)) :
                            try :
                                pareil = plaquette_est.index(presque, num-1, num)
                                pareil = True
                            except ValueError :
                               pareil = False
                            if pareil == True :
                                nombre = nombre + 1
                                verif_show.append(plaquette_est.index(presque, num-1, num))
                    presque = jeton + 0.2
            if nombre >= 1 :
                # pion a prendre
                gagner.prendre(jeton, ordi_num, verif_show)
            else :
                gagner.jeter(jeton, ordi_num)
                
    if ordi_num == "sud" :
        #Recherche de pion pareil a JETON dans la plaquette_sud.
        print("l")
    if ordi_num == "ouest" :
        #Recherche de pion pareil a JETON dans la plaquette_ouest.
        print("l")

def main(jeton, ordi_num) :
    algo_ia(jeton, ordi_num)

if __name__ == "__main__" :
    a = 0
    b = ""
    a = input()
    b = input()
    print(a, b)
    algo_ia(a, b)