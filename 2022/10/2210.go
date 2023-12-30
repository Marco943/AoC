package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

const year, day, input string = "2022", "10", "input"

func main() {
	file, err := os.Open(fmt.Sprintf("%v/%v/%v.txt", year, day, input))
	if err != nil {
		log.Fatal("erro na leitura do arquivo", err)
	}
	scanner := bufio.NewScanner(file)
	var x, cycle, signalStrength int = 1, 0, 0
	screen := strings.Builder{}
	for scanner.Scan() {
		instruction := scanner.Text()
		var wait int = 1
		var sum int
		if instruction == "noop" {
			wait = 1
		} else {
			num, err := strconv.Atoi(strings.Split(instruction, " ")[1])
			if err != nil {
				log.Fatal("erro na conversão de string em int", err)
			}
			wait = 2
			sum = num
		}
		for wait != 0 {
			if cycle%40 == 0 {
				screen.WriteString("\n")
			}
			if cycle%40 >= x-1 && cycle%40 <= x+1 {
				screen.WriteString("#")
			} else {
				screen.WriteString(".")
			}
			cycle++
			wait--
			if cycle >= 20 && (cycle-20)%40 == 0 {
				signalStrength += cycle * x
			}
		}
		x += sum
	}
	fmt.Println("PARTE 1:", signalStrength)
	fmt.Println("PARTE 2:", screen.String())
}
