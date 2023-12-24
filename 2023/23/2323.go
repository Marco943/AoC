package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
)

type Tile struct {
	i    int16
	n    uint16
	seen []int16
}

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

func main() {
	lines := read_file()
	h := int16(len(lines))
	w := int16(len(lines[0]))

	var done uint16
	paths := []Tile{{0*w + 1, 0, []int16{}}}

	for len(paths) != 0 {

		path := paths[0]
		paths = paths[1:]

		c := path.i / w
		r := path.i - w*c

		// fmt.Println(path.i, r, c)

		if r == h-1 && c == w-2 && path.n > done {
			done = path.n
			continue
		}

		if slices.Contains(path.seen, path.i) {
			continue
		}

		seen := make([]int16, len(path.seen), cap(path.seen))
		copy(seen, path.seen)
		seen = append(seen, path.i)

		for _, dir := range [4][2]int16{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
			ndr, ndc := dir[0], dir[1]
			nr := (r) + ndr
			nc := (c) + ndc
			if (nr < 0) || (nr >= h) || (nc < 0) || (nc >= w) {
				continue
			}

			nt := lines[nr][nc]
			if nt == "#" {
				continue
			}
			paths = append(paths, Tile{nc*w + nr, path.n + 1, seen})

		}
	}

	fmt.Println("PARTE 2:", done)
}
