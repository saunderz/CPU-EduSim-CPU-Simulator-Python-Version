# 🖥️ CPU EduSim – Simulador de CPU - Versão Python

![Language](https://img.shields.io/badge/Language-Python-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Ativo-success)

## 📚 Descrição

**CPU EduSim** é um simulador didático de CPU escrito em **Python puro**, que permite:

- Visualização gráfica do fluxo de dados
- Simulação de registradores, ALU, memória principal e cache
- Execução passo a passo de instruções (LOAD, STORE, ADD, SUB)
- Análise de desempenho via ciclos de clock (esforço computacional)

Ideal para estudantes de **Arquitetura de Computadores**, **Sistemas Embarcados** e disciplinas de **Organização de Computadores**.

---

## 🎯 Funcionalidades

✅ Visualização em tempo real de registradores, cache e memória  
✅ Execução passo a passo de instruções  
✅ Contagem de ciclos de clock (esforço computacional)  
✅ Visualização de HIT/MISS na cache (mapeamento direto)  
✅ Modo explicativo com histórico detalhado  
✅ Gráfico de desempenho com Matplotlib  
✅ Reset completo do sistema  
✅ **Sem necessidade de compilação C** – versão Python puro

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.9+**
  - Tkinter (interface gráfica)
  - Matplotlib (gráficos)

---

## 🗃️ Estrutura do Projeto
```
📁 CPU-EduSim-CPU-Simulator/
┣ 📄 main.py
┣ 📄 README.md
```
---

## 🚀 Como Executar

### 🔧 Pré-requisitos

- **Git**
- **Python 3.9 ou superior**

### 🖥️ Passos para Execução

1. **Clone o repositório:**
```bash
   git clone https://github.com/saunderz/CPU-EduSim-CPU-Simulator-Python-Version.git
   cd CPU-EduSim-CPU-Simulator
```
2. Instale as dependências Python:
```bash
pip install matplotlib
```
3. Execute o simulador:
```
python cpu_frontend.py
```
# 💡 Conceitos Demonstrados

🔹 Mapeamento direto de cache

🔹 Políticas de escrita (Write-Through + Write-Allocate)

🔹 Ciclos de clock e esforço computacional

🔹 Fluxo de dados entre memória, cache e registradores

# ✨ Agradecimentos

Este projeto foi desenvolvido para fins didáticos, como ferramenta prática de apoio ao estudo de Arquitetura de Computadores e Sistemas Embarcados.
