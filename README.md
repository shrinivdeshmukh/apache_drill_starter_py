# Apache drill setup with example jupyter notebook

# Step 1
## Option 1: Use `docker-compose` to start all the services

```
docker-compose up -d
```
Wait until all services are started.

## Option 2: Use `Makefile` to start all the services

```
make start
```

# Step 2
## Browse the Apache drill and HDFS UI

* Browse through http://localhost:8047, http://localhost:8048, http://localhost:8049 to access UI for the 3 drill instances.

* Browse through http://localhost:50070 to access HDFS UI.

# Step 3
## Test the code/notebook

* Go to any one of the drill instances' web UI.
* Click on the `options` tab in the top right corner.
* Search for `planner.parser.quoting_identifiers` option in the search bar on the UI
* Update the backtick ` ` ` to  double quote "
* Go to `Storage` tab in the top left menu bar
* Click on `update` button for the `dfs` storage
* Change the URL from `file:///` to `hdfs://hdfs:8020`
* In the `formats`-> `csv` section, after `"type": "text`, add the line `"extractHeader": true,`
* Click `Update` button at the bottom.
* Open the jupyter notebook on http://localhost:8899. You can get the token for logging in to jupyter by issuing:<br />
`docker-compose logs -f jupyter` command.
* Execute all the cells.
