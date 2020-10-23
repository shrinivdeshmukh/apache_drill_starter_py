build:
	docker-compose build ${SERVICE}

start:
	docker-compose up -d

stop:
	docker-compose down

clean:
	docker-compose down -v

logs:
	docker-compose logs -f ${SERVICE}

token: 
	docker-compose logs -f jupyter

hdfs:
	docker-compose up --build -d hdfs