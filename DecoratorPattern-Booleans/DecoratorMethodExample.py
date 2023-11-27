# DecoratorMethodExample.py
# @ author: Administrator
# Date: 22.11.23

'''
The decorator pattern allows you to decide the behaviour of existing code
by using a conditional statement that either executes the original code or
a decorator class or method that returns a replacement or a different
behaviour to the original code in the form of a wrapper.
'''
def conditional_decorator(dec, condition):
    def decorator(func):
        if not condition:
            # Return the function unchanged, not decorated
            return func
        return dec(func)
    return decorator

# Conditional decorator
@conditional_decorator(args...)
def foo():
    # Return decoration



# The decorator could also be a class:
class conditional_decorator(object):
    def __init__(self, dec, condition):
       # Stored as arguments
        self.decorator = dec
        self.condition = condition

    def __call__(self, func):
        if not self.condition:
            # Return the function unchanged, not decorated.
            return func
        return self.decorator(func)

'''
The __call__ method is acting the same as the decorator() method in
the first example. The dec and conditional parameters are stored as arguments
in the initialiser that can be updated with the decorator.

In basic terms a decorator is a function added to another function.

The Decorator Pattern is used when we may have the need to add functions on top
of existing code, without breaking the Single Responsibility Principle.
Therefore we need to add a class or function that will replace the existing
code or wrap it in another behaviour that meets these new required needs.
This means that the wrapper will be responsible for one function as it adds
to the existing code.
Due to the behavioural nature of this pattern, we may or may not want to wrap
the object in the decorator, therefore we use a conditional statement to make
this decision. This shows the importance of boolean functions within the
Decorator Method pattern.
'''

'''
Another example where this might be used is if we wanted to provide a format
text tool. We already have a feature that bolds and underlines the text.
However, we want to add an italic feature. Again we don't want to break the
Single Responsibility Principle. The solution to solve this problem is to use
the decorator method to create multiple wrapper classes. First we use a
BoldWrapperClass over the written text, which converts it into bold letters,
then we apply the ItalicWrapperClass and UnderlineWrapperClass over the bold
text, giving us the result we need.
'''

class WrittenText:
    # Represents a Written text
    def __init__(self, text):
        self._text = text
 
    def render(self):
        return self._text
 
class UnderlineWrapper(WrittenText):
    # Wraps a tag in <u>
    def __init__(self, wrapped):
        self._wrapped = wrapped
 
    def render(self):
        return "<u>{}</u>".format(self._wrapped.render())
 
class ItalicWrapper(WrittenText):
    # Wraps a tag in <i>
    def __init__(self, wrapped):
        self._wrapped = wrapped
        
    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())
 
class BoldWrapper(WrittenText):
    # Wraps a tag in <b>
    def __init__(self, wrapped):
        self._wrapped = wrapped
 
    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())
 
# main method
if __name__ == '__main__':

    # Original text
    before_gfg = WrittenText("ThisIsWrittenText")
    
    # ItalicWrapper wraps the UnderlineWrapper, which wraps the BoldWrapper, using the written text
    after_gfg = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_gfg)))
 
    print("before :", before_gfg.render())
    print("after :", after_gfg.render())

