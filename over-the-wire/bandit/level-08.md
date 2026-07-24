# Bandit Level 08

## Goal

Celem tego poziomu jest znalezienie słowa znajdującego się w pliku data.txt, oraz występującego tylko raz

host: **bandit.labs.overthewire.org**

nazwa użytkownika: bandit8
hasło: sprawdz level-07

ssh bandit8@bandit.labs.overthewire.org -p 2220

Przydatne komendy:
ssh z flagą -p


## Solution

Otwórz terminal/cmd

uzyj komendy ssh:

ssh bandit8@bandit.labs.overthewire.org -p 2220

okreslamy tutaj konkretny port po ktorym chcemy sie polaczyc, defaultowo jest to 22

Po poprawnym zalogowaniu mozemy przejsc do podstawowej enumeracji:

whoami
pwd
ls


Ten level wymaga od nas posortowania pliku i znalezienia unikalnej wartości. 

Na szczescie mamy na to konkretny sposób.

To zadanie wymaga od nas wykorzystanie pipelinu
Komenda którą użyjemy wygląda następująco:

sort data.txt | uniq -u

flaga -u przy uniq wypisze tylko unikalna wartosc

mozemy uzyc flagi -c wtedy uzyskamy wszystkie wartosci i liczbe ich wystapien.

Tym sposobem uzyskujemy flage do poziomu 9 :D