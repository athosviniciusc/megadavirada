# Gerador de Palpites para a Mega-Sena da Virada

Este projeto é um script em Python que gera jogos aleatórios para a Mega-Sena da Virada com base nos últimos 10 resultados conhecidos. Ele utiliza uma lógica que considera os números mais frequentes nos sorteios anteriores para aumentar a relevância dos palpites gerados.

## Funcionalidades

- Geração de palpites únicos para jogos da Mega-Sena.
- Baseado em dados estatísticos dos últimos 10 sorteios da Mega-Sena da Virada.
- Adiciona variação aleatória para evitar repetições.

## Requisitos

- Python 3.6 ou superior.

### Instalação do Python

Caso você não tenha o Python instalado, siga as etapas abaixo:

1. Acesse o site oficial do Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Baixe a versão mais recente compatível com seu sistema operacional.
3. Siga as instruções do instalador para completar a instalação.
4. Durante a instalação, marque a opção **"Add Python to PATH"** para facilitar o uso do Python no terminal.

## Como executar o script

1. Clone ou baixe este repositório para o seu computador.
   ```bash
   git clone https://github.com/seu_usuario/seu_repositorio.git
   cd seu_repositorio
   ```
2. Abra um terminal na pasta onde o arquivo está localizado.
3. Execute o script com o comando:

   ```bash
   python nome_do_arquivo.py
   ```

4. Insira o número de jogos que deseja gerar quando solicitado.

## Exemplo de Uso

Após executar o script, você verá a seguinte interação:

```bash
Bem-vindo ao Gerador de Palpites para a Mega-Sena da Virada!
Quantos jogos você deseja gerar? 3

Seus jogos gerados com base nos últimos resultados:
Jogo 1: 3, 10, 12, 21, 23, 27
Jogo 2: 24, 56, 33, 48, 21, 41
Jogo 3: 6, 21, 35, 38, 53, 57
```

