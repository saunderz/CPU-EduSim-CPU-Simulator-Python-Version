import tkinter as tk
import time #método sleep utilizado
from tkinter import font
import matplotlib.pyplot as plt

class CPUVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulação de CPU")
        self.root.geometry("1920x1080")  # fullHD

        self.registers = {"R1": 0, "R2": 0, "R3": 0, "R4": 0}
        self.memory = [i * 10 for i in range(10)] 
        self.instructions = []
        self.current_instruction_index = 0
        self.clock_count = 0
        self.history = []
        self.execution_times = []
        self.explanation_mode = False  # modo explicativo desativado de início
        self.total_cycles = 0  # contador dos ciclos

        self.create_widgets()
        self.load_instructions()

    def create_widgets(self):
        self.large_font = font.Font(family="Arial", size=14, weight="bold")
        self.medium_font = font.Font(family="Arial", size=12)

        # caminhos de dados
        self.canvas = tk.Canvas(self.root, width=1600, height=800, bg="white")  
        self.canvas.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # unidade de Controle
        self.control_box = self.canvas.create_rectangle(500, 50, 900, 150, fill="lightblue", tags="control")
        self.canvas.create_text(700, 100, text="Unidade de Controle", font=self.large_font, tags="control_text")
        self.control_button = tk.Button(self.root, text="?", font=self.medium_font, command=lambda: self.show_component_info("Unidade de Controle", "Gerencia e coordena todas as operações da CPU."))
        self.control_button.place(x=495, y=45)

        # ALU
        self.alu_box = self.canvas.create_rectangle(500, 200, 900, 300, fill="lightgreen", tags="alu")
        self.canvas.create_text(700, 250, text="ALU", font=self.large_font, tags="alu_text")
        self.alu_button = tk.Button(self.root, text="?", font=self.medium_font, command=lambda: self.show_component_info("ALU", "Executa operações aritméticas e lógicas."))
        self.alu_button.place(x=495, y=195)

        # ciclos totais
        self.cycles_label = tk.Label(self.root, text="Esforço Computacional: 0", font=self.medium_font)
        self.cycles_label.place(x=650, y=420)

        # registradores
        self.register_boxes = {}
        for i, reg in enumerate(self.registers.keys()):
            x1, y1, x2, y2 = 100, 50 + i * 120, 400, 150 + i * 120
            self.register_boxes[reg] = self.canvas.create_rectangle(x1, y1, x2, y2, fill="lightyellow", tags=reg)
            self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=f"{reg}: {self.registers[reg]}", font=self.large_font, tags=f"{reg}_text")
            button = tk.Button(self.root, text="?", font=self.medium_font, command=lambda r=reg: self.show_component_info(r, "Armazena dados temporários para operações."))
            button.place(x=95, y=45 + i * 120)

        # memória
        self.memory_box = self.canvas.create_rectangle(1100, 50, 1350, 600, fill="lightgray", tags="memory")  # Diminuído para caber
        self.canvas.create_text(1225, 25, text="Memória", font=self.large_font, tags="memory_label")
        self.memory_button = tk.Button(self.root, text="?", font=self.medium_font, command=lambda: self.show_component_info("Memória", "Armazena dados e instruções para a CPU."))
        self.memory_button.place(x=1095, y=45)

        self.memory_labels = []
        for i in range(len(self.memory)):
            text_x, text_y = 1225, 70 + i * 50 
            label = self.canvas.create_text(text_x, text_y, text=f"[{i}]: {self.memory[i]}", font=self.large_font, tags=f"memory_{i}")
            self.memory_labels.append(label)

        # botões 
        self.next_button = tk.Button(self.root, text="Próxima Instrução", font=self.medium_font, command=self.next_instruction)
        self.next_button.grid(row=1, column=0, pady=10, padx=10)

        self.reset_button = tk.Button(self.root, text="Resetar", font=self.medium_font, command=self.reset)
        self.reset_button.grid(row=1, column=1, pady=10, padx=10)

        self.explanation_button = tk.Button(self.root, text="Modo Explicação: Desativado", font=self.medium_font, command=self.toggle_explanation)
        self.explanation_button.grid(row=1, column=2, pady=10, padx=10)

        self.history_button = tk.Button(self.root, text="Exibir Histórico", font=self.medium_font, command=self.show_history)
        self.history_button.grid(row=2, column=0, pady=10, padx=10)

        self.edit_memory_button = tk.Button(self.root, text="Editar Memória", font=self.medium_font, command=self.edit_memory)
        self.edit_memory_button.grid(row=2, column=1, pady=10, padx=10)

        self.edit_instructions_button = tk.Button(self.root, text="Editar Instruções", font=self.medium_font, command=self.edit_instructions)
        self.edit_instructions_button.grid(row=2, column=2, pady=10, padx=10)

        self.performance_button = tk.Button(self.root, text="Gráfico de Desempenho", font=self.medium_font, command=self.show_performance)
        self.performance_button.grid(row=3, column=1, pady=10, padx=10)

        # explicações
        self.current_instruction_label = tk.Label(self.root, text="Instrução Atual:", font=self.large_font, wraplength=400, justify="left", bg="lightyellow", anchor="nw", relief="solid", bd=2)
        self.current_instruction_label.place(x=1400, y=50)

        # histórico dinâmico
        self.dynamic_history_labels = []
        self.history_title_label = tk.Label(self.root, text="Histórico de Instruções:", font=self.large_font, wraplength=400, justify="left", bg="lightyellow", anchor="nw", relief="solid", bd=2)
        self.history_title_label.place(x=1400, y=200)
    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Histórico de Instruções")
        history_window.geometry("600x400")

        history_text = tk.Text(history_window, wrap="word", font=self.medium_font)
        history_text.pack(expand=True, fill="both", padx=10, pady=10)

        for entry in self.history:
            history_text.insert("end", entry + "\n")
        history_text.config(state="disabled")

    def show_component_info(self, component_name, info): #criação do pop-up das informações
        info_window = tk.Toplevel(self.root)
        info_window.title(f"Informação: {component_name}")
        tk.Label(info_window, text=info, font=self.medium_font, wraplength=400, justify="left").pack(padx=10, pady=10)

    def toggle_explanation(self): #modo explicativo
        self.explanation_mode = not self.explanation_mode
        state = "Ativado" if self.explanation_mode else "Desativado"
        self.explanation_button.config(text=f"Modo Explicação: {state}")

    def update_registers(self):
        for reg, value in self.registers.items():
            self.canvas.itemconfig(f"{reg}_text", text=f"{reg}: {value}")

    def update_memory(self):
        for i, value in enumerate(self.memory):
            self.canvas.itemconfig(f"memory_{i}", text=f"[{i}]: {value}")

    def load_instructions(self):
        self.instructions = [
            ("LOAD", "R1", 5),
            ("LOAD", "R2", 9),
            ("ADD", "R3", "R1", "R2"),
            ("STORE", "R3", 2),
            ("LOAD", "R4", 4),
            ("SUB", "R1", "R4", "R2"),
            ("STORE", "R1", 3)
        ]
        self.current_instruction_index = 0

    def reset(self):
        self.registers = {reg: 0 for reg in self.registers}
        self.memory = [i * 10 for i in range(len(self.memory))]
        self.load_instructions()
        self.update_registers()
        self.update_memory()
        self.clock_count = 0
        self.total_cycles = 0
        self.history.clear()
        self.execution_times.clear()
        self.canvas.delete("data_path")
        self.current_instruction_label.config(text="Instrução Atual:")
        self.cycles_label.config(text="Esforço Computacional: 0")

        for label in self.dynamic_history_labels:
            label.destroy()
        self.dynamic_history_labels.clear()

    def next_instruction(self):
        if self.current_instruction_index < len(self.instructions):
            instruction = self.instructions[self.current_instruction_index]
            start_time = self.clock_count
            self.execute_instruction(instruction)
            end_time = self.clock_count
            self.execution_times.append(end_time - start_time)
            self.current_instruction_index += 1
        else:
            self.canvas.itemconfig("control_text", text="Fim das Instruções")

    def execute_instruction(self, instruction):
        operation_text = ""
        explanation_text = ""

        if instruction[0] == "LOAD":
            _, reg, value = instruction # _ignora a operação, reg é o qual registrador e value o indice do valor na memória
            value = int(value)
            if 0 <= value < len(self.memory):
                self.registers[reg] = self.memory[value]
                self.update_registers()
                operation_text = f"Memória[{value}] -> {reg}"
                explanation_text = f"LOAD: Carrega o valor {self.memory[value]} da posição {value} da memória no registrador {reg}."
                self.draw_data_path("memory", reg, memory_index=value)
                self.total_cycles += 5  # esforço para LOAD
            else:
                explanation_text = f"Erro: Índice {value} fora dos limites da memória."

        elif instruction[0] == "STORE":
            _, reg, address = instruction  # _ignora a operação, reg é o qual registrador e address o indice do valor na memória
            address = int(address)
            if 0 <= address < len(self.memory):
                self.memory[address] = self.registers[reg]
                self.update_memory()
                operation_text = f"{reg} -> Memória[{address}]"
                explanation_text = f"STORE: Armazena o valor de {reg} no endereço {address} da memória."
                self.draw_data_path(reg, "memory", memory_index=address)
                self.total_cycles += 5  # esforço para STORE
            else:
                explanation_text = f"Erro: Índice {address} fora dos limites da memória."

        elif instruction[0] == "ADD":
            _, dest, src1, src2 = instruction # _ignora a operação, dest é o destino, src1 de onde vem o primeiro dado e src2 de onde vem o segundo dado
            self.registers[dest] = self.registers[src1] + self.registers[src2]
            self.update_registers()
            operation_text = f"{src1} + {src2} -> {dest}"
            explanation_text = f"ADD: Soma os valores de {src1} ({self.registers[src1]}) e {src2} ({self.registers[src2]}), armazenando o resultado em {dest}."
            self.draw_data_path(src1, "alu")
            self.draw_data_path(src2, "alu")
            self.draw_data_path("alu", dest)
            self.total_cycles += 3  # esforço para ADD

        elif instruction[0] == "SUB":
            _, dest, src1, src2 = instruction # _ignora a operação, dest é o destino, src1 de onde vem o primeiro dado e src2 de onde vem o segundo dado
            self.registers[dest] = self.registers[src1] - self.registers[src2]
            self.update_registers()
            operation_text = f"{src1} - {src2} -> {dest}"
            explanation_text = f"SUB: Subtrai o valor de {src2} ({self.registers[src2]}) de {src1} ({self.registers[src1]}), armazenando o resultado em {dest}."
            self.draw_data_path(src1, "alu")
            self.draw_data_path(src2, "alu")
            self.draw_data_path("alu", dest)
            self.total_cycles += 3  # esforço para SUB

        self.canvas.itemconfig("control_text", text=operation_text)

        if self.explanation_mode:
            self.current_instruction_label.config(text=f"Instrução Atual:\n{explanation_text}")
            self.add_to_dynamic_history(explanation_text)

        self.history.append(f"Instrução: {instruction}, Estado: {self.registers}")
        self.clock_count += 1

        # atualização do contador de ciclos
        self.cycles_label.config(text=f"Esforço Computacional: {self.total_cycles}")

    def add_to_dynamic_history(self, explanation_text):
        new_label = tk.Label(self.root, text=explanation_text, font=self.medium_font, wraplength=400, justify="left", bg="lightyellow", anchor="nw", relief="solid", bd=2)
        new_label.place(x=1400, y=250 + len(self.dynamic_history_labels) * 50)
        self.dynamic_history_labels.append(new_label)

    def draw_data_path(self, source, destination, memory_index=None): #desenha o caminho dos dados, seta vermelha
        self.canvas.delete("data_path")

        if source in self.register_boxes:
            x1, y1, x2, y2 = self.canvas.coords(self.register_boxes[source])
        elif source == "memory":
            if memory_index is not None:
                x1, y1 = 1225, 70 + memory_index * 50
                x2, y2 = x1, y1
            else:
                x1, y1, x2, y2 = self.canvas.coords(self.memory_box)
        elif source == "alu":
            x1, y1, x2, y2 = self.canvas.coords(self.alu_box)
        else:
            return

        if destination in self.register_boxes:
            x3, y3, x4, y4 = self.canvas.coords(self.register_boxes[destination])
        elif destination == "memory":
            if memory_index is not None:
                x3, y3 = 1225, 70 + memory_index * 50
                x4, y4 = x3, y3
            else:
                x3, y3, x4, y4 = self.canvas.coords(self.memory_box)
        elif destination == "alu":
            x3, y3, x4, y4 = self.canvas.coords(self.alu_box)
        else:
            return

        self.canvas.create_line((x1 + x2) // 2, (y1 + y2) // 2,
                                (x3 + x4) // 2, (y3 + y4) // 2,
                                arrow=tk.LAST, fill="red", width=4, tags="data_path")
        self.root.update()
        time.sleep(1)

    def edit_memory(self):
        memory_window = tk.Toplevel(self.root)
        memory_window.title("Editar Memória")
        memory_window.geometry("400x600")

        entries = []

        def save_memory():
            for i, entry in enumerate(entries):
                try:
                    self.memory[i] = int(entry.get())
                except ValueError:
                    pass
            self.update_memory()
            memory_window.destroy()

        for i in range(len(self.memory)):
            tk.Label(memory_window, text=f"Endereço {i}:").grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(memory_window)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entry.insert(0, str(self.memory[i]))
            entries.append(entry)

        save_button = tk.Button(memory_window, text="Salvar", command=save_memory)
        save_button.grid(row=len(self.memory), column=0, columnspan=2, pady=10)

    def edit_instructions(self):
        instructions_window = tk.Toplevel(self.root)
        instructions_window.title("Editar Instruções")
        instructions_window.geometry("600x600")

        entries = []

        def save_instructions():
            new_instructions = []
            for entry in entries:
                try:
                    line = entry.get().strip()
                    if line:
                        parts = line.split()
                        processed_parts = [int(p) if p.isdigit() else p for p in parts]
                        new_instructions.append(tuple(processed_parts))
                except Exception:
                    pass
            if new_instructions:
                self.instructions = new_instructions
                self.current_instruction_index = 0
            instructions_window.destroy()

        for i, instruction in enumerate(self.instructions):
            tk.Label(instructions_window, text=f"Instrução {i}:").grid(row=i, column=0, padx=5, pady=5)
            entry = tk.Entry(instructions_window, width=50)
            entry.grid(row=i, column=1, padx=5, pady=5)
            entry.insert(0, " ".join(map(str, instruction)))
            entries.append(entry)

        save_button = tk.Button(instructions_window, text="Salvar", command=save_instructions)
        save_button.grid(row=len(self.instructions), column=0, columnspan=2, pady=10)

    def show_performance(self): #plot do gráfico de perfomance
        if not self.execution_times:
            return

        plt.figure(figsize=(10, 6))
        plt.bar(range(1, len(self.execution_times) + 1), self.execution_times, color="blue")
        plt.xlabel("Instruções", fontsize=14)
        plt.ylabel("Ciclos de Clock", fontsize=14)
        plt.title("Desempenho por Instrução", fontsize=16)
        plt.xticks(range(1, len(self.execution_times) + 1))
        plt.grid(axis="y", linestyle="--", alpha=0.7)
        plt.show()

if __name__ == "__main__": #execução direta, não há inport de outro módulo externo, logo usa-se main
    root = tk.Tk() #cria janela principal
    app = CPUVisualizer(root) #chama a instância da classe, contendo toda a lógica dos metodos
    root.mainloop() #inicia o loop principal, sem o loop a janela aparece e fecha

