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

  # Object References

  """
  What is actually happending when you make a variable assignment?
  This is important question in Python, because the answer differs somewhat from what you'd find in many other programming languages.

  Python is a highly object-oriented language.
  In fact, virtually every item of data in a Python program is an object of a specific type or class.
  (This point will be reiterated many times over the course of these tutorials.)

  Consider this code:
  """

  print(300)

  """
  When presented with the statement print (3000), the interpreter does not the following:
  - Creates an integer object
  - Gives it the value 300
  - Displays it to the console

  You can see that an integer object is created using the built-in type() function:
  """

  print(type(300))

  """
  A Python variable is a symbolic name that is a reference or pointer to an object.
  Once an object is assigned to a variable, you can refer to the object by that name.
  But the data itself is still contained within the object.

  For example:
  """

  n = 300

  """
  This assignment creates an integer object with the value 300 and assign the variable n to point to that object.

  The following code verifies that n points to an integer object:
  """

  print(n)
  print(type(n))

  """
  Now consider the following statement:
  """

  m = n

  """
  What happens when it is executed?
  Python does not create another object.
  It simply creates a new symbolic name or reference, m, which points to the same object that n points to.

  Next, suppose you do this:
  """

  m = 400

  """
  Now Python creates a new integer object with the value 400, and m becomes a reference to it.

  Lastly, suppose this statement is executed next:
  """

  n = "foo"

  """
  Now Python creates a string object with the value "foo" and makes n reference that.

  There is no longer any reference to the integer obejct 300.
  It is orphaned, and there is no way to access it.

  Tutorials in this series will occasionally refer to the lifetime of an object.
  An object's life begins when it is created, at which time at least one reference to it is created.
  During an object's lifetime, addtional references to it may be created, as you saw above, and references to it may be deleted as well.
  An object stays alive, as it were, so long as there is at least one reference to it.

  When the number of references to an object drops to zero, it is no longer accessible.
  At that point, its lifetime is over.
  Python will eventually notice that it is inaccessible and reclaim the allocated memory so it can be used for something else.
  In computer lingo, this process is referred to as garbage collection.
  """

  # Object Identity

  """
  In Python, every object that is created is given a number that uniquely identifies it.
  It is guaranteed that no two objects will hjave the same identifier during any period in which their lifetime overlap.
  Once an object's reference count drops to zero and it is garbage collected, as happened to the 300 object above, then its identifying number becomes available and may be used again.

  The built-in Python function id() returns an object's integer identifier.
  Using the id() function, you can verify that two variables indeed point to the same object:
  """

  n = 300
  m = n
  print(id(n))
  print(id(m))

  m = 400
  print(id(n))
  print(id(m))

  """
  After the assignment m = n, m and n both point to the same object, confirmed by the fact that id(m) and id(n) return the same number.
  Once m is reassigned to 400, m and n point to different objects with different identities.
  """

  # Deep Dive: Caching Small Integer Values

  """
  From what you knwow about variable assignment and object references in Python, the following probably won't surprise you:
  """

  m = 300
  n = 300
  print(id(m))
  print(id(n))

  """
  With the statement m = 300, Python creates an integer object with the value 300 and sets m a reference to it.
  n is then similarly assigned to an integer object with value 30 - but not the same object.
  Thus, they have different identities, which you can verify from the values returned by id().

  But consider this:
  """

  m = 300
  n = 300
  print(id(m))
  print(id(n))

  """
  Here, m and n are separately assigned to integer objects having value 30.
  But in this case, id(m) and id(n) are identical!

  For purposes of optimization, the interpreter creates objects for the integers in the range [-5, 256] at startup, and then reuses them during program execution.
  Thus, when you assign separate variables to an integer value in this range, they will actually reference the same object.
  """

  # Variable Names

  """
  The examples you have seen so far have used short, terse variable names like m and n.
  But variable names can be more verbose.
  In fact, it is usually beneficial if they are because it makes the purpose of the variable more evident at first glance.

  Officially, variable names in Python can be any length and can consist of uppercase and lowercase letters (A-Z, a-z), digits (0-9). and the underscore character (_).
  An addtional restriction is that, although a variable name can contain digits, the first character of a variable name cannot be a digit.

  For example, all of the following are valid variable names:
  """

  name = "Bob"
  Age = 54
  has_W2 = True
  print(name, Age, has_W2)

  """
  But this one is not, because a variable naem can't begin with a digit:
  """

  # 1099_filed = False
  # SyntaxError: invalid token

  """
  Note that case is significant.
  Lowercase and uppercase letters are not the same.
  use of the underscore character is significant as well.
  Each of the following defines a different variable:
  """

  age = 1
  Age = 2
  aGe = 3
  AGE = 4
  a_g_e = 5
  _age = 6
  age_ = 7
  _AGE_ = 8
  print(age, Age, aGe, AGE, a_g_e, _age, age_, _AGE_)

  """
  There is nothing stopping you from creating two different variables in the same program called age and Age, or for that matter agE.
  But it is probably ill-advised.
  It would certainly be likely to confuse anyone trying to read your code,
  and even yourself, after you'd been away from  it awhile.

  It is worthwhile to give a variable a name that is descriptive enough to make clear what it is being used for.
  For example, suppose you are tallying the number of people who have graduated college.
  You could conceivably choose any of the following:
  """

  numberofcollegegraduates = 2500
  NUMBEROFCOLLEGEGRADUATES = 2500
  numberOfCollegeGraduates = 2500
  NumberOfCollegeGraduates = 2500
  number_of_college_graduates = 2500

  print(numberofcollegegraduates,
    NUMBEROFCOLLEGEGRADUATES,
    numberOfCollegeGraduates,
    NumberOfCollegeGraduates,
    number_of_college_graduates)

  """
  All of them are probably better choices than n, or ncg, or the like.
  At least you can tell from the name what the value of the variable is suppose to represent.

  On the other hand, they aren't all necessarily equally legible.
  As with many things, it is a matter of personal preference,
  but most people would find the first two examples,
  whether the letters are all shoved together, to be harder to read,
  particularly the one in all capital leters.
  The most commonly used methods of constructing a multi-word variable name are the last there examples:

  - Camel Case: Second and subsequence words are capitalized, to make word boundaries easier to see.
  (Presumably, it struck someone at some point that the capital letters strewn throughout the variable name vaguely resemble camel humps.)
  - Pascal Case: identical to Camel Case, except the first world is also capitalized
  - Snake Case: Words are seperated by underscores.

  Programmers debate hotly, with surprising fevor, which of these is preferable.
  Decent arguments can be made for all of them.
  Use whichever of three is most visually appearing to you.
  Pick one and use it consistently.

  You will see later that variables aren't the only things that can be given names.
  You can also name functions, classes, modules, and so on.
  The rules that apply to variable names also apply to identifiers, the more general term for names given to program objects.

  The Style Guide for Python Code, also known as PEP 8, contains Naming Conventions that list suggested standard for names of different obejct types.
  PEP 8 includes the following recommendations:
  - Smake Case should be used for functions and variable names.
  - CamelCase should be used for class names.
  (PEP 8 refers to this as the "CapWords" convention.)
  """
