package main

import (
	"bufio"
	"fmt"
	"os"
)

type Grid struct {
	grid [][]string
	w    int
	h    int
}

func NewGrid(grid [][]string) *Grid {
	var h int = len(grid)
	var w int = len(grid[0])
	return &Grid{grid, w, h}
}

func (g Grid) get(x int, y int) string {
	return g.grid[y][x]
}

func (g Grid) row(y int) []string {
	return g.grid[y]
}

func (g Grid) print() {
	fmt.Println()
	for y := 0; y < g.h; y++ {
		fmt.Println(g.row(y))
	}
	fmt.Println()
}

func (g Grid) set(x int, y int, v string) {
	g.grid[y][x] = v
}

func contains(elems [][2]int, val [2]int) bool {
	for _, elem := range elems {
		if elem == val {
			return true
		}
	}
	return false
}

var dia string = "Day21"
var dirs [4][2]int = [4][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

func parse_file(path string) Grid {
	file, err := os.Open(path)
	if err != nil {
		panic("erro na leitura do arquivo")
	}

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanRunes)

	var grid [][]string

	var line int = 0
	grid = append(grid, []string{})
	for scanner.Scan() {
		char := scanner.Text()
		if char == "\n" {
			line++
			grid = append(grid, []string{})
			continue
		} else if char != "\r" {
			grid[line] = append(grid[line], char)
		}
	}

	file.Close()

	return *NewGrid(grid)
}

func main() {
	os.Chdir(dia)
	grid := parse_file("input.txt")
	var starting_pos [2]int
	for y := 0; y < grid.h; y++ {
		for x := 0; x < grid.w; x++ {
			if grid.get(x, y) == "S" {
				starting_pos = [2]int{x, y}
				goto out
			}
		}
	}
out:

	positions := make([][2]int, 0, 10000000)
	positions = append(positions, starting_pos)

	c := map[int][][2]int{}

	for step := 0; step < 64; step++ {
		n := len(positions)
		for i := 0; i < n; i++ {
			position := positions[0]
			x, y := position[0], position[1]
			idx_position := grid.w*y + x
			positions = positions[1:]

			walked_plots_cached, found := c[idx_position]

			walked_plots := [][2]int{}

			if !found {

				for _, dir := range dirs {
					dx, dy := dir[0], dir[1]
					nx := x + dx
					ny := y + dy
					npos := [2]int{nx, ny}
					if (nx < 0) || (nx >= grid.w) || (ny < 0) || (ny >= grid.h) || (grid.get(nx, ny) == "#") {
						continue
					}
					walked_plots = append(walked_plots, npos)
				}

				c[idx_position] = walked_plots

			} else {
				walked_plots = walked_plots_cached
			}

			for _, plot := range walked_plots {
				if contains(positions, plot) {
					continue
				}
				positions = append(positions, plot)
				grid.set(plot[0], plot[1], "O")
			}
			// fmt.Println(positions)
			grid.set(x, y, ".")
		}
	}
	fmt.Println("PARTE 1:", len(positions), "posições")
}
