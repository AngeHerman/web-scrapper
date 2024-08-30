from wiki_scrapper.starwars_sc import starwars_parser
from download_scrapper.nycbikesdata_sc import nycbikes_parser

def main():
    while True:
        print("---------------------------------------------------------")
        print("Choisissez une option :")
        print("1. Lancer le parser Star Wars")
        print("2. Lancer le parser NYC Bikes")
        print("3. Quitter")
        print("---------------------------------------------------------")

        choix = input("Tapez 1, 2 ou 3 : ")

        if choix == '1':
            starwars_parser()
        elif choix == '2':
            nycbikes_parser()
        elif choix == '3':
            print("Au revoir!")
            break
        else:
            print("Choix non valide, veuillez réessayer.")

if __name__ == "__main__":
    main()
