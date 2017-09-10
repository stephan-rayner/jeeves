dev: down
	docker-compose up --build
build:
	docker-compose build
up:
	docker-compose up -d
down:
	docker-compose down
prod: down
	docker-compose -f docker-compose.prod.yml build; docker-compose -f docker-compose.prod.yml up -d
