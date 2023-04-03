package main

import "fmt"

type Animal struct {
	genus string
}

type Person struct {
	Animal
	name string
	age  int
}

func newPerson(name string) *Person {
	p := Person{Animal: Animal{"Homo"}, name: name}
	p.age = 42
	return &p
}

func main() {
	fmt.Println(Person{Animal{"Homo"}, "Bob", 20})
	fmt.Println(Person{name: "Alice", age: 30})
	fmt.Println(Person{name: "Fred"})
	fmt.Println(&Person{name: "Ann", age: 40})

	fmt.Println(newPerson("John"))

	sarah := newPerson("Sarah")
	fmt.Println(sarah.age)
	otherSarah := sarah
	otherSarah.age = 100
	fmt.Println(sarah.age)

	a := Person{Animal{"B"}, "A", 10}
	b := a
	b.age = 8
	fmt.Println(a.age)
	fmt.Println(b.age)
}
