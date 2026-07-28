# Bandit Level 10

## Goal

Celem tego poziomu jest znalezienie słowa znajdującego się w pliku data.txt, oraz występującego tylko raz

host: **bandit.labs.overthewire.org**

nazwa użytkownika: bandit9
hasło: sprawdz level-09

ssh bandit10@bandit.labs.overthewire.org -p 2220

Przydatne komendy:
ssh z flagą -p


## Solution

Otwórz terminal/cmd

uzyj komendy ssh:

ssh bandit10@bandit.labs.overthewire.org -p 2220

okreslamy tutaj konkretny port po ktorym chcemy sie polaczyc, defaultowo jest to 22

Po poprawnym zalogowaniu mozemy przejsc do podstawowej enumeracji:

whoami
pwd
ls

Hasło znajduję się w pliku `data.txt` który zawiera dane zakodowane w base64

Sprawdźmy najpierw co to za plik na podstawie zawartości:
`file data.txt`

Zwróci:
`data.txt: ASCII text`

Czyli jest to dokument tekstowy.

Możemy odkodować dane jedną komendą:
`base64 -d data.txt`
`-d` - decode

Mamy hasło :)



