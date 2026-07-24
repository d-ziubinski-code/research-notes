# Bandit Level 07

## Goal

Celem tego poziomu jest znalezienie słowa znajdującego się w pliku data.txt, oraz następnego do słowa millionth 

host: **bandit.labs.overthewire.org**

nazwa użytkownika: bandit7
hasło: sprawdz level-06

ssh bandit7@bandit.labs.overthewire.org -p 2220

Przydatne komendy:
ssh z flagą -p


## Solution

Otwórz terminal/cmd

uzyj komendy ssh:

ssh bandit7@bandit.labs.overthewire.org -p 2220

okreslamy tutaj konkretny port po ktorym chcemy sie polaczyc, defaultowo jest to 22

Po poprawnym zalogowaniu mozemy przejsc do podstawowej enumeracji:

whoami
pwd
ls


W tym przypadku używamy komendy grep z zastosowaniem regexa

grep -oP "millionth\s+\K\S+" data.txt

-o = wypisz tylko dopasowany fragment
-P = uzyj składki regexow PCRE, dzieki czmeu mozemy uzyc \K \s \S

\s = oznacza bialy znak: spacja, tab, enter
"+" = oznacza jeden lub wiecej

\K = kontrukcja dosteona w PCRE - mowi zapomnij wszystko co dopiero dopasowales

\S = znak niebedacy spacja

Działa to w taki sposób:

millionth <- znajdz to słowo
\s+ <- potem jedna lub wiecej spacji
\K <- zapomnij o tym, co było wcześniej
\S+ <- dopasuj następne słowo

Po zastosowaniu komendy, ukaże się hasło :)
