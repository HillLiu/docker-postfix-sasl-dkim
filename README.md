Alpine postfix + dkim + cyrus-sasl
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
echo -ne '\000test_user@mail.example.com\000test_password' | openssl base64
```

## Test send mail
  * HELO mail.example.com
  * MAIL FROM: test@example.com
  * RCPT TO: your@example.com
  * data
  * Subject: test message
  * press enter twice
  * /* Wirte something */
  * .
  * QUIT

