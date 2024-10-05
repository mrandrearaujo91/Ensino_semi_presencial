import customtkinter as ctk
ctk.set_appearance_mode('dark')

janela = ctk.CTk()
janela.geometry('400 x 250')
janela.resizable(False,False)

ctk.CTkLabel(janela,
             text="Sistema de Conversão"#tema que vai aparecer na tela
             text_color="yelloy"#cor da letra
             font=("arial",25,"bold")#tipo da letra, tamanho, borda ou negrito
             ).pack()
valor = ctk.CTkEntry(janela,
                     width=350,
                     height=45
                     )
valor.pack()



janela.mainloop()