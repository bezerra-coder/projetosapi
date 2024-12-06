# Cotação de moedas com API
O projeto, basicamente, envolve um script em Python e consulta a cotação de moedas em tempo real utilizando uma API [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas)

---------------
## Descrição 📝 
Este script permite que o usuário:
1. Informe uma moeda de origem (exemplo: BRL, USD, EUR, CYN etc).
2. Veja as cotações das principais moedas (USD, EUR, GBP, etc.) em relação à moeda de origem selecionada.
3. Receba mensagens de erro em caso de problemas na requisição da API.

Ele é útil para pessoas que precisam de informações rápidas e confiáveis sobre taxas de câmbio em suas aplicações ou estudos.

---------------
## Pré-requisitos 👮

- Qualquer versão moderna do Python.
- Biblioteca requests: para instalar, rode o comando abaixo no terminal:
  
  Bash em Linux 🐧 e Windows 🪟 :
  
  pip install requests

  Bash em MacOS 🍎 :
  
  pip3 install requests

  ---------------
  ## Como Executar 🛠 :
    
  1. Bash:
  
  git clone https://github.com/bezerra-coder/projetosapi.git
  
  cd APIcotacao

  2. Execute o script: 
  python3 APIcotacao.py


  3. Informe a moeda de origem, seja em maiúsculo ou minúsculo, usando o formato de três letras como solicitado.
     
  ---------------
  ## Script 📜 :

  1. Entrada: informe uma moeda. A entrada dela será convertida em letras maiúsculas com upper(), uma vez que a API da AwesomeAPI é sensível a letras maiúsculas e minúsculas, ela também exige que a sigla das moedas sejam todas maiúsculas.
 
  2. Iteração pelas moedas: verifica a cotação da moeda informada pelo usuário na entrada em relação a uma lista de moedas principais

  3. Requisição à API: a utilização do formato https://economia.awesomeapi.com.br/json/last/{moeda1}-{moeda2} faz com que a moeda1, informada pelo usuário, seja convertida em todas moedas presentes na lista de principais moedas.
 
  4. Erros: Verifica se houve sucesso ou não pela requisição em (raise_for_status()). Dessa forma, é exibido uma mensagem informando caso a API não retorne a cotação ou haja problemas nos dados.

  5. Exibição: Oferece o resutado da cotação ou mensagens de erro.
 
  ---------------
  ## Exemplo de saída 📊:

  Ao executar o script como informado, se oferecer BRL como entrada, verá algo como:

  A cotação de BRL para USD é ...
  
  A cotação de BRL para EUR é ...
  
  A cotação de BRL para GBP é ...
  
  A cotação de BRL para JPY é ...
  
  A cotação de BRL para AUD é ...
  
  A cotação de BRL para CAD é ...
  
  A cotação de BRL para CNY é ...

  ## Personalização 🎨:

  É possível ajustar a lista de moedas para adiconar ou remover pares, para isso, é preciso editar a variável principais_moedas

  ## Tratamento de erros 🛡️:

  Problemas de conexão: se a API não estiver acessível, exibe uma mensagem amigável.
  Respostas inesperadas: caso o formato da resposta não contenha o par de moedas esperado, uma mensagem é exibida informando o problema.

  ## Melhorias:

  Seria muito interessante aprofundar e montar um projeto com quem tenha conhecimentos sobre front-end para que faça uma interface gráfica.



