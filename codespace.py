def todolist():
    # Créer une liste pour stocker les tâches
    taches = []
    #entre dans une boucle infinie
    while True:
        print("\n Option de la To do list:")
        print(" 1. Afficher les taches")
        print(" 2. Ajouter une tache")
        print(" 3. Supprimer une tache")
        print(" 4. Supprimer toutes les taches")
        print(" 5. Quitter")
        #print(" 5. Enregistrer les taches dans un fichier texte")
        print("")
        # Demander à l'utilisateur de choisir une option et enleve les espaces inutiles
        choix = input(" Choisissez une option:  ").strip()
        print("")

        if choix == "1":
            
               
            if taches:
                print("Les taches dans la liste sont:")
                print("____________________________________________\n")
                #affiche toute les taches de la liste avec un numero devant chaque tache ( possibilité d'utiliser enumerate(for i, tache in enumerate(taches, start=1))
                i=1
                for tache in taches:
                    print(f"{i}. {tache}")
                    i+=1
                print("____________________________________________\n")
        
            else:
                print("____________________________________________\n")
                print(" Il n'y a pas encore de tache dans la liste.")
                print("____________________________________________\n")
               


        elif choix == "2":
            nouvelle_tache = input("Entrez la tache a ajouter:  ").strip()
            print("")
            #ajoutes un nouvelle tache ans la liste puis reviens au haut de la boucle
            taches.append(nouvelle_tache)
            print("_____________________________________________________________\n")
            print("")
            print(f"La tache \"{nouvelle_tache}\" a bien ete ajouter a la liste.")
            print("_____________________________________________________________\n")
            print("")
            print("Les taches dans la liste sont:")
            print("____________________________________________\n")
            
            i=1
            for tache in taches:
                print(f"{i}. {tache}")
                i+=1
            print("____________________________________________\n")   

        elif choix == "3":
            if taches:
                print("Les taches de la listes sont:")
                print("____________________________________________\n")   

                i=1
                for tache in taches:
                    print(f"{i}.{tache}")
                    i+=1
                print("____________________________________________\n")   

                tache_suprimee = input("Entrez le numero de la taches a suprimez:  ").strip()
                
                print("")
                if tache_suprimee.isdigit() == False:
                    print("Veuillez entrer un numéro valide.")
                else:
                    tache_suprimee = int(tache_suprimee)
                    nombre_taches = len(taches)
                    if 0 < (tache_suprimee) <= nombre_taches:
                        tache_suprimee = taches.pop((tache_suprimee) - 1)
                        print("\n\n_____________________________________________________________\n")
                        print(f"La taches \"{tache_suprimee}\" à bien été suprimée de la liste.")
                        print("_____________________________________________________________\n")
                    elif tache_suprimee > nombre_taches:
                        print("Veuillez entrer un numéro valide.")
            else:
                print("Il n'y a pas de tache a suprimer dans la liste.")

        elif choix == "4":
                if taches:
                    print("_____________________________________________________________\n")
                    print("Toutes les taches ont été suprimées de la liste.")
                    print("_____________________________________________________________\n")
                taches.clear()
        

        
        elif choix == "5":
                    print(" Aurevoir!")
                    break
        else: 
            print(" -------------------------------------")
            print(" |Option introuvable.                |")
            print(" |Veuillez choisir une option valide.|")
            print(" -------------------------------------")

todolist()
 