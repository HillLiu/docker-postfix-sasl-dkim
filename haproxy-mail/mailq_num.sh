#!/bin/bash

docker exec -it haproxy-mail_mail_1 sh -c 'mailq | grep -c "^[A-F0-9]"'
