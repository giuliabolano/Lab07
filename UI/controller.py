import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):

        self.model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN -> scrivo le funzioni che riempiono le dropdown
    def handler_btn_biblioteche(self,e):

        biblioteche = self.model.get_biblioteche() # dal model prendo le biblioteche

        if biblioteche is None:
            self._view.show_alert("scegliere biblioteca") # scateno un alert se non ho scelto nessuna biblioteca
            return

        self._view.dd.options.clear() # cancello sempre in contenuto della dropdown
        self._view.dd.options.append(ft.dropdown.Option("Nessun filtro"))


        for b in biblioteche:
            self._view.dd.options.append(ft.dropdown.Option(b.nome)) # scandisco le biblioteche e le appendo alla dropdown
        self._view.update()

    def handler_btn_genere(self,e):
        generi = self.model.get_generi()
        if generi is None:
            self._view.show_alert("scegliere generi")
            return

        self._view.dd_g.options.clear()
        self._view.dd_g.options.append(ft.dropdown.Option("Nessun filtro"))

        for g in generi:
            self._view.dd_g.options.append(ft.dropdown.Option(g))

        self._view.update()

    # CALLBACKS DROPDOWN -> scrivo le funzioni che memorizzano le selezioni dell'utente
    def handler_dd_biblioteca(self,e):
        valore = e.control.value
        if valore == "Nessun filtro":
            self.biblioteca_selezionata= None

        else:
            self.biblioteca_selezionata= valore

    def handler_dd_genere(self, e):
        valore = e.control.value # vado a prendere il valore dalla drop down
        if valore == "Nessun filtro":
            self.genere_selezionato = None

        else:
            self.genere_selezionato = valore



    # AZIONE: MOSTRA LIBRI -> ciò che accade quando premo il pulsante mostra libri
    def handler_mostra_libri(self,e):
        libri = self.model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        self._view.list_view.controls.clear()

        if not libri:
            self._view.show_alert("Nessun libro presente")
            self._view.update()
            return

        for titolo in libri:
            self._view.list_view.controls.append(ft.Text(titolo))
        self._view.update()
