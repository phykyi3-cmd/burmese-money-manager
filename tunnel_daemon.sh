#!/bin/bash
while true; do
  ssh -o StrictHostKeyChecking=no \
      -o ServerAliveInterval=15 \
      -o ServerAliveCountMax=4 \
      -o ConnectTimeout=10 \
      -R 80:localhost:8085 nokey@localhost.run
  sleep 3
done
