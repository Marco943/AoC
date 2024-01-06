package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

const year, day, input string = "2022", "03", "input"
const prioridade string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

func readFile() []string {
	file, err := os.Open(fmt.Sprintf("%v/%v/%v.txt", year, day, input))
	if err != nil {
		log.Fatal("erro na leitura do arquivo:", err)
	}

	scanner := bufio.NewScanner(file)

	lines := []string{}
	for scanner.Scan() {
		newLine := scanner.Text()
		lines = append(lines, newLine)
	}

	return lines
}

func main() {
	lines := readFile()
	var soma int
	for _, line := range lines {
		length := len(line)
		items1 := line[:length/2]
		items2 := line[length/2:]
		var comum string
		for _, i1 := range items1 {
			for _, i2 := range items2 {
				if i1 == i2 {
					comum = string(i1)
					goto outPart1
				}
			}
		}
	outPart1:
		prioridade := strings.Index(prioridade, comum)
		if prioridade >= 0 {
			soma += prioridade + 1
		}
	}
	fmt.Println("PARTE 1:", soma)

	soma = 0
	for i := 0; i < len(lines); i += 3 {
		items1 := lines[i]
		items2 := lines[i+1]
		items3 := lines[i+2]
		var comum string
		for _, i1 := range items1 {
			for _, i2 := range items2 {
				for _, i3 := range items3 {
					if (i1 == i2) && (i2 == i3) {
						comum = string(i1)
						goto outPart2
					}
				}
			}
		}
	outPart2:
		prioridade := strings.Index(prioridade, comum)
		if prioridade >= 0 {
			soma += prioridade + 1
		}
	}
	fmt.Println("PARTE 2:", soma)

}
