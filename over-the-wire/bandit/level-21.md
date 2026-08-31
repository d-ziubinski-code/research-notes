# Bandit Level 20

## Goal

W tym poziomie mamy wskazówkę, że program uruchamia się automatycznie w regularnych odstępach czasu za pośrednictwem crona (harrmonogram zadań oparty na czasie)

Zadanie jest proste, mamy sprawdzić pliki konfiguracyjne w katalogu /etc/cron.d/ i ustalić jakie polecenie się wykonuje.

host: **bandit.labs.overthewire.org**

nazwa użytkownika: `bandit21`  
hasło: sprawdź level-20

`ssh bandit21@bandit.labs.overthewire.org -p 2220`

Przydatne komendy:  
`ssh` z flagą `-p`

### Solution

Po zalogowaniu, przechodzimy do folderu `/etc/cron.d`.
```bash
cd /etc/cron.d
```

Następnie, wyświetlamy co znajduje się w tym folderze.
```bash
ls -la
```


Wynik:
```
drwxr-xr-x   2 root root  4096 Jul  3 16:19 .
drwxr-xr-x 124 root root 12288 Aug 17 21:05 ..
-rw-r--r--   1 root root   102 Nov  5  2025 .placeholder
-r--r-----   1 root root    47 Jun 24 14:59 behemoth4_cleanup
-rw-r--r--   1 root root   127 Jul  3 16:19 clean_tmp
-rw-r--r--   1 root root   120 Jun 24 14:58 cronjob_bandit22
-rw-r--r--   1 root root   122 Jun 24 14:58 cronjob_bandit23
-rw-r--r--   1 root root   120 Jun 24 14:59 cronjob_bandit24
-rw-r--r--   1 root root   188 Feb 13  2026 e2scrub_all
-r--r-----   1 root root    48 Jun 24 15:00 leviathan5_cleanup
-rw-------   1 root root   138 Jun 24 15:01 manpage3_resetpw_job
-rwx------   1 root root    52 Jun 24 15:02 otw-tmp-dir
```

Jak widzimy, znajduje się w nim kilka plików.

Nas - ze względu na to, że szukamy hasła do następnego (`22`) poziomu - powinien interesować plik `cronjob_bandit22`

Najpierw sprawdźmy jaki format ma naprawdę ten plik:
```bash
file cronjob_bandit22
```

Wynik:
```
cronjob_bandit22: ASCII text
```

Jak widzimy, jest to zwykły plik tekstowy, możemy w takim razie wyświetlić jego zawartość:
```bash
cat cronjob_bandit22
```

Wynik:
```
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
```

Skrypt jest uruchamiany jako użytkownik `bandit22`: raz przy starcie systemu (`@reboot`) oraz dodatkowo co minutę (`* * * * *`)

Z poziomu folderu `etc/cron.d`
Sprawdźmy co to za plik i jaka jest jego zawartość:

`file file ../../usr/bin/cronjob_bandit22.sh`

Wynik:
`../../usr/bin/cronjob_bandit22.sh: Bourne-Again shell script, ASCII text executable
` 
jest to skrypt, wyświetlmy jego zawartość:
```bash
cat ../../usr/bin/cronjob_bandit22.sh
```

Wynik:
```
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

Skrypt wyświetla plik `/etc/bandit_pass/bandit22` i kopiuje jego zawartość do `/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv`

Sprawdźmy zawartość tego pliku

```bash
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

Mamy hasło do następnego poziomu :)
### Lessons learned

- **Cron służy do automatycznego wykonywania poleceń w określonych odstępach czasu.** Konfiguracje zadań systemowych można znaleźć m.in. w `/etc/cron.d/`.
- **Wpis crona określa użytkownika, jako którego wykonywane jest polecenie.** W tym przypadku zadanie uruchamia skrypt jako `bandit22`.
- **Warto sprawdzać pliki wskazane przez konfigurację zamiast zatrzymywać się na samym wpisie crona.** `cronjob_bandit22` wskazywał na `/usr/bin/cronjob_bandit22.sh`, a dopiero ten skrypt ujawnił właściwą logikę.
- - **Ważne jest śledzenie całego przepływu danych:** cron → skrypt → plik źródłowy → plik tymczasowy → wynik.
- **Uprawnienia plików mają znaczenie.** `chmod 644` sprawia, że utworzony plik jest możliwy do odczytania przez innych użytkowników.
- **Nie zawsze trzeba atakować sam proces — czasami wystarczy znaleźć jego artefakt.** Tutaj hasło zostało zapisane przez skrypt w `/tmp`, więc mogliśmy odczytać właśnie ten plik.