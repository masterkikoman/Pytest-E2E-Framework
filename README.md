# knowell.almazan

1. What other possible scenario’s would you suggest for testing the Jupiter Toys application?
   - I would add checking for telephone name since it is not mandatory to check if fields are accepting only integer values.
   - I will test the whole checkout process upto ordering of my items
   - test the cart page fields after check out (e.g, Personal info field, Credit card field)
   - Verify if i had successfully order with invoice



2. Jupiter Toys is expected to grow and expand its offering into books, tech, and modern art. We are expecting the of tests will grow to a very large number.
What approaches could you used to reduce overall execution time?
  - identify all tests that are repeatable and divide it into small tests.
  - Do parallel test execution.
  - Use waits smartly.
  - Identify the critical tests that needs to be retested.
  - Use headless capabilities.
  - Utilize API services (if there are any) so that we can focus on the webservice and not the UI.
  
How will your framework cater for this?
  - My framework can be optimize and can be also integrated in a CI environment. I can test and divide all test cases into small but readable test cases.
  - Framework can also be used in API automation so that if ever needed, we can utilize this framework in order for us to test more services rather than UI.
  
3. Describe when to use a BDD approach to automation and when NOT to use BDD 
  - If a lot of business people are involve in the project and they need to input acceptance criteria, BDD is better.
  - BDD if there are a lot of collaboration between Business people and dev and qa team.
  - If results and tests are needed for readability of non-technical people, BDD is better.
  - If poeple or business are not interested on the readability reports, collaboration, they just need the test results, I think Non-BDD approach can be use.
  - If project does not require a lot of collaboration between parties, non-BDD is ok.
  
