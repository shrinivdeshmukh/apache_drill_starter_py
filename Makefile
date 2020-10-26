build:
	docker-compose build ${service}

start:
	docker-compose up -d

stop:
	docker-compose down

clean:
	docker-compose down -v

logs:
	docker-compose logs -f ${service}

token: 
	docker-compose logs -f jupyter

hdfs:
	docker-compose up --build -d hdfs