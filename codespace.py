def todolist():
    taches = []

    while True:
        print("\n menu de la To do list:")
        print(" 1. afficher les taches")
        print(" 2. ajouter une tache")
        print(" 3. supprimer une tache")
        print(" 4. quitter")

        choix = input(" choisissez une option:").strip()

        if choix == "1":   
            if taches:
                print("les taches dans la liste sont:")
                for i, tache in enumerate(taches, start=1):
                    print(f"{i}. {tache}")
        
            else:
                print("il n'y a pas encore de tache dans la liste.")


        elif choix == "2":
            nouvelle_tache = input("entrez la tache").strip()
            taches.append(nouvelle_tache)
            print(f"la tache {nouvelle_tache} a bien ete ajouter a la liste.")
            
            

            

todolist()