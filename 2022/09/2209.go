package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
)

const year, day, input string = "2022", "09", "input"

type Point struct {
	x  int
	y  int
	dx int
	dy int
}

type Move struct {
	dx    int
	dy    int
	tiles int
}

func readFile() []Move {
	file, err := os.Open(fmt.Sprintf("%v/%v/%v.txt", year, day, input))
	if err != nil {
		log.Fatal("erro na leitura do arquivo", err)
	}
	scanner := bufio.NewScanner(file)
	moves := []Move{}
	for scanner.Scan() {
		line := scanner.Text()
		lineSplit := strings.Split(line, " ")
		var dx, dy int
		switch lineSplit[0] {
		case "U":
			dy = 1
		case "D":
			dy = -1
		case "L":
			dx = -1
		case "R":
			dx = 1
		}
		tiles, err := strconv.Atoi(lineSplit[1])
		if err != nil {
			log.Fatal("erro na conversão de string em int", err)
		}
		moves = append(moves, Move{dx: dx, dy: dy, tiles: tiles})
	}
	return moves
}

func isTailAdj(head *Point, tail *Point) bool {
	dx := head.x - tail.x
	dy := head.y - tail.y
	if dx >= -1 && dx <= 1 && dy >= -1 && dy <= 1 {
		tail.dx, tail.dy = 0, 0
		return true
	}
	return false
}

func moveTail(head *Point, tail *Point) {
	switch offsetX := head.x - tail.x; {
	case offsetX < 0:
		tail.dx = -1
	case offsetX > 0:
		tail.dx = 1
	default:
		tail.dx = 0
	}
	switch offsetY := head.y - tail.y; {
	case offsetY < 0:
		tail.dy = -1
	case offsetY > 0:
		tail.dy = 1
	default:
		tail.dy = 0
	}
	tail.x += tail.dx
	tail.y += tail.dy
}

func main() {
	moves := readFile()
	rope := make([]Point, 10)
	visited2nd := [][2]int{}
	visitedTail := [][2]int{}
	for _, move := range moves {
		for i := 0; i < move.tiles; i++ {
			cur2nd := rope[1]
			curTail := rope[len(rope)-1]
			if !slices.Contains(visited2nd, [2]int{cur2nd.x, cur2nd.y}) {
				visited2nd = append(visited2nd, [2]int{cur2nd.x, cur2nd.y})
			}
			if !slices.Contains(visitedTail, [2]int{curTail.x, curTail.y}) {
				visitedTail = append(visitedTail, [2]int{curTail.x, curTail.y})
			}
			rope[0].dx, rope[0].dy = move.dx, move.dy
			rope[0].x += rope[0].dx
			rope[0].y += rope[0].dy
			for i := 0; i < len(rope)-1; i++ {
				if !isTailAdj(&rope[i], &rope[i+1]) {
					moveTail(&rope[i], &rope[i+1])
				}
			}
		}
	}
	fmt.Println("PARTE 1:", len(visited2nd))
	fmt.Println("PARTE 2:", len(visitedTail))
}
