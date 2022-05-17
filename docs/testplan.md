# SSN (Social Security Number) Validator

# Test Plan

## Index
1. [Positive Scenarios](#positive-scenarios)
2. [Negative Scenarios](#negative-scenarios)

## Positive Scenarios (Valid Data)

### Test Cases

* **PTC-1:** 005232002 should return 005-23-2002 with a message that says it is a valid SSN.

* **PTC-2:** 868762457 should return 868-76-2457 with a message that says it is a valid SSN.

## Negative Scenarios (Invalid Data)

### Test Cases

* **NTC-1:** Any character input other than numbers such as 005df2002 should return a message that says it is an invalid SSN explaining that it shouldn't be letters.

* **NTC-2:** Any input that doesn't match the correct length (three / two / four) will return the SSN with a message explaining the error.

* **NTC-3:** 000232002 should return 000-23-2002 with a message that says it is not a valid SSN explaining that the first three numbers cannot be 000.

* **NTC-4:** 666232002 should return 666-23-2002 with a message that says it is not a valid SSN explaining that the first three numbers cannot be 666.

* **NTC-5:** 945232002 should return 945-23-2002 with a message that says it is not a valid SSN explaining that the first three numbers cannot be greater than 900.

* **NTC-6:** 005002002 should return 005-00-2002 with a message that says it is not a valid SSN explaining that the second combination must be between 01 and 99.

* **NTC-7:** 005-23-0000 should return 005-23-0000 with a message that says it is not a valid SSN explaining that the third combination must be between 0001 and 9999.