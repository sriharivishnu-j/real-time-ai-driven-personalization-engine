package main

import (
	"log"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	log.Println("Processing data")
	w.Write([]byte("Data processed successfully"))
}

func main() {
	http.HandleFunc("/process", handler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
