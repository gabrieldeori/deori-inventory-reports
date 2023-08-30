# Relatórios de estoque

- [Data de entrega](#data-de-entrega)
- [O que deverá ser desenvolvido](#o-que-deverá-ser-desenvolvido)
- [Desenvolvimento e testes](#desenvolvimento-e-testes)
- [Dados](#dados)
- [Antes de começar a desenvolver](#antes-de-começar-a-desenvolver)

Lista de requisitos:
- [Requisitos](#requisitos-obrigatórios)
  - [1 - Criar um método `generate` numa classe `SimpleReport` do módulo `inventory_report/reports/simple_report.py`. Esse método deverá receber dados numa lista contendo estruturas do tipo `dict` e deverá retornar uma string formatada como um relatório](#1---criar-um-método-generate-numa-classe-simplereport-do-módulo-inventory_reportreportssimple_reportpy-esse-método-deverá-receber-dados-numa-lista-contendo-estruturas-do-tipo-dict-e-deverá-retornar-uma-string-formatada-como-um-relatório)
  - [2 - Criar um método `generate` numa classe `CompleteReport` do módulo `inventory_report/reports/complete_report.py`. Esse método deverá receber dados numa lista contendo estruturas do tipo `dict` e deverá retornar uma string formatada como um relatório](#2---criar-um-método-generate-numa-classe-completereport-do-módulo-inventory_reportreportscomplete_reportpy-esse-método-deverá-receber-dados-numa-lista-contendo-estruturas-do-tipo-dict-e-deverá-retornar-uma-string-formatada-como-um-relatório)
  - [3 - Criar um método `import_data` dentro de uma classe `Inventory` do módulo `inventory_report/inventory/inventory.py`, capaz de ler um arquivo CSV o qual o caminho é passado como parâmetro](#3---criar-um-método-import_data-dentro-de-uma-classe-inventory-do-módulo-inventory_reportinventoryinventorypy-capaz-de-ler-um-arquivo-csv-o-qual-o-caminho-é-passado-como-parâmetro)
  - [4 - Criar um método `import_data` dentro de uma classe `Inventory` do módulo `inventory_report/inventory/inventory.py`, capaz de ler um arquivo JSON o qual o caminho é passado como parâmetro](#4---criar-um-método-import_data-dentro-de-uma-classe-inventory-do-módulo-inventory_reportinventoryinventorypy-capaz-de-ler-um-arquivo-json-o-qual-o-caminho-é-passado-como-parâmetro)
  - [5 - Criar um método `import_data` dentro de uma classe `Inventory` do módulo `inventory_report/inventory/inventory.py`, capaz de ler um arquivo XML o qual o caminho é passado como parâmetro](#5---criar-um-método-import_data-dentro-de-uma-classe-inventory-do-módulo-inventory_reportinventoryinventorypy-capaz-de-ler-um-arquivo-xml-o-qual-o-caminho-é-passado-como-parâmetro)
  - [6 - Criar uma classe abstrata `Importer` no módulo `inventory_report/importer/importer.py`, que terá três classes herdeiras: `CsvImporter`, `JsonImporter` e `XmlImporter`, cada uma definida em seu respectivo módulo](#6---criar-uma-classe-abstrata-importer-no-módulo-inventory_reportimporterimporterpy-que-terá-três-classes-herdeiras-csvimporter-jsonimporter-e-xmlimporter-cada-uma-definida-em-seu-respectivo-módulo)
  - [7 - Criar uma classe `InventoryIterator` no módulo `inventory_report/inventory/inventory_iterator.py`, que implementa a interface de um iterator (`Iterator`). A classe `InventoryRefactor` deve implementar o método `__iter__`, que retornará este iterador](#7---criar-uma-classe-inventoryiterator-no-módulo-inventory_reportinventoryinventory_iteratorpy-que-implementa-a-interface-de-um-iterator-iterator-a-classe-inventoryrefactor-deve-implementar-o-método-__iter__-que-retornará-este-iterador)
- [Requisitos bônus](#requisitos-bônus)
  - [8 - Preencha a função main no módulo `inventory_report/main.py` que, ao receber pela linha de comando o caminho de um arquivo e o tipo de relatório, devolve o relatório correto](#8---preencha-a-função-main-no-módulo-inventory_reportmainpy-que-ao-receber-pela-linha-de-comando-o-caminho-de-um-arquivo-e-o-tipo-de-relatório-devolve-o-relatório-correto)

- [Depois de terminar o desenvolvimento (opcional)](#depois-de-terminar-o-desenvolvimento)
  - [Revisando um Pull Request](#revisando-um-pull-request)
- [Avisos finais](#avisos-finais)

---

## Data de entrega

  - Serão `2` dias de projeto.
  - Data de entrega do projeto: `04/03/2022 14:00`.

---

## O que deverá ser desenvolvido

Foi implementado um gerador de relatórios que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados.

Esses dados de estoque poderão ser obtidos de diversas fontes:

- Através da importação de um arquivo `CSV`;

- Através da importação de um arquivo `JSON`;

- Através da importação de um arquivo `XML`;

Além disso, o relatório final deverá é gerado em duas versões: simples e completa.

### Como o projeto deve ser executado

Um executável **via linha de comando** com o comando `inventory_report <argumento1> <argumento2>`:

- O **<argumento 1>** deve receber o caminho de um arquivo a ser importado. O arquivo pode ser um `csv`, `json` ou `xml`.

- O **<argumento 2>** pode receber duas strings: `simples` ou `completo`, cada uma gerando o respectivo relatório.

---

## Desenvolvimento e testes

Para executar os testes, **crie e ative o ambiente virtual**, além de também instalar as dependências do projeto. Isso pode ser feito através dos comandos:

```bash
$ python3 -m venv .venv

$ source .venv/bin/activate

$ python3 -m pip install -r dev-requirements.txt
```

O arquivo `dev-requirements.txt` contém todos as dependências que serão utilizadas no projeto com as dependências já instaladas, para executar os testes basta usar o comando:

```bash
$ python3 -m pytest
```

Para verificar o padrão de estilo do Python em todo código, execute o seguinte comando:

```bash
$ python3 -m flake8
```

---

## Dados

Arquivos de exemplo nos três formatos de importação estão disponíveis no diretório `data` dentro do diretório `inventory_report`.

### Importação de arquivos CSV

Os arquivos **CSV** são separados por vírgula, como no exemplo abaixo:

```csv
id,nome_do_produto,nome_da_empresa,data_de_fabricacao,data_de_validade,numero_de_serie,instrucoes_de_armazenamento
1,Nicotine Polacrilex,Target Corporation,2020-02-18,2022-09-17,CR25 1551 4467 2549 4402 1,morbi ut odio cras mi pede malesuada in imperdiet et commodo vulputate justo in blandit
2,fentanyl citrate,"Galena Biopharma, Inc.",2019-12-06,2022-12-25,FR29 5951 7573 74OY XKGX 6CSG D20,bibendum morbi non quam nec dui luctus rutrum nulla tellus in
3,NITROUS OXIDE,Keen Compressed Gas Co. Inc.,2019-12-22,2023-11-07,CZ09 8588 0858 8435 9140 2695,ipsum dolor sit amet consectetuer adipiscing elit proin risus praesent
```

### Importação de arquivos JSON

Os arquivos JSON seguem o seguinte modelo:

```json
[
  {
    "id":1,
    "nome_do_produto":"CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa":"Forces of Nature",
    "data_de_fabricacao":"2020-07-04",
    "data_de_validade":"2023-02-09",
    "numero_de_serie":"FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento":"in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices phasellus"
  }
]
```

### Importação de arquivos XML

Os arquivos **XML** seguem o seguinte modelo:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<dataset>
  <record>
    <id>1</id>
    <nome_do_produto>valsartan and hydrochlorothiazide</nome_do_produto>
    <nome_da_empresa>Lake Erie Medical &amp; Surgical Supply DBA Quality Care Products LLC</nome_da_empresa>
    <data_de_fabricacao>2019-10-27</data_de_fabricacao>
    <data_de_validade>2022-08-31</data_de_validade>
    <numero_de_serie>MT08 VVDN 2131 9NFL C1JG KTDV RS1L LOZ</numero_de_serie>
    <instrucoes_de_armazenamento>at lorem integer tincidunt ante vel ipsum praesent blandit lacinia erat</instrucoes_de_armazenamento>
  </record>
</dataset>
```

---


### PARA TESTAR OU DESENVOLVER:

1. Clone o repositório

- `git clone xxxx`.
- Entre na pasta do repositório que você acabou de clonar:
  - `xxxx`

2. Crie o ambiente virtual para o projeto

- `python3 -m venv .venv && source .venv/bin/activate`

Nota: após terminar o trabalho, para desativar o ambiente virtual digite `deactivate`

3. Instale as dependências

- `python3 -m pip install -r dev-requirements.txt`

4. Para desenvolver crie uma branch a partir da branch `main`

- Verifique que você está na branch `main`
  - Exemplo: `git branch`
- Se não estiver, mude para a branch `main`
  - Exemplo: `git checkout main`
- Agora crie uma branch à qual você vai submeter os `commits` do seu projeto
  - Você deve criar uma branch no seguinte formato: `feat/some-feature`
  - Exemplo: `git checkout -b feat/some-feature`

5. Adicione as mudanças ao _stage_ do Git e faça um `commit`

- Verifique que as mudanças ainda não estão no _stage_
  - Exemplo: `git status` (deve aparecer listada a pasta _exemplo_ em vermelho)
- Adicione o novo arquivo ao _stage_ do Git
  - Exemplo:
    - `git add .` (adicionando todas as mudanças - _que estavam em vermelho_ - ao stage do Git)
    - `git status` (deve aparecer listado o arquivo _exemplo/README.md_ em verde)
- Faça o `commit` inicial
  - Exemplo:
    - `git commit -m 'feat: something inventory-report'` (fazendo o primeiro commit)
    - `git status` (deve aparecer uma mensagem tipo _nothing to commit_ )

6. Adicione a sua branch com o novo `commit` ao repositório remoto

- Usando o exemplo anterior: `git push -u origin exemplo-project-name`

7. Crie um novo `Pull Request` _(PR)_

- Vá até a página de _Pull Requests_ do [repositório no GitHub](xxxx)
- Clique no botão verde _"New pull request"_
- Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
- Clique no botão verde _"Create pull request"_
- Adicione uma descrição para o _Pull Request_ e clique no botão verde _"Create pull request"_
- **Não se preocupe em preencher mais nada por enquanto!**
- Volte até a [página de _Pull Requests_ do repositório](xxxx/pulls) e confira que o seu _Pull Request_ está criado

---

## Requisitos:

#### 1 - Criar um método `generate` numa classe `SimpleReport` do módulo `inventory_report/reports/simple_report.py`. Esse método deverá receber dados numa lista contendo estruturas do tipo `dict` e deverá retornar uma string formatada como um relatório.

- Deve ser possível executar o método `generate` sem instanciar um objeto de `SimpleReport`
- O método deve receber de parâmetro uma lista de dicionários no seguinte formato:

   ```json
   [
     {
       "id": 1,
       "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2020-07-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
       "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
     }
   ]
   ```

- O método deverá retornar uma saída com o seguinte formato:

   ```bash
   Data de fabricação mais antiga: YYYY-MM-DD
   Data de validade mais próxima: YYYY-MM-DD
   Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA
   ```
- A data de validade mais próxima, somente considera itens que ainda não venceram.

**Nota**: Usei o módulo [datetime](https://docs.python.org/3/library/datetime.html).

##### As seguintes verificações serão feitas:

- 1.1 - É validado que é possível que o método `generate` da classe `SimpleReport` retorne a data de fabricação mais antiga

- 1.2 - É validado que é possível que o método `generate` da classe `SimpleReport` retorne a validade mais próxima

- 1.3 - É validado que é possível que o método `generate` da classe `SimpleReport` retorne a empresa com maior estoque

- 1.4 - É validado que é possível que o método `generate` da classe `SimpleReport` retorne o relatório no formato correto

#### 2 - Criar um método `generate` numa classe `CompleteReport` do módulo `inventory_report/reports/complete_report.py`. Esse método deverá receber dados numa lista contendo estruturas do tipo `dict` e deverá retornar uma string formatada como um relatório.

- A classe `CompleteReport` deve herdar o método (`generate`) da classe `SimpleReport`, de modo a especializar seu comportamento.

- O método deve receber de parâmetro uma lista de dicionários no seguinte formato:

   ```json
   [
     {
       "id": 1,
       "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2020-07-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
       "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
     }
   ]
   ```

- O método deverá retornar uma saída com o seguinte formato:

   ```bash
   Data de fabricação mais antiga: YYYY-MM-DD
   Data de validade mais próxima: YYYY-MM-DD
   Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA

   Produtos estocados por empresa:
   - Physicians Total Care, Inc.: QUANTIDADE
   - Newton Laboratories, Inc.: QUANTIDADE
   - Forces of Nature: QUANTIDADE
   ```

##### As seguintes verificações serão feitas:

- 2.1 - É validado que é possível que o método `generate` da classe `CompleteReport` retorne a data de fabricação mais antiga

- 2.2 - É validado que é possível que o método `generate` da classe `CompleteReport` retorne a validade de fabricação mais próxima

- 2.3 - É validado que é possível que o método `generate` da classe `CompleteReport` retorne a empresa com maior estoque

- 2.4 - É validado que é possível que o método `generate` da classe `CompleteReport` retorne a quantidade de produtos por empresa

- 2.5 - É validado que é possível que o método `generate` da classe `CompleteReport` retorne o relatório no formato correto

#### 3 - Criar um método `import_data` dentro de uma classe `Inventory` do módulo `inventory_report/inventory/inventory.py`, capaz de ler um arquivo CSV o qual o caminho é passado como parâmetro.

- O método, receberá como parâmetro o caminho para o arquivo CSV e o tipo de relatório a ser gerado (`"simples"`, `"completo"`). De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe `Inventory` deve chamar o método `generate` da classe que vai gerar o relatório (`SimpleReport`, `CompleteReport`).

##### As seguintes verificações serão feitas:

- 3.1 - É validado que ao importar um arquivo csv simples será retornado com sucesso

- 3.2 - É validado que ao importar um arquivo csv completo será retornado com sucesso

#### 4 - Criar um método `import_data` dentro de uma classe `Inventory` do módulo `inventory_report/inventory/inventory.py`, capaz de ler um arquivo JSON o qual o caminho é passado como parâmetro.

- O método, receberá como parâmetro o caminho para o arquivo JSON e o tipo de relatório a ser gerado (`"simples"`, `"completo"`). De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe `Inventory` deve chamar o método `generate` da classe que vai gerar o relatório (`SimpleReport`, `CompleteReport`).

Nota: Estamos utilizando o mesmo método do requisito anterior.

##### As seguintes verificações serão feitas:

- 4.1 - É validado que ao importar um arquivo json simples será retornado com sucesso

- 4.2 - É validado que ao importar um arquivo json completo será retornado com sucesso

#### 5 - Criar um método `import_data` dentro de uma classe `Inventory` do módulo `inventory_report/inventory/inventory.py`, capaz de ler um arquivo XML o qual o caminho é passado como parâmetro.

- O método, receberá como parâmetro o caminho para o arquivo XML e o tipo de relatório a ser gerado (`"simples"`, `"completo"`). De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe `Inventory` deve chamar o método `generate` da classe que vai gerar o relatório (`SimpleReport`, `CompleteReport`).

Nota: Estamos utilizando o mesmo método do requisito anterior.

##### As seguintes verificações serão feitas:

- 5.1 - É validado que ao importar um arquivo xml simples será retornado com sucesso

- 5.2 - É validado que ao importar um arquivo xml completo será retornado com sucesso

#### 6 - Criar uma classe abstrata `Importer` no módulo `inventory_report/importer/importer.py`, que terá três classes herdeiras: `CsvImporter`, `JsonImporter` e `XmlImporter`, cada uma definida em seu respectivo módulo.

- A classe abstrata deve definir a assinatura do método `import_data` a ser implementado por cada classe herdeira. Ela deve receber como parâmetro o nome do arquivo a ser importado.

- O método `import_data` definido por cada classe herdeira deve lançar uma exceção caso a extensão do arquivo passado por parâmetro seja inválida. Por exemplo, quando se passa um  caminho de um arquivo extensão CSV para o `JsonImporter`.

- O método deverá ler os dados do arquivo passado e retorná-los estruturados em uma lista de dicionários conforme exemplo abaixo:

   ```json
   [
     {
       "id": 1,
       "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2020-07-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
       "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
     }
   ]
   ```

##### Validações:

- 6.1 - É validado que a casse CsvImporter está herdando a classe Importer

- 6.2 - É validado que a casse JsonImporter está herdando a classe Importer

- 6.3 - É validado que a casse XmlImporter está herdando a classe Importer

- 6.4 - É validado que a classe CsvImporter esta importando os dados para uma lista

- 6.5 - É validado que a classe JsonImporter esta importando os dados para uma lista

- 6.6 - É validado que a classe XmlImporter esta importando os dados para uma lista

- 6.7 - É validado que ao enviar um arquivo com extensão incorreta para o CsvImporter irá gerar um erro

- 6.8 - É validado que ao enviar um arquivo com extensão incorreta para o JsonImporter irá gerar um erro

- 6.9 - É validado que ao enviar um arquivo com extensão incorreta para o XmlImporter irá gerar um erro

👀 Estamos separando a lógica em várias classes (estratégias), preparando para aplicarmos o padrão de projeto **Strategy**. É uma solução para o caso em que uma classe possui muitas responsabilidades (propósitos).

#### 7 - Criar uma classe `InventoryIterator` no módulo `inventory_report/inventory/inventory_iterator.py`, que implementa a interface de um iterator (`Iterator`). A classe `InventoryRefactor` deve implementar o método `__iter__`, que retornará este iterador.

- A classe `Inventory` deverá ser refatorada (copiada) em outro arquivo chamado `inventory_report/inventory/inventory_refactor.py`. Nesse arquivo você irá refatorar a classe `Inventory` chamando-a de `InventoryRefactor`.

- A classe `InventoryRefactor` deve utilizar as classes definidas no requisito 6 para lidar com a lógica de importação, via **composição** no método `import_data`.

- A classe `InventoryRefactor` deve receber por seu construtor a classe que será utilizada para lidar com a lógica de importação e armazenar em um atributo chamado `importer`.

- As classes `InventoryIterator` e `InventoryRefactor` devem implementar corretamente a interface do padrão de projeto **Iterator**, de modo que seja possível iterar sobre os itens em estoque.

- Ao importar os dados, os mesmos devem ser armazenados na instância, em adição aos itens já presentes naquela instância. O atributo de `InventoryRefactor` que armazena esses dados deve se chamar `data`.

- Os atributos e os métodos devem ser públicos.

> Para testar manualmente você pode fazer:

```python
iterator = iter(inventory)
first_item = next(iterator)
```

##### As seguintes verificações serão feitas:

- 7.1 - É validado que a instancia de InventoryRefactor é iterável (Iterable)

- 7.2 - É validado que é possivel iterar o primeiro item da lista usando csv

- 7.3 - É validado que é possivel iterar o primeiro item da lista usando json

- 7.4 - É validado que é possivel iterar o primeiro item da lista usando xml

- 7.5 - É validado que é possivel receber duas fontes de dados sem sobreescrita

- 7.6 - É validado que não é possivel enviar arquivo inválido


## Requisitos bônus:

#### 8 - Preencha a função `main` no módulo `inventory_report/main.py` que, ao receber pela linha de comando o caminho de um arquivo e o tipo de relatório, devolve o relatório correto.

- Deverá ser usado a classe `InventoryRefactor` para recuperar os dados e gerar o relatório.

- Ao chamar o comando no formato abaixo pelo terminal, deve ser impresso na tela o devido relatório no formato da saída dos requisitos `1` e `2`: 

```bash
$ inventory_report <caminho_do_arquivo_input> <tipo_de_relatório>
```

- Caso a chamada tenha menos de três argumentos (o nome `inventory_report` é considerado o primeiro argumento), exiba a mensagem de erro "Verifique os argumentos" na `stderr`.

Nota: A função `sys.argv` deve ser utilizada para receber a entrada de dados da pessoa usuária.

> Teste manual: dentro de um ambiente virtual onde seu projeto foi configurado, digite o comando `inventory_report parametro_1 parametro_2`, assim você conseguirá interagir com o menu.

##### As seguintes verificações serão feitas:

- 8.1 - É validado se o menu importa um arquivo csv simples

- 8.2 - É validado se o menu importa um arquivo csv completo

- 8.3 - É validado se o menu importa um arquivo json simples

- 8.4 - É validado se o menu importa um arquivo json completo

- 8.5 - É validado se o menu importa um arquivo xml simples

- 8.6 - É validado se o menu importa um arquivo xml completo

- 8.7 - É validado se houverem argumentos faltantes será retornando um erro

---

## Depois de terminar o desenvolvimento

Para sinalizar que o seu projeto está pronto para o _"Code Review"_ a seus pares, faça o seguinte:

* Vá até a página **DO SEU** _Pull Request_, adicione a label de _"code-review"_ e marque seus pares:

  * No menu à direita, clique no _link_ **"Labels"** e escolha a _label_ **code-review**;

  * No menu à direita, clique no _link_ **"Assignees"** e escolha **o seu usuário**;

  * No menu à direita, clique no _link_ **"Reviewers"** e selecione o time designado pela liderança.
#   d e o r i - i n v e n t o r y - r e p o r t s 
 
 