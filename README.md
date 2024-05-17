# Projeto de Balanceador de Carga com Docker e Nginx

Este projeto é uma configuração de exemplo para um balanceador de carga usando Docker e Nginx, com três servidores de backend Flask. O objetivo é demonstrar como configurar um ambiente de balanceamento de carga simples usando contêineres Docker.

## Estrutura do Projeto

O projeto é dividido em várias partes:

1. **Nginx**: O contêiner do Nginx atua como o balanceador de carga, distribuindo as solicitações entre os servidores de backend.
2. **Servidores Flask**: Três servidores Flask de backend, cada um representando uma instância do serviço que está sendo balanceado.

## Configuração

A configuração do projeto é feita usando Docker Compose. O arquivo `docker-compose.yml` define os serviços e suas configurações.

### Nginx

O contêiner do Nginx é configurado para encaminhar solicitações para os servidores de backend Flask. O arquivo de configuração do Nginx está localizado em `./Conf/nginx.conf`.

### Servidores Flask

Cada servidor Flask é configurado para responder a solicitações em uma porta específica e é construído a partir de um Dockerfile localizado em seu diretório respectivo (`./Server1`, `./Server2`, `./Server3`).

## Executando o Projeto

Para executar o projeto, siga estas etapas:

1. Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.

2. Clone este repositório em sua máquina local:

   ```
   git clone https://github.com/VORP2830/Nginx
   ```

3. Navegue até o diretório do projeto:

   ```
   cd Nginx
   ```

4. Execute o comando abaixo para iniciar os contêineres:

   ```
   docker-compose up --build
   ```

   Isso irá criar e iniciar os contêineres do Nginx e dos servidores Flask.

5. Após a execução bem-sucedida, você pode acessar a aplicação em seu navegador:

   - Nginx (Balanceador de Carga): [http://localhost:90/server/](http://localhost:90/server/)
   - Servidor 1: [http://localhost:90/server1/](http://localhost:90/server1/)
   - Servidor 2: [http://localhost:90/server2/](http://localhost:90/server2/)
   - Servidor 3: [http://localhost:90/server3/](http://localhost:90/server3/)

## Notas Adicionais

- Os logs do Nginx são salvos em `./log` no host.
