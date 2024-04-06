docker network create postgres_nw

docker run --name postgres_server -e POSTGRES_PASSWORD=start123 -d --network postgres_nw  postgres

docker run -it --rm --network postgres_nw postgres psql -h postgres_server -U postgres
