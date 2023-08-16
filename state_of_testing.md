# State of Software Testing
The art and craft of developing code that capture bugs 

---
# About Me
- 40 summers of coding
- Consulting and developing test automation infrastructure
- Leading Terminal7
---
# One Goal Many Names

```
                           White Box
   Unit                       |              Performance
                              |
  Functional                  |               Load  
                              |
  Regression                  |
                              |               Stress
                              |
  Unit -----------------------+------------------------ Whole
                          Component
                              |         Integration
                              |
                              |                System
                              |                Acceptance
                              |
                          Contract                  Chaos
                              |                      End2End
                          Black Box             Smoke/Sanity
```
---
# Test Driven Development Benefits

1. **Early Bug Detection**: Find and fix issues early.
2. **Improved Code Quality**: Simpler, clearer, and modular code.
3. **Refactoring Confidence**: Safely modify and improve code.
4. **Enhanced Collaboration**: Clearer requirements and shared understanding.
5. **Better Design**: Intuitive, user-centric software.
6. **Built-in Documentation**: Tests highlight intended functionality.
7. **Continuous Feedback**: Immediate insights during development.
8. **Cost Efficiency**: Cheaper to fix bugs during development.
9. **Faster Debugging**: Pinpoint issues quickly.
10. **Peace of Mind**: Reliable, well-tested software.


---
# Testing code is different

- Readability is paramount
- Do repeat yourself
- As little structure as possible
- No Constants
---
# Tests can get ugly
```python
# Test for add(x, y) and multiply(x, y) by ChatGPT4
class BadTestSuite(unittest.TestCase):

    CONSTANTS = [3, 7, 10]

    def helper_function(self, x, y):
        return x * y + self.CONSTANTS[1]

    def test_complicated_addition(self):
        for i in range(1, 5):
            for j in self.CONSTANTS:
                self.assertEqual(add(i, j), self.helper_function(i, j))

    def test_unrelated_maths(self):
        magic_numbers = [i for i in range(10) if i % 2 == 0]
        for magic in magic_numbers:
            self.assertEqual(multiply(magic, 3),
                             add(magic, self.CONSTANTS[2]))
```
---
# Behind Unit Testing
Things get complicated:

- A Virtual Lab
- Servers Doubles (aka Mocks)
- Remote Automation
- Complex State

With so many moving parts, stability is a top challenge
---
# Terminal7's Virtual Lab

- 3 owned project: client, server and peerbook.io
- Redis for PeerBook use
- RevenueCat RESTfull double
- A test runner
---
# Directory Layout
```bash
lsd --tree aatp --depth 1 --icon always --no-symlink
```
---
# Scenario Layout
```bash
lsd --tree aatp/peerbook_webrtc --icon always --no-symlink
```
---
# Defining a virtual lap
```bash
cd aatp
git log --oneline peerbook_webrtc/lab.yaml | cut -f 2- -d " "
```
---
# Running Black Box Tests
Playwright is the clear winner of the browser automation rapid evolution
(sorry Cypress).
```bash
cd aatp
git log --oneline peerbook_webrtc/admin.spec.ts | cut -f 2- -d " "
```

---
# Duping Servers
Tools like wire-mock and mock-server feature:
- Proxy and record responses
- File based configuration 
- Validate Proper Requests were made
```bash
cd aatp
git log --oneline peerbook_webrtc/revenuecat_double.json | cut -f 2- -d " "
```

