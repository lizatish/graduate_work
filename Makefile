.PHONY: gen_reqs down build up


DOCKER_COMPOSE_CMD = docker-compose

gen_reqs:
	poetry lock
	poetry install
	poetry export -f requirements.txt --output requirements.txt --without-hashes --dev

down:
	${DOCKER_COMPOSE_CMD} down -v --remove-orphans

build:
	DOCKER_BUILDKIT=1 ${DOCKER_COMPOSE_CMD} build

up:
	${DOCKER_COMPOSE_CMD} up

