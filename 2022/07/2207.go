package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

const year, day, input string = "2022", "07", "input"

func readFile() {
	file, err := os.Open(fmt.Sprintf("%v/%v/%v.txt", year, day, input))
	if err != nil {
		log.Fatal("erro na leitura do arquivo", err)
	}
	scanner := bufio.NewScanner(file)
	files := map[string]int{}
	dirs := []string{}
	var cur_dir string = ""
	for scanner.Scan() {
		line := scanner.Text()
		lineSplit := strings.Split(line, " ")
		switch string(lineSplit[0]) {
		case "$":
			if lineSplit[1] == "cd" {
				switch lineSplit[2] {
				case "..":
					lastDir := strings.LastIndex(cur_dir[:len(cur_dir)-1], "/")
					cur_dir = cur_dir[:lastDir+1]
				default:
					if cur_dir == "" {
						cur_dir = "/"
					} else {
						cur_dir += lineSplit[2] + "/"
					}
				}
			}
		case "dir":
			dirs = append(dirs, fmt.Sprintf("%v/", lineSplit[1]))
		default:
			size, err := strconv.Atoi(lineSplit[0])
			if err != nil {
				log.Fatal("erro na conversão de string em int", err)
			}
			files[fmt.Sprintf("%v%v", cur_dir, lineSplit[1])] = size
		}
	}

	dir_sizes := map[string]int{"/": 0}
	for _, dir := range dirs {
		for file, size := range files {
			if strings.Contains(file, dir) {
				dir_sizes[dir] += size
			}
		}
	}
	for _, size := range files {
		dir_sizes["/"] += size
	}

	var part1 int
	for _, size := range dir_sizes {
		if size <= 100000 {
			part1 += size
		}
	}

	fmt.Println("DIRS:", dirs)
	fmt.Println("FILES:", files)
	fmt.Println("PARTE 1:", part1)
}

func main() {
	readFile()
}
