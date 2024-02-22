# 02/17/2024:

## Section 2: Intorduction to Testing Software

* Code/System Under Test -> code/system that is being tested.
* Ideal code coverage range is ~70-80%

* Testing types:
    * Unit Tests:
        1. Should be "unity" and execute very fast.
        2. Should have no dependency. (Mocking behaviour)
        3. ie no database, Spring context, etc.
    * Integration Tests: 
        1. Designed to test behaviours between objects and parts of the overall system.
        2. Much larger scope.
        3. Can include the database, Spring context, message brokers.
    * Functional Tests:
        1. Typically means you are testing the running application.
        2. Application is live, deployed in a known environment.
        3. Functional touch points are tested.

[Testing Pyramid](https://prnt.sc/P1eLsoY5MbWd)

* Test coverage cannot overcome poor coding practices. ("Clean code", good quality code, etc.)
* Agile Testing Methods -> TDD (code to "fix" tests), BDD (given, when, then)
> Use both of these methods.

[Test Containers](https://prnt.sc/)

> Continuous Deployment is the process of generating the artifact if the CI process (testing phase, quality check, dependency check, etc.) is exectued successfully. Continuous Delivery means moving the artifact to the live environment and making it accessible by the end user. 

* TDD is widely considered a **best practice** in software development.

> opt + enter to the class name in intelliJ to create test class (X -> XTest)


## Section 3: Test Driven Development By Example

* Steps of TDD: https://prnt.sc/Sva2DRKhXFnK
    1. Told a story about how we wanted to view on operation (in test). https://prnt.sc/K6zWMTo_e50h
    2. Make the code compiling but eventually failing. https://prnt.sc/SyUuO_r8FvfP
    3. Write AWFUL code to pass the test. https://prnt.sc/GhJfjm0hFhnl
    4. Refactor. https://prnt.sc/prQ3ybaqSDp1
    
* TDD Cycle Review:
    1. Write a Test: Think about how the code should work.
    2. Make it Run: Quickly get the code working. Make the test "Green"
    3. Make it Right: Refactor the running code to quality, proper code.
    
**Degenerate Classes/Objects.** 
[Stackoverflow](https://stackoverflow.com/a/24382345/15258184)
[TDD by Kent Beck](https://dev.to/edgenard/chapter-2-degenerate-objects-1mgj)
-> In our money example, since we were mutating the actual object in the "times" method, the second assertion did not work as expected. In this situation, instead of mutating the object variable, we made the "times" method returning a "Dollar" object with the intended amount variable assigned to it. Any wrapper class that is intended for classifying object variables (Point.class -> int x, int y) is also an example of "degenerate"

This degenerate chapter discusses that the intention in the TDD is the first getting the "green" passing tests. Then worying about the architecture/design of the system. From that aspect, we wanted to get rid of the "side-effects" of our times method which is being a design concern.

**Equality for All** 
https://prnt.sc/jJ8jynFU_pIa
-> We added "equals()" method to ensure that two objects holding the same _amount_ value are considered as equals. But the implementation lacked certain aspects, e.g. when the null is given or when the given object cannot be casted to dollar.


**Privacy**
https://prnt.sc/WvwMplfGIr8L

-> Only expose what you need to. Private object variables.


**Equality for All, Redux**
https://prnt.sc/Ny691Ph3fJSM
https://prnt.sc/9bQqpxJYbyGY / https://prnt.sc/jovvaeKMjXFW

> However, by adding "Franc" to our code base, we have introduced many duplicate code into our code base which is a major design issue. Also having multiple currencies requires a common way of comparing them.

By creating a common parent class, we have enabled common equality (equals()::Money) but with wrong functionality.


**Apples and Oranges**
https://prnt.sc/-XcqylTOb_Qr

-> Dollar(5) and Franc(5) equality bug is resolved by adding an another condition for equals method. 

return this.amount == object.amount && this.getClass().equals(object.getClass())


**Makin' Objects**
https://github.com/springframeworkguru/tdd-by-example/tree/makenobjects
https://prnt.sc/hVuGk-2VN2q6

-> We got rid of all the direct references of the subclasses in our codebase and used the Money class as a factory class.

In TDD, all you have to focus on is little refactoring that makes the code better quality. When adding a new functionality, the same principle applies. 


# 02/19/2024:

## Section 4: Getting Started with JUnit 5

[JUnit 5 Modules](https://prnt.sc/kWVvjRYrwd81)
[JUnit 5 Test Lifecycle](https://prnt.sc/JlsRmDT0KNal)
[JUnit Dependencies](https://prnt.sc/uhyJC8bYl0FU)
* Managing the dependency versions through environment variables.



