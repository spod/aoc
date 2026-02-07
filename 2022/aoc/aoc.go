package aoc

import (
	"bytes"
	"fmt"
	"os"
	"strings"
)

// shared code

// GetInputs - reads days input, takes test_input_raw string and returns string arrays split on '\n'
func GetInputs(day string, test_input_raw string) (test_input []string, input []string) {
	test_input = strings.Split(test_input_raw, "\n")
	fullBytes, err := os.ReadFile(fmt.Sprintf("./inputs/day%s", day))
	if err != nil {
		fmt.Printf("error reading day file: %s\n", err)
		return test_input, nil
	}
	input = strings.Split(bytes.NewBuffer(fullBytes).String(), "\n")
	return
}
