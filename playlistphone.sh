#!/bin/bash
playlist_computer=$1
playlist_phone=${1/.xspf}.phone.xspf

cp $playlist_computer $playlist_phone
vim -s playlistphone.vim $playlist_phone
