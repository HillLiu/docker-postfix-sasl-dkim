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
echo -ne '\000test_user@mail.example.com\000test_password' | openssl base64
```

## Test send mail

### Test mail with telnet
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

### Test mail with script
```
#!/bin/bash

DIR="$( cd "$(dirname "$0")" ; pwd -P )"
MAIL_FROM=test@mail.example.com
MAIL_TO=$1
MAIL_SUBJECT=test-subject
MAIL_BODY=test-body
MTA_HOST=localhost
MTA_USER=test_user@mail.example.com
MTA_PASSWORD=test_password

${DIR}/support/sendemail -f $MAIL_FROM -t $MAIL_TO -s $MTA_HOST -xu $MTA_USER -xp $MTA_PASSWORD -u $MAIL_SUBJECT -m $MAIL_BODY
```
