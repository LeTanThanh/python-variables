if __name__ == "__main__":
  """
  In the previous tutorial on Basic Date Type in Python, you saw how values of various Python data types can be created.
  But so far, all the values shown have been literal or constant values:
  """

  print(5.3)

  """
  If you're writing more complex code, your program will need data that can change as program execution preceeds.

  Here's what you'll learn in this tutorial: You will learn how every item of data in a Python program can be described by the abstract term object, and you'll learn how to manipulate object using symbolic names called variables.
  """

  # Variable Assignment

  """
  Think of a variables as a name attached to a particular object.
  In Python, variables need not be declared or defined in advance, as is the case in many other programming languages.
  To create a variable, you just assign it a value and then start using it.
  Assignment is done with a single equals sign (=):
  """

  n = 300
  print(n)

  """
  Just as a literal value can be displayed directly from the interpreter prompt in a REPL session without the need for print(), so can a variable:

  Later, if you change the value of n and use it again, the new value will be substituted instead:
  """

  n = 1000
  print(n)

  """
  Python also allows chained assignment, which makes it possible to assign the same value to several variables simultaneously:
  """

  a = b = c = 300
  print(a, b, c)

  """
  The chained assignment above assigns 300 to the variables a, b and c simultaneously.
  """

  # Variable Types in Python

  """
  In many programming languages, variables are statically typed.
  That means a variable is initially declared to have a specific data type, and any value assigned to it during its lifetime must always have that type.

  Variables in Python are not subject to this restriction.
  In Python, avariable may be assigned a value of one type and then later re-assign a value of a different type:
  """

  var = 23.5
  print(var)

  var = "Now I'm a string"
  print(var)
