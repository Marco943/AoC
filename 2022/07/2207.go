package main

import (
	"bufio"
	"cmp"
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
)

const year, day, input string = "2022", "07", "input"

type File struct {
	name    string
	dirPath string
	size    int
}

type Dir struct {
	name string
	path string
	size int
}

func main() {
	file, err := os.Open(fmt.Sprintf("%v/%v/%v.txt", year, day, input))
	if err != nil {
		log.Fatal("erro na leitura do arquivo", err)
	}
	scanner := bufio.NewScanner(file)
	files := []File{}
	dirs := []Dir{{name: "/", path: "/", size: 0}}
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
			dirs = append(dirs, Dir{name: lineSplit[1], path: fmt.Sprintf("%v%v/", cur_dir, lineSplit[1]), size: 0})
		default:
			size, err := strconv.Atoi(lineSplit[0])
			if err != nil {
				log.Fatal("erro na conversão de string em int", err)
			}
			files = append(files, File{name: lineSplit[1], dirPath: cur_dir, size: size})
		}
	}

	var part1 int
	for i_d, dir := range dirs {
		for _, file := range files {
			if strings.Contains(file.dirPath, dir.path) {
				dirs[i_d].size += file.size
			}
		}
	}
	for _, dir := range dirs {
		if dir.size <= 100000 {
			part1 += dir.size
		}
	}

	fmt.Println("PARTE 1:", part1)

	const availableSpace, unusedRequiredSpace int = 70000000, 30000000
	slices.SortFunc(dirs, func(a, b Dir) int {
		return cmp.Compare(a.size, b.size)
	})

	neededSize := dirs[len(dirs)-1].size - availableSpace + unusedRequiredSpace
	for i := 0; i < len(dirs); i++ {
		if dirs[i].size >= neededSize {
			fmt.Println("PARTE 2:", dirs[i].size)
			break
		}
	}

}
