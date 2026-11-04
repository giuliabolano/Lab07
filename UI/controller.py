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
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def handler_btn_biblioteche(self, e):

        biblioteche = self._model.get_biblioteche()
        if biblioteche is None:
            self._view.show_alert("devi scegliere una biblioteca!")
            return

        self._view.dd.options.clear()


        for b in biblioteche:
            (self._view.dd.options.append(ft.dropdown.Option(key=str(b.id), text= str(b.nome))))
        self._view.update()




    def handler_genere(self,e):
        generi= self._model.get_generi()
        if generi is None:
            self._view.show_alert("scegli un genere!")
            return

        self._view.dd_genere.options.clear()
        for g in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(text=str(g)))
        self._view.update()



    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA LIBRI
    # TODO
