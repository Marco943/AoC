package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

const year, day, input string = "2022", "04", "input"

func readFile() [][2][2]int {
	file, err := os.Open(fmt.Sprintf("%v/%v/%v.txt", year, day, input))
	if err != nil {
		log.Fatal("erro ao ler o arquivo", err)
	}
	scanner := bufio.NewScanner(file)
	lines := [][2][2]int{}
	for scanner.Scan() {
		newLine := scanner.Text()
		pairsLine := strings.Split(newLine, ",")
		nums := strings.Split(pairsLine[0], "-")
		num1, err1 := strconv.Atoi(nums[0])
		num2, err2 := strconv.Atoi(nums[1])
		nums2 := strings.Split(pairsLine[1], "-")
		num21, err21 := strconv.Atoi(nums2[0])
		num22, err22 := strconv.Atoi(nums2[1])
		if err1 != nil || err2 != nil || err21 != nil || err22 != nil {
			log.Fatal("erro ao converter string em int", err1, err2)
		}
		lines = append(lines, [2][2]int{{num1, num2}, {num21, num22}})
	}
	return lines
}

func pairContains(e1 *[2]int, e2 *[2]int) int {
	if (e1[0] >= e2[0]) && (e1[1] <= e2[1]) {
		return 1
	} else if (e2[0] >= e1[0]) && (e2[1] <= e1[1]) {
		return 1
	}
	return 0
}

func pairOverlaps(e1 *[2]int, e2 *[2]int) int {
	if (e1[0] >= e2[0]) && (e1[0] <= e2[1]) {
		return 1
	} else if (e1[1] >= e2[0]) && (e1[1] <= e2[1]) {
		return 1
	} else if (e2[0] >= e1[0]) && (e2[0] <= e1[1]) {
		return 1
	} else if (e2[1] >= e1[0]) && (e2[1] <= e1[1]) {
		return 1
	}
	return 0
}

func main() {
	lines := readFile()
	var sum int
	var sum2 int
	for _, pair := range lines {
		// fmt.Println(pair[0], pair[1], pairContains(&pair[0], &pair[1]))
		sum += pairContains(&pair[0], &pair[1])
		sum2 += pairOverlaps(&pair[0], &pair[1])

	}
	fmt.Println("PARTE 1:", sum)
	fmt.Println("PARTE 2:", sum2)
}
