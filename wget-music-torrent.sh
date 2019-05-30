#!/bin/bash

wget http://music-torrent.net

for i in $(seq 2 122)
do
    wget http://music-torrent.net/$i
done
