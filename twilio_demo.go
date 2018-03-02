package main

import (
	"encoding/json"
	"io/ioutil"
	"log"
	"net/url"

	twilio "github.com/saintpete/twilio-go"
)

//Struct to hold the various key data
type keys struct {
	Sid        string `json:"twilio_sid"`
	Token      string `json:"twilio_token"`
	MyNumber   string `json:"my_number"`
	CompNumber string `json:"comp_number"`
	MaskOff    string `json:"maskoff"`
}

func main() {

	var dat keys
	bdata, err := ioutil.ReadFile("creds.json")
	if err != nil {
		log.Fatal("Could not read data properly", err)
	}

	//Unmarshaling the data into a datAuth struct to hold sensative information
	if json.Unmarshal(bdata, &dat) != nil {
		log.Fatal("Error Unmarshalling the data")
	}

	client := twilio.NewClient(dat.Sid, dat.Token, nil)
	if u, err := url.Parse(dat.MaskOff); err != nil {
		log.Fatal(err)
	} else {
		client.Calls.MakeCall(dat.CompNumber, dat.MyNumber, u)
	}
}
