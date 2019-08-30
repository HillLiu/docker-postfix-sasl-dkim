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
       musl \
       musl-utils \
       nano \
      && (rm "/tmp/"* 2>/dev/null || true) \
      && (rm -rf /var/cache/apk/* 2>/dev/null || true)

# Set up configuration
COPY supervisord.conf /etc/supervisord.conf
COPY rsyslog.conf /etc/rsyslog.conf
COPY entrypoint.sh /usr/local/bin/

# Run supervisord
WORKDIR /tmp

ENTRYPOINT ["entrypoint.sh"]
CMD ["server"]
