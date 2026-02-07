package main

import (
	"fmt"

	"github.com/spod/aoc/2022/aoc"
)

func main() {
	const day = "01"
	const test_input_raw = `
	1000
	2000
	3000
	
	4000
	
	5000
	6000
	
	7000
	8000
	9000
	
	10000
	`
	test_input, input := aoc.GetInputs(day, test_input_raw)

	fmt.Printf("Day %s\n", day)
	fmt.Printf("test partA: %d\n", partA(test_input))
	fmt.Printf("partA: %d\n", partA(input))
	fmt.Printf("test partB: %d\n", partB(test_input))
	fmt.Printf("partB: %d\n", partB(input))
}

func partA(input []string) int {
	return 42
}

func partB(input []string) int {
	return 69
}
