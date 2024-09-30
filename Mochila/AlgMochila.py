import random
import tkinter as tk
from tkinter import ttk, messagebox
import threading

class AlgoritmoGenetico:
    def __init__(self, itens, peso_maximo, tamanho_populacao, geracoes, taxa_mutacao):
        self.itens = itens
        self.peso_maximo = peso_maximo
        self.tamanho_populacao = tamanho_populacao
        self.geracoes = geracoes
        self.taxa_mutacao = taxa_mutacao

    def criar_individuo(self):
        return [random.randint(0, 1) for _ in range(len(self.itens))]

    def fitness(self, individuo):
        peso_total = sum(item[0] * gene for item, gene in zip(self.itens, individuo))
        if peso_total > self.peso_maximo:
            return 0
        return sum(item[1] * gene for item, gene in zip(self.itens, individuo))

    def selecao(self, populacao):
        return random.choices(
            populacao,
            weights=[self.fitness(ind) for ind in populacao],
            k=2
        )

    def cruzamento(self, pai1, pai2):
        ponto = random.randint(1, len(pai1) - 1)
        filho = pai1[:ponto] + pai2[ponto:]
        return filho

    def mutacao(self, individuo):
        for i in range(len(individuo)):
            if random.random() < self.taxa_mutacao:
                individuo[i] = 1 - individuo[i]
        return individuo

    def executar(self, progress_callback=None):
        populacao = [self.criar_individuo() for _ in range(self.tamanho_populacao)]
        melhores_individuos = []
        
        for geracao in range(self.geracoes):
            nova_populacao = []
            for _ in range(self.tamanho_populacao // 2):
                pai1, pai2 = self.selecao(populacao)
                filho1 = self.mutacao(self.cruzamento(pai1, pai2))
                filho2 = self.mutacao(self.cruzamento(pai2, pai1))
                nova_populacao.extend([filho1, filho2])
            populacao = nova_populacao
            
            melhor_individuo_geracao = max(populacao, key=self.fitness)
            melhores_individuos.append((melhor_individuo_geracao, self.fitness(melhor_individuo_geracao)))
            if progress_callback:
                progress_callback((geracao + 1) / self.geracoes * 100)
        
        melhor_individuo = max(populacao, key=self.fitness)
        return melhor_individuo, self.fitness(melhor_individuo), melhores_individuos  

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Problema da Mochila - Algoritmo Genético")
        self.geometry("700x600")
        self.configure(bg='#f0f0f0')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self, padding="20 20 20 20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        item_frame = ttk.LabelFrame(main_frame, text="Adicionar Itens", padding="10 10 10 10")
        item_frame.pack(fill=tk.X, pady=(0, 10))

        param_frame = ttk.LabelFrame(main_frame, text="Parâmetros do Algoritmo", padding="10 10 10 10")
        param_frame.pack(fill=tk.X, pady=(0, 10))

        result_frame = ttk.LabelFrame(main_frame, text="Resultados", padding="10 10 10 10")
        result_frame.pack(fill=tk.BOTH, expand=True)

        # Widgets para adicionar itens
        ttk.Label(item_frame, text="Peso:").grid(row=0, column=0, padx=5, pady=5)
        self.peso_entry = ttk.Entry(item_frame, width=10)
        self.peso_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(item_frame, text="Valor:").grid(row=0, column=2, padx=5, pady=5)
        self.valor_entry = ttk.Entry(item_frame, width=10)
        self.valor_entry.grid(row=0, column=3, padx=5, pady=5)

        ttk.Button(item_frame, text="Adicionar Item", command=self.adicionar_item).grid(row=0, column=4, padx=5, pady=5)
        ttk.Button(item_frame, text="Remover Item Selecionado", command=self.remover_item).grid(row=0, column=5, padx=5, pady=5)

        # Lista de itens
        self.item_listbox = tk.Listbox(item_frame, width=50, height=5)
        self.item_listbox.grid(row=1, column=0, columnspan=6, pady=5, sticky="nsew")
        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.grid_rowconfigure(1, weight=1)

        # Scrollbar para a lista de itens
        scrollbar = ttk.Scrollbar(item_frame, orient="vertical", command=self.item_listbox.yview)
        scrollbar.grid(row=1, column=6, sticky="ns")
        self.item_listbox.configure(yscrollcommand=scrollbar.set)

        # Parâmetros do algoritmo
        params = [
            ("Peso Máximo:", "peso_maximo_entry"),
            ("Tamanho da População:", "pop_entry"),
            ("Número de Gerações:", "gen_entry"),
            ("Taxa de Mutação:", "mut_entry")
        ]

        for i, (label, attr) in enumerate(params):
            ttk.Label(param_frame, text=label).grid(row=i, column=0, sticky="e", padx=5, pady=5)
            setattr(self, attr, ttk.Entry(param_frame, width=15))
            getattr(self, attr).grid(row=i, column=1, sticky="w", padx=5, pady=5)

        ttk.Button(param_frame, text="Executar Algoritmo", command=self.executar_algoritmo).grid(row=len(params), column=0, columnspan=2, pady=10)

        # Barra de progresso
        self.progress = ttk.Progressbar(param_frame, orient="horizontal", length=200, mode="determinate")
        self.progress.grid(row=len(params)+1, column=0, columnspan=2, pady=5)

        # Área de resultado
        self.result_text = tk.Text(result_frame, wrap=tk.WORD, width=70, height=10)
        self.result_text.pack(fill=tk.BOTH, expand=True)

    def adicionar_item(self):
        try:
            peso = float(self.peso_entry.get())
            valor = float(self.valor_entry.get())
            self.item_listbox.insert(tk.END, f"Peso: {peso:.2f}, Valor: {valor:.2f}")
            self.peso_entry.delete(0, tk.END)
            self.valor_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para peso e valor.")

    def remover_item(self):
        try:
            index = self.item_listbox.curselection()[0]
            self.item_listbox.delete(index)
        except IndexError:
            messagebox.showerror("Erro", "Por favor, selecione um item para remover.")

    def executar_algoritmo(self):
        try:
            itens = []
            for item in self.item_listbox.get(0, tk.END):
                peso, valor = item.split(", ")
                peso = float(peso.split(": ")[1])
                valor = float(valor.split(": ")[1])
                itens.append((peso, valor))

            peso_maximo = float(self.peso_maximo_entry.get())
            tamanho_populacao = int(self.pop_entry.get())
            geracoes = int(self.gen_entry.get())
            taxa_mutacao = float(self.mut_entry.get())

            if not itens:
                raise ValueError("A lista de itens está vazia.")

            self.progress['value'] = 0
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Executando algoritmo...\n")
            
            ag = AlgoritmoGenetico(itens, peso_maximo, tamanho_populacao, geracoes, taxa_mutacao)
            
            def run_algorithm():
                melhor_solucao, melhor_valor, melhores_individuos = ag.executar(progress_callback=self.update_progress)
                self.mostrar_resultados(melhor_solucao, melhor_valor, itens, melhores_individuos)


            thread = threading.Thread(target=run_algorithm)
            thread.start()

        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def update_progress(self, value):
        self.progress['value'] = value
        self.update_idletasks()

    def mostrar_resultados(self, melhor_solucao, melhor_valor, itens, melhores_individuos):
        resultado = f"Melhor solução encontrada: {melhor_solucao}\n"
        resultado += f"Valor total: {melhor_valor:.2f}\n"
        resultado += "Itens selecionados na melhor solução:\n"
        peso_total = 0
        for i, gene in enumerate(melhor_solucao):
            if gene == 1:
                peso, valor = itens[i]
                resultado += f"Item {i+1}: Peso = {peso:.2f}, Valor = {valor:.2f}\n"
                peso_total += peso
        resultado += f"Peso total: {peso_total:.2f}\n\n"

    # Adicionar lista dos melhores indivíduos de cada geração
        resultado += "Melhores indivíduos por geração:\n"
        for idx, (individuo, valor) in enumerate(melhores_individuos):
            resultado += f"Geração {idx+1}: Indivíduo = {individuo}, Valor = {valor:.2f} - Peso = {peso:.2f}\n"

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, resultado)


if __name__ == "__main__":
    app = Application()
    app.mainloop()