from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    #metodo per leggere i generi dalla tabella libro nel database
    def leggere_genere_libri(self):

        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")

            query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL"
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query)
            risultato = []
            for row in cursor:
                #row[0] è la colonna del genere e la aggiungiamo direttamente
                risultato.append(row['genere'])
            cursor.close()
            cnx.close()
            return risultato


#metoto che legge i libri filtrati
    def leggere_libri_filtrati(self, biblioteca, genere):

        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")

            query = """SELECT * FROM libro l
                        WHERE l.id_biblioteca = COALESCE(%s, l.id_biblioteca) AND genere= COALESCE(%s,genere)"""

            cursor = cnx.cursor()
            cursor.execute(query, (biblioteca, genere))
            risultato = []
            for row in cursor:
                libro = Libro(*row)
                risultato.append(libro)
            cursor.close()
            cnx.close()
            return risultato
