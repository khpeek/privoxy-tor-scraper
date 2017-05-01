FROM alpine:latest
EXPOSE 9050 9051
ARG password
RUN apk --update add tor
RUN echo "ControlPort 9051" >> /etc/tor/torrc
RUN echo "HashedControlPassword $(tor --quiet --hash-password $password)" >> /etc/tor/torrc
CMD ["tor"]