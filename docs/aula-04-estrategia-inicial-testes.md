# Estratégia Inicial de Testes – LocalEats

Disciplina: Qualidade de Software.  
Aula 4 – Estratégia de Testes.  
Equipe: Solo dev.  
Integrante: Marcelo Oscaberry.  

## 1. Funcionalidades

- Login  
- Busca de restaurantes (com filtros)  
- Visualização de restaurante (cardápio, fotos, avaliações)  
- Sistema de avaliações  
- Recomendações personalizadas  
- Favoritos  

### 1.1 Fluxo Principal do Usuário

Essas funcionalidades representam o caminho natural do usuário dentro da plataforma:  

Usuário entra → Login  
Procura algo → Busca  
Analisa opções → Visualização  
Interage → Avaliações / Favoritos  
Continua usando → Recomendações  

## 2. Níveis de Teste

**Funcionalidade: Login**  
- Unitário: checar senha e campos obrigatórios  
- Integração: validar comunicação com banco de dados  
- Sistema: fluxo completo de login pelo usuário  
- Aceitação: usuário consegue acessar o sistema sem problemas  

**Funcionalidade: Busca de restaurantes**  
- Unitário: verificar filtros (tipo de culinária, faixa de preço, localização)  
- Integração: Banco/API de restaurantes  
- Sistema: usuário filtra e recebe os resultados da busca  
- Aceitação: usuário localiza restaurantes que atendem seus critérios  

**Funcionalidade: Visualização de restaurante**  
- Unitário: carregar dados (nome, cardápio, avaliações)  
- Integração: conexão com banco de dados e imagens  
- Sistema: exibição completa da página do restaurante  
- Aceitação: usuário consegue visualizar todas as informações  

**Funcionalidade: Sistema de avaliações**  
- Unitário: checar nota e texto da avaliação  
- Integração: salvar e recuperar avaliações do banco  
- Sistema: usuário submete e visualiza avaliações  
- Aceitação: avaliações são exibidas corretamente após envio  

**Funcionalidade: Recomendações personalizadas**  
- Unitário: sugestões baseadas em preferências do usuário  
- Integração: integração com histórico de uso  
- Sistema: plataforma gera recomendações personalizadas  
- Aceitação: usuário recebe sugestões relevantes  

**Funcionalidade: Favoritos**  
- Unitário: adicionar e remover restaurantes dos favoritos  
- Integração: persistir favoritos do usuário no banco  
- Sistema: usuário gerencia sua lista de favoritos  
- Aceitação: favoritos são exibidos corretamente  

## 3. Prioridades e Riscos

**Alta prioridade:**  
- Login → sem login o usuário não consegue acessar o sistema  
- Busca de restaurantes → usuário não encontra o que procura  
- Visualização de restaurante → usuário não visualiza detalhes  

**Justificativa:**  
Falhas nessas áreas bloqueiam o uso da plataforma. Sem elas o usuário não consegue completar sua jornada: sem login não entra, sem busca não encontra e sem visualização não vê informações.  

**Média prioridade:**  
- Avaliações → compromete a confiabilidade do sistema e do restaurante  
- Recomendações → afeta a credibilidade do estabelecimento  

**Justificativa:**  
Embora não impeçam o uso básico, essas funcionalidades impactam a percepção e experiência emocional do usuário.  

**Baixa prioridade:**  
- Favoritos → não bloqueia o uso  

**Justificativa:**  
É uma funcionalidade extra, complementar. Não impede a utilização real do sistema.  

## 4. Pirâmide de Testes

- Maior foco: Testes Unitários  
- Médio foco: Testes de Integração  
- Menor foco: Testes de sistema  

**Justificativa:**  
Testes unitários são ágeis, econômicos e previnem erros desde o início.  
Testes de integração são necessários neste sistema, pois diversas falhas relatadas envolvem comunicação entre componentes (ex: banco de dados, APIs, mobile/web).  
Testes de sistema são mais custosos e demorados, devendo ser reservados para fluxos críticos (ex: login e busca).  
O ideal é antecipar a detecção de falhas para evitar problemas maiores no futuro.  

## 5. Testes em Produção

- Uso de produção de maneira controlada, com feature flags (canário), monitoramento de desempenho e análise de logs  
- Aplicar monitoramento de desempenho, logs e análise de erros reais, além de feature flags (canário).  

**Justificativa:**  
Considerando que o sistema já teve problemas reais após o lançamento, testes em produção auxiliam na identificação de falhas que não surgem em ambiente de teste, especialmente:  
problemas de escala  
comportamento real dos usuários  
compatibilidade com diferentes dispositivos  

Contudo, precisam ser controlados para não prejudicar os usuários.
