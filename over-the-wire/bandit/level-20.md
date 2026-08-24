# Bandit Level 20

## Goal

Ten level wymaga od nas użycia programu z ustawionym bitem `setuid` znajdującego się w katalogu `/home` użytkownika. Program ten wykonuje połączenie do localhosta na porcie podanym jako argument.

Następnie program czyta linie tekstu z połączenia i porównuje to do hasła do tego levelu (bandit20), jeśli podane hasło jest poprawne, zwraca hasło do levelu 21.

host: **bandit.labs.overthewire.org**

nazwa użytkownika: `bandit20`  
hasło: sprawdź level-19

`ssh bandit20@bandit.labs.overthewire.org -p 2220`

Przydatne komendy:  
`ssh` z flagą `-p`

### Solution

Na początku na `localhost` nie ma usługi nasłuchującej na wybranym przez nas porcie. Musimy więc utworzyć własny listener za pomocą `nc`:

```
nc -l 3333
```

W tym momencie **proces** `**nc**` **nasłuchuje na porcie TCP 3333** i czeka na połączenie.

Następnie, w drugim terminalu, uruchamiamy:

```
./suconnect 3333
```

Program `suconnect` nawiązuje połączenie TCP z `localhost:3333`.

Po ustanowieniu połączenia mamy więc:

```
Terminal 1                         Terminal 2

nc -l 3333  <──── TCP ──────>  ./suconnect 3333
    │                                  │
    │ wysyłamy hasło                   │
    └─────────────────────────────────>│
                                       │
                              sprawdza hasło
                                       │
                                       ▼
                              hasło do bandit21
```

W terminalu, w którym działa `nc`, wpisujemy aktualne hasło do levelu 20:

```
HASŁO_DO_BANDIT20
```

i zatwierdzamy Enterem.

`suconnect` odbiera przesłaną linię, porównuje ją z hasłem do `bandit20`, a ponieważ hasło jest poprawne, zwraca hasło do użytkownika `bandit21`.

**Mamy nowe hasło :)**


### Lessons learned
- `nc -l PORT` pozwala utworzyć prosty **TCP listener**.
- `./suconnect PORT` działa jako **klient TCP**, który łączy się z `localhost` na wskazanym porcie.
- `localhost` (`127.0.0.1`) oznacza tę samą maszynę, na której aktualnie pracujemy.
- Dwa procesy mogą komunikować się ze sobą przez TCP nawet wtedy, gdy działają na **tej samej maszynie**.
- TCP jest połączeniem dwukierunkowym — po ustanowieniu połączenia obie strony mogą wysyłać i odbierać dane.