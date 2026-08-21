# Bandit Level 18

## Goal

W tym poziomie, problemem jest to, że po zalogowaniu na serwer automatycznie jesteśmy wylogowywani.
Jest to związane z modyfikacją pliku `.bashrc` po stronie serwera.
Przy próbie logowania i wpisaniu poprawnego hasła serwer zwróci:
`Byebye !`

W `bandit18` ktoś dopisał na samym końcu pliku `~/.bashrc` komendę wychodzącą:
`exit`
lub
`logout`

host: **bandit.labs.overthewire.org**

nazwa użytkownika: `bandit18`
hasło: sprawdz level-17

`ssh bandit18@bandit.labs.overthewire.org -p 2220`

Przydatne komendy:
`ssh z flagą -p`

### Solution

#### Czym jest plik `.bashrc`?

Jest to skrypt konfiguracyjny powłoki Bash (Bourne Again Shell) znajdujący się w katalogu domowym użytkownika.

Uruchamia się automatycznie za każdym razem, gdy otwieramy nową, nie-logowaniową sesję powłoki (czyli interaktywny terminal, w tym sesje SSH Basha).

Mamy 3 proste sposoby jak to obejść:
- `ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme"` - zamiast logować się interaktywnie, możemy od razu wykonać polecenie czytające plik (np. `cat`) i zakończyć połączenie.
- `ssh bandit18@bandit.labs.overthewire.org -p 2220 "/bin/bash --noprofile --norc"` - możemy nakazać powłoce `bash` uruchomienie się bez czytania domyślnego `.bashrc`
- `ssh bandit18@bandit.labs.overthewire.org -p 2220 "cat readme" > pobrany_plik.txt` - możemy zwrócić wartość zapisując ją od razu do pliku

### Lessons learned

- SSH pozwala na wykonanie pojedynczej komendy bez otwierania interaktywnej sesji (np. `ssh user@host "polecenie"`). W takim przypadku proces kończy działanie natychmiast po zwróceniu wyniku.
- Wynik komendy uruchomionej na zdalnym serwerze można bezpośrednio przechwycić i zapisać do pliku na lokalnej maszynie za pomocą operatora `>` (np. `ssh user@host "cat file" > local_file.txt`).
- `.bashrc` jest wykonywany automatycznie podczas tworzenia interaktywnej powłoki Bash. Jeśli plik ten zostanie uszkodzony lub zmanipulowany (np. zawiera `exit`), można ominąć jego ładowanie za pomocą flag `--norc` / `--noprofile` lub uruchamiając komendę bezpośrednio.
- Modyfikacja plików domowych użytkownika (`.bashrc`, `.profile`) nie jest skutecznym sposobem na ograniczenie uprawnień w systemie Linux.