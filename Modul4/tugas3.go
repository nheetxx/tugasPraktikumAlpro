package main

import "fmt"

func main() {
	jarak := 3

	for {
		var n int
		fmt.Print("Masukkan n: ")
		fmt.Scan(&n)

		if n <= 0 {
			continue
		}

		for i := 1; i <= n; i++ {

			for s := 0; s < n-i; s++ {
				fmt.Print(" ")
			}
			for a := i; a >= 1; a-- {
				fmt.Print(a % 10)
			}
			for b := 2; b <= i; b++ {
				fmt.Print(b % 10)
			}
			for s := 0; s < n-i; s++ {
				fmt.Print(" ")
			}

			for g := 0; g < jarak; g++ {
				fmt.Print(" ")
			}

			k := n - i + 1
			for s := 0; s < i-1; s++ {
				fmt.Print(" ")
			}
			for a := k; a >= 1; a-- {
				fmt.Print(a % 10)
			}
			for b := 2; b <= k; b++ {
				fmt.Print(b % 10)
			}

			fmt.Println()
		}

		break
	}
}