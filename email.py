from email_validator import validate_email, EmailNotValidError

email = "egoitzaulestia@gmail.com"
is_new_account = True # False for login pages

try:
  # Check that the email address is valid.
  validation = validate_email(email, check_deliverability=is_new_account)

  # Take the normalized form of the email address
  # for all logic beyond this point (especially
  # before going to a database query where equality
  # may not take into account Unicode normalization).  
  email = validation.email
except EmailNotValidError as e:
  # Email is not valid.
  # The exception message is human-readable.
  print(str(e))
