Feature: Busca de restaurantes

  Scenario: Buscar restaurantes por localizacao existente
    Given que o usuario autenticado esta na pagina de exploracao
    When pesquisar por "Centro"
    Then o sistema deve exibir restaurantes encontrados

  Scenario: Buscar restaurantes por termo inexistente
    Given que o usuario autenticado esta na pagina de exploracao
    When pesquisar por "XYZ123"
    Then o sistema deve informar que nenhum restaurante foi encontrado
