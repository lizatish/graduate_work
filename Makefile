.PHONY: gen_reqs down build up


DOCKER_COMPOSE_CMD = docker-compose

gen_reqs:
	poetry lock
	poetry install
	poetry export -f requirements.txt --output requirements.txt --without-hashes --dev

down:
	${DOCKER_COMPOSE_CMD} down -v --remove-orphans

build:
	DOCKER_BUILDKIT=1 ${DOCKER_COMPOSE_CMD} build --build-arg DEPLOY_TOKEN_NAME=${DEPLOY_TOKEN_NAME} --build-arg DEPLOY_TOKEN=${DEPLOY_TOKEN}

up:
	${DOCKER_COMPOSE_CMD} up

