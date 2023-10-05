import re

def pc_validate(postcode: str):
  """
  A function to validate a United Kingdom Postcode
  Function accepts 1 argument, which must be a string.
  :param postcode: the postcode to be validated
  """
  postcode_check = re.fullmatch('^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$', postcode)
  return postcode_check != None

