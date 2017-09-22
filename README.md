# debezium-docker
Playground for Debezium

# Stepts

    # boot up 
    docker-compose up
    # create a topic
    docker run -it --rm --link zookeeper:zookeeper debezium/kafka create-topic [-p numPartitions] [-r numReplicas] topic-name

 
