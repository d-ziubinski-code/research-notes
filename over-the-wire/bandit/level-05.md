# Bandit Level 05

## Goal

Celem tego poziomu jest znalezienie hasła znajdującego w jedynym pliku, który posiada następujące właściwości: jest czytelny dla czlowieka, ma 1033 bajty, i nie jest executable. Dodatkowo znajduje sie w folderze inhere.




host: **bandit.labs.overthewire.org**

nazwa użytkownika: bandit5
hasło: sprawdz level-04

ssh bandit5@bandit.labs.overthewire.org -p 2220

Przydatne komendy:
ssh z flagą -p


## Solution

Otwórz terminal/cmd

uzyj komendy ssh:

ssh bandit5@bandit.labs.overthewire.org -p 2220

okreslamy tutaj konkretny port po ktorym chcemy sie polaczyc, defaultowo jest to 22

Po poprawnym zalogowaniu mozemy przejsc do podstawowej enumeracji:

whoami
pwd
ls

W tym levelu problemem jest to, że w folderze w ktorym jest nasz plik, jest kilka innych plikow.

Plik ktory musimy znalezc to plik czytelny dla czlowieka, plik zajmujący 1033 bajty miejsca i plik ktory nie jest executable

Mozemy to zrobic za pomoca komendy find:

find inhere -type f -size 1033c ! -executable
./inhere/maybehere07/.file2

nasteonie wyswietlamy zawartosc

cat ./inhere/maybehere07/.file2

mamy hasło.
