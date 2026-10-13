<!-- Episódio novo: python motor/repo.py (da pasta fqz) copia o notebook e os dados; aqui, uma linha na tabela da
     temporada, um quadrado 🟦 no mapa, o número no selo "episódios com código" e no "Já tem código para N". -->

<div align="center">

<img src="assets/logo.svg" width="120" alt="Logo: um zero cortado por um passeio aleatório">

# Finanças Quantitativas do Zero

**Do cassino à curva de juros, uma linha de numpy por vez.**

Os notebooks da série do Instagram [@gabrielp.pires](https://instagram.com/gabrielp.piress): cada vídeo vira código que roda, com dado de verdade.

[![Python](https://img.shields.io/badge/Python-3.12%2B-1E56B8?logo=python&logoColor=white)](#-comece-em-30-segundos)
[![Jupyter](https://img.shields.io/badge/Jupyter-notebooks_executados-1B2A4A?logo=jupyter&logoColor=white)](#-os-episódios)
[![Instagram](https://img.shields.io/badge/@gabrielp.piress-Instagram-E4405F?logo=instagram&logoColor=white)](https://instagram.com/gabrielp.piress)
[![Site](https://img.shields.io/badge/gabrielppires.com-site-1E56B8)](https://gabrielppires.com)
[![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-55617A)](LICENSE)
![Não é recomendação](https://img.shields.io/badge/n%C3%A3o_%C3%A9-recomenda%C3%A7%C3%A3o_financeira-B42318)

[O que é](#-o-que-é-isto) · [Comece](#-comece-em-30-segundos) · [Episódios](#-os-episódios) · [O mapa](#-o-mapa-da-série) · [Regras da casa](#-regras-da-casa) · [Dados](#-de-onde-vêm-os-dados) · [FAQ](#-perguntas-que-sempre-aparecem)

</div>

---

## 🎬 O que é isto

**Finanças Quantitativas do Zero** é uma série diária de vídeos curtos. Cada episódio pega **um** conceito do mercado,
faz **duas perguntas** sobre ele e responde com matemática na tela e código digitado linha a linha. Sem enrolação e
sem mistério: se tem número no vídeo, tem código que chega nele.

Este repositório guarda o código. Cada episódio traz um notebook executado, que começa pelo **código da tela** (o mesmo
do vídeo, de 11 a 14 linhas) e depois vai fundo: demonstração, tabela, gráfico, um exemplo de mesa, um exemplo do
investidor e, quando cabe, a **replicação de um artigo clássico** com dados do Brasil.

| Pedaço do episódio | Onde mora |
|---|---|
| 🎬 Reel de até 3 minutos | Instagram [@gabrielp.pires](https://instagram.com/gabrielp.piress) |
| 🖼️ Carrossel de 10 lâminas | Instagram [@gabrielp.pires](https://instagram.com/gabrielp.piress) |
| ✍️ Post com a leitura econômica | [gabrielppires.com](https://gabrielppires.com) |
| 📓 Notebook executado + os dados | **aqui** 👇 |

## 📚 Os episódios

| # | Episódio | A pergunta | O número que fica | 📜 Replica ou testa | Código |
|:-:|---|---|---|---|:-:|
| 06 | **Valor presente** | Por que um dólar hoje vale mais que um dólar daqui a 10 anos? | a 5 % ao ano, $100 daqui a 10 anos valem **$61,39** hoje; a 2 %, **$82,03**; a 10 %, só **$38,55** *(números de exemplo)* | conferência: $61,39 × 1,05¹⁰ = **$100,00** | *em breve* |

## ❓ Perguntas que sempre aparecem

<details>
<summary><b>Preciso saber programar?</b></summary>
<br>
Se você já mexeu numa planilha, consegue acompanhar. O código da tela tem de 11 a 14 linhas e cada uma aparece no
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
Nacional, Banco Central, FRED, Federal Reserve, Yahoo Finance) e seguem os termos de cada uma.

---

<div align="center">

<img src="assets/logo.svg" width="44" alt="">

<sub>Feito com numpy, café e muitos <code>assert</code> por <a href="https://gabrielppires.com">Gabriel Pires</a> ·
<a href="https://instagram.com/gabrielp.pires">@gabrielp.pires</a></sub>

</div>
