from database import libro_DAO
from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        dao= LibroDAO()
        return dao.leggere_libri_filtrati(biblioteca, genere)

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        #preso i metodi creati nelle cartelle DAO e messi nel model così da poterli usare nel controller ecc
        dao= LibroDAO()
        return dao.leggere_genere_libri()

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        dao = BibliotecaDAO()
        return dao.leggere_nomi_biblioteche()
