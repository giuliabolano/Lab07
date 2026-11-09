from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # Leggo i generi dei libri dal db

    def leggere_genere(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")

            query = "SELECT DISTINCT genere FROM libro"
            cursor = cnx.cursor()
            cursor.execute(query)
            result = []
            for row in cursor:
                result.append(row[0]) # estraggo una sola colonna
            cursor.close()
            cnx.close()

        return result

    # leggo i libri filtrati dal DB

    def leggere_libri_filtrati(self, biblioteca, genere):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection established")

            query = """SELECT l.titolo
                   FROM libro l, biblioteca b
                   WHERE l.id_biblioteca = b.id
                     AND b.nome = COALESCE(%s, b.nome)
                     AND l.genere = COALESCE(%s, l.genere)"""
            cursor = cnx.cursor()
            cursor.execute(query, (biblioteca, genere))
            result = []
            for row in cursor:
                result.append(row[0])
            cursor.close()
            cnx.close()

            return result