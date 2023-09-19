# Cracking the Code

A Deep Dive into Automated Testing Strategies

> "Software testing can be used to show the presence of bugs, but never to show their absence." - Edsger Dijkstra

---
# About Me
- Programming since the 8bit days
- Co-founder of Open Knesset and The Public Knowledge Workshop
- Consulting and developing test automation infrastructure
- Leading Terminal7 - probably the best terminal in the world
- @daonb on X & github
---
# Why start with tests?


```




Will it                                           Will it 
always work?                                      pass review?

-------------------------------------------------------------->
                            time 
```
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
# Testing code is different

- Readability is paramount
- Do repeat yourself
- As little structure as possible
- Few util functions
- No Constants 
---
# Doing it wrong
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
The enviornment gets complicated:

- A Virtual Lab
- Servers Doubles (aka Mocks)
- Remote Automation
- Complex State

With so many moving parts, stability is a constant challenge
---
# Breaking it to Three Layers

- Testing Suite
- Local Infrastructure
- Global Infrastructure
---
# Terminal7's Virtual Lab
```bash
imgcat vlab.png
```
---
# All in one simple workflow

```bash
bat ./workflows/test.yml
```
---
# Directory Layout
```bash
lsd --tree aatp --depth 2 --icon always --no-symlink
```
---
# Scenario Layout
```bash
lsd --tree aatp/peerbook_webrtc --icon always --no-symlink
```
---
# Defining a virtual lap
```bash
bat aatp/peerbook_webrtc/lab.yaml
```
---
# Running Black Box Tests
Playwright is the clear winner of the browser automation rapid evolution
(sorry Cypress).

---
# HTTP Servers Doubles
Tools like wire-mock and mock-server feature:
- Proxy and record responses
- File based configuration 
- RESTfull API to assrt proper requests were made
```bash
cd aatp
bat peerbook_webrtc/revenuecat_double.json
```
---
# Summary

- More tests, less bugs
- Invest in tools and infrastructure
- The open source stack is here, use it

## Thanks to Ronen Levinson for his help

### Q&A

