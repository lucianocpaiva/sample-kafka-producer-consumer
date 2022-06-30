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
		"auto.offset.reset": "beginning",
	})

	if err != nil {
		panic(err)
	}

	topic := os.Getenv("TOPIC_ORDERS")

	err = c.SubscribeTopics([]string{topic}, nil)

	if err == nil {
		fmt.Printf("Subscribed to topic: %s\n", topic)
	} else {
		fmt.Printf("Error subscribing to topic: %s %s\n", topic, err)
	}

	fmt.Printf("\nWaiting...\n")

	for {
		msg, err := c.ReadMessage(-1)

		if err == nil {
			fmt.Printf("\nMessage on %s: %s\n", msg.TopicPartition, string(msg.Value))
		} else {
			fmt.Printf("Consumer error: %v (%v)\n", err, msg)
		}
	}

	c.Close()
}
