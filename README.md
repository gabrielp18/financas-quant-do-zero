<!-- Episódio novo: python motor/repo.py (da pasta fqz) copia o notebook e os dados; aqui, uma linha na tabela da
     temporada, um quadrado 🟦 no mapa, o número no selo "episódios com código" e no "Já tem código para N". -->

<div align="center">

<img src="assets/logo.svg" width="120" alt="Logo: um zero cortado por um passeio aleatório">

# Finanças Quantitativas do Zero

Os notebooks da série do Instagram [@gabrielp.pires](https://instagram.com/gabrielp.piress): cada vídeo vira código que roda, com dado de verdade.

[![Python](https://img.shields.io/badge/Python-3.12%2B-1E56B8?logo=python&logoColor=white)](#-comece-em-30-segundos)
[![Jupyter](https://img.shields.io/badge/Jupyter-notebooks_executados-1B2A4A?logo=jupyter&logoColor=white)](#-os-episódios)
[![Instagram](https://img.shields.io/badge/@gabrielp.piress-Instagram-E4405F?logo=instagram&logoColor=white)](https://instagram.com/gabrielp.piress)
[![Site](https://img.shields.io/badge/gabrielppires.com-site-1E56B8)](https://gabrielppires.com)
[![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-55617A)](LICENSE)
![Não é recomendação](https://img.shields.io/badge/n%C3%A3o_%C3%A9-recomenda%C3%A7%C3%A3o_financeira-B42318)

</div>

---

## 🎬 O que é isto

**Finanças Quantitativas do Zero** é uma série diária de vídeos curtos. Cada episódio pega **um** conceito do mercado,
faz **duas perguntas** sobre ele e responde com matemática na tela e código digitado linha a linha. Sem enrolação e
sem mistério: se tem número no vídeo, tem código que chega nele.

Este repositório guarda o código. Cada episódio traz um notebook executado, que começa pelo **código da tela** (o mesmo
do vídeo, de 12 a 16 linhas) e depois vai fundo: demonstração, tabela, gráfico, um exemplo de mesa, um exemplo do
investidor e, quando cabe, a **replicação de um artigo clássico** com dados do Brasil.

## 📚 Os episódios

| # | Episódio | A pergunta | O número que fica | 📜 Replica ou testa | Código |
|:-:|---|---|---|---|:-:|
| 01 | [**O passeio aleatório**](codigos/01_passeio_aleatorio) | Um gráfico de ações é só cara ou coroa? | com a vantagem do cassino (+2,7¢ por lance), a deriva só passa o ruído depois de **1.368** lances | Lo & MacKinlay (1988): o Ibovespa de 1995 a 2026 não rejeita o passeio aleatório | [📓](codigos/01_passeio_aleatorio/passeio-aleatorio.ipynb) [📄](codigos/01_passeio_aleatorio/passeio-aleatorio_nota_tecnica.pdf) |
| 02 | [**A curva de sino**](codigos/02_curva_normal) | Por que passos aleatórios sempre formam o mesmo sino? | Ibovespa: **113** dias além de 3 desvios em 31 anos, onde o sino previa **21** | Fama (1965) e Mandelbrot (1963) com o Ibovespa; VaR de 99 % com backtest de Kupiec | [📓](codigos/02_curva_normal/curva-normal.ipynb) [📄](codigos/02_curva_normal/curva-normal_nota_tecnica.pdf) |
| 03 | [**Retornos**](codigos/03_retornos_log) | Por que cair 50 % pede subir 100 %? | o Ibovespa "rende" **1,34 %** ao mês na média e **1,01 %** de verdade | Hudson & Gregoriou (2015) em 38 ações da B3: 34 mudam de posição no ranking | [📓](codigos/03_retornos_log/retornos-log.ipynb) [📄](codigos/03_retornos_log/retornos-log_nota_tecnica.pdf) |
| 04 | [**Volatilidade**](codigos/04_volatilidade) | Mesma média de 8 % ao ano: por que uma perde dinheiro em **2,7 %** dos anos e a outra em **46,8 %**? | **3,9 %** contra **31,6 %** de vol ao ano; o Ibovespa tem **31,1 %** | RiskMetrics (1996) no Ibovespa: o melhor λ é 0,935, colado no 0,94 | [📓](codigos/04_volatilidade/volatilidade.ipynb) [📄](codigos/04_volatilidade/volatilidade_nota_tecnica.pdf) |
| 05 | [**O índice de Sharpe**](codigos/05_sharpe) | O dobro do retorno por oito vezes o risco é bom negócio? | **0,36** contra **0,99**; o Ibovespa sobre o CDI desde 1995: **0,10**, com intervalo de −0,25 a 0,42 | Lo (2002): o erro do Sharpe no Ibovespa, em 38 ações e em 155 fundos da CVM | [📓](codigos/05_sharpe/sharpe.ipynb) [📄](codigos/05_sharpe/sharpe_nota_tecnica.pdf) |
| 06 | [**Correlação**](codigos/06_correlacao) | Por que a mesma carteira meio a meio oscila 19,0 %, 14,1 % ou 10,0 %? | correlação +0,80: **19,0 %**; zero: **14,1 %**; −0,50: **10,0 %** | Forbes & Rigobon (2002) na crise de 2020: de 0,55 para 0,83, e sem contágio | [📓](codigos/06_correlacao/correlacao.ipynb) [📄](codigos/06_correlacao/correlacao_nota_tecnica.pdf) |

Cada pasta tem o notebook executado (📓), a nota técnica em PDF (📄), os dados que o notebook lê e um README com o código da tela.

## ❓ Perguntas que sempre aparecem

<details>
<summary><b>Preciso saber programar?</b></summary>
<br>
Se você já mexeu numa planilha, consegue acompanhar. O código da tela tem de 12 a 16 linhas e cada uma aparece no
vídeo com a conta que ela faz. Comece rodando, depois mude um número e veja o que acontece.
</details>

<details>
<summary><b>Preciso saber finanças?</b></summary>
<br>
Não. Está no nome: do zero. Cada episódio retoma o anterior, então seguir a ordem da tabela ajuda.
</details>

<details>
<summary><b>Os números do notebook batem com os do vídeo?</b></summary>
<br>
Batem. Se não baterem, é bug, e eu quero saber (veja abaixo).
</details>

<details>
<summary><b>Isso é recomendação de investimento?</b></summary>
<br>
Não. É educação. Nenhum notebook diz o que comprar. Eles mostram como a conta funciona, inclusive quando ela não
funciona.
</details>

<details>
<summary><b>Achei um erro!</b></summary>
<br>
Ótimo. Abra uma <a href="https://github.com/gabrielp18/financas-quant-do-zero/issues">issue</a> dizendo o episódio e a célula. Erro de conta em público é o melhor
tipo de erro: aparece, é corrigido e todo mundo aprende junto.
</details>

## 🤝 Quer ajudar?

- ⭐ **Dê uma estrela.** Não mexe no preço de nada, mas mexe com o meu dia.
- 🐛 **Achou um número estranho?** Abra uma issue com o episódio e a célula.
- 💡 **Tem um tema que deveria virar episódio?** Sugira numa issue. Se tiver um artigo para replicar, melhor ainda.
- 📲 **Quer o vídeo antes do código?** Siga [@gabrielp.pires](https://instagram.com/gabrielp.pires). Sai um por dia.

## ⚠️ Aviso

Conteúdo educacional. Nada aqui é recomendação de investimento, oferta ou análise de valor mobiliário. Os exemplos
marcados como *ilustrativos* usam taxas inventadas, e os dados reais trazem fonte e data. Resultado passado não garante
resultado futuro, e isso vale em dobro para backtest.

## 📄 Licença e agradecimentos

O código está sob a licença [MIT](LICENSE). Os dados nas pastas `dados*/` pertencem às respectivas fontes (Tesouro
Nacional, Banco Central, CVM, FRED, Federal Reserve, Yahoo Finance) e seguem os termos de cada uma.

---

<div align="center">

<img src="assets/logo.svg" width="44" alt="">

<sub>Feito com numpy, café e muitos <code>assert</code> por <a href="https://gabrielppires.com">Gabriel Pires</a> ·
<a href="https://instagram.com/gabrielp.pires">@gabrielp.pires</a></sub>

</div>
