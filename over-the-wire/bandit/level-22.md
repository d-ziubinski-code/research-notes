# Bandit Level 22

## Goal

W tym poziomie znowu pracujemy z  cronem

Musimy sprawdzić pliki konfiguracyjne w katalogu /etc/cron.d/ i ustalić jakie polecenie się wykonuje.

host: **bandit.labs.overthewire.org**

nazwa użytkownika: `bandit22`  
hasło: sprawdź level-21

`ssh bandit22@bandit.labs.overthewire.org -p 2220`

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
total 56
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

Nas - ze względu na to, że szukamy hasła do następnego (`23`) poziomu - powinien interesować plik `cronjob_bandit23`

Najpierw sprawdźmy jaki format ma naprawdę ten plik:
```bash
file cronjob_bandit23
```

Wynik:
```
cronjob_bandit23: ASCII text
```

Jak widzimy, jest to zwykły plik tekstowy, możemy w takim razie wyświetlić jego zawartość:
```bash
cat cronjob_bandit23
```

Wynik:
```
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null

```

Tak jak w poprzednim levelu, skrypt jest uruchamiany jako użytkownik `bandit23`: raz przy starcie systemu (`@reboot`) oraz dodatkowo co minutę (`* * * * *`)

Z poziomu folderu `etc/cron.d`
Sprawdźmy co to za plik i jaka jest jego zawartość:

Właścicielem pliku jest `bandit23`

`file ../../usr/bin/cronjob_bandit23.sh`

Wynik:
`../../usr/bin/cronjob_bandit22.sh: Bourne-Again shell script, ASCII text executable
` 
jest to skrypt, wyświetlmy jego zawartość:
```bash
cat ../../usr/bin/cronjob_bandit23.sh
```

Wynik:
```
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```

Skrypt kolejno:
- Tworzy zmienna myname, wywołując komende `whoami`
- Tworzy string mytarget za pomocą pipeline'u kolejno wyswietla za pomoca echo tekst, nastepnie oblicza sume kontrolna MD5 dla tekstu, nastepnie za pomoca polecenia cut wycinamy pierwsza kolumne
- skrypt odczytuje plik z `/etc/bandit_pass/$myname` i przekierowuje (`>`) jego zawartość do `/tmp/$mytarget`. Nie wyświetla niczego na ekranie (wszystko leci do pliku, a w cronie standardowe wyjście i błędy są wyciszone przez `&> /dev/null`

Aby dowiedziec się jaka to nazwa możemy odpalic ten pipeline podstawiajac odpowiednia nazwe usera

W naszym terminalu:
```bash
echo I am user bandit23 | md5sum | cut -d ' ' -f 1
```

Wynik: 
`8ca319486bfbbc3663ea0fbe81326349`

Wysiwietlmy zawartosc pliku z ta nazwa:
```bash
cat ../../tmp/8ca319486bfbbc3663ea0fbe81326349
```

Mamy hasło do poziomy 23 :)
### Lessons learned

- **Podatność (Insecure Temporary File):** Zapisywanie wrażliwych danych (np. haseł) do `/tmp` pod przewidywalną nazwą to poważny błąd projektowy.
- **Determinizm MD5:** Funkcja MD5 dla tego samego ciągu znaków zawsze daje ten sam wynik, co pozwala bez zgadywania i bez uprawnień do podglądu `/tmp` poznać dokładną nazwę pliku docelowego.
- **Wektor Privilege Escalation:** Cykliczne skrypty Crona uruchamiane przez uprzywilejowane konta to częsty cel – zamiast zgadywać pliki, kluczem jest przeanalizowanie ich kodu źródłowego i odtworzenie logiki zmiennych w lokalnej powłoce.

