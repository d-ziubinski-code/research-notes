# Bandit Level 19

## Goal

Ten level wymaga od nas użycia pliku binarnego z ustawionym bitem `setuid` znajdującego się w katalogu `/home` użytkownika.

host: **bandit.labs.overthewire.org**

nazwa użytkownika: `bandit19`  
hasło: sprawdź level-18

`ssh bandit19@bandit.labs.overthewire.org -p 2220`

Przydatne komendy:  
`ssh` z flagą `-p`

### Solution

Po zalogowaniu sprawdzamy zawartość katalogu home razem z flagą odpowiadającą za wyświetlanie uprawnień. Użyjemy polecenia `ls -la`.

Jednym ze zwróconych w ten sposób elementów jest:

`-rwsr-x--- 1 bandit20 bandit19 14880 Jun 24 14:59 bandit20-do`

Jak możemy zauważyć, w uprawnieniach pliku mamy wartość `-rws-`, zamiast klasycznego `-rwx-`.

`s` znajduje się w pierwszej grupie uprawnień, czyli w miejscu `x` ownera. To oznacza SUID.

W przypadku **pliku wykonywalnego** SUID powoduje, że program uruchamia się z uprawnieniami właściciela pliku, a nie osoby, która go uruchomiła.

Sprawdzamy działanie pliku:

`./bandit20-do`

Wynik:

```text
Run a command as another user.
  Example: ./bandit20-do whoami
```

Z opisu programu możemy wywnioskować, że służy on do wykonywania komend jako użytkownik `bandit20`.

Sprawdzamy to za pomocą komendy `whoami`.

```text
bandit19@bandit:~$ ./bandit20-do whoami
bandit20
```

Jak widzimy, komenda została wykonana z poziomu usera `bandit20`. Stało się to ze względu na `s` w uprawnieniach, które omówiliśmy wcześniej.

Z treści zadania, jak i z poprzednich zadań, wiemy, że hasła do wszystkich poziomów znajdują się w folderze `/etc/bandit_pass` pod nazwą usera.

Możemy sprawdzić, jakie uprawnienia są ustawione na pliku z hasłem.

Z poziomu home wykonujemy komendę:

`ls -l ../../etc/bandit_pass/bandit20`

Wynik:

`-r-------- 1 bandit20 bandit20 33 Jun 24 14:58 ../../etc/bandit_pass/bandit20`

Oznacza to, że owner ma uprawnienia tylko do czytania pliku (wynika to też z poprzednich poziomów).

W takim razie, jeśli program w naszym home `./bandit20-do` jest w stanie wykonywać uprawnienia użytkownika, który jest ownerem tego pliku (`bandit20`), a uprawnienia do pliku `/etc/bandit_pass/bandit20` wskazują na możliwość przeczytania hasła przez ownera, możemy wykorzystać nasz program do odczytania zawartości pliku.

Używając naszego programu i komendy `cat` możemy przeczytać zawartość pliku:

`./bandit20-do cat ../../etc/bandit_pass/bandit20`

Mamy hasło.

## Skąd wiedzieć jakie komendy działają?

Nie wiemy z góry.

SUID nie daje listy typu „te komendy tak / te nie”. On daje uprawnienia procesu. To, czy konkretna komenda z nich skorzysta, zależy od tego, co ta komenda robi.

## Schemat myślenia przy SUID

1. **Sprawdź, kto jest właścicielem programu**
    
    ```bash
    ls -l program
    ```
    
    - Zwróć uwagę na ownera i grupę.
    - Ustal, z uprawnieniami którego użytkownika program może się wykonywać.
2. **Sprawdź, co właściwie robi program**
    
    ```bash
    ./program
    strings program
    file program
    ```
    
    - Uruchom program i obserwuj jego zachowanie.
    - `strings` może ujawnić komunikaty, ścieżki lub używane polecenia.
    - `file` pozwala ustalić typ pliku.
3. **Sprawdź, co możesz zrobić z uprawnieniami ownera**
    
    ```bash
    ls -l /jakis/plik
    ```
    
    Następnie zadaj sobie pytanie:
    
    Czy użytkownik, z którego uprawnieniami działa SUID, może ten plik czytać, zapisywać lub wykonywać?
    
4. **Ustal, jakiej operacji potrzebujesz**
    
    Nie zaczynaj od pytania:
    
     „Jaką komendę mam wpisać do SUID?”
    
    Najpierw określ:
    
     **„Jaką operację chcę wykonać?”**
    
5. **Dobierz program do operacji**
    
    - Chcesz **czytać plik** → `cat`
    - Chcesz **sprawdzić użytkownika** → `id`, `whoami`
    - Chcesz **wyszukać plik lub coś w systemie** → `find`
    - Chcesz **wyszukać tekst** → `grep`
6. **Połącz operację z uprawnieniami**
    
    Ostateczne pytanie brzmi:
    
     **„Czy program, który potrafi wykonać potrzebną mi operację, może zostać uruchomiony z uprawnieniami użytkownika właściciela SUID?”**
    

### Najważniejsza zasada

 **Nie szukaj komendy do SUID. Najpierw określ operację, którą chcesz wykonać, a dopiero potem znajdź program, który potrafi ją wykonać.**

### Lessons learned

- `SUID` nie oznacza zmiany użytkownika, tylko wykonywanie programu z uprawnieniami właściciela pliku.
- `s` w miejscu `x` oznacza SUID.
- Właściciel pliku i użytkownik uruchamiający plik to dwie różne rzeczy.
- `id` pozwala sprawdzić różnicę pomiędzy `uid` i `euid`.
- `euid` określa, z uprawnieniami którego użytkownika wykonywane są operacje.
- SUID dotyczy procesu, a nie automatycznie każdej kolejnej powłoki.
- Nie każda komenda zachowuje się tak samo po uruchomieniu przez program SUID.
- Przy analizowaniu SUID należy sprawdzić, kto jest właścicielem programu, jakie ma uprawnienia oraz do czego ten użytkownik ma dostęp.
- Najpierw należy określić operację, którą chcemy wykonać, a dopiero później dobrać odpowiednią komendę.