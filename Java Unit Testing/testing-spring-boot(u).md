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

> Continuous Deployment is the process of generating the artifact if the CI process (testing phase, quality check, dependency check, etc.) is executed successfully. Continuous Delivery means moving the artifact to the live environment and making it accessible by the end user. 

* TDD is widely considered a **best practice** in software development.

> opt + enter to the class name in intelliJ to create test class (X -> XTest)


## Section 3: Test Driven Development By Example

* Steps of TDD: https://prnt.sc/Sva2DRKhXFnK
    1. Told a story about how we wanted to view on operation (in test). https://prnt.sc/K6zWMTo_e50h
    2. Make the code compiling but failing the test. https://prnt.sc/SyUuO_r8FvfP
    3. Write AWFUL code to pass the test. https://prnt.sc/GhJfjm0hFhnl
    4. Refactor. https://prnt.sc/prQ3ybaqSDp1
    
* TDD Cycle Review:
    1. Write a Test: Think about how the code should work.
    2. Make it Run: Quickly get the code working. Make the test "Green"
    3. Make it Right: Refactor the running code to quality, proper code.
    
**Degenerate Classes/Objects.** 
[Stackoverflow](https://stackoverflow.com/a/24382345/15258184)
[TDD by Kent Beck](https://dev.to/edgenard/chapter-2-degenerate-objects-1mgj)
-> In our money example, since we were mutating the actual object in the "times" method, the second assertion did not work as expected. In this situation, instead of mutating the object variable, we made the "times" method returning a "Dollar" object with the intended amount variable assigned to it. WHAT IS THE DEGENERATE CLASS HERE??

 Any wrapper class that is intended for classifying object variables (Point.class -> int x, int y) is also an example of "degenerate"

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



# 02/21/2024:

* You can run "**mvn test**" to make sure that there is no any problem with the application setup (maven dependencies).

> Only executing the mvn test script will also trigger the mvn compile.

* maven-surefire-plugin and maven-failsafe-plugins are required for running JUnit in our application. maven-surefire-plugin is designed for running unit tests and if any of the tests fail then it will fail the build immediately. maven-failsafe-plugin is designed for running integration tests, and decouples failing the build if there are test failures from actually running the tests.

* Use @BeforeEach annotation as a setUp method that will be executed before each @Test.

[JUnit 5 Test Lifecycle](https://prnt.sc/JlsRmDT0KNal) -> @BeforeAll, @BeforeEach, @Test, @AfterEach, @AfterAll

@BeforeAll and @AfterAll's scope is the test class. (not the whole test package)

mvn clean test
./mvnw clean test
Both of these scripts will trigger the maven clean and test steps, respectively. The difference is that the 'mvn' uses the local environment maven and 'mvnw' (maven wrapper) uses the project maven that is nested within the project folder for the execution. (Be wary of the stale maven version if using 'mvn')

[JUnit 5 Class Assertions](https://junit.org/junit5/docs/5.0.1/api/org/junit/jupiter/api/Assertions.html)

[Using Lambda in JUnit assertions](https://prnt.sc/fODKqNlTY1sV)
Because the lambda expressions are evaluated lazily, they provide a better performance for the application as opposed the traditional java methods. If you have an expensive operation for a message generation for a failing test, using lambda expressions will do the job perfectly.

* Grouped Assertions: Set of assertions that are not blocked by each other in case of failing. 
Example: https://prnt.sc/gkhgmlWYaXFy
!! The expected (true) value must come first, in the example it is the other way around.


* Dependent Assertions: 'Nested' set of assertions that are not blocked by each other in case of failing.
You can go down multiple layers of assertAll() 
Example: https://prnt.sc/E7TT4-Kzkm53


* @Disabled for ignoring tests. It can also be called at the class level. 
You can set a 'value' property as a reminder for why you disabled the test/class.


* @DisplayName for assigning a name for a test. It will appear on the "Test Results" section in intelliJ. Even emojis are allowed.
Example: https://prnt.sc/lMW8icbHTC_u


* Expected Exception: When the output is an exception use assertThrows() assertion. The first argument is the type of the exception that is expected to be thrown. The second argument is a lambda expression that contains the assertion body. If the exception is no thrown, the test will fail.
Example: https://prnt.sc/vHuvc4ykwJz4


* Test Timeouts: As opposed to assertTimeout, assertTimeoutPreemptively will execute the assertion body on a seperate thread which allows the application to terminate the test if the execution of the test took longer than expected. assertTimeout however, does wait for the test to make the assertion which might take forever. 
Examples: https://prnt.sc/CsdvzGGzD1Oz
