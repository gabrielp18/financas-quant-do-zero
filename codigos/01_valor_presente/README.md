<!-- T2.02 · README do episódio, escrito à mão. O notebook e os dados vêm de motor/repo.py; a nota técnica, de reel-ve-6/nota.md. -->

<img align="right" src="img/abertura.gif" width="260" alt="Abertura do vídeo: os 100 dólares do ano 10 descontados ano a ano até 61,39 hoje">

# T2.02 · Valor presente

**Por que \$100 daqui a 10 anos valem só \$61,39 hoje?**

Temporada 2 · *Juros e renda fixa* · episódio 2 de 12

[![Notebook](https://img.shields.io/badge/notebook-executado-1B2A4A?logo=jupyter&logoColor=white)](valor-presente.ipynb)
[![Nota técnica](https://img.shields.io/badge/nota_t%C3%A9cnica-PDF_14_p%C3%A1ginas-1E56B8)](valor-presente_nota_tecnica.pdf)
[![Tesouro](https://img.shields.io/badge/Tesouro_Prefixado-3.757%2F3.757_ao_centavo-1B7A4A)](#-o-teste-que-ninguém-pediu)
[![Python](https://img.shields.io/badge/Python-3.12%2B-1E56B8?logo=python&logoColor=white)](#-como-rodar)

Um dólar hoje vale mais que um dólar daqui a 10 anos, porque ele já pode render juros. **Descontar põe um número nisso.** Este é o episódio que segura todos os outros da temporada: duration, convexidade, curva de juros, carry… tudo começa dividindo por $(1+r)^n$.

**[📓 Abrir o notebook](valor-presente.ipynb)** · **[📄 Ler a nota técnica](valor-presente_nota_tecnica.pdf)** · **[🎬 Ver no Instagram](https://instagram.com/gabrielp.pires)** · **[🗺️ Todos os episódios](https://github.com/gabrielp18/financas-quant-do-zero#-os-episódios)**

<br clear="right">

## ⚡ O episódio em 30 segundos

Coloque \$100 no banco a 5 % ao ano. Depois de um ano, \$105; depois de dez, \$162,89 (com juros simples seriam \$150; os \$12,89 de diferença são juros sobre juros). Agora rode o filme ao contrário: quanto valem hoje \$100 que só chegam daqui a 10 anos? Divida por 1,05 dez vezes.

| A taxa | \$100 daqui a 10 anos valem hoje |
|---|---|
| 2 % ao ano | \$82,03 |
| 5 % ao ano | **\$61,39** |
| 10 % ao ano | \$38,55 |
| Selic de 13,75 % | R\$ 27,57 |

**A taxa muda tudo.** À Selic de hoje, a taxa come mais de 70 % do valor.

## 🐍 O código da tela

As 10 linhas que aparecem digitadas no vídeo. O notebook começa exatamente por elas.

```python
import numpy as np
taxa = 0.05                         # 5 % ao ano
anos = np.arange(11)                # ano 0 a 10
dinheiro = 100 * (1 + taxa) ** anos
print(dinheiro[[1, 10]].round(2)) # 105 e 162.89
futuro = 100                        # pago no ano 10
hoje = futuro / (1 + taxa) ** 10
print(round(hoje, 2))              # 61.39 hoje
for r in [0.02, 0.05, 0.10]:
    print(r, round(100 / (1 + r) ** 10, 2))
```

```text
[105.   162.89]
61.39
0.02 82.03
0.05 61.39
0.1 38.55
```

## 🎯 O teste que ninguém pediu

O vídeo usa anos inteiros. O Tesouro Direto usa dias úteis. A pergunta: a fórmula do vídeo, na convenção brasileira, reproduz o preço **oficial** do Tesouro Prefixado?

$$
PU = \frac{1.000}{(1 + \text{taxa})^{du/252}}
$$

Reproduz. **Todos os 3.757 preços de compra de 02/01/2024 a 09/10/2026, ao centavo.** Mas só se você acertar quatro detalhes de mesa:

1. 📅 **Calendário da ANBIMA:** carnaval, Corpus Christi e, desde 2024, 20 de novembro.
2. 🏦 **Liquidação:** os dias úteis contam do dia útil **seguinte** à compra, e o Tesouro não liquida em 24/12 nem em 31/12.
3. 🎆 **A exceção:** o título que vence em 1º de janeiro, cotado em 30/12, liquida no próprio 31/12. Senão ele venceria antes de ser pago.
4. ✂️ **Truncamento:** o PU é truncado em duas casas, não arredondado.

Esqueça uma regra e veja o que acontece:

| Regra esquecida | Preços que deixam de bater (de 3.757) |
|---|---|
| Contar os dias úteis da data da compra | **todos** |
| Arredondar em vez de truncar | 1.863 |
| Liquidar em 24/12 e 31/12 | 20 |

> Se o seu PU deu um centavo a mais, você arredondou. O Tesouro trunca.

## 🗺️ O que tem no notebook

| Seção | O que você leva |
|:-:|---|
| 0 | O código da tela (`vp.py`), linha por linha |
| 1 | Juros compostos: \$105 em um ano, \$162,89 em dez |
| 2 | De onde vêm os \$12,89 de juros sobre juros: o binômio de Newton |
| 3 | Rodar ao contrário: descontar e conferir |
| 4 | A taxa muda tudo, e a sensibilidade que vira *duration* |
| 5 | Quanto tempo para dobrar: a regra de 72 (e por que 72) |
| 6 | Mesma taxa, quatro respostas: anual, mensal, contínua e simples |
| 7 | 🇧🇷 Dias úteis e o preço oficial do Tesouro Prefixado |
| 8 | 🏦 **Mesa:** a curva do DI como fator de desconto |
| 9 | 🛒 **Investidor:** à vista com desconto ou 10× "sem juros"? |
| 10 | Na teoria, o preço de tudo: perpetuidade e Gordon |
| 11 | O que o valor presente não vê + exercícios |

## 📐 As oito equações

As mesmas no notebook e na nota técnica. A nota continua a numeração até a (18), com as demonstrações.

| | Equação | O que ela diz |
|:-:|---|---|
| (1) | $VF = VP\,(1+r)^{n}$ | juros compostos |
| (2) | $(1+r)^n = 1 + nr + \binom{n}{2}r^2 + \cdots$ | juros simples + juros sobre juros |
| (3) | $VP = VF/(1+r)^{n}$ | descontar |
| (4) | $dVP/dr = -\frac{n}{1+r}\,VP$ | quanto mais longe o dinheiro, mais ele treme com a taxa |
| (5) | $n_{\times 2} = \ln 2/\ln(1+r) \approx 72/(100\,r)$ | tempo para dobrar |
| (6) | $PU = 1.000/(1+\text{taxa})^{du/252}$ | a convenção brasileira |
| (7) | $VP = \sum_j CF_j\,\delta_j$ | vários fluxos, uma curva |
| (8) | $C/r$ e $C/(r-g)$ | perpetuidade e Gordon |

## 💸 Dois usos que valem dinheiro

**🏦 Na mesa.** Uma empresa tem R\$ 1 milhão a receber em jan/27, jan/28 e jan/29. Pela curva do DI de 09/10/2026, os recebíveis valem **R\$ 2.614.267,89** hoje. Descontados à Selic, R\$ 2.579.485,32. A diferença, R\$ 34.782,58, é o preço de ignorar que a curva embute cortes de juros.

**🛒 No caixa da loja.** R\$ 1.000 à vista ou 10× de R\$ 100 "sem juros"? Com o dinheiro no CDI, as parcelas valem **R\$ 943,48** hoje. Então:

| Seu dinheiro fica em… | Desconto à vista que empata |
|---|---|
| 100 % do CDI | 5,7 % |
| 80 % do CDI (≈ depois do IR) | 4,6 % |
| Poupança | 3,0 % |

Desconto maior que isso? Pague à vista. Menor? Parcele e deixe o dinheiro rendendo. **"Sem juros" quer dizer que os juros estão no preço.**

## 📄 A nota técnica

14 páginas em A4 com nove proposições demonstradas. Três que costumam surpreender:

- 🐢 **Para frações de período, juros simples rendem mais que compostos.** Meio ano a 5 %: 2,50 % contra 2,47 %.
- 🎯 **A regra de 72 só é exata a 7,85 % ao ano.** Abaixo disso ela exagera o prazo; acima, encurta. A regra "69,3 + 0,35" acerta em qualquer taxa usual.
- 📈 **Numa ação de Gordon (r = 10 %, g = 3 %), os 10 primeiros anos de dividendos valem só 48 % do preço.** O resto vem de longe, e por isso ações tremem tanto com os juros.

**[📄 Baixar a nota técnica (PDF)](valor-presente_nota_tecnica.pdf)**

## 🧩 Teste você mesmo

<details>
<summary><b>1.</b> Quanto valem hoje R&#36; 1.000 recebidos daqui a 3 anos, a 12 % ao ano? E a 8 %?</summary>
<br>
R&#36; 711,78 e R&#36; 793,83: alta de 11,53 %. A sensibilidade (4) previa 10,71 %; a diferença é a convexidade, que favorece quem ganha com a queda da taxa.
</details>

<details>
<summary><b>2.</b> Em quantos anos um capital dobra a 9 % ao ano?</summary>
<br>
Regra de 72: 8 anos. Conta exata: ln 2 / ln 1,09 = 8,04 anos.
</details>

<details>
<summary><b>3.</b> Um Tesouro Prefixado tem 504 dias úteis até o vencimento e taxa de 12,5 %. Qual o PU?</summary>
<br>
504/252 = 2 anos, e 1.000/1,125² = 790,123…, truncado em R&#36; 790,12.
</details>

<details>
<summary><b>4.</b> Uma perpetuidade paga R&#36; 10 por ano, para sempre. Quanto vale a 8 % e a 10 %?</summary>
<br>
10/0,08 = R&#36; 125 e 10/0,10 = R&#36; 100. Dois pontos a mais na taxa tiram 20 % do preço.
</details>

## 🚀 Como rodar

Na sua máquina, da raiz do repositório:

```bash
pip install -r requirements.txt
jupyter lab temporada-2-juros-e-renda-fixa/02-valor-presente/valor-presente.ipynb
```

No Google Colab, rode isto numa célula antes (o notebook lê os dados da pasta `dados_td/`):

```python
!git clone -q https://github.com/gabrielp18/financas-quant-do-zero.git
%cd financas-quant-do-zero/temporada-2-juros-e-renda-fixa/02-valor-presente
```

## 📂 Nesta pasta

| Arquivo | O que é |
|---|---|
| [`valor-presente.ipynb`](valor-presente.ipynb) | o notebook, executado, com 7 gráficos e um `assert` para cada número do vídeo |
| [`valor-presente_nota_tecnica.pdf`](valor-presente_nota_tecnica.pdf) | a nota técnica: demonstrações, tabelas, exercícios e referências |
| [`dados_td/tesouro_prefixado_2024_2026.csv`](dados_td/tesouro_prefixado_2024_2026.csv) | 3.757 taxas e preços de compra do Tesouro Prefixado, de 02/01/2024 a 09/10/2026 ([Tesouro Transparente](https://www.tesourotransparente.gov.br/)) |
| `img/abertura.gif` | a abertura do vídeo, aí em cima |

Os ajustes do DI futuro de 09/10/2026 (seção 8) estão digitados dentro do notebook.

## 🧭 Navegação

| ← Anterior | ↑ | Próximo → |
|---|:-:|---:|
| T2.01 · *O CDI de cada dia* (em breve) | [Todos os episódios](https://github.com/gabrielp18/financas-quant-do-zero#-o-mapa-da-série) | T2.03 · *O título "seguro" que oscila* (em breve) |

Com código, o próximo é o **[T2.04 · Duration](https://github.com/gabrielp18/financas-quant-do-zero/tree/main/temporada-2-juros-e-renda-fixa/04-duration)**, que pega a equação (4) daqui e faz dela o número mais importante da renda fixa.

---

<sub>O vídeo é inspirado na Parte 6 de *Quant Finance from Scratch*, de [@quantfinancetogo](https://instagram.com/quantfinancetogo). Números de exemplo nas seções 0 a 6 do notebook; dados reais do Tesouro Transparente e do DI de 09/10/2026 nas seções 7 e 8. Só educação, não é recomendação de investimento. Feito por [Gabriel Pires](https://gabrielppires.com) · [@gabrielp.pires](https://instagram.com/gabrielp.pires)</sub>
