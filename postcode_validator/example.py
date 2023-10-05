from postcode_validator import postcode_validator

if postcode_validator.pc_validate("M1 1AE") == True:
  print("Valid Postcode")
else:
  print("Invalid Postcode")
