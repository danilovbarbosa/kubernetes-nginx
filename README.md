# Projeto kubernetes-nginx

Projeto kubernetes para servidor nginx

## Execução

- Docker-compose:

```sh
docker-compose up
```

## Comandos para possíveis configurações

- Adicione o bash e o nano:

```sh
docker-compose exec nginx apk add bash
docker-compose exec nginx apk add nano
```

- Execute o bash:

```sh
docker-compose exec nginx bash
```
