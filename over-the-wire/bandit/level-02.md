# Bandit Level 02

## Goal

Celem tego poziomu jest znalezienie hasła znajdującego się w pliku --spaces in this filename--  


host: **bandit.labs.overthewire.org**

nazwa użytkownika: bandit2
hasło: sprawdz level-01

ssh bandit2@bandit.labs.overthewire.org -p 2220

Przydatne komendy:
ssh z flagą -p


## Solution

Otwórz terminal/cmd

uzyj komendy ssh:

ssh bandit2@bandit.labs.overthewire.org -p 2220

okreslamy tutaj konkretny port po ktorym chcemy sie polaczyc, defaultowo jest to 22

Po poprawnym zalogowaniu mozemy przejsc do podstawowej enumeracji:

whoami
pwd
ls

W tym levelu problemem jest nazwa pliku "--spaces in this filename --"

jesli sprobujemy otworzyc go klasycznym podejściem:
cat --spaces in this filename-- dostaniemy blad bo slowo spaces zostanie potraktowane jak argument


## Jak w takim razie otworzyć taki plik?

Musimy uzyc argumentu -- przed nazwa pliku z -/--.

Opcja -- mowi systemowi ze to co jest po tej opcji jest plikiem ktory chcemy wyswietlic a nie agumentem programu.

Dodatkowo ze względu na spacje pomiedzy slowami, musimy cala nazwe pliku opakowac w " ".

cat -- "--spaces in this filename--"

W taki sposob mozemy wyswietlic kolejne hasło :)


https://www.geeksforgeeks.org/linux-unix/cat-command-in-linux-with-examples/