# payres-backend
## Payres - Sistema de Gerenciamento de Pagamentos para Restaurantes  🍽 

### Website desenvolvido em Angular 6 + Django. ###
##### Este projeto se refere apenas ao back-end em Django. #####

**Link do front-end: https://github.com/henriquechang/payres-webapp/**

**Link da página: https://payres-webapp.herokuapp.com/**

**Link da API: https://payres-backend.herokuapp.com/**

Pontos de melhoria do sistema:

- Implementar Autenticação (API/Website)
- Implementar casos de teste.
- Implementar Roles para os Usuários do sistema. Exemplo:
  - Garçom: Pode apenas lançar consumo e registrar pagamentos.
  - Admin: Pode criar/remover mesas, produtos, lançar consumo e registrar pagamentos.
- Permitir cancelamento de itens já registrados e ainda não pagos.
- Criar uma tabela de ingredientes, que define o custo e o estoque de cada produto
- Criar um estoque para cada ingrediente, limitando o estoque de cada produto 
- Permitir pagamento opcional de valor de 10% da conta ao garçom.
