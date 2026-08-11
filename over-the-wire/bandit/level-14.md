# Bandit Level 14

## Goal

Do tego poziomu logujemy się za pomocą klucza prywatnego ssh znalezionego w levelu 13
Celem tego poziomu jest przesłanie hasła aktualnego użytkownika (`bandit14`) do lokalnej usługi działającej na porcie `30000`. 

Serwer oczekuje, że połączymy się z nim przez `localhost` i wyślemy nasze hasło. Jeżeli hasło będzie poprawne, otrzymamy hasło do następnego poziomu.

host: **bandit.labs.overthewire.org**

nazwa użytkownika: bandit14
hasło: sprawdz level-13

ssh-i nazwa_pliku bandit14@bandit.labs.overthewire.org -p 2220

Przydatne komendy:
ssh z flagą -p

### Solution

W levelu 13 dostaliśmy podpowiedź: `The password for the next level is stored in **/etc/bandit_pass/bandit14 and can only be read by user bandit14**`

Po zalogowaniu jako `bandit14` musimy najpierw znaleźć aktualne hasło. Jak wskazuje podpowiedź w levelu 13, hasło użytkownika `bandit14` znajduje się w pliku: `/etc/bandit_pass/bandit14`

Możemy je odczytać:

`cat /etc/bandit_pass/bandit14`

Otrzymamy hasło, które musimy przesłać do usługi działającej na porcie `30000`.  

 Do komunikacji z portem użyjemy programu `nc` (netcat). Składnia:
`nc host port`

W naszym przypadku:
`nc localhost 30000`

Po uruchomieniu komendy połączenie pozostanie otwarte i będzie czekało.

Wpisujemy hasło użytkownika `bandit14`

Otrzymujemy nowe hasło :)
### Lessons learned

- `nc` (netcat) pozwala komunikować się bezpośrednio z usługami działającymi przez TCP/UDP.
- Port identyfikuje konkretną usługę działającą na hoście (np. `localhost:30000`).
- `localhost` oznacza ten sam komputer, na którym aktualnie wykonujemy polecenie.
- Usługa sieciowa może nasłuchiwać na porcie i oczekiwać określonych danych wejściowych od klienta.
- Pipe (`|`) pozwala przekazywać wynik jednego polecenia jako wejście do drugiego programu.
- Komunikacja klient-serwer może odbywać się bez SSH — wystarczy bezpośrednie połączenie TCP z odpowiednim portem.
- Narzędzia takie jak `ss`, `netstat`, `lsof` oraz `nmap` pozwalają sprawdzić, jakie usługi działają i jakie porty są otwarte.

## Related projects -
[Python TCP Server](https://github.com/d-ziubinski-code/toolbox/tree/main/networking/tcp/python/tcp-server) - [Python TCP Client](https://github.com/d-ziubinski-code/toolbox/tree/main/networking/tcp/python/tcp-client)