# Bandit Level 00

## Goal

Celem tego poziomu jest zalogowanie się do pierwszej maszyny używając protokołu SSH na niestandardowym porcie 2220

host: **bandit.labs.overthewire.org**

nazwa użytkownika: bandit0
hasło: bandit0

Po zalogowaniu przechodzimy do levelu 1.

Przydatne komendy:
ssh z flagą -p


## Solution

Otwórz terminal/cmd

uzyj komendy ssh:

ssh bandit0@bandit.labs.overthewire.org -p 2220

okreslamy tutaj konkretny port po ktorym chcemy sie polaczyc, defaultowo jest to 22

Po poprawnym zalogowaniu mozemy przejsc do podstawowej enumeracji:

whoami
pwd
ls

widzimy plik readme

uzywamy komendy cat aby wyswietlic content:

cat readme

w pliku jest hasło :)
