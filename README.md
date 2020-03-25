Alpine postfix + cyrus-sasl + dkim
======

## Docker hub
  * https://hub.docker.com/r/hillliu/postfix-sasl-dkim

## Test auth
  * docker-compose up
  * docker-compose exec mail sh 
  * apk add busybox-extras
  * telnet localhost 25
  * EHLO mail.example.com
  * AUTH PLAIN AHRlc3RfdXNlckBtYWlsLmV4YW1wbGUuY29tAHRlc3RfcGFzc3dvcmQ=

### get password with base64
```
echo -ne '\000omnichabot@omnicloud.tech\000omnicha2019bot' | openssl base64
```

## Test send mail
  * HELO mail.example.com
  * MAIL FROM: test@mail.example.com
  * RCPT TO: your@mail.example.com
  * data
  * Subject: test message
  * From:
  * To:
  * press enter twice
  * /* Wirte something */
  * .
  * QUIT

## use script
```
$ bash support/test_email.sh <email_adddress_destionation> <total email send>

$ bash support/test_email.sh hill.tw@gmail.com 10000
```
