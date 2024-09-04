import customtkinter
from telas import exibir_tela_login

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def exibir_tela_principal(janela):
    for widget in janela.winfo_children():
        widget.destroy()
    from telas import exibir_tela_principal
    exibir_tela_principal(janela)

# mostra os coisa lá
janela = customtkinter.CTk()
janela.title("Login")
janela.geometry("500x300")

# puxa
exibir_tela_login(janela, exibir_tela_principal)


janela.mainloop()
