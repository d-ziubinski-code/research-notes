# Vulnerable Auth App

Prosta aplikacja webowa napisana w celu zademonstrowania podatności Login Enumeration oraz Password Brute-Force.

Służy do analizy błędów uwierzytelniania, automatyzacji ataków w Pythonie oraz testowania ruchu HTTP w Burp Suite. 

---

### Szczegóły Techniczne

| Cecha | Opis |
| :--- | :--- |
| **Technologie** | Python, FastAPI, HTML |
| **Główne podatności** | User Enumeration, Brak rate limiting / Lockout mechanism |
| **Narzędzia testowe** | Burp Suite (Intruder), Autorskie skrypty Python |

---

### Struktura Projektu

```text
demo/
├── main.py
├── index.html
└── requirements.tx
