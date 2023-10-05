# postcode-validator

A library to validate United Kingdom(UK) postcodes. These are mailing addresses that follow a scrict format that this library will help in reducing false and incorrect postcodes.

I have included built distos of this library in /dist

## Example usage
```
from postcode_validator import postcode_validator

if postcode_validator.pc_validate("M1 1AE") == True:
  print("Valid Postcode")
else:
  print("Invalid Postcode")
```

Terminal Output:
```
╭─benclarke@SkyNet ~/code/ScurriCodingPuzzle/postcode_validator  ‹main*› 
╰─➤  python3 example.py
Valid Postcode
```
