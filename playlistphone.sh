#!/bin/bash
playlist_computer=$1
playlist_phone=${1/.xspf}.phone.xspf

cp $playlist_computer $playlist_phone
vim -c "
:%s/\/mnt\/Data\/Music\/Albums/\.\.\/albums/g
:g/\<image\>/normal dd
:wq
" $playlist_phone
