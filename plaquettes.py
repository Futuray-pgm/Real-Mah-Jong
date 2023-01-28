class modifier :
    class creer :
        def norm() :
            # création des variables qui représentes les plaquettes
            plaquette_joueur = [1.1,2.2,2.3,3.3,3.4,3.5,3.8,3.9,4.2,4.7,4.7,5.6,5.6] # Nord
            plaquette_est = [1.3,2.2,3.2,3.2,3.3,3.7,4.1,4.3,4.7,4.8,5.4,5.5,5.5]
            plaquette_sud = [1.1,1.2,1.3,2.1,3.1,3.4,3.5,3.6,3.7,3.9,4.2,4.6,5.2]
            plaquette_ouest = [1.2,1.1,2.1,2.4,3.6,3.8,4.4,4.5,4.5,4.6,5.1,5.4,5.9]
        def pan() :
            # création des variables qui représentes les plaquettes des pans et show
            plaquette_pans_joueur = [0,0,0,0,0,0,0,0,0,0,0,0,0,0] # Nord
            plaquette_pans_est = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            plaquette_pans_sud = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            plaquette_pans_ouest = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    class suprimer :
        class norm :
            def joueur(num) :
                if num in plaquette_joueur :
                    plaquette_joueur.remove(num)
            def est(num) :
                if num in plaquette_est :
                    plaquette_est.remove(num)
            def sud(num) :
                if num in plaquette_sud :
                    plaquette_sud.remove(num)
            def ouest(num) :
                if num in plaquette_ouest :
                    plaquette_ouest.remove(num)
    class ajouter :
        class norm :
            def joueur(num) :
                plaquette_joueur.append(num)
            def est(num) :
                plaquette_est.append(num)
            def sud(num) :
                plaquette_sud.append(num)
            def ouest(num) :
                plaquette_ouest.append(num)
        class pan :
            def est() :
                plaquette_pans_est.append(num)

class dire :
    def norm(ordi_num) :
        if ordi_num == "est" :
            return(plaquette_est)

'''
modifier.creer.norm()
modifier.creer.pan()
modifier.suprimer.norm.sud(3.4)
print(plaquette_sud)
modifier.ajouter.norm.sud(9.9)
print(plaquette_sud)
'''