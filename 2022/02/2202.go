package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

const year, day string = "2022", "02"

const path string = "input.txt"

func read_file() [][2]string {
	file, err := os.Open(path)
	if err != nil {
		panic("erro ao ler o arquivo")
	}

	scanner := bufio.NewScanner(file)

	guide := [][2]string{}

	for scanner.Scan() {
		line := scanner.Text()
		plays := strings.Split(line, " ")
		guide = append(guide, [2]string{plays[0], plays[1]})

	}

	return guide
}

// A => Rock
// B => Paper
// c => Scissor

// X => Rock
// Y => Paper
// z => Scissor

func main() {
	os.Chdir(year + "/" + day)

	guide := read_file()
	pts_abc := map[string]int{"A": 1, "B": 2, "C": 3}
	pts_xyz := map[string]int{"X": 1, "Y": 2, "Z": 3}

	points := 0
	for _, plays := range guide {
		pts_1, pts_2 := pts_abc[plays[0]], pts_xyz[plays[1]]
		points += pts_2
		if pts_1 == pts_2 {
			points += 3
		} else if (pts_1 == 1 && pts_2 == 2) || (pts_1 == 2 && pts_2 == 3) || (pts_1 == 3 && pts_2 == 1) {
			points += 6
		}
	}

	fmt.Println("PARTE 1:", points)

	points = 0
	for _, plays := range guide {
		pts_1, result := pts_abc[plays[0]], plays[1]
		var pts_2 int
		switch result {
		case "X":
			pts_2 = pts_1 - 1
			if pts_2 == 0 {
				pts_2 = 3
			}
		case "Y":
			points += 3
			pts_2 = pts_1
		case "Z":
			points += 6
			pts_2 = pts_1 + 1
			if pts_2 == 4 {
				pts_2 = 1
			}
		}
		points += pts_2

	}

	fmt.Println("PARTE 2:", points)
}
