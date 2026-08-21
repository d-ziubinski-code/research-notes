# Bandit Level 17

## Goal

Na tym poziomie, po zalogowaniu kluczem prywatnym SSH musimy sprawdzić czym różni się content dwoch plików `passwords.old`, `passwords.new`


host: **bandit.labs.overthewire.org**

nazwa użytkownika: `bandit17`
hasło: sprawdz level-16

`ssh -i bandit17.key bandit17@bandit.labs.overthewire.org -p 2220`

Przydatne komendy:
`ssh z flagą -p`

### Solution

Logujemy się do konta bandit17 po ssh za pomocą klucza prywatnego.

Po zalogowaniu możemy sprawdzić co znajduje sie w naszym katalogu `/home` komendą `ls`

Widzimy dwa pliki, możemy sprawdzić ich typ za pomocą komendy `file`

Oba pliki są tekstowe, zapisane w formacie ASCII:
```
passwords.old: ASCII text
passwords.new: ASCII text
```

Ab znaleźć hasło do następnego poziomu, musimy porównać zawartość obydwu plików. Użyjemy do tego komendy `diff`:

```
diff passwords.old passwords.new
```

Nasze hasło znajduje się w pliku `passwords.new`
### Lessons learned

- `diff` analizuje pliki linia po linii. Znak `<` wskazuje linię obecną w pierwszym pliku, znak `>` wskazuje nową, zmienioną linię z drugiego pliku.

