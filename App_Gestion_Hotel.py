#Projet de gestion de chambres de l'hôtel de Jules Coomans

class Hotel:
    def __init__(self):
        self.clients = []
        self.chambres = []
        self.reservations = []

    # Clients
    def ajouter_client(self, client):
        self.clients.append(client)

    def lister_clients(self):
        for client in self.clients:
            client.afficher()

    # Chambres
    def ajouter_chambre(self, chambre):
        self.chambres.append(chambre)

    def lister_chambres(self):
        for chambre in self.chambres:
            print(f"Chambre : {chambre.numero}  Type : {chambre.type} Prix : {chambre.prix}€")

    # Réservations
    def ajouter_reservation(self, reservation , client, chambre):
        self.reservations.append(reservation)
        self.clients.append(client)
        self.chambres.append(chambre)
        print(f"Réservation effectuée pour {client.nom} {client.prenom} dans la chambre {chambre.numero}.")

    def lister_reservations(self):
        ...
# -----------------------------------------------------------------------------------------


class Client:
    def __init__ (self, nom, prenom , adresse , numero_tel ):
        self.nom = nom
        self.prenom = prenom
        self.numero_tel = numero_tel
        self.adresse = adresse

    def afficher(self):
        print(f"Client : {self.nom} {self.prenom}")

# -----------------------------------------------------------------------------------------
class FichierClient:
    def __init__(self):
        self.liste_clients = []  # Correction ici : self.liste_clients

    def ajouter_client(self):
        nom = input("nom ?")
        prenom = input("prenom ?")
        numero_tel = input("Numéro de téléphone ? ")
        adresse = input("adresse ?")
        nouveau_client = Client(nom, prenom, adresse, numero_tel)
        self.liste_clients.append(nouveau_client)
        print(f"Le client {nom} {prenom} a bien été ajouté à la liste des clients.")

# -----------------------------------------------------------------------------------------
class Chambre:
    def __init__ (self, numero, type, prix):
        self.numero = numero
        self.type = type
        self.prix = prix

# -----------------------------------------------------------------------------------------
class Reservation:
    def __init__ (self, date, nom_client, numero_tel):
        self.date = date
        self.nom_client = nom_client
        self.numero_tel = numero_tel

    def afficher_reservation(self):
        print(f"Réservation pour {self.nom_client} le {self.date}.")
        print(f"Numéro de téléphone : {self.numero_tel}")
        # Ces champs ne sont pas définis dans l'objet
        # print(f"Chambre réservée : {self.chambre_id}")
        # print(f"Date d'arrivée : {self.date_arrivee}")
        # print(f"Date de départ : {self.date_depart}")
        print(f"Client : {self.nom_client}")


# -----------------------------------------------------------------------------------------
# MENU PRINCIPAL
# -----------------------------------------------------------------------------------------

def clear_console():
    print("\n" * 50)

def afficher_menu():
    print("Bonjour, application de gestion de chambre d'hôtel de l'hôtel GEMA !")
    print("1. Ajouter un client")
    print("2. Faire une réservation")
    print("3. Afficher les réservations")
    print("4. Afficher les clients")
    print("5. Afficher les chambres")
    print("q. Quitter l'application")

# -------------------------------------- MAIN ---------------------------------------------------
if __name__ == "__main__":
    # Données des clients déjà présents dans l'hôtel
    client1 = Client("Alice", "Martine", "78 rue champ", "0689562457")
    client2 = Client("Bob", "Martin", "78 rue champ", "07821976348")
    client3 = Client("Light", "Yagami", "7 rue champ", "0667812459")

    fichier_reservation = []  # Initialisation correcte
    hotel = Hotel()

    hotel.ajouter_client(client1)
    hotel.ajouter_client(client2)
    hotel.ajouter_client(client3)

    while True:
        clear_console()
        afficher_menu()
        choix = input("Choisissez une option : ")

        # --------------------------------------------- CHOIX 1 ---------------------------------------------
        if choix == "1":
            clear_console()
            print("Ajout d'un nouveau client dand l'hotel")
            nom = input("Nom du client : ")
            prenom = input("Prenom :")
            numero_tel = input("numero_tel:")
            adresse = input("adresse:")
            nouveau_client = Client(nom, prenom ,numero_tel, adresse)
            hotel.ajouter_client(nouveau_client)
            print(f"Le client {nom} {prenom} a été ajouté à la liste des clients du super hôtel.")
            input("Appuyez sur Entrée pour revenir au menu...")


        # --------------------------------------------- CHOIX 2 ---------------------------------------------
        elif choix == "2":
            clear_console()
            print("Faire une réservation")
            nom_client = input("Nom du client : ")
            numero_tel = input("Numéro de téléphone : ")
            date = input("Date de réservation : ")
            chambre_numero = input("Numéro de chambre : ")
            reservation = Reservation(date, nom_client, numero_tel)
            fichier_reservation.append(reservation)
            print(f"Réservation effectuée pour {nom_client} le {date}.")
            input("Appuyez sur Entrée pour revenir au menu...")

        # --------------------------------------------- CHOIX 3 ---------------------------------------------
        elif choix == "3":
            clear_console()
            print("Afficher les réservations")
            print("Voici les Réservations :")
            for reservation in fichier_reservation:
                print(f"Réservation pour {reservation.nom_client} le {reservation.date}.")
            input("Appuyez sur Entrée pour revenir au menu...")

        # --------------------------------------------- CHOIX 4 ---------------------------------------------
        elif choix == "4":
            clear_console()
            for client in hotel.clients:
                client.afficher()
            input("Appuyez sur Entrée pour revenir au menu...")

        # --------------------------------------------- CHOIX 5 ---------------------------------------------
        elif choix == "5":
            clear_console()
            print("Afficher les chambres")
            print("Les chambres disponibles sont  :")
            chambres = [Chambre(101, "simple", 50), Chambre(102, "double", 100), Chambre(103, "suite", 150)]
            for chambre in chambres:
                print(f"Chambre {chambre.numero} : Type - {chambre.type}, Prix - {chambre.prix}€")
            input("Appuyez sur Entrée pour revenir au menu...")

        # --------------------------------------------- QUITTER ---------------------------------------------
        elif choix.lower() == "q":
            print("Merci d'avoir utilisé l'application de gestion d'hôtel et si notre appli vous a plu, laissez-nous 5 étoiles :)")
            break

        else:
            print("Choix invalide, veuillez réessayer.")

