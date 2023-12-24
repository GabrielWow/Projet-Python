import random

def choisir_mot():
    mots = ["python", "programmation", "ordinateur", "développement", "algorithmique", "openai"]
    return random.choice(mots).upper()

def afficher_mot_cache(mot, lettres_trouvees):
    mot_cache = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_cache += lettre
        else:
            mot_cache += "_"
    return mot_cache

def jouer_pendu():
    mot_a_trouver = choisir_mot()
    lettres_trouvees = []
    tentatives_max = 6
    tentatives = 0

    print("Bienvenue au jeu du pendu!")
    print(afficher_mot_cache(mot_a_trouver, lettres_trouvees))

    while tentatives < tentatives_max:
        proposition = input("Devinez une lettre : ").upper()

        if proposition in lettres_trouvees:
            print("Vous avez déjà deviné cette lettre. Essayez une autre.")
            continue

        if proposition in mot_a_trouver:
            print("Bonne devinette!")
            lettres_trouvees.append(proposition)
        else:
            print("Mauvaise devinette. Essayez encore.")
            tentatives += 1

        mot_cache = afficher_mot_cache(mot_a_trouver, lettres_trouvees)
        print(mot_cache)

        if "_" not in mot_cache:
            print("Félicitations, vous avez gagné!")
            break

    if "_" in afficher_mot_cache(mot_a_trouver, lettres_trouvees):
        print(f"Dommage! Le mot était {mot_a_trouver}.")

if __name__ == "__main__":
    jouer_pendu()
