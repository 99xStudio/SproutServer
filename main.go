// 99xStudio/SproutServer
// by reddust9

package main

import (
	"fmt"
	"net/http"
	"os"

	"github.com/gorilla/mux"
)

func log(text string) {
	fmt.Println("[SproutServer] " + text)
}

func handleRoot(w http.ResponseWriter, req *http.Request) {
	log("Request for root page!")
	fmt.Fprintf(w, "SproutServer v1.0.0\n")
}

func handleHb(w http.ResponseWriter, req *http.Request) {
	fmt.Fprintf(w, "OK")
}

func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	log("Port set to " + port)

	r := mux.NewRouter()
	r.HandleFunc("/", handleRoot).Methods("GET")
	r.HandleFunc("/hb", handleHb).Methods("GET")

	srv := &http.Server{
		Addr:    ":" + port,
		Handler: r,
	}
	log("Starting server...")
	srv.ListenAndServe()
}
