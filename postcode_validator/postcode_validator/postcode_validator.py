import re

def pc_validate(postcode: str):
  postcode_check = re.fullmatch('^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$', postcode)
  if postcode_check == None:
    return False
  else:
    return True

# if __name__ == "__main__":
#   pc_validate("M1 1AE")
