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

            query = "SELECT genere FROM libro WHERE genere = COALESCE(%s, genere)"
            cursor = cnx.cursor()
            cursor.execute(query)
            risultato = []
            for row in cursor:
                libro = Libro(*row)
                risultato.append(libro)
            cursor.close()
            cnx.close()
            return risultato


#metoto che legge i libri filtrati
    def leggere_libri_filtrati(self, biblioteca, genere):

        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")

            query = f"""SELECT * FROM libro l
                        WHERE l.id_biblioteca = b.id AND genere= coalesce(%s,genere)"""

            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query, genere)
            risultato = []
            for row in cursor:
                libro = Libro(*row)
                risultato.append(libro)
            cursor.close()
            cnx.close()
            return risultato