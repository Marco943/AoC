package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
)

const year, day string = "2022", "01"

func read_file(path string) *[][]int {
	file, ok := os.Open(path)
	if ok != nil {
		panic("erro ao ler o arquivo")
	}

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)
	block_count := 0

	var lines [][]int
	lines = append(lines, []int{})

	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			block_count++
			lines = append(lines, []int{})
			continue
		}

		number, err := strconv.Atoi(line)
		if err != nil {
			panic("falha em converter str em int: " + line)
		}
		lines[block_count] = append(lines[block_count], number)
	}

	file.Close()

	return &lines
}

func main() {
	os.Chdir(year + "/" + day)
	elves := *read_file("input.txt")

	var calories_per_elf []int
	var max_calories int

	for _, elf := range elves {
		calories := 0
		for _, v := range elf {
			calories += v
		}
		max_calories = max(max_calories, calories)
		calories_per_elf = append(calories_per_elf, calories)
	}

	fmt.Println("PARTE 1", max_calories)
	slices.Sort(calories_per_elf)
	top_3_calories := calories_per_elf[len(calories_per_elf)-3:]

	var sum_top_3 int
	for _, v := range top_3_calories {
		sum_top_3 += v
	}
	fmt.Println("PARTE 2", sum_top_3)
}
