package main

import (
	"fmt"

	"github.com/spod/aoc/2022/aoc"
)

func main() {
	const day = "02"
	const test_input_raw = `
	A Y
	B X
	C Z
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
