# Gerador-de-CPF
Um simples gerador de CPF válido

O código consiste em criar 9 dígitos aleatórios, os quais serão a base do CPF, e depois calcular os dois números validadores
A fórmula para os validadores consiste em:

1 - Pegar todos os algarismos individualmente e multiplicar por uma ordem decrescente começando por 10 
Exemplo com os números 123.456.789: 1 * 10, 2 * 9, 3 * 8, ..., 9 * 2

2 - O resultado de todas as multiplicações é somado e depois multiplicado por 10 
Exemplo com os números 123.456.789: 10 + 18 + 24 + 28 + 30 + 30 + 28 + 24 + 18 = 210 // 210 * 10 = 2100

3 - Esse resultado é então dividido por 11; caso o resto da divisão seja menor ou igual a 9, o primeiro dígito validador será o resto, senão o dígito será igual a 0 
Continuação do exemplo: 2100 / 11 = 190, com resto de 10. Logo, como 10 > 9, o primeiro dígito validador será 0

4 - Para o segundo número validador, repete-se o processo, porém é adicionado o primeiro dígito validador no CPF e a contagem regressiva começa a partir de 11 
Continuação do exemplo: 123.456.789-0 // 1 * 11, 2 * 10, 3 * 9, ..., 9 * 3, 0 * 2

5 - Nova soma da multiplicação e a multiplicação por 10: 1 * 11, 2 * 10, ..., 0 * 2 = 255 // 255 * 10 = 2550 
Resto da divisão por 11: 2550 / 11 = 231, com resto 9. Logo, como 9 ≥ 9, o segundo dígito validador será 9

Resultado do número 123.456.789 é de 123.456.789-09
