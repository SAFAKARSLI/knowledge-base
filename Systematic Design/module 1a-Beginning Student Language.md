# 01/31/2024:

- Why do we care about systematic design?
* The desing method allows us to:
    1. Understand the problem we are trying the solve, therefore the aspects of our application.
    2. Break the problem into the well-chosen smaller pieces.
    3. Write one part of the program for each piece of the problem. With this approach the program is easy to 
    read anb easy to modify. This trait of the program will allow you to easily test the application. 


- What is BSL?
* (B)eginning (S)tudent (L)anguage.  


- In the words of a former student:
* It's funny how repetuition in actually doing the work leads to it all of a sudden making sense to me. I can't explain it. I don't have a sense of growing understanding. I have confusion, repetition, and suddenly a sense of understanding. It's not coming through watching or reading, though. **It comes from replicating what I've watched several times.** This has happened repetedly for me in this class. I start the week with a sense of accomplishment, well being, peace of mind, and confidence from the victory over last week's homework. I am then submerged in doubt, confusion, and erm, terror. (Why not be melodramatic?) Suddenly there is a working epiphany and I have victory again. 


- Learning Goals of the first module (Beginning Student Language)
* Be able to write expressions that operate on primitive data including numbers, strings, images, and booleans.
* Be able to write constant and function definitions.
* Be able to write out the step-by-step evaluation of simple expressions including function calls.
* Be able to use the stepper to automatically step through the evaluation of an expression.
* Be able to use the DrRacket help desk to discover new primitives.


- What are primitive calls (expressions)? 
* A primitive call is an expression that starts with an open paranthesis and a primitive operator. Anything that comes after the operator is called opperand which can either be some other primitive call or a value (number) 
Example: (Pythagorean Theorem) = (sqrt (+ (sqr 3) (sqr 4))) 


- What are some agraggate functions in BSL?
* sqr, sqrt (square root)

- Explain the behavior of the BSL
* BSL works from left to right, inside to outside. 


- How to append strings in BSL? 
* There are speacial string operators, e.g. string-append, string-lenght, substring.

> "+" operator is not allowed for strings.  


- Using image operators in BSL 
* Some of them are "circle", "rectangle", "text", "above", "overlay". In order to use them, we must require ("import") the 2htdp/image package. 
https://prnt.sc/U0kOVzqpEC2M
https://prnt.sc/aIcOrM_l9Md4
https://prnt.sc/VD6ZFYbi_yMg
https://prnt.sc/Z_FLtCPwajUm -> Note that the order of the expressions is important. (First expression goes above.)


- Constant declaration and how to rotate image.
* (define <name> <expression>). Expression part gets evaluated and stored in the memory with the reference of <name>. So the <expression> part doesn't have to be a value, it can rather be a primitive call (expression).
* [An interesting image feature in BSL and 'rotate' operation on an image.](https://prnt.sc/-IyNAP8PR7vc)


- Funciton definition.
* (define (<name>(function name)  <name>(parameters)...)
     <expression>(function body))
* [Usage examples of functions.](https://prnt.sc/LXM_3r3SHiYg)
* [1 line body restraint in BSL](https://prnt.sc/3BgF90nmt-Ze)







# 02/01/2024:

- With a programming language that only gives you the ability of "creating functions" you can do everything that any could do with any other programming langauge. Functions are the building blocks of coding.

- Booleans and Conditions in BSL:
* An expression or a function that produces a boolean is called **predicate**.
* [Basic boolean operations](https://prnt.sc/qbHtN4Bo2QMu)
* Sudo: (if <expression> (question: true?/false?)
        <expression> (true answer)
        <expression> (false answer))
* [Usage of if statement](https://prnt.sc/XmeLx1irPrct)


- [Handling multiple if statments. (and/or)](https://prnt.sc/3Cco7q-gX7n0)

- Use "Stepper" functionality to see step by step evalutaion of the BSL.

- Utilizing "Help Desk" for learning/discovering more about DrRacket (more primitives, built-in fuctions, etc.).
