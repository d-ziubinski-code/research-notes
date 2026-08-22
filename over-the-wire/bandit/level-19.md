# Bandit Level 19

## Goal

Ten level wymaga od nas użycia pliku biarnego z ustawionym bitem `setuid` znajdującego się w katalogu `/home` użytkownika. 


host: **bandit.labs.overthewire.org**

nazwa użytkownika: `bandit19
hasło: sprawdz level-18

`ssh bandit19@bandit.labs.overthewire.org -p 2220`

Przydatne komendy:
`ssh z flagą -p`

## Skąd wiedzieć jakie komendy działają?

Nie wiemy z góry.

SUID nie daje listy typu "te komendy tak/ te nie". On daje uprawnienia procesu. To, czy konkretna komenda z nich skorzysta, zależy od tego, co ta komenda robi.

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
    
    > Czy użytkownik, z którego uprawnieniami działa SUID, może ten plik czytać, zapisywać lub wykonywać?
    
4. **Ustal, jakiej operacji potrzebujesz**
    
    Nie zaczynaj od pytania:
    
    > „Jaką komendę mam wpisać do SUID?”
    
    Najpierw określ:
    
    > **„Jaką operację chcę wykonać?”**
    
5. **Dobierz program do operacji**
    
    - Chcesz **czytać plik** → `cat`
    - Chcesz **sprawdzić użytkownika** → `id`, `whoami`
    - Chcesz **wyszukać plik lub coś w systemie** → `find`
    - Chcesz **wyszukać tekst** → `grep`
6. **Połącz operację z uprawnieniami**
    
    Ostateczne pytanie brzmi:
    
    > **„Czy program, który potrafi wykonać potrzebną mi operację, może zostać uruchomiony z uprawnieniami użytkownika właściciela SUID?”**
    

### Najważniejsza zasada

> **Nie szukaj komendy do SUID. Najpierw określ operację, którą chcesz wykonać, a dopiero potem znajdź program, który potrafi ją wykonać.**
	
### Lessons learned

