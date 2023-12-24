package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
)

func read_file() [][]string {
	const year, day, path string = "2023", "23", "input.txt"
	os.Chdir(year + "/" + day)
	file, err := os.Open(path)
	if err != nil {
		panic("erro ao ler o arquivo")
	}

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanRunes)

	var lines [][]string
	lines = append(lines, []string{})
	line_dx := 0
	for scanner.Scan() {
		text := scanner.Text()
		if text == "\r" {
			continue
		} else if text == "\n" {
			line_dx++
			lines = append(lines, []string{})
			continue
		}
		lines[line_dx] = append(lines[line_dx], text)
	}
	file.Close()
	return lines
}

var best, starting, target, h, w int
var lines [][]string
var visited_ar []bool

func dfs(i int, visited int) {
	visited_ar[i] = true

	if i == target {
		if visited > best {
			best = visited
		}
	} else {
		for _, nd := range [4]int{1, -1, w, -w} {
			ni := i + nd
			if (ni < 0) || (ni >= w*h) || (lines[ni/w][ni%w] == "#") || visited_ar[ni] {
				continue
			}
			dfs(ni, visited+1)
		}

	}
	visited_ar[i] = false
}

func main() {
	lines = read_file()
	h = int(len(lines))
	w = int(len(lines[0]))
	visited_ar = make([]bool, h*w)

	starting = slices.Index(lines[0], ".")
	target = (h-1)*w + slices.Index(lines[h-1], ".")

	dfs(starting, 0)

	fmt.Println("PARTE 2:", best)
}
