package main

import (
	"fmt"

)

func main() {
	painelValues := map[rune]int{
		'1': 2,
		'2': 5,
		'3': 5,
		'4': 4,
		'5': 5,
		'6': 6,
		'7': 3,
		'8': 7,
		'9': 6,
		'0': 6,
	}

	var nRuns int
	fmt.Scan(&nRuns)

	for i := 0; i < nRuns; i++ {
		var painel string
		fmt.Scan(&painel)

		quantidadeLeds := 0
		for _, value := range painel {
			quantidadeLeds += painelValues[value]
		}

		fmt.Println(quantidadeLeds, "leds")
	}

}