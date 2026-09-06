
import tkinter as tk
from chat import meu_chat


class Aplicativo:

    def __init__(self):

        # ==========================================
        # JANELA
        # ==========================================

        self.janela = tk.Tk()

        self.janela.title("Meu Chat")
        self.janela.geometry("600x500")

        self.janela.configure(
            bg="#212121"
        )


        # ==========================================
        # TÍTULO
        # ==========================================

        self.titulo = tk.Label(
            self.janela,
            text="🤖 Meu ChatGPT",
            font=("Arial", 18, "bold"),
            bg="#212121",
            fg="white"
        )

        self.titulo.pack(
            pady=15
        )


        # ==========================================
        # FRAME DA CONVERSA
        # ==========================================

        self.frame_conversa = tk.Frame(
            self.janela,
            bg="#212121"
        )

        self.frame_conversa.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )


        # ==========================================
        # ÁREA DA CONVERSA
        # ==========================================

        self.conversa = tk.Text(
            self.frame_conversa,
            bg="#2f2f2f",
            fg="white",
            insertbackground="white",
            font=("Arial", 11),
            relief="flat",
            wrap="word"
        )

        self.conversa.pack(
            fill="both",
            expand=True
        )


        # ==========================================
        # CAMPO DE DIGITAÇÃO
        # ==========================================

        self.entrada = tk.Entry(
            self.janela,
            bg="#404040",
            fg="white",
            insertbackground="white",
            font=("Arial", 11),
            relief="flat"
        )

        self.entrada.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(15, 5),
            pady=10
        )


        # ==========================================
        # BOTÃO
        # ==========================================

        self.botao = tk.Button(
            self.janela,
            text="Enviar",
            command=self.enviar
        )

        self.botao.pack(
            side="left",
            padx=5,
            pady=15
        )


        # ==========================================
        # ENTER
        # ==========================================

        self.entrada.bind(
            "<Return>",
            self.enviar
        )

        self.entrada.focus()

    def enviar(self, event=None): #Enviar

        pergunta = self.entrada.get()

        print("Pergunta recebida:", pergunta)

        if pergunta.strip() == "":
            return

        # Pergunta ao Chat
        resposta = meu_chat.perguntar(
            pergunta
        )

        print("Resposta:", resposta)

        # Mostra pergunta
        self.conversa.insert(
            tk.END,
            f"👤 Você: {pergunta}\n"
        )

        # Mostra resposta
        self.conversa.insert(
            tk.END,
            f"🤖 ChatGPT: {resposta}\n\n"
        )

        # Limpa entrada
        self.entrada.delete(
            0,
            tk.END
        )

        # Vai para última mensagem
        self.conversa.see(
            tk.END
        )

    def executar(self):# Executar
        self.janela.mainloop()
