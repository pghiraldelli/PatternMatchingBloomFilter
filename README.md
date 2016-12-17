# PatternMatchingBloomFilter

Trabalho desenvolvido na disciplina Estrutura de Dados 2, no período 2016.2. Foi sugerida uma implementação do algoritmo de pattern matching com filtros por linha, a fim de responder rapidamente se uma determinada palavra está presente em um texto aletório e muito grande.

Como rodar:
 ```sh
$ python patternmatching.py
```

Entradas esperadas:
   - K: representa a quantidade de caracteres das substring utilizadas para a busca e indexação das palavras no texto.
   - B: representa a quantidade de funções hash utilizadas na indexação de cada substring indexada (máximo de 6).
   - M: representa o tamanho do vetor de bits que receberá 1 nas posições cujas as funções hash retornam.
   - Palavra a ser pesquisada no texto

**Lógica utilizada**
Inicialmente o programa pré processa o texto, linha por linha, percorrendo-a de substring a substring de tamanho *K*. Para cada uma das substrings são obtidos *B* valores, referentes a cada saída de função hash. Finalmente, para cada um desses valores, a posição correspondente no vetor de bits da linha é marcada como 1 (inicialmente todas são zero).

Após isso é passada uma palavra a ser buscada e realizamos as mesmas operações que o pré processamento para obter seu próprio vetor de bits.

Dessa forma é possível comparar seu próprio vetor com o vetor de cada linha do texto. Caso os mesmos coincidam não há garantias de que a palavra realmente se encontra na determinada linha. Para contornar tal problema, utilizamos a função *find* do python para determinar se a palavra pertence à linha.

**Referências**
Texto utilizado:
  - Retirado do link: http://norvig.com/big.txt
  -	Tamanho: 6,5 MB
  -	Salvo como *big.txt*

Funções Hash utilizadas:
- MD5
- SHA1
- SHA224
- SHA256
- SHA384
- SHA512
