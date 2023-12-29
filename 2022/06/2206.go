package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

const year, day, input string = "2022", "06", "input"

func checkDistinct(chars []string) bool {
	for i := 0; i < len(chars); i++ {
		for j := i + 1; j < len(chars); j++ {
			if chars[i] == chars[j] {
				return false
			}
		}
	}
	return true
}

func main() {
	file, err := os.Open(fmt.Sprintf("%v/%v/%v.txt", year, day, input))
	if err != nil {
		log.Fatal("erro na leitura do arquivo", err)
	}
	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanRunes)

	chars := make([]string, 4)
	chars2 := make([]string, 14)

	found, found2 := false, false
	for i := 1; scanner.Scan(); i++ {
		text := scanner.Text()
		chars[i%4] = text
		chars2[i%14] = text
		if (i >= 4) && !found {
			if checkDistinct(chars) {
				fmt.Println("PARTE 1:", i)
				found = true
			}
		}
		if (i >= 14) && !found2 {
			if checkDistinct(chars2) {
				fmt.Println("PARTE 2:", i)
				found2 = true
			}
		}
		if found && found2 {
			break
		}
	}
}
