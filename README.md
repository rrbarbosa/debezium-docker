# debezium-docker

Playground for Debezium. Following the steps from the [tutorial](http://debezium.io/docs/tutorial/), wrapping it all in docker-compose and (hopefully soon) adding python-base test case.

# Steps

    # boot up containers
    docker-compose up mysql
    docker-compose up zookeeper
    docker-compose up kafka
    docker-compose up connect
    
	# create/feed topic
	curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" localhost:8083/connectors/ -d '{ "name": "inventory-connector", "config": { "connector.class": "io.debezium.connector.mysql.MySqlConnector", "tasks.max": "1", "database.hostname": "mysql", "database.port": "3306", "database.user": "debezium", "database.password": "dbz", "database.server.id": "184054", "database.server.name": "dbserver1", "database.whitelist": "inventory", "database.history.kafka.bootstrap.servers": "kafka:9092", "database.history.kafka.topic": "dbhistory.inventory" } }'

	# boot up testing cotainer
	docker-compose run test
	# ...start a flask app on localhost:5000

Every time an GET is issued, all unread messages in the topic are retrieved. The app remembers the last read message, so only updates will are in subsequent requests.
