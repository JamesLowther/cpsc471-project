INSERT INTO Patient VALUES
  (012345678, "pass");

INSERT INTO Doctor VALUES
  (222111222, "GP", "Brody", "Wells", NULL, "1990-01-01", "pass123");

INSERT INTO Clerk VALUES
  (333888333, "Justin", "P", "Trudeau", "1990-01-01", "primePass");

INSERT INTO Report VALUES
  (0, 012345678, 222111222),
  (1, 012345678, 222111222);

-- INSERT INTO New_Applicant_Form VALUES
--   ("test@test.com", 012345678, "M", "M", "1234443323", "James", "E", "Lowther", "123122", "01/02/03", "AB", "10/10/10");