package main

import (
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/ingest", func(w http.ResponseWriter, r *http.Request) {
		// Placeholder for data ingestion logic
		log.Println("Data ingestion endpoint hit")
		w.Write([]byte("Ingestion successful"))
	})

	log.Println("Starting server on :8080")
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		log.Fatalf("Could not start server: %s", err.Error())
	}
}