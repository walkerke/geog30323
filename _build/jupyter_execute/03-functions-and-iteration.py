#!/usr/bin/env python
# coding: utf-8

# ## Assignment 3: Functions, conditional statements, and iteration in Python
# 
# Congratulations on completing your first Python assignment!  You'll be progressively building on those core skills throughout the semester.  
# 
# In this week's notebook, you are first going to learn about functions.  Functions are in some ways the bread-and-butter of Python programming.  They make code re-usable, as they allow you to apply your code in other contexts and circumstances.  You can think about functions this way: while variables store elements of your code (e.g. numbers, strings, lists), functions can store entire chunks of your code, which can in turn be re-used as necessary.  
# 
# Functions include a __definition__ and __parameters__, and are specified with `def` as follows: 
# 
# ```python
# def myfunction(parameter1, parameter2, parameter3): 
#     """Your code goes here"""
# ```
# 
# The `def` command allows you to introduce a function definition.  You then specify the __parameters__ within parentheses following the function name, which are like variables that operate within your function.  A colon (`:`) then follows the parentheses, and the contents of the function are found beginning on the next line as an indented code block (more on indentation soon).  
# 
# After you've defined the function, it can be __called__ by supplying __arguments__ to the parameters you've defined, again within parentheses.  For example: 
# 
# ```python
# myfunction(arg1, arg2, arg3)
# ```
# 
# So how does this all work?  Let's try it out!
# 
# At a very basic level, you can define a function without parameters - an _empty_ function.  This function will return whatever you've specified after it is called.  

# In[1]:


def print_five():
    print(5)


# Now, we call the function:    

# In[2]:


print_five()


# Notice what happened when we called our `print_five` function.  As the function has no parameters, it will always give us back 5.  Naturally, you're going to want your functions to get more complicated than this - which is what parameters are for.   Let's try out a function that has a parameter and performs a basic mathematical operation.  

# In[3]:


def divide_by_two(x):
    print(x / 2)

divide_by_two(11)


# The function itself is fairly straightforward.  Our new function, `divide_by_two`, takes a number, which we are calling `x`.  It divides `x` by two, and then prints the result for us.  By adding a parameter, however, our function is now re-usable.  Let's try it out: 

# In[4]:


divide_by_two(55)


# In[5]:


## Now it's your turn!  Write a new, empty function that prints your name when called.  Call the function.


# __The 'return' statement__
# 
# In the above examples, we've created functions that print some result to our screen when called.  Often, however, we want our functions to work as part of a larger workflow.  This is accomplished with the `return` statement, which allows the output of functions to be assigned to a new variable.  
# 
# For example, let's try to assign the result of the `divide_by_two` function to a new variable: 

# In[6]:


y = divide_by_two(12)


# And when we ask Python for the value of y: 

# In[7]:


y


# We don't get anything back.  Now, let's try modifying the function with `return` used instead of `print`.  

# In[8]:


def divide_by_two(x):
    return x / 2

y = divide_by_two(12)

y


# In[9]:


## Now it's your turn!  Write a new function that subtracts 7 from a number
## and returns the result.  Assign the result of the function to a new 
## variable (your argument can be any number you want).


# __Python and whitespace__
# 
# You may have noticed that the statements that follow the function definitions above are __indented__.  Python code obeys __whitespace__ for code organization.  In many languages, functions, loops, and conditional logic (which we'll get to next week), etc. are organized with curly braces, like the equivalent R code below:  
# 
# ```r
# divide_by_two <- function(x) {
#     return(x / 2)
# }
# ```
# 
# The R code, like in many languages, is organized in relation to the position of the curly braces, not the positioning of the code itself per se.  In Python, curly braces are not used in this capacity.  Instead, code is organized by indentation and whitespace.  Within a function definition, for example, the code to be executed by the function call should be indented with four spaces beneath the line that contains the `def` statement.  In many Python IDEs and the IPython Notebook, the software will already know this and indent your code accordingly.  In addition, the Tab key is set to be equivalent to the four spaces in most of these software packages as well.  Without proper indentation, however, your code will not run correctly. 

# In[10]:


def divide_by_three(x):
return x / 3


# __Named arguments__
# 
# Later in the semester, we'll get started using external libraries to do our work, which have many pre-built functions for accomplishing data analysis tasks.  Many of these functions are very flexible - which means they have a lot of parameters!  It turn, it can be helpful to keep your code organized when you are working with multiple parameters in a function.  
# 
# There are a couple ways to supply multiple arguments to a function in Python: 
# 
# * In the order they are specified in the function definition; 
# * As _named_ arguments, in which both the parameter name and the argument are invoked.  
# 
# I'll explain this further.  Let's define a function, `subtract`, that takes two numbers and will subtract the second number from the first.  

# In[11]:


def subtract(x, y):
    return x - y


# Now, we call the function by supplying two arguments to it: 

# In[12]:


subtract(11, 7)


# We could get the same result by supplying _named_ arguments to the function, which take the form of `parameter = argument`: 

# In[13]:


subtract(x = 11, y = 7)


# Flipping the order of the arguments will give us a different result _unless_ we name the arguments accordingly.  Take a look: 

# In[14]:


subtract(7, 11)


# In[15]:


subtract(y = 7, x = 11)


# Be careful when mixing named and unnamed arguments, however.  When arguments are unnamed, Python assumes that you are supplying them in the order of the corresponding parameters in the function definition.  As such, you can mix named and unnamed arguments, but unnamed arguments cannot follow named arguments in a function call.  

# In[16]:


subtract(11, y = 7)


# In[17]:


subtract(x = 11, 7)


# __Docstrings and documenting your code__
# 
# You've already learned how to use comments to document your code with the `#` operator, like this: 
# 
# ```python
# # I just commented out this line!
# ```
# 
# Comments are generally best used for small descriptive statements about your code, or notes to yourself regarding something you'd like to remember.  More formal documentation of your code - e.g. what you functions are supposed to do - are best handled through __docstrings__.  Docstrings are enclosed in triple quotes (`"""`), and can go beneath the function definition to explain its components.  Let's try using a docstring to explain, in basic terms, the contents of our `subtract` function.  

# In[18]:


def subtract(x, y):
    """
    Subtract one number from another.

    Parameters:
    -----------
    x: The number you would like to subtract a quantity from (the minuend).
    y: The quantity you would like to subtract from x (the subtrahend).
    """

    return x - y


# You've now created a new function, `subtract()` with associated help documentation.  To view the documentation, you can use the built-in `help()` function to print the docstring, or type the function name followed by a question mark to pop up the documentation at the bottom of the screen.  Try it out!

# In[19]:


help(subtract)


# In[20]:


get_ipython().run_line_magic('pinfo', 'subtract')


# In[21]:


# Now it is your turn!

# Create a new function, "multiply", that multiplies two numbers together.
# Write a docstring in the function definition that describes what the function does,
# and explains the parameters to the user.
# Run your function and call it to test it out.


# ## Booleans and conditional statements
# 
# The above functions we've written perform the same operations for any input values that are passed to them.  When writing programs, however, you'll often have to design them to be flexible to user input where outcomes may vary based on what users supply to the program.  In regards to data analysis, you might want to produce a particular type of chart if the data are structured a certain way, which wouldn't work in another scenario.  You can build this type of logic into your programs with __conditional statements__.  
# 
# Before we get into this, however, I want to introduce __booleans__ in Python.  You may have heard this term before in other classes.  Booleans in Python are the values `True` and `False`; they can be used to evaluate, understandably, if a condition is true or not.  For example: 

# In[22]:


3 > 2


# In[23]:


2 > 3


# In[24]:


2 == 3


# In[25]:


2 != 3


# In the above lines of code, we used basic mathematical operators to see if conditions are true or false.  When we asked Python if 3 is greater than 2, it told us it was True; when we asked it if 2 is greater than 3, it said False.  Such true/false logic can be used with conditional statements in your code.  To do this, you'll often use __conditional operators__, which you'll be familiar with from basic mathematics, possibly with a couple exceptions.  Conditional operators in Python are as follows: 
# 
# * `<` Less than
# * `>` Greater than
# * `<=` Less than or equal to
# * `>=` Greater than or equal to
# * `==` Is equal to
# * `!=` Is not equal to
# 
# As humans, we use conditional logic all of the time without really thinking about it.  For example, __if__ I am hungry, I'll probably go eat something; otherwise, I won't.  Such logic can be expressed in Python as a series of `if`, `elif` (which means _else if_), and `else` statements.  
# 
# Let's try to express this now in code in basic terms.  This is made-up code, so we don't need to understand everything, but here are the basics of it.  We define a function, `hungry`, that measures the biological/psychological properties that govern hunger reflexes in the human body.  We say, hypothetically, that a hunger index value encapsulating these properties that exceeds 100 means that a person is hungry; in turn, the function returns `True`.  Otherwise, it returns `False`. 

# In[26]:


def hungry(hunger_index):
    if hunger_index > 100:
        return True
    else:
        return False

hungry(103)


# In[27]:


hungry(88)


# We can then pass a variable `kyle`, which represents my hunger index, to the function.  The function then checks to see if I am hungry, and returns `True` if I am, and `False` otherwise.  These results can then be embedded in other workflows, in which you program Python to perform different tasks depending on the function results.  For example: 
# 
# ```python
# if hungry(kyle):  
#     eat()
# else: 
#     stay_put()
# ```
# 
# As you can see above, this can be simplified in Python as the code `if hungry(kyle)` checks to see if the returned value is `True`.  If I am hungry, the code calls an unseen `eat()` function telling me to go eat; otherwise, it tells me to stay put with an unseen `stay_put()` function.  
# 
# Simple enough, right?  Not quite.  I'm hungry right now, but I'm not currently eating.  Why is that the case?  Well... I have to get this assignment written for you!  While I am hungry, my level of hunger is not so debilitating that I am unable to work, and I know that finishing my work is a higher priority than eating at the moment.  In reality, there are countless conditions that influence whether we eat or not beyond simply how hungry we are.  For example - is there food accessible?  Are you in a place where it is socially acceptable to eat?  Perhaps you are at a party where pizza is available - you aren't hungry, but you eat it anyway?  Your brain processes all of this conditional logic at once as you make decisions, so we aren't always used to thinking explicitly about conditionals in such discrete ways.  However, to get a computer to understand this, you have to make it explicit in your code!
# 
# The `hungry` function we defined above used conditional logic, telling Python to return `True` or `False` depending on the value of the hunger index.  Note that the `if` statement starts on a new indented line of code beneath the function definition, and itself is followed by a colon; the code associated with the `if` statement then follows on another, indented line of code.  The same goes for the `else` statement beneath it.  You should be getting a sense now of style rules in Python, and the importance of whitespace for code organization, which applies to conditional statements as well.  
# 
# Now I'd like you to try to replicate this yourself!  Define a function called `greater_than_two` that checks to see if a number is greater than 2 or not.  Call the function.  

# In[28]:


### Your code goes here!


# ### Loops
# 
# In programming, you will often want to do an operation multiple times, or carry out some process over a list of values that you've created.  To do this, you will frequently turn to __iterators__.  
# 
# The most commonly used iterators in Python are `for` and `while`.  A `for` loop carries out an action, or set of actions, for every element that you tell it to.  Let's give it a try in very simple terms.  I've created a list of teams in the Big 12 below; we'll loop through this list with `for` and concatenate another string to each element.  

# In[29]:


big12 = ["TCU Horned Frogs", "Baylor Bears", "Oklahoma Sooners", "Oklahoma State Cowboys", "Texas Longhorns", 
         "Texas Tech Red Raiders", "West Virginia Mountaineers", "Kansas Jayhawks", "Kansas State Wildcats",
         "Iowa State Cyclones"]


# In[30]:


for team in big12: # You can read this here as "for every team in the Big 12....
    print(team + " are in the Big 12.") # ... print the name of the team along with "are in the Big 12."


# A couple notes about the above code.  Notice that I'm using `team` as a temporary variable that will successively store each value of the list as we loop through it.  This variable, `team`, takes on each value of the list in turn; and presently stores the last value of the list. 

# In[31]:


team


# As such, this is how the `for` loop works.  `for` tells Python to evaluate every element of the list `big12`; these elements will be represented by the variable `team`.  The loop then walks through the list `big12` and prints the specified text __for__ every element in the list.  This `for` loop is equivalent, then, to: 
# 
# ```python
# print("TCU Horned Frogs are in the Big 12")
# print("Baylor Bears are in the Big 12")
# print("Oklahoma Sooners are in the Big 12")
# 
# # ... and so forth
# 
# ```
# 
# but you don't really want to do that manually, especially when you might have thousands of strings to evaluate.  In turn, the `for` loop does the work for you, which is one of the main benefits of programming.  
# 
# Also, I'd like you to notice the structure of the loop.  Like functions, loops obey __whitespace__ rules for code organization, and will fail if your code is not properly indented.  The first line of the loop - in this case `for team in big12` - is not indented, and is followed by a colon.  Everything else contained in the loop is found in an indented block on the line(s) following the `for` loop call.  As with functions, your loop will fail without proper indentation.  

# In[32]:


for team in big12: 
print(team + " are in the Big 12.")


# Now let's say you want to create a new list of the "...are in the Big 12" elements.  There are a couple ways to do this.  In the first, you define an empty list object, then populate the list with the for loop and the `append` method, as shown below.  

# In[33]:


teams = [] # The empty brackets designate an empty list, which you'll fill up with the loop.

for team in big12:
    teams.append(team + " are in the Big 12.")

teams


# You can also do the same thing with something called __list comprehension__.  List comprehension allows for the creation of a new list with one line of code.  In this case, the `for` loop is embedded within the statement you make.  Below is an example: 

# In[34]:


teams2 = [team + " are in the Big 12." for team in big12]

teams2


# You can use methods and functions in your list comprehension as well, as in the example below: 

# In[35]:


swap = [name.swapcase() for name in big12]

swap


# Loops also work for strings - though in this case the loop will iterate through each character contained in your string.  An example: 

# In[36]:


tcu = "Texas Christian University"

idx = 0
for character in tcu:
    print("The index of " + character + " is " + str(idx))
    idx = idx + 1


# __The `while` loop__
# 
# `for` is not the only loop you'll come across in Python.  You can also specify a `while` loop, which will run a loop until a given condition is satisfied.  I'll give you an example below.  Let's say you only want to return the first five elements of your list.  While you could do this with indexing (which is simpler), let's try the `while` loop instead. 

# In[37]:


newlist = []

i = 0

while i < 5:
    newlist.append(big12[i])
    i = i + 1

newlist


# Have a look at what we did.  We created an empty list, and set a new variable, `i`, to 0.  We then looped through the elements of the list index by index, adding 1 to `i` with each run of the loop, and then stopping the code when `i` became equal to 5.  In turn, we got back the elements of the `big12` list indexed 0 to 4, which are the first five elements.  
# 
# Be careful with while loops, however.  If you don't specify them correctly, you can get stuck in an infinite loop, which will not stop!  For example, if we had not continued to add 1 to `i`, the loop would have never stopped and would have kept iterating through the list.  This can cause your computer to lock up, as it is infinitely trying to carry out an operation!  I've been there a few times...

# ## Exercises
# 
# As with the previous Jupyter Notebook you worked with, I'll ask you to complete a series of small exercises below to get full credit for this week's assignment.  Some of these exercises will build upon the skills you learned last week - so be prepared!
# 
# __Exercise 1:__ Explain, in your own words, the difference between using `print` and `return` for the output of a function.  Write your response below, in this Markdown cell.  
# 

# __Exercise 2:__ Write a function called `make_big` that takes a lowercase string as input and prints the string with all capital letters.  Create a new variable and assign to it a string with all lowercase letters, then call the `make_big` function with that variable as its argument.  

# In[38]:


# Your answer goes here!


# __Exercise 3:__  Write a function called `first_word` that takes a list of character strings as input and returns the first element of the list in alphabetical order.  For example, your function should work like this: 
# 
# ```python
# 
# students = ['Mary', 'Zelda', 'Jimmy', 'Jack', 'Bartholomew', 'Gertrude']
# 
# first_word(students)
# 
# 'Bartholomew' # The result
# 
# ```
# 
# _Hint:_ You'll need to first sort your list in the function to accomplish this, then identify the first element.  Within a function, it is a good idea to use multiple lines of code to separate out the different steps.  Just make sure all the code that belongs to the function is indented!
# 
# After you've written the function, run it by supplying the list `teams` to your function as an argument to test it.  

# In[39]:


teams = ['Stars', 'Cowboys', 'Rangers', 'Mavericks', 'FC Dallas']

# Your code goes below!


# __Exercise 4:__ Explain, in your own words, the difference between a `for` loop and a `while` loop.  Write your response below in this Markdown cell.  

# __Exercise 5 (from your textbook, p. 49):__ 
# 
# > If you are given three sticks, you may or may not be able to arrange them in a triangle.
# For example, if one of the sticks is 12 inches long and the other two are one inch long, it is clear that
# you will not be able to get the short sticks to meet in the middle. For any three lengths, there is a
# simple test to see if it is possible to form a triangle:
# If any of the three lengths is greater than the sum of the other two, then you cannot
# form a triangle. Otherwise, you can. (If the sum of two lengths equals the third, they
# form what is called a “degenerate” triangle.)
# > 
# > Write a function named `is_triangle` that takes three integers as arguments, and that returns either `True` or `False` depending on whether you can or cannot form a triangle from sticks with the given lengths.  _Hint_: you'll need to use 
# 
# For example: 
# 
# ```python
# is_triangle(2, 2, 11)
# 
# False
# 
# is_triangle(5, 5, 6)
# 
# True
# ```

# In[40]:


## Your code goes here!


# __Exercise 6__: Sequences of numbers in Python can be generated by typing them out, as you've learned how to do in this class.  However, they can also be produced by the built-in `range` function, which can simplify things for you significantly if you need to generate a long list of integers.  `range` has three parameters: `start`, which is the first integer you want to start with; `stop`, which is the first integer you __don't__ want to include, and `step`, which optionally specifies the integer interval.  For example: 

# In[41]:


x = range(1, 21, 5)

x


# In[42]:


type(x)


# We've created a __range__ object which conforms to the arguments we supplied to the `range` function.  Notably, the range object can be looped through:

# In[43]:


for y in x:
    print(y)


# If need be, your range object can also be converted to a list with the `list` function.  

# In[44]:


list(x)


# Your job in Exercise 3 is to use the `range` function to print the following text to the screen: 
# 
# ```
# 2!
# 4!
# 6!
# 8!
# Who do we appreciate?
# ```
# 
# The printing of the numbers should be done in a loop over the numbers generated by the `range` function.  

# In[45]:


## Your code goes here!

