import tkinter as tk
from tkinter import messagebox  # Import necessário para exibir alertas na tela
import webbrowser
import random

# Link do vídeo para a trollagem
URL_VIDEO = "https://www.tiktok.com/@aquinx_0/video/7616412540586806548?is_from_webapp=1&sender_device=pc" 

def abrir_video():
    """Abre o link do vídeo no navegador padrão."""
    webbrowser.open(URL_VIDEO)
    raiz.destroy()

def mostrar_mensagem():
    """Mostra uma mensagem engraçada quando o usuário clica no botão 'Não'."""
    # Lista de frases para o sorteio funcionar corretamente
    mensagens = [
        "vc definitivamente é a belbag, pare de ser mentirosa",
        "Não adianta mentir, o sistema já sabe a verdade!",
        "Abaixe esse dedo e clique em Sim."
    ]
    # Sorteia uma frase da lista e exibe em uma janela de aviso
    messagebox.showwarning("Aviso", random.choice(mensagens))

# Configuração da janela principal
raiz = tk.Tk()
raiz.title("Pergunta Séria")
raiz.geometry("400x250")
raiz.eval('tk::PlaceWindow . center') # Centraliza a janela na tela

# Texto da pergunta
pergunta = tk.Label(raiz, text="Você é a Belbag?", font=("Arial", 16, "bold"))
pergunta.pack(pady=30)

# Botão "Sim" (Abre o vídeo direto)
botao_sim = tk.Button(raiz, text="Sim", font=("Arial", 12), width=10, command=abrir_video)
botao_sim.place(x=80, y=100)

# Botão "Não" (Aparece a mensagem de aviso)
botao_nao = tk.Button(raiz, text="Não", font=("Arial", 12), width=10, command=mostrar_mensagem)
botao_nao.place(x=220, y=100)

# Executa o programa
raiz.mainloop()
