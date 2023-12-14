package main

import (
	"github.com/emersion/hydroxide/auth"
	smtpbackend "github.com/emersion/hydroxide/smtp"
	"log"
	"os"
)

func main() {
	bridgePassword := "DUMMY_PASSWORD"
	username := "DUMMY_USERNAME"

	c, privateKeys, err := auth.NewManager(newClient).Auth(username, bridgePassword)
	if err != nil {
		log.Fatal(err)
	}

	u, err := c.GetCurrentUser()
	if err != nil {
		log.Fatal(err)
	}

	addrs, err := c.ListAddresses()
	if err != nil {
		log.Fatal(err)
	}

	err = smtpbackend.SendMail(c, u, privateKeys, addrs, rcpt, os.Stdin)
	if err != nil {
		log.Fatal(err)
	}
}
