# Bandit Level 01

## Goal

Celem tego poziomu jest znalezienie hasła znajdującego się w pliku - w /home/ directory

host: **bandit.labs.overthewire.org**

nazwa użytkownika: bandit1
hasło: sprawdz level-00

ssh bandit1@bandit1.labs.overthewire.org -p 2220

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

W tym levelu problemem jest nazwa pliku "-"

W wielu programach w cmd (np. cat, tar, git) sam znak "-" użyty jako nazwa pliku ma specjalne znaczenie:
- Oznacza STDIN (standardowe wejście) lub STDOUT(standardowe wyjście) - czyli przekazywanie danych w strumienie, a nie konkretny plik na dysku.
 
Jeśli spróbujemy wyświetlić zawartość "cat -"
program nie sprobuje otworzyc pliku o nazwie "-". 
Zamiast tego uzna, że prosisz go o czytanie ze standardowego wejścia (będzie czekał, aż zaczniesz wpisywać wpisywać tekst z klawiatury)

## Jak w takim razie otworzyć taki plik?

Musimy wskazać programowi pełną lub względną ścieżkę do pliku, żeby program nie pomylił go z flagą lub strumieniem:

cat ./-

W taki sposob mozemy wyswietlic hasło :)
