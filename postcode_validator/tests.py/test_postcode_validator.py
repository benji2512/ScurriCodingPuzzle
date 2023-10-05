from postcode_validator import postcode_validator

def test_valid_postcode():
  assert postcode_validator.pc_validate("M1 1AE") == True

def test_short_invalid_postcode():
  assert postcode_validator.pc_validate("B 8TH") == False

def test_no_space_valid_postcode():
  assert postcode_validator.pc_validate("SG120ES") == True

def test_valid_postcode_8_space():
  assert postcode_validator.pc_validate("SG12 0ES") == True

def test_valid_postcode_short_no_space():
  assert postcode_validator.pc_validate("L18DS") == True

def test_valid_postcode_short_space():
  assert postcode_validator.pc_validate("L7 7AG") == True

def test_valid_postcode_7_space():
  assert postcode_validator.pc_validate("SG1 8XQ") == True

def test_valid_postcode_6_no_space():
  assert postcode_validator.pc_validate("SG16BG") == True

def test_invalid_postcode_9_space():
  assert postcode_validator.pc_validate("SG12 0ESD") == False
