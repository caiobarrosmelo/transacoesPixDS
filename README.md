# transacoesPixDS
Estudo sobre as estatísticas de transações PIX da API do Banco Central (BCB) acerca do volume financeiro e da quantidade de transações PIX liquidadas mensalmente, incluindo informações sobre o Sistema de Pagamentos Instantâneos (SPI) e transações fora do SPI.

# **Estatísticas de transações Pix**

Quantidade e volume financeiro de transações Pix liquidadas mensalmente. Não inclui Pix liquidados nos livros do participante, isto é, transações não enviadas para liquidação no SPI.

## **Parâmetros**

| Nome | Tipo | Título | Descrição |
| --- | --- | --- | --- |
| Database | texto | Data-base | Data-base de referência no formato AAAAMM |
| $format | texto | $format | Tipo de conteúdo que será retornado |
| $select | texto | $select | Propriedades que serão retornadas |
| $filter | texto | $filter | Filtro de seleção de entidades. e.g. Nome eq 'João'. [Clique aqui](https://olinda.bcb.gov.br/olinda/servico/ajuda) para as opções de operadores e funções. |
| $orderby | texto | $orderby | Propriedades para ordenação das entidades. e.g. Nome asc, Idade desc |
| $skip | inteiro | $skip | Índice (maior ou igual a zero) da primeira entidade que será retornada |
| $top | inteiro | $top | Número máximo (maior que zero) de entidades que serão retornadas |

## **Resultado**
| Nome | Tipo | Título | Descrição |
| --- | --- | --- | --- |
| AnoMes | inteiro | Data-base - ano/mês | Data-base - ano/mês |
| PAG_PFPJ | texto | Tipo de Pessoa do Pagador | PF= Pessoa Física PJ= Pessoa Jurídica |
| REC_PFPJ | texto | Tipo de Pessoa do Recebedor | PF= Pessoa Física PJ= Pessoa Jurídica |
| PAG_REGIAO | texto | Região do Pagador | Região do domicílio do usuário pagador. |
| REC_REGIAO | texto | Região do Recebedor | Região do domicílio do usuário recebedor. |
| PAG_IDADE | texto | Idade do Pagador | Idade em anos do usuário pagador |
| REC_IDADE | texto | Idade do Recebedor | Idade em anos do usuário recebedor |
| FORMAINICIACAO | texto | Forma de iniciação da transação | Forma de iniciação das transações: iniciador com todas as informações do recebedor (INIC), QR Code estático(QRES), QR Code dinâmico (QRDN), inserção manual (MANU) e chave Pix (DICT). |
| NATUREZA | texto | Natureza da transação | P2P - Pessoa para Pessoa, B2B - Empresa para Empresa, P2B - Pessoa para Empresa, B2P - Empresa para Pessoa, P2G - Pessoa para Governo, B2G - Empresa para Governo |
| FINALIDADE | texto | Finalidade da Transação | Finalidade da transação Pix: transferência, saque ou troco. |
| VALOR | decimal | Valor das Transações Pix | Volume financeiro de transações Pix liquidadas mensalmente |
| QUANTIDADE | decimal | Quantidade Total de Transações Pix | Quantidade de transações Pix liquidadas mensalmente |

## **Links**
- [BCB - Transação Pix](https://dadosabertos.bcb.gov.br/dataset/pix/resource/9eb0f16d-4a38-4936-be2a-6c0dd18f87f7?inner_span=True)
- [BCB - Estatísticas Pix](https://dadosabertos.bcb.gov.br/dataset/pix)

## **Grupo**
Airon Valentim<br />
Caio Barros<br />
Edmundo Duarte<br />
Filipe Macedo <br />
Gustavo Carvalho<br />


