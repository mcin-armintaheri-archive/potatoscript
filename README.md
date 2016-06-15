# potatoscript
PotatoScript is a simple general programming language. Write a .tater script to do anything you want!


# Specification
primitive types:
 - Bool 
 - Number
 - Char
 - String

structural types:
 - Map
 - List

```
If statement:
if conditional-expression then
  expression1
else 
  expression2
done

Switch statement:
switch expression
 | expression1 -> output-expression1
 | expression2 -> output-expression2
 | otherwise -> default-expression
done

Function declaration:
function sum(n) = expression;

Expressions = 
 {expression}
 (expression)
 let (bindings) in expression
 if-statement
 switch-statement
 function call
 binary expressions (+ - / * ** && || == =/= < > <= >=)
 unary expression (- not)

Stateful operations:
do
  statements
done

Statement:
  assignment: set line1 to readLine()
  function call: writeLine('I love taters')

Let bindings:
function add8and12 = {
  let (
    double4 = double(4);
    double6 = double(6);
  ) in {
    double4 + double6;
  };
};
```
