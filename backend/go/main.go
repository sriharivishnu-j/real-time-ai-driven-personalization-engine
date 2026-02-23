package main

import (
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/interaction", func(w http.ResponseWriter, r *http.Request) {
		log.Println("Interaction endpoint called")
		w.Write([]byte("Interaction service is running"))
	})

	log.Fatal(http.ListenAndServe(":8080", nil))
}