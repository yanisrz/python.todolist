def todolist():
    taches = []

    while True:
        print("\n Option de la To do list:")
        print(" 1. Afficher les taches")
        print(" 2. Ajouter une tache")
        print(" 3. Supprimer une tache")
        print(" 4. Supprimer toutes les taches")
        print(" 5. Quitter")
        #print(" 5. Enregistrer les taches dans un fichier texte")
        print("")

        choix = input(" Choisissez une option:  ").strip()
        print("")

        if choix == "1":   
            if taches:
                print("Les taches dans la liste sont:")
                
                i=1
                for tache in taches:
                    print(f"{i}.{tache}")
                    i+=1
                    
        
            else:
                print(" Il n'y a pas encore de tache dans la liste.")
                


        elif choix == "2":
            nouvelle_tache = input("Entrez la tache a ajouter:  ").strip()
            print("")
            taches.append(nouvelle_tache)
            print(f"La tache \"{nouvelle_tache}\" a bien ete ajouter a la liste.")

        elif choix == "3":
            if taches:
                print("Les taches de la listes sont:")
                i=1
                for tache in taches:
                    print(f"{i}.{tache}")
                    i+=1
                tache_suprimee = input("Entrez le numero de la taches a suprimez:  ").strip()
                
                print("")
                if tache_suprimee.isdigit() == False:
                    print("Veuillez entrer un numero valide.")
                else:
                    tache_suprimee = int(tache_suprimee)
                    nombre_taches = len(taches)
                    if 0 < (tache_suprimee) <= nombre_taches:
                        tache_suprimee = taches.pop((tache_suprimee) - 1)
                        print(f"La taches \"{tache_suprimee}\" a bien ete suprimez de la liste.")
                    elif tache_suprimee > nombre_taches:
                        print("Veuillez entrer un numero valide.")
            else:
                print("Il n'y a pas de tache a suprimez dans la liste.")

        elif choix == "4":
                if taches:
                    print("Toutes les taches ont ete suprimez de la liste.")
                taches.clear()
        

        
        elif choix == "5":
                    print(" Aurevoir!")
                    break
        else: 
            print(" Option introuvable.")
            print(" Veuillez choisir une option valide.")


                


            
            

            

todolist()
