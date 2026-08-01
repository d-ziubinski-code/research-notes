# Bandit Level 13

## Goal

Na tym poziomie nie otrzymujemy hasła do następnego poziomu, ale prywatny klucz SSH, którego możemy użyć do zalogowanie się do następnego poziomu.


host: **bandit.labs.overthewire.org**

nazwa użytkownika: bandit13
hasło: sprawdz level-12

ssh bandit13@bandit.labs.overthewire.org -p 2220

Przydatne komendy:
ssh z flagą -p

### Solution

Po zalogowaniu na konto użytkownika bandit13 i użyciu komendy `ls`, możemy zauważyć plik o nazwie `sshkey.private`

Naszym celem w tym poziomie jest zalogowanie się przy użyciu tego właśnie klucza, więc możemy to zrobić z poziomu serwera:
`ssh -i sshkey.private bandit14@localhost -p 2220`

Otrzymamy błąd:
```
!!! You are trying to log into this SSH server with a password on port 2220 from localhost.
!!! Connecting from localhost is blocked to conserve resources.
!!! Please log out and log in again.
```
Co oznacza że nie zalogujemy się się, będąc zalogowani na jakiekolwiek konto bandit.

Musimy przenieść klucz prywatny na nasz desktop i połączyć się bezpośrednio.

Użyjemy do tego komendy `scp`

Co to `SCP`?
`scp` - (Secure Copy Protocol) - służy do bezpiecznego kopiowania plików pomiędzy komputerami z wykorzystaniem protokołu SSH

`scp` =`cp + SSH`


Nie możemy, z poziomu serwera, połączyć się z naszym hostem, ponieważ nie mamy adresu publicznego oraz port forwardingu na zewnatrz poza siec lokalną. Serwer nas po prostu nie "dosięgnie", bo nie ma technicznie jak.


Możemy jednak z poziomu naszego hosta pobrać plik `sshkey.private` za pomocą `scp`, ponieważ to **nasz host inicjuje połączenie SSH z serwerem OverTheWire**.

Użyjemy:

`scp -P 2220 bandit13@bandit.labs.overthewire.org:sshkey.private . `

W ten sposób mamy klucz prywatny SSH na naszym hoście i możemy przejść do levelu 14.
### Lessons learned

- `scp` wykorzystuje protokół SSH do bezpiecznego kopiowania plików między hostami.
- Połączenie zawsze inicjuje komputer, na którym uruchamiana jest komenda `scp`.
- Prywatne adresy IP (np. `10.0.2.x` w VirtualBox NAT) nie są osiągalne z Internetu bez odpowiedniej konfiguracji sieci.

