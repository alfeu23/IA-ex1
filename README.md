# Sistema de Recomendacao de Cursos UFSC

## Descricao

Este projeto implementa um sistema de recomendacao inteligente que analisa o perfil do estudante e sugere cursos da UFSC compatíveis com suas preferencias e qualificacoes.

## Estrutura do Projeto

```
.
├── src/
│   ├── main.py           # Arquivo principal com interface do usuário
│   ├── template.py       # Templates CLIPS e dicionários de dados
│   ├── cursos.py         # Base de dados dos cursos da UFSC
│   └── regras.py         # Regras de inferência do sistema especialista
├── data/
│   ├── cursos.txt        # Dados brutos dos cursos
│   ├── scraping.py       # Script para extração de dados do PDF
│   └── notas-maximas-minimas-sisu2024.pdf
├── pyproject.toml
└── README.md
```

## Tecnologias Utilizadas

- **Python 3.13+**
- **ClipsPy**: Interface Python para CLIPS
- **PDFPlumber**: Extração de dados de PDFs
- **Sistema CLIPS**: Motor de regras para sistema especialista

## Instalacao

1. Clone o repositorio:

```bash
git clone https://github.com/alfeu23/IA-ex1.git
cd IA-ex1
```

2. Instale as Dependencias

```bash
pip install pyproject.toml
```

ou usando uv:

```bash
uv sync
```

## Como utilizar

1. **Execute o sistema**

```bash
python3 src/main.py
```

2. **Siga as instrucoes do terminal**

   - Escolha sua preferencia de turno
   - Digite sua nota no ENEM
   - Escolha as areas de interesse
   - - Se escolher engenharia como uma das areas, sera necessario especificar o foco
   - Seleciona os campus de interesse
   - Especifique o tipo de curso desejado
   - Defina a duracao maxima do curso

3. **Resultado**
   O sistema exibira todos os cursos que atendem as especificacoes do seu perfil.
