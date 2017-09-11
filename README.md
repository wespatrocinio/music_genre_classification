# Music genre classification

Este projeto tem como objetivo mostrar os passos básicos do processo de construção de um clasificador, baseado em _Machine Learning_ que classifica o gênero musical de uma faixa baseado em sua letra.

## Preparando o ambiente

Para preparar o ambiente, eu sugiro que você crie um ambiente virtual específico para esta aplicação. Supondo que você é usuário do Anaconda (http://anaconda.com), o comando é:

```sh
conda create --name music_genre_classification
source activate music_genre_classification
```

Feito isso, instale as dependências, via PyPi, rodando o seguinte comando na raiz do projeto:

```sh
pip install -r requirements
```

Com isso, você terá o seu ambiente pronto para rodar a aplicação.

## Executando a criação do modelo

Para acompanhar e reexecutar a criação do modelo, você deverá excutar Jupyter Notebook e abrir o notebook disponível em `notebooks/music_genre_classification.ipynb`

```sh
jupyter-notebook
```

Após aberto o notebook, basta executar as células e verificar o que está sendo feito.

## Executando a API

Para executar e testar a API, você deverá ir até a raiz da aplicação (`/music_genre_classification`) e executar o seguinte comando:

```sh
python app.py
```

Isso executará a aplicação, a qual irá disponibilizar a API na porta padrão do Flask (5000). Se você acessar o endereço `http://localhost:5000`, acessará a documentação básica da API (via Swagger), onde poderá testar a API a partir da interface.

Como a API tem como dependência algumas bibliotecas do pacote NLTK, a primeira execução da aplicação será um pouco lenta devido ao _download_ de tais recursos. Após isso, não há mais este _overhead_. 
