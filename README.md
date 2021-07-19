# S_expr_calculator

README

Result: I am following the S-Expression syntax

With Python2:

➜  test python --version
Python 2.7.16
➜  test ./S-Expr-Calculator.py "(add (add (add 10 (add 123 245)) (add 120 121)) (add 342 12 1) (multiply 12 10 (add 1 2) 12 23) ( Multiply 1 12 12) (add 12 12 1))"
100503
➜  test python S-Expr-Calculator.py "(add (add (add 10 (add 123 245)) (add 120 121)) (add 342 12 1) (multiply 12 10 (add 1 2) 12 23) ( Multiply 1 12 12) (add 12 12 1))"
100503

With Python3:
➜  test python3 --version
Python 3.7.4
➜  test python3 S-Expr-Calculator.py "(add (add (add 10 (add 123 245)) (add 120 121)) (add 342 12 1) (multiply 12 10 (add 1 2) 12 23) ( Multiply 1 12 12) (add 12 12 1))"
100503
➜  test

My considerations. Please note that these are additional cases that I could think of:


1.	I used python on a Mac. There are two ways of executing it.
	./S-Expr-Calculator.py
	python S-Expr-Calculator.py

	The code accepts an S-Expression and tries to parse it. The logic is the following.
	Take the right most sub S-Expression, perform the operation, and the result of it is now replaced with the right most expression.
	This is performed in a recursion until there are no paranthesis in the expression, meaning that the count
	of the right paranthesis is 0.

2.	Following error scenarios are handled. An exception is raised if:

	a. there is no S-expression provided as a runtime argument.
	b. count of parathesis do not match.
	c. Keywords other than add and multiply are used.
	d. If the number of operands are less than 2

3. The code will accept more than two operands ands there is no restriction on number of operands.

4. I have used logging package for debugging purposes. This allows better troubleshooting.

5. For any new operation support,  it is just required to add new code for the operation and the remaining code need not be modified.

6. The following three packages were used.

import os
import sys
import logging

7. It should run in python2 and python3.

8. The given expression is converted to lower case first and then actions are performed.

9. I am also stripping the preceeding spaces for the partial expression so that while validating the keywords or while performing operations on the sub S-Expression.
