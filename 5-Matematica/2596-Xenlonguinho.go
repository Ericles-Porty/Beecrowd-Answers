package main

import (
	"fmt"

)

func main() {
	var nRuns int

	fmt.Scan(&nRuns)
	for i := 0; i < nRuns; i++ {
		var nEsferas int
		fmt.Scan(&nEsferas)

		esferasNecessarias := 0

		// j percorre as esferas
		for j := 2; j <= nEsferas; j++ {
			quantidadeDivisores := 0
			// k percorre os divisores
			for k := 2; k < j; k++ {
				if j%k == 0 {
					quantidadeDivisores++
				}
			}

			// tratamento para o caso de ser primo
			if quantidadeDivisores == 0 {
				esferasNecessarias++
				continue
			}

			if quantidadeDivisores%2 == 0 {
				esferasNecessarias++
			}
		}
		fmt.Println(esferasNecessarias)
	}
}