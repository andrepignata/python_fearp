# Dashboard Interativo de Análise de Dados Financeiros

Este projeto faz parte de uma introdução ao Python voltada para alunos de **economia**, **administração** e **contabilidade**, com foco em **manipulação de dados** e **visualização interativa**. O projeto usa **Jupyter Notebook** para aprendizado prático e **Streamlit** para criação de dashboards dinâmicos.

## Objetivo

O objetivo deste projeto é ensinar os conceitos básicos de Python e sua aplicação prática em análise de dados financeiros. Além disso, apresenta uma abordagem prática utilizando o Jupyter Notebook para manipulação de dados e o Streamlit para criar visualizações interativas. O projeto ajuda os alunos a aprender como trabalhar com dados financeiros e contábeis, e como apresentar esses dados de maneira visual e interativa.

Os principais recursos do projeto incluem:

- Filtros interativos para selecionar produtos e definir um preço mínimo.
- Visualização da **evolução da quantidade de vendas** por produto, com opções de gráficos de linha e de barras.
- Cálculo e visualização da **evolução do lucro** (receita - custos) por mês, agregando todos os produtos ou separando por produto.

## Funcionalidades

1. **Filtros por Preço Mínimo e Produto**: Permite selecionar um preço mínimo e escolher quais produtos exibir.
1. **Gráficos de Vendas**: Exibe a evolução da quantidade de vendas em gráficos de linha ou de barras.
1. **Gráficos de Lucro**: Exibe a evolução do lucro mensal, podendo agrupar todos os produtos ou dividir por produto específico.

## Como Utilizar

### 1. Clone o Repositório

```bash
git clone https://github.com/andrepignata/python_fearp.git
cd python_fearp
```

#### 1.1 Caso não tenha o git instalado

Baixe o repositório como zip e extraia os arquivos.

[Download do repositório](https://github.com/andrepignata/python_fearp/archive/refs/heads/main.zip)

### 2. Criar e Ativar um Ambiente Virtual com Conda

Este projeto recomenda o uso de um ambiente virtual para isolar as dependências. Para criar um ambiente virtual chamado `fearp`, utilize o **Conda**:

```bash
conda create -f conda_env.yml
```

Este projeto utiliza **Jupyter Notebook**, **Streamlit**, **Pandas** e **Matplotlib** que são instalados automaticamente com a criação do ambiente.

Após a criação, ative o ambiente:

```bash
conda activate fearp
```

### 2. Utilizando o Jupyter Notebook

Antes de utilizar o dashboard interativo com Streamlit, é recomendável começar pelo **Jupyter Notebook** para explorar e aprender a manipulação de dados com Python. Para abrir o Jupyter Notebook, execute o seguinte comando:

```bash
jupyter notebook
```

No navegador, acesse o arquivo `palestra_python_dados.ipynb` que contém os exemplos práticos ensinados na palestra.

### 4. Executar o Dashboard com Streamlit

Após aprender a manipular os dados com o Jupyter, você pode rodar o dashboard interativo criado com **Streamlit**. Para rodar o aplicativo no navegador, execute o seguinte comando:

```bash
streamlit run dashboard.py
```

O aplicativo abrirá em seu navegador padrão, e você poderá começar a explorar os dados financeiros interativamente.

### 5. Arquivo de Dados

O arquivo de dados `dados_financeiros.csv` já está incluído no projeto. Ele contém 1000 observações fictícias com dados de produtos, preços, quantidades, receitas e custos.

## Exemplo de Uso

No dashboard, você poderá:

1. **Filtrar por Preço Mínimo e Produto**: Ajuste o slider de preço e selecione os produtos desejados.
1. **Visualizar Vendas**: Veja a evolução das vendas ao longo do tempo, em gráficos de linha ou de barras.
1. **Visualizar Lucro**: Acompanhe a evolução do lucro mensalmente, tanto de forma agregada quanto separada por produto.

## Licença

Este projeto é licenciado sob a **MIT License**. Você pode reproduzir e modificar o código, desde que seja feita a devida atribuição ao autor original.

## Autor

André Pignata

[LinkedIn](https://www.linkedin.com/in/andre-pignata/)

[GitHub](https://github.com/andrepignata)
