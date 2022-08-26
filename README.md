![](https://img.shields.io/badge/version-v0.4.1-gold)  
![](https://img.shields.io/badge/python-v3.10.1-blue)
![](https://img.shields.io/badge/Flask-v2.1.2-pink)
![](https://img.shields.io/badge/Docker-v20.10.17-orange)

![](https://img.shields.io/badge/pytest-v7.1.2-black)
![](https://img.shields.io/badge/passed_tests-16-brightgreen)
![](https://img.shields.io/badge/failed_tests-0-red)

![](https://img.shields.io/badge/coverage-100%25-brightgreen)

# Shape Challenge
The challenge was to build an API which could receive a number, encode it, and after get the encoded value, and decode it back.
The whole solution was built with `Flask`, tested with `pytest`, and documented with `flask-restx`.

## The Encode Feature
For encoding the number ina code with fixed six characters, I chose to use base32 with the expanded hexadecimal alphabet

| Decimal | Base32(Hex-like alphabet) | Decimal | Base32(Hex-like alphabet) |
|---------|---------------------------|---------|---------------------------|
| 0       | 0                         | 16      | G                         |
| 1       | 1                         | 17      | H                         |
| 2       | 2                         | 18      | I                         |
| 3       | 3                         | 19      | J                         |
| 4       | 4                         | 20      | K                         |
| 5       | 5                         | 21      | L                         |
| 6       | 6                         | 22      | M                         |
| 7       | 7                         | 23      | N                         |
| 8       | 8                         | 24      | O                         |
| 9       | 9                         | 25      | P                         |
| 10      | A                         | 26      | Q                         |
| 11      | B                         | 27      | R                         |
| 12      | C                         | 28      | S                         |
| 13      | D                         | 29      | T                         |
| 14      | E                         | 30      | U                         |
| 15      | F                         | 31      | V                         |

So I get the number (which must have a maximun of 8 characters) and do the manual conversion from decimal to base32
I had to do the conversion manually because I couldn't find a way to do it properly with `python-base64` library.
The convertions it does are from another base32 pattern, not the extended alphabet.
For manual converting a decimal number to a base32 we need to do like this: