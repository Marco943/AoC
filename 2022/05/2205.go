package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

const year, day, input string = "2022", "05", "input"

func main() {
	file, err := os.Open(fmt.Sprintf("%v/%v/%v.txt", year, day, input))
	if err != nil {
		log.Fatal("erro na leitura do arquivo", err)
	}
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanRunes)

	stacks_map := map[int][]string{}
	col := 0
	for scanner.Scan() {
		if text := scanner.Text(); text == "\n" {
			if col == 1 {
				break
			}
			col = 0
			continue
		} else if (text != " ") && (text != "[") && (text != "]") && (text != "\r") {
			if _, ok := stacks_map[col]; !ok {
				stacks_map[col] = []string{}
			}
			stacks_map[col] = append(stacks_map[col], text)
		}
		col++
	}

	stacks := map[int][]string{}
	for _, stack := range stacks_map {
		stack_slice := stack[0 : len(stack)-1]
		stack_no, err := strconv.Atoi(stack[len(stack)-1])
		if err != nil {
			log.Fatal("erro ao converter string em int", err)
		}
		for i, j := 0, len(stack_slice)-1; i < j; i, j = i+1, j-1 {
			stack_slice[i], stack_slice[j] = stack_slice[j], stack_slice[i]
		}
		stacks[stack_no] = stack_slice
	}

	moves := [][]int{{}}
	line := 0
	for scanner.Scan() {
		text := scanner.Text()
		if num, err := strconv.Atoi(text); err == nil {
			moves[line] = append(moves[line], num)
		} else if text == "\n" {
			if len(moves[line]) == 4 {
				moves[line] = []int{moves[line][0]*10 + moves[line][1], moves[line][2], moves[line][3]}
			}
			line++
			moves = append(moves, []int{})
			continue
		}
	}
	stacks1 := make(map[int][]string, len(stacks))
	stacks2 := make(map[int][]string, len(stacks))
	for k, v := range stacks {
		copyV1 := make([]string, len(v))
		copyV2 := make([]string, len(v))
		copy(copyV1, v)
		copy(copyV2, v)
		stacks1[k] = copyV1
		stacks2[k] = copyV2
	}
	for _, move := range moves {
		from := move[1]
		to := move[2]
		for i := 0; i < move[0]; i++ {
			length_from := len(stacks1[from])
			crate := stacks1[from][length_from-1]
			stacks1[from] = stacks1[from][0 : length_from-1]
			stacks1[to] = append(stacks1[to], crate)
		}
	}
	var r strings.Builder
	for i := 1; i <= len(stacks1); i++ {
		stack := stacks1[i]
		r.WriteString(stacks1[i][len(stack)-1])
	}

	fmt.Println("PARTE 1:", r.String())

	for _, move := range moves {
		from := move[1]
		to := move[2]
		length_from := len(stacks2[from])
		stacks2[to] = append(stacks2[to], stacks2[from][length_from-move[0]:]...)
		stacks2[from] = stacks2[from][0 : length_from-move[0]]
	}

	var r2 strings.Builder
	for i := 1; i <= len(stacks2); i++ {
		stack := stacks2[i]
		r2.WriteString(stacks2[i][len(stack)-1])
	}

	fmt.Println("PARTE 2:", r2.String())

}
