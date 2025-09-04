from app_controller import executar_login
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class AutomacaoUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Central de Automações – Interface")
        self.geometry("980x620")
        self.minsize(900, 560)

        # ===== Layout base =====
        self.columnconfigure(0, weight=0)  # sidebar
        self.columnconfigure(1, weight=1)  # conteúdo
        self.rowconfigure(0, weight=1)

        self._build_sidebar()
        self._build_content()

    # ---------------- Sidebar -----------------
    def _build_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsw")
        self.sidebar.grid_rowconfigure(99, weight=1)

        ctk.CTkLabel(self.sidebar, text="Lojas", font=("Inter", 18, "bold")).grid(
            row=0, column=0, padx=16, pady=(16, 8), sticky="w"
        )

        # Seletor de loja (1, 2, 3)
        self.loja_var = ctk.IntVar(value=1)
        for idx, nome in enumerate(["Loja 1", "Loja 2", "Loja 3"], start=1):
            rb = ctk.CTkRadioButton(self.sidebar, text=nome, variable=self.loja_var, value=idx)
            rb.grid(row=idx, column=0, padx=16, pady=(0, 8), sticky="w")

        ctk.CTkLabel(self.sidebar, text="Opções", font=("Inter", 14, "bold")).grid(
            row=10, column=0, padx=16, pady=(12, 6), sticky="w"
        )

        self.chk_logs_verbosos = ctk.CTkCheckBox(self.sidebar, text="Logs detalhados")
        self.chk_logs_verbosos.grid(row=11, column=0, padx=16, pady=(0, 6), sticky="w")

        self.chk_continuar_em_erro = ctk.CTkCheckBox(self.sidebar, text="Continuar em caso de erro")
        self.chk_continuar_em_erro.grid(row=12, column=0, padx=16, pady=(0, 6), sticky="w")

        self.btn_sobre = ctk.CTkButton(self.sidebar, text="Sobre", command=self._mostrar_sobre, width=120)
        self.btn_sobre.grid(row=98, column=0, padx=16, pady=(16, 8), sticky="w")

    # ---------------- Conteúdo -----------------
    def _build_content(self):
        content = ctk.CTkFrame(self)
        content.grid(row=0, column=1, sticky="nsew")
        content.rowconfigure(2, weight=1)
        content.columnconfigure(0, weight=1)

        header = ctk.CTkFrame(content)
        header.grid(row=0, column=0, sticky="ew", padx=16, pady=(16, 8))
        header.columnconfigure(1, weight=1)

        ctk.CTkLabel(header, text="Central de Execução (Interface)", font=("Inter", 20, "bold")).grid(
            row=0, column=0, padx=(8, 8), pady=8, sticky="w"
        )

        self.status_label = ctk.CTkLabel(header, text="Pronto", anchor="e")
        self.status_label.grid(row=0, column=1, padx=8, pady=8, sticky="e")

        # Painel de ações (apenas UI)
        actions = ctk.CTkFrame(content)
        actions.grid(row=1, column=0, sticky="ew", padx=16, pady=(0, 8))
        for i in range(6):
            actions.columnconfigure(i, weight=1)

        self.btn_executar = ctk.CTkButton(
            actions,
            text="▶ Executar (Loja selecionada)",
            command=self._on_executar_click,  # TODO: conectar sua função aqui
            height=40,
        )
        self.btn_executar.grid(row=0, column=0, padx=8, pady=8, sticky="ew", columnspan=2)

        self.btn_executar_todas = ctk.CTkButton(
            actions,
            text="⏩ Executar Todas (1→3)",
            command=self._on_executar_todas,  # TODO: conectar sua função aqui
            height=40,
        )
        self.btn_executar_todas.grid(row=0, column=2, padx=8, pady=8, sticky="ew", columnspan=2)

        self.btn_parar = ctk.CTkButton(
            actions,
            text="■ Parar",
            command=self._on_parar_click,  # TODO: conectar sua função aqui (se tiver)
            height=40,
        )
        self.btn_parar.grid(row=0, column=4, padx=8, pady=8, sticky="ew")

        self.progress = ctk.CTkProgressBar(actions, mode="indeterminate")
        self.progress.grid(row=0, column=5, padx=8, pady=8, sticky="ew")

        # Área de logs (apenas visual)
        logs_frame = ctk.CTkFrame(content)
        logs_frame.grid(row=2, column=0, sticky="nsew", padx=16, pady=(0, 16))
        logs_frame.rowconfigure(1, weight=1)
        logs_frame.columnconfigure(0, weight=1)

        ctk.CTkLabel(logs_frame, text="Logs da execução", font=("Inter", 14, "bold")).grid(
            row=0, column=0, padx=8, pady=(8, 0), sticky="w"
        )

        self.txt_logs = ctk.CTkTextbox(logs_frame, wrap="word")
        self.txt_logs.grid(row=1, column=0, sticky="nsew", padx=8, pady=8)

        # Rodapé com dica
        footer = ctk.CTkFrame(content, fg_color="transparent")
        footer.grid(row=3, column=0, sticky="ew", padx=16, pady=(0, 12))
        ctk.CTkLabel(footer, text="Selecione a loja e clique em Executar. Depois conecte sua função.", anchor="w").pack(anchor="w")

    # -------------- Handlers/UI-only (stubs) --------------
    def _on_executar_click(self):
        loja = int(self.loja_var.get())
        self.status_label.configure(text=f"Executar Loja {loja}")
        print(f"[DEBUG] Botão Executar clicado — Loja selecionada: {loja}")
        executar_login(loja)
        print(f"[DEBUG] Finalizou execução da loja {loja}")

    def _on_executar_todas(self):
        self.status_label.configure(text="Executar Todas 1→3")
        print("[DEBUG] Iniciando execução em todas as lojas...")
        for loja in (1, 2, 3):
            print(f"[DEBUG] Chamando executar_login para loja {loja}")
            executar_login(loja)
        print("[DEBUG] Finalizou execução de todas as lojas.")

    def _on_parar_click(self):
        self.status_label.configure(text="Parar")
        print("[DEBUG] Botão Parar clicado — implementar lógica de cancelamento se necessário")
        # Se sua automação tiver mecanismo de parada/cancelamento, chame aqui


    def _mostrar_sobre(self):
        # Apenas texto simples. Você pode substituir por um toplevel personalizado.
        janela = ctk.CTkToplevel(self)
        janela.title("Sobre")
        janela.geometry("420x240")
        janela.resizable(False, False)
        ctk.CTkLabel(
            janela,
            text=(
                "Central de Automações – Interface\n\n"
                "Esta janela é somente UI. Conecte seus scripts nos handlers com TODO.\n"
                "Se quiser, personalize o tema e os textos."
            ),
            justify="left",
        ).pack(padx=16, pady=16, anchor="w")


if __name__ == "__main__":
    app = AutomacaoUI()
    app.mainloop()
