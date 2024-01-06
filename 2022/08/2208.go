package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

const year, day, input string = "2022", "08", "input"

func readFile() [][]int {
	file, err := os.Open(fmt.Sprintf("%v/%v/%v.txt", year, day, input))
	if err != nil {
		log.Fatal("erro na leitura de arquivo", err)
	}
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanRunes)
	trees := [][]int{{}}
	i_line := 0
	for scanner.Scan() {
		text := scanner.Text()
		if text == "\n" {
			i_line += 1
			trees = append(trees, []int{})
			continue
		} else if text == "\r" {
			continue
		}
		intText, err := strconv.Atoi(text)
		if err != nil {
			log.Fatal("erro na conversão de string em int", err)
		}
		trees[i_line] = append(trees[i_line], intText)
	}
	return trees
}

func main() {
	trees := readFile()
	visible := 2*(len(trees)+len(trees[0])) - 4
	hightestScore := 0
	for y := 1; y < len(trees)-1; y++ {
		for x := 1; x < len(trees[y])-1; x++ {
			viewBottom := 0
			viewTop := 0
			viewRight := 0
			viewLeft := 0
			height := trees[y][x]
			visibleBottom := true
			visibleTop := true
			visibleRight := true
			visibleLeft := true
			for ny := y + 1; ny <= len(trees)-1; ny++ {
				viewBottom++
				if trees[ny][x] >= height {
					visibleBottom = false
					break
				}
			}
			for ny := y - 1; ny >= 0; ny-- {
				viewTop++
				if trees[ny][x] >= height {
					visibleTop = false
					break
				}
			}
			for nx := x + 1; nx <= len(trees[0])-1; nx++ {
				viewRight++
				if trees[y][nx] >= height {
					visibleRight = false
					break
				}
			}
			for nx := x - 1; nx >= 0; nx-- {
				viewLeft++
				if trees[y][nx] >= height {
					visibleLeft = false
					break
				}
			}
			if visibleBottom || visibleLeft || visibleRight || visibleTop {
				visible++
			}
			hightestScore = max(hightestScore, viewTop*viewRight*viewBottom*viewLeft)
		}
	}

	fmt.Println("PART 1:", visible)
	fmt.Println("PART 2:", hightestScore)

}
