# 🖥️ CPU Visualizer

![Language](https://img.shields.io/badge/Language-C%20%26%20Python-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Ativo-success)

## 📚 Descrição

Este projeto é uma **simulação prática de uma CPU** com suporte a:

- Registradores (R1, R2, R3, R4)
- Memória Principal (RAM)
- Memória Cache (mapeamento direto, política Write-Through + Write-Allocate)
- Unidade de Controle (UC)
- ALU (Unidade Lógica e Aritmética)

O programa possui um **backend implementado em C** para maior performance e controle dos dados e um **frontend em Python com Tkinter** para interface gráfica, permitindo visualização do fluxo de dados (com setas), execução de instruções e análise de esforço computacional (ciclos de clock).

---

## 🎯 Funcionalidades

✅ Visualização em tempo real dos registradores, cache e memória principal  

✅ Execução passo a passo de instruções (LOAD, STORE, ADD, SUB)  

✅ Contagem de ciclos de clock (esforço computacional)  

✅ Demonstração de HIT e MISS na cache  

✅ Edição dinâmica dos valores de registradores, memória, cache e instruções  

✅ Modo explicativo com histórico detalhado das operações  

✅ Gráfico de desempenho (Matplotlib)  

✅ Reset completo do sistema  

---

## 🛠️ Tecnologias Utilizadas

- **C (Backend)**
  - Controle de registradores, memória, cache e execução de instruções
- **Python (Frontend)**
  - Interface gráfica com Tkinter
  - Visualização de gráficos com Matplotlib
  - Comunicação com o backend via `ctypes`

---

## 🗃️ Estrutura do Projeto
```
📁 cpu-visualizer/
┣ 📄 cpu_backend.c
┣ 📄 cpu_backend.h
┣ 📄 cpu_backend.dll (gerado ao compilar no Windows)
┣ 📄 cpu_frontend.py
┣ 📄 README.md
```


---

## 🚀 Como Executar

### 🔧 Pré-requisitos

- Compilador C (GCC ou MinGW para Windows)
- Python 3.9 ou superior
- Bibliotecas Python:
```bash
  pip install matplotlib
```
---

# 🖥️ Script de Clone, Compilação e Execução do CPU Visualizer


REPO_URL="https://github.com/seuusuario/cpu-visualizer.git"

# 1. Clonar repositório
```
git clone https://github.com/seuusuario/cpu-visualizer.git
cd cpu-visualizer
```
# 2. Instalar dependências Python
```
pip install matplotlib
```
# 3. Compilar backend
- Windows (MinGW):
```
gcc -shared -o cpu_backend.dll cpu_backend.c
```
- Linux/MacOS:
```
gcc -shared -o libcpu_backend.so -fPIC cpu_backend.c
```

# 4. Executar frontend
```
python cpu_frontend.py
```

# 📝 Exemplo de Uso

- Clique em “Próxima Instrução” para executar cada instrução carregada.

- Ative o Modo Explicação para visualizar descrições detalhadas.

- Edite memória, registradores, cache ou instruções usando os botões dedicados.

- Clique em “Gráfico de Desempenho” para visualizar os ciclos de clock gastos por instrução.

- Clique em “Resetar” para reiniciar todo o sistema.

# 💡 Conceitos Demonstrados

🔹 Mapeamento direto de cache

🔹 Políticas de escrita (Write-Through + Write-Allocate)

🔹 Ciclos de clock e esforço computacional

🔹 Fluxo de dados entre memória, cache e registradores

🔹 Implementação de backend de alto desempenho em C integrado ao frontend em Python

# ✨ Agradecimentos

Este projeto foi desenvolvido para fins didáticos, como ferramenta prática de apoio ao estudo de Arquitetura de Computadores e Sistemas Embarcados.


### 🔖 **Orientações Finais**

- Substitua **`seuusuario`**, **`SEUID`** e links pelo seu usuário GitHub e LinkedIn.
- 
- Adicione imagens reais do programa na pasta `images` para as seções de screenshots.
- 
- Confirme se o nome do seu repositório corresponde ao projeto antes de publicar.


