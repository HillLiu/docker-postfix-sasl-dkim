FROM alpine:latest

RUN  apk update \ 
     && apk add \
       cyrus-sasl \
       cyrus-sasl-plain \
       cyrus-sasl-login \
       postfix \
       opendkim \
       opendkim-utils \
       ca-certificates \
       supervisor \
       rsyslog \
      && (rm /tmp/* 2>/dev/null || true) \
      && (rm -rf /var/cache/apk/* 2>/dev/null || true)

# Set up configuration
COPY ./conf/supervisord.conf /etc/supervisord.conf
COPY ./conf/rsyslog.conf /etc/rsyslog.conf
COPY ./conf/transport /etc/postfix/transport 
COPY ./conf/aliases /etc/postfix/aliases 
COPY ./entrypoint.sh /usr/local/bin/

# Volume
VOLUME /etc/opendkim/keys

# Run supervisord
WORKDIR /tmp
ENTRYPOINT ["entrypoint.sh"]
CMD ["server"]
