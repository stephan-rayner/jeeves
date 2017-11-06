
build:
	docker build -t cheesemanor/jeeves .

run:
	docker run -d --name Jeeves cheesemanor/jeeves

clean:
	docker rm Jeeves
	docker rmi cheesemanor/jeeves

kill:
	docker kill Jeeves

reload: kill clean build run