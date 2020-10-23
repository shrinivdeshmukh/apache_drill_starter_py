# Apache drill setup with example jupyter notebook

## Option 1: Start all the services

```
docker-compose up -d
```
Wait until all services are started.

## Option 2: Use `Makefile` to start all the services

```
make start
```

### Build services

* <b> Build a specific service: </b> <br />
      ```SERVICE=app make build``` (replace `app` by your desired service name) <br /><br />
* <b> Build all services: </b> <br /> `make build`

## Browse the Apache drill and HDFS UI

* Browse through http://localhost:8047, http://localhost:8048, http://localhost:8049 to access UI for the 3 drill instances.

* Browse through http://localhost:50070 to access HDFS UI.

## Test the pyspark code

* Go to any one of the drill instances' web UI.
* Click on the `options` tab in the top right corner.
* Search for `planner.parser.quoting_identifiers` option in the search bar on the UI
* Update the backtick ` ` ` to  double quote "
* Go to `Storage` tab in the top left menu bar
* Click on `update` button for the `dfs` storage
* Change the URL from `file:///` to `hdfs://hdfs:8020`
* In the `formats`-> `csv` section, add the line `"extractHeader": true,` after `"type": "text`
* upload any csv to `/` folder in `HDFS`
* Open the jupyter notebook on http://localhost:8889. You can get the token for logging in to jupyter by issuing:
`docker-compose logs -f jupyter` command.
* Execute all the cells.
