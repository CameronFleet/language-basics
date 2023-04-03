package main

import "fmt"

func zeroval(ival int) {
	ival = 0
}

func zeroptr(iptr *int) {
	*iptr = 0
}

func printReference(ref *string) {
	fmt.Println(ref)
}

type Animal interface {
	speak()
}

type Dog struct {
	name string
}

func (d *Dog) speak() {
	fmt.Println("My name is: ", *&d.name)
}

func (d *Dog) transformDoesNotWork() {
	// d is a passing the reference by value, does not pass the pointer on the stack
	// instead creates a copy
	d = new(Dog)
	d.name = "Bob"
}

func (d *Dog) transformDoesWork() {
	*d = Dog{"Bob"}
}

func main() {
	i := 1
	fmt.Println("initial:", i)

	zeroval(i)
	fmt.Println("zeroval:", i)

	zeroptr(&i)
	fmt.Println("zeroptr:", i)

	fmt.Println("pointer:", &i)

	value := "value"
	fmt.Println("Pointer ref in main: ", &value)
	printReference(&value)

	dog := new(Dog)
	dog.name = "Jeff"
	dog.speak()
	dog.transformDoesNotWork()
	dog.speak()
	dog.transformDoesWork()
	dog.speak()
}
