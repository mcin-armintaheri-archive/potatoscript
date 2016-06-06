# potatoscript
PotatoScript is a simple general programming language. Write a .tater script to do anything you want!


# Specification

if, while loops, function declaration, variables, functions are first class citizen, objects x = {one: "hello", two: "world"}


primitive types:
 - Bool 
 - Number
 - Char
 - String

structural types:
 - Map
 - List

Linked list:
  `[value|-]->[value|-]->[value|-]->[value|-]->[value|null]`

```
if conditional-expression then
  expression1
else 
  expression2

function sum(n) = expression

expression = 
 {expression}
 let (bindings) in expression
 if-statement
 function call
 binary expressions (+ - / * ** && || == =/= < > <= >=)
 unary expression (- not)

do
  statements
done

statement
  assignment: set line1 to readLine()
  function call:


function double(arg1, arg2, arg3) = expression

function add8and12 = {
  let (
    double4 = double(4);
    double6 = double(6);
  ) in {
    double4 + double6;
  }
}
```
