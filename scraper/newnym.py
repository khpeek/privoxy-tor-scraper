#!/usr/bin/python3
# -*- coding: utf-8 -*-

from time import sleep, time

import requests as req
import telnetlib


def get_ip():
    IPECHO_ENDPOINT = 'http://ipecho.net/plain'
    # HTTP_PROXY = 'http://localhost:8118'
    HTTP_PROXY = 'http://privoxy:8118'
    return req.get(IPECHO_ENDPOINT, proxies={'http': HTTP_PROXY}).text


def request_ip_change():
    # tn = telnetlib.Telnet('127.0.0.1', 9051)
    tn = telnetlib.Telnet('tor', 9051)
    tn.read_until("Escape character is '^]'.", 2)
    tn.write('AUTHENTICATE ""\r\n')
    tn.read_until("250 OK", 2)
    tn.write("signal NEWNYM\r\n")
    tn.read_until("250 OK", 2)
    tn.write("quit\r\n")
    tn.close()


if __name__ == '__main__':
    dts = []
    try:
        while True:
            ip = get_ip()
            t0 = time()
            request_ip_change()
            while True:
                new_ip = get_ip()
                if new_ip == ip:
                    sleep(1)
                else:
                    break
            dt = time() - t0
            dts.append(dt)
            print("{} -> {} in ~{}s".format(ip, new_ip, int(dt)))
    except KeyboardInterrupt:
        print("Stopping...")
        print("Average: {}".format(sum(dts) / len(dts)))
