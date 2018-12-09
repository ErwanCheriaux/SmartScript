# SmartScript
Smart scripts for daily help.

## findiff
Useful to compare two similar directories. 
You will see every diffrences between your computer music folder and your phone music folder. If you don't remember photos you pasts between all your hard drives, use findiff !  
Example  
```sh
findiff path/directory_1 path/directory_2
```

## playlistphone
Create your playlist on your laptop, enjoy it on your phone !  
With playlistphone, you can quickly adapt a XSPF file for your phone or other computer. Edit playlistphone.sh to chose the new path of your albums used in your playlist. 
Note that music folders have to be identical. You can be sure about that with the __findiff__ script.  
Example  
```sh
playlistphone file.xspf
```
## trustedcard
Decode Trusted Card.  
```
  a b c d e f g h i j  
  -------------------  
1|s f d f 4 8 r 6 e v  
2|e f 5 4 d s 3 f 5 f  
3|f e r v d 8 4 e 3 9  
4|a 8 7 p i h 2 1 d k  
5|s d z 8 4 6 a 1 3 a  
```
The card text file have to be like a matrix:  
```
sfdf48r6ev  
ef54ds3f5f  
fervd84e39  
a87pih21dk  
sdz846a13a  
```
