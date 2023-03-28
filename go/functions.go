package main

import "fmt"

func plus(a int, b int) int {
	return a + b
}

func plusPlus(a, b, c int) int {
	return a + b + c
}

// multiple return values
func vals() (int, int) {
	return 8, 9
}

// variadic
func sum(nums ...int) int {
	total := 0
	for _, num := range nums {
		total += num
	}
	return total
}

// closures
func intSeq() func() int {
	i := 0
	return func() int {
		i++
		return i
	}
}

// recursion
func fact(n int) int {
	if n == 0 {
		return 1
	}
	return n * fact(n-1)
}

func main() {
	res := plus(1, 2)
	fmt.Println("1+2 =", res)

	res = plusPlus(1, 2, 3)
	fmt.Println("1+2+3 =", res)

	a, b := vals()
	fmt.Println("a =", a, "b =", b)

	_, c := vals()
	fmt.Println("c =", c)

	fmt.Println("sum(1,2,3)", sum(1, 2, 3))
	fmt.Println("sum([]int{1, 3, 6}...)", sum([]int{1, 3, 6}...))

	nextInt := intSeq()

	fmt.Println(nextInt())
	fmt.Println(nextInt())
	fmt.Println(nextInt())

	nextInt2 := intSeq()
	fmt.Println(nextInt2())

	fmt.Println(fact(7))
}
