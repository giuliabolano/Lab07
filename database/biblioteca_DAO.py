from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # leggo dal database tutte le biblioteche

    def leggere_biblioteche(self):
        cnx = DBConnect.get_connection() # mi connetto e controllo di aver stabilito la connnessione
        result = []
        if cnx is not None:
            print("Connessione stabilita")

            query = "SELECT id, nome, indirizzo FROM biblioteca"
            cursor = cnx.cursor()
            cursor.execute(query)
            for row in cursor:
                result.append(Biblioteca(*row)) # perche estraggo tutte le colonne
            cursor.close()
            cnx.close()

            return result
