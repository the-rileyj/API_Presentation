package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"

	"github.com/gin-contrib/static"
	"github.com/gin-gonic/gin"
)

type credentials struct {
	Nasa string `json:"nasa"`
}

func getCredentials(file string) (credentials, error) {
	c := credentials{}
	if raw, err := ioutil.ReadFile(file); err == nil {
		json.Unmarshal(raw, &c)
		return c, nil
	} else {
		return credentials{}, fmt.Errorf("Could not read JSON from %s: %v", file, err)
	}
}

func main() {
	creds, err := getCredentials("creds.json")
	if err != nil {
		log.Fatal(err)
	}

	r := gin.Default()
	r.GET("/", func(c *gin.Context) { http.ServeFile(c.Writer, c.Request, "./index.html") })
	r.GET("/static/css/:fi", static.Serve("/static/css", static.LocalFile("static/css/", true)))
	r.GET("/static/img/:fi", static.Serve("/static/img", static.LocalFile("static/img/", true)))
	r.GET("/static/js/:fi", static.Serve("/static/js", static.LocalFile("static/js/", true)))
	r.GET("/static/custom/:fi", static.Serve("/static/custom", static.LocalFile("static/custom/", true)))

	api := r.Group("/api")

	api.GET("/creds/nasa", func(c *gin.Context) {
		c.JSON(200, gin.H{"key": creds.Nasa})
	})

	r.Run(":5566")
}
