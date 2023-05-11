# Atividade
---

1. Crie uma classe Calculadora com os metodos somar, subtrair, multiplicar, dividir. Siga o ciclo do TDD, escrevendo um arquivo de testes automatizados com ao menos 3 testes para cada método. 
IMPORTANTE: Lembre-se que a divisão não é possível dividir por ZERO (0).

2 Seguindo o ciclo, crie uma classe Empregado, que contem  os atributos primeiro_nome, sobrenome, cargo e salario; além disso, deve haver um atributo taxa_reajuste, com valor padrao de 1.05, referente ao reajuste anual de salario. Todos os atributos devem ser definidos no construtor da classe. 

Crie também os métodos:
* calcular_reajuste, o qual irá exibir o novo salario do funcionario, baseado no salário atual e sua taxa de reajuste;
* gerar_nome_completo, que combinara seus ambos os nomes e exibir o nome completo do funcionário;
* validar_cargo, que deverá verificar se o cargo atual está dentro de uma lista de cargos implementados pela empresa (presidente, diretor, gerente, analista e auxiliar)