# RELATORIO DE IMPLEMENTAÇÃO DE SERVIÇOS AWS

Data: [22/01/2036]
Empresa: Abstergo Industries 
ResponsÃ¡vel: [Lucas]

## IntroduÃ§Ã£o
Este relatório apresenta o processo de implementação de ferramentas de otimização de nuvem na empresa Abstergo Industries, realizado por Lucas. O objetivo principal do projeto foi elencar e configurar 3 serviços AWS estratégicos, com a finalidade de realizar a diminuição de custos imediatos, aumentar a visibilidade dos gastos e evitar desperdícios de recursos computacionais.

## Descrição do Projeto
O projeto de implementação foi dividido em 3 etapas, cada uma focada em um pilar da gestão financeira na nuvem (FinOps): Visibilidade, Controle e Otimização. A seguir, estão descritas as etapas do projeto:

Etapa 1: 
- [AWS Cost Explorer]
- [Visualização e gerenciamento de custos e uso da AWS.]
- [Implementação de painéis personalizados para identificar tendências de gastos da Abstergo Industries nos últimos meses. A ferramenta permite filtrar os custos por serviço (ex: EC2, S3) e por tags de projeto, facilitando a identificação imediata de quais departamentos estão consumindo mais orçamento e onde estão os picos de gastos anômalos.]

Etapa 2: 
- [AWS Budgets]
- [Definição de orçamentos personalizados e alertas de custos.]
- [Criação de limites orçamentários mensais para a conta da empresa. Configuramos alertas automáticos que notificam o responsável (Lucas) via e-mail sempre que os custos reais ou previstos excederem 80% do valor estipulado. Isso impede surpresas na fatura no final do mês e permite uma ação rápida antes que o orçamento estoure.]

Etapa 3: 
- [AWS Compute Optimizer]
- [Recomendações de "Right-sizing" (dimensionamento correto) de recursos.]
- [Utilização de aprendizado de máquina para analisar o histórico de utilização das instâncias EC2 e volumes EBS da Abstergo. A ferramenta identificou recursos superdimensionados (ex: servidores com muita CPU ociosa) e recomendou a troca para tipos de instâncias menores e mais baratos, gerando uma redução direta no custo mensal sem perda de performance.]



## Conclusão
A implementação destas ferramentas na empresa Abstergo Industries tem como resultado esperado uma redução significativa nas despesas operacionais (OpEx) e uma maior transparência financeira. Com o uso do Cost Explorer, Budgets e Compute Optimizer, a empresa não apenas corta gastos supérfluos, mas também estabelece uma cultura de responsabilidade fiscal na nuvem.

## Anexos
https://docs.aws.amazon.com/pt_br/cost-management/latest/userguide/ce-what-is.html
https://docs.aws.amazon.com/pt_br/cost-management/latest/userguide/budgets-managing-costs.html
https://docs.aws.amazon.com/pt_br/compute-optimizer/latest/ug/what-is-compute-optimizer.html

Assinatura do ResponsÃ¡vel pelo Projeto:

[Lucas]