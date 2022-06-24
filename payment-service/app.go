package main

import (
	"fmt"
	"os"
	"github.com/confluentinc/confluent-kafka-go/kafka"
)

func main() {

	c, err := kafka.NewConsumer(&kafka.ConfigMap{
		"bootstrap.servers": "kafka:9092",
		"group.id":          "group-payment",
		"auto.offset.reset": "earliest",
	})

	if err != nil {
		panic(err)
	}

	topic := os.Getenv("TOPIC_SALES")

	c.SubscribeTopics([]string{topic}, nil)

	fmt.Printf("Waiting...\n")

	for {
		msg, err := c.ReadMessage(-1)
		if err == nil {
			fmt.Printf("Message on %s: %s\n", msg.TopicPartition, string(msg.Value))
		} else {
			fmt.Printf("Consumer error: %v (%v)\n", err, msg)
		}
	}

	c.Close()
}