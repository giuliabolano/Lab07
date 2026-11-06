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
    # gstione della selezione dell'utente salvandola nelle variabili
    def handler_dd_biblioteca(self, e):
        self.biblioteca_selezionata = self._view.dd.value

    def handler_dd_genere(self, e):
        self.genere_selezionato = self._view.dd_genere.value

    # AZIONE: MOSTRA LIBRI
    # logica che verifica i filtri, interroga il model e aggiorna la schermata
    def handler_mostra_libri(self, e):
        # Controllo se almeno un filtro è stato selezionato (opzionale o richiesto a seconda dei casi)
        if self.biblioteca_selezionata is None and self.genere_selezionato is None:
            self._view.show_alert("Seleziona almeno una biblioteca o un genere!")
            return

        # Chiamata al model per recuperare i libri filtrati
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        # Pulisci la lista visiva precedente
        self._view.list_view.controls.clear()

        if not libri:
            self._view.show_alert("Nessun libro trovato con i criteri selezionati.")
        else:
            for libro in libri:
                self._view.list_view.controls.append(ft.Text(str(libro)))

        self._view.update()

