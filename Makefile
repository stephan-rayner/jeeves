dev: down
	docker-compose up --build
build:
	docker-compose build
up:
	docker-compose up -d
down:
	docker-compose down