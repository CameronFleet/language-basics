package main

import (
	"fmt"
	"time"
)

func worker(done chan bool) {
	fmt.Print("working...")
	time.Sleep(time.Second)
	fmt.Println("done")

	done <- true
}

// can specify channel direction!
func ping(pings chan<- string, msg string) {
	pings <- msg
}

func pong(pings <-chan string, pongs chan<- string) {
	msg := <-pings
	pongs <- msg
}

func main() {
	messages := make(chan string)

	// sends to a channel using  messages <-
	go func() { messages <- "ping" }()

	// <- messages; recieves from channel
	msg := <-messages
	fmt.Println(msg)

	// send and receive block until both sender and receiver are ready

	// Channel buffering; default is unbuffered, meaning only accept
	// sends once there is a corresponding recieve
	messages = make(chan string, 2)
	messages <- "buffered"
	messages <- "channel"
	fmt.Println(<-messages)
	fmt.Println(<-messages)

	// Channel Synchronizaiton
	done := make(chan bool, 1)
	go worker(done)
	<-done

	// Channel Directions
	pings := make(chan string, 1)
	pongs := make(chan string, 1)
	ping(pings, "passed message")
	pong(pings, pongs)
	fmt.Println(<-pongs)
}
