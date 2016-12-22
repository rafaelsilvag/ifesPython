#!/usr/bin/env python3
#
# Rafael S. Guimaraes <rafaelg@ifes.edu.br>
#
import random
import tkinter as tk
import sys


class FrmPrincipal(object):
    """
    Janela Principal - Sorteio
    """
    def __init__(self, instance_tk):
        self.window = instance_tk
        self.window.title = "Sorteio de Grupos"
        self.frame = tk.Frame(instance_tk)
        self.frame.pack()
        self.bt_sortear = tk.Button(self.frame)
        self.bt_sortear['text'] = u"Sortear"
        self.bt_sortear['background'] = "blue"
        self.bt_sortear.bind("<Button-1>", self.realizar_sorteio)
        self.bt_sortear.bind("<Return>", self.realizar_sorteio)
        self.bt_sair = tk.Button(self.frame)
        self.bt_sair['text'] = u"Sair"
        self.bt_sair.bind("<Button-1>", self.sair)
        self.bt_limpar = tk.Button(self.frame)
        self.bt_limpar['text'] = u"Limpar"
        self.bt_limpar.bind("<Button-1>", self.limpar)
        self.lb_titulo = tk.Label(self.frame)
        self.lb_titulo['text'] = u"Sorteio de Grupos".upper()
        self.lb_titulo['font'] = ('Verdana', '13', 'bold')
        self.lb_titulo.grid(row=1, column=1, sticky=tk.N, columnspan=3)
        self.lb_grupos = tk.Label(self.frame)
        self.lb_grupos['text'] = u"Grupos"
        self.lb_grupos.grid(row=2, column=1, sticky=tk.N)
        self.lb_temas = tk.Label(self.frame)
        self.lb_temas['text'] = u"Temas"
        self.lb_temas.grid(row=2, column=2, sticky=tk.N)
        self.lb_resultado = tk.Label(self.frame)
        self.lb_resultado['text'] = u"Resultado"
        self.lb_resultado.grid(row=2, column=3, sticky=tk.N)
        self.sbar_grupos = tk.Scrollbar(
            self.frame,
            orient=tk.VERTICAL
        )
        self.sbar_trabalhos = tk.Scrollbar(
            self.frame,
            orient=tk.VERTICAL
        )
        self.sbar_resultados = tk.Scrollbar(
            self.frame,
            orient=tk.VERTICAL
        )
        self.lbox_grupos = tk.Listbox(
            self.frame,
            yscrollcommand=self.sbar_grupos.set
        )
        self.lbox_grupos.grid(row=3, column=1, sticky=tk.N)
        self.lbox_trabalhos = tk.Listbox(
            self.frame,
            yscrollcommand=self.sbar_trabalhos.set
        )
        self.lbox_trabalhos.grid(row=3, column=2, sticky=tk.N)
        self.lbox_resultado = tk.Listbox(
            self.frame,
            yscrollcommand=self.sbar_trabalhos.set
        )
        self.lbox_resultado.grid(row=3, column=3, sticky=tk.N)

        self.e_text = tk.Entry(self.frame)
        self.e_text.grid(row=4, column=2, padx=5, sticky=tk.N)

        self.lb_status = tk.Label(self.frame)
        self.lb_status['text'] = u"".upper()
        self.lb_status.grid(row=4, column=3)

        self.bt_cad_grupos = tk.Button(self.frame)
        self.bt_cad_grupos['text'] = u"Cadastrar Grupo"
        self.bt_cad_grupos['background'] = "yellow"
        self.bt_cad_grupos.bind("<Button-1>", self.cadastrar_grupo)
        self.bt_cad_grupos.grid(row=5, column=1)

        self.bt_cad_temas = tk.Button(self.frame)
        self.bt_cad_temas['text'] = u"Cadastrar Tema"
        self.bt_cad_temas['background'] = "yellow"
        self.bt_cad_temas.bind("<Button-1>", self.cadastrar_tema)
        self.bt_cad_temas.grid(row=5, column=2)

        self.bt_sortear.grid(row=5, column=3)
        self.bt_limpar.grid(row=6, column=2, sticky=tk.N)
        self.bt_sair.grid(row=6, column=3, sticky=tk.N)

        self.sorteio_realizado = False

    def realizar_sorteio(self, event):
        if(not self.sorteio_realizado):
            trabalhos = list(self.lbox_trabalhos.get(0, tk.END))
            grupos = list(self.lbox_grupos.get(0, tk.END))
            grupos.sort()

            for i in grupos:
                aux = random.choice(trabalhos)
                trabalhos.remove(aux)
                res = "{:<10}->{:>10}".format(i, aux)
                self.lbox_resultado.insert(tk.END, res)

            self.sorteio_realizado = True
        else:
            self.lb_status['text'] = "Sorteio Realizado!".upper()

    def cadastrar_grupo(self, event):
        # grupo = msgbox.askinteger("Hello World", "Teste")
        aux = self.e_text.get()
        if aux != "":
            self.lbox_grupos.insert(tk.END, self.e_text.get())
            self.e_text.delete(0, tk.END)

    def cadastrar_tema(self, event):
        aux = self.e_text.get()
        if aux != "":
            self.lbox_trabalhos.insert(tk.END, self.e_text.get())
            self.e_text.delete(0, tk.END)

    def limpar(self, event):
        self.lbox_grupos.delete(0, tk.END)
        self.lbox_resultado.delete(0, tk.END)
        self.lbox_trabalhos.delete(0, tk.END)
        self.sorteio_realizado = False
        self.lb_status['text'] = ""

    def sair(self, event):
        sys.exit(0)


def main():
    grupos = {}
    sorteios = []
    frame = FrmPrincipal(instance_tk=tk.Tk())
    frame.window.mainloop()

if __name__ == '__main__':
    main()
