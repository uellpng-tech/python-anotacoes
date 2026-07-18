# Primeiros passos

## Conceitos iniciais

Para compreendermos como que funciona a linguagem de programação Python devemos abordar os conceitos iniciais. Entre os conceitos iniciais veremos como os comandos se comportam, inicialmente vamos analizar o comando utilizado para voltar uma mensagem, esse comando se chama print e ele é constantemente usado para saída de dados, o print é utilizado da seguinte maneira:

`print("Olá, Mundo")`<br>
&ensp;&ensp;&ensp;Retorno: Olá, Mundo

Como podemos observar o comando vem primeiro, em seguida os parênteses para sinalizar oque o comando vai executar e por fim as aspas que guarda a frase, no mundo da programação chamamos oque está dentro das aspas de strings, as strings sinalizam a linguagem que os dados são os que estão dentro das aspas, strings podem guardar tanto texto quanto, números, acentos e simbolos. Geralmente os comandos abordam a mesma lógica que o comando de exemplo, eles vem primeiro e depois vem os parênteses sinalizando oque o comando irá executar ou fazer, também é importante afirmar que os números não precisam de delimitação pois a linhagem os reconhece.

## Operações simples

No Python as operações matemáticas abordam um sistema bem simples. De inicio vamos ver como as operações simples (adição e subtração) são efetuadas no Python e como elas se comportam dentro do ambiente da linguagem. As operações de adição e subtração são bem simples:

`print(7+2)`
&ensp;&ensp;&ensp;Retorno: 9

Como podemos ver no exemplo de operação de adição com o comando print a conta deu certo, a linguagem Python identifica as operações simples como mais e menos da forma que conhecemos, o exemplo vale tanto para a adição quanto para a subtração, podemos observar tanbém que os números não então entre aspas, oque significa que o Python consegue identificar números sem necessidade de utilizar as aspas. Também podemos usar um outro exemplo que entra no tema abordado:

`print('7'+'2')`
&ensp;&ensp;&ensp;Retorno: 72

Aqui podemos ver como o Python se comporta diante de duas strings dentro de uma operação, o Python identifica esses dois números como duas strings como vimos anteriormente uma string é tudo aquilo que é um dado, podendo ser tanto número quanto simbolo e outras coisas. O Python se comporta juntando essas duas strings oque abre margem para outro conceito inicial da linguagem a concatenação.

## Concatenação

A concatenação na linguagem Python é a junção de dois elementos. A concatenação junta dois elementos sendo eles listas ou strings, os dois elementos usados de exemplo anteriormente foram o "7" e o "2", a junção deles foi efetuada pelo simbolo de mais (+), fazendo com que a linguagem Python identificasse os dois números como duas mensagens, isso também funciona utilizando strings ou utilizando como simbolo de junção a vírgula ",". Para entendermos melhor esse conceito vamos a um exemplo:

`print('Olá'+'Mundo!')`

&ensp;&ensp;&ensp;Retorno: Ola Mundo!

Esse exemplo também funcionaria utilizando a vírgula, porém nesse caso o simbolo de adição se torna mais comum.

## Variáveis 

No Python as variáveis são espaços usados para armazenar dados. O comportamento das variáveis dentro do Python são bem simples, você atribui um nome a variável que deseja salvar algo e quando utilizada passara a ser oque você atribuiu, dentro desse conceito a regras muito simples, nenhum nome de variável pode começar com um número, letras minúsculas ou maiuscula são diferentes (a variável nome é diferente da variável Nome) e é importante não usar acentuação para evitar erros de codificação. Para entendermos melhor podemos usar um simples exemplo:

`nome = "joão"` 

`print(nome)`

&ensp;&ensp;&ensp;Retorno: joão

Como podemos ver a estrutura da variável aborda o nome, simbolo de igual e o dado, o dado atribuido a variável pode ser tanto string quanto qualquer outra coisa. Dois pontos muito importantes podem ser abordados aqui, no Python toda variável é considerada um objeto, isso é muito importante para entendermos a lógica  da linguagem, a segunda observação é que quando algo que não seja uma string está no comando print não a necessidade de utilizar aspas, como já dito antes tudo que está entre aspas são dados. Podemos entrar mais nesse conceito abordando outro exemplo bem similar:

`nome = "joão"`

`idade = 16`

`peso = 70.9` 

`print(nome,idade,peso)`

&ensp;&ensp;&ensp;Retorno: joão 16 70.9

Esse exemplo aborda como a vírgula se comporta no comando print e como podemos mostrar mais de uma variável. Isso é muito importante inicialmente pois mostra que o uso da concatenação tornasse um erro em certos casos, como nesse caso onde a saida de dados não é uma string então utilizamos a vírgula como separação para as variáveis, outro ponto muito importante é que as variáveis como dito antes armazena qualquer tipo de dado, como podemos observar na variável peso o número é um número quebrado, dentro do Python como a vírgula é utilizada com outro intuito utilizamos o ponto (.) para representar um úmero quebrado. Depois que entendemos a lógica das váriaveis podemos entrar em outro tema que envolve as variáveis.

## Entrada de dados

No Python o comando input é utilizado para entrada de dados, esse comando interage com o usuário possibilitando ao comando receber uma entrada de dados. O comando input é utilizado para receber dados, ele é utilizado em conjunto com as variáveis para guardar informações, apesar de poder ser utilizado sozinho ele apenas interage com o usuário e não armazena os dados, por isso a utilização dele é em conjunto com as variáveis. Para compreendermos melhor a utilização do input temos um exemplo:

`nome = input('Qual seu nome? ')`

`idade = input('Qual é a sua idade? ')`

`peso = input('Quanto você pesa? ')` 

`print(nome,idade,peso)`

&ensp;&ensp;&ensp; Retorno: Qual seu nome?

&ensp;&ensp;Usuário: pedro

&ensp;&ensp;&ensp; Retorno: Qual seu nome?

&ensp;&ensp;Usuário: 20

&ensp;&ensp;&ensp; Retorno: Qual seu nome?

&ensp;&ensp;Usuário: 80kg

&ensp;&ensp;&ensp; Retorno: pedro 20 80kg

Nesse exemplo o input guarda oque o usuário responde e retorna através dos print. Nesse exemplo o retorno representa o comando e o usuário representa quem esta respondendo, na prática funciona da mesma maneira, o usuário responde e a variável em conjunto com o input guarda a resposta, a estrutura do input em conjunto com a variável é bem simples, primeiro o nome da variável, o comando input e a string contendo a pergunta dentro dos parenteses. Um bom ponto a se abordar é que o input sem delimitação prévia permite a entrada de qualquer dado tanto de número quanto de letra como podemos ver no input na variável peso que o usuário colocou "80KG" utilizando número e letra juntos.

## Exercícios Relacionados 

- [Exercício 001](../exercicios/aula%205%20exercicio%2001.py)
- [Exercício 002](../exercicios/aula%205%20exercicio%2002.py)