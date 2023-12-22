package main

import (
	aoc "aoc"
	"fmt"
	"os"
	"slices"
)

const ano string = "2023"
const dia string = "21"

var dirs [4][2]int = [4][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

func main() {
	os.Chdir(ano + "/" + dia)
	grid := *aoc.NewGrid("input.txt")
	var starting_pos [2]int
	for y := 0; y < grid.H; y++ {
		for x := 0; x < grid.W; x++ {
			if grid.Get(x, y) == "S" {
				starting_pos = [2]int{x, y}
				goto out
			}
		}
	}
out:

	positions := make([][2]int, 0, grid.H*grid.W)
	positions = append(positions, starting_pos)

	c := map[int][][2]int{}

	for step := 0; step < 64; step++ {
		n := len(positions)
		for i := 0; i < n; i++ {
			position := positions[0]
			x, y := position[0], position[1]
			idx_position := grid.W*y + x
			positions = positions[1:]

			walked_plots_cached, found := c[idx_position]

			walked_plots := [][2]int{}

			if !found {

				for _, dir := range dirs {
					dx, dy := dir[0], dir[1]
					nx := x + dx
					ny := y + dy
					npos := [2]int{nx, ny}
					if (nx < 0) || (nx >= grid.W) || (ny < 0) || (ny >= grid.H) || (grid.Get(nx, ny) == "#") {
						continue
					}
					walked_plots = append(walked_plots, npos)
				}

				c[idx_position] = walked_plots

			} else {
				walked_plots = walked_plots_cached
			}

			for _, plot := range walked_plots {
				if slices.Contains(positions, plot) {
					continue
				}
				positions = append(positions, plot)
				grid.Set(plot[0], plot[1], "O")
			}
			// fmt.Println(positions)
			grid.Set(x, y, ".")
		}
	}
	fmt.Println("PARTE 1:", len(positions), "posições")
}
