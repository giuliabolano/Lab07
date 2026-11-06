from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    #metoto per leggere dal database tutte i nomi delle biblioteche presenti
    def leggere_nomi_biblioteche(self):
        cnx= DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")

            query= "SELECT id, nome, indirizzo FROM biblioteca"
            cursor= cnx.cursor()
            cursor.execute(query)
            nomi_b= []
            for row in cursor:
                biblioteca= Biblioteca(*row)
                nomi_b.append(biblioteca)
            cursor.close()
            cnx.close()
            return nomi_b
