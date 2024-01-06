package aoc

import (
	"bufio"
	"fmt"
	"os"
)

func Sum[V int | float32 | float64](s *[]V) V {
	var resultado V
	for _, v := range *s {
		resultado += v
	}
	return resultado
}

type Grid struct {
	Data [][]string
	W    int
	H    int
}

func NewGrid(path string) *Grid {
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

	var h int = len(grid)
	var w int = len(grid[0])
	return &Grid{grid, w, h}
}

func (g *Grid) Get(x int, y int) string {
	return g.Data[y][x]
}

func (g *Grid) Row(y int) []string {
	return g.Data[y]
}

func (g *Grid) Print() {
	fmt.Println()
	for y := 0; y < g.H; y++ {
		fmt.Println(g.Row(y))
	}
	fmt.Println()
}

func (g *Grid) Set(x int, y int, v string) {
	g.Data[y][x] = v
}
