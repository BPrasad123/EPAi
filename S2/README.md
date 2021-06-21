
# Session1

The session focussed on following topics:
1. Variables and Memory References
   * Memory address reference by using id() function that returns a base-10 number. We can covert the same to hex format using hex() function.
2. Reference Counting
   * sys.getrefcount(my_var) => increases reference count by 1 and returns the count
   * ctypes.c_long.from_address(address).value => returns the correct count where address is id(my_var)
3. Garbage Collection
   * Releases memory (more useful in circular references)
4. Dynamic vs Static Typing
5. Variable Re-Assignment
6. Object Mutability
7. Function Arguments & Mutability
8. Shared References & Mutability
   * Integers in the range -5 to 256 are singleton objects
9.  Variable Equality
10. Everything is an Object
11. Python Optimizations: Interning
12. Python Optimizations: String Interning
    * Generally small strings automatically interned but do not count on it
    * Use sys.intern(string) to intern the string object and use a is b comparison for faster processing
13. Python Optimizations: Peephole
    * Use set instead of list and tuple when checking if an object is present in a collection

## Assignment
 --Here in this code we will be leaking memory because we are creating cyclic reference. 
 --Find that we are indeed making cyclic references.
 --Eventually memory will be released, but that is currently not happening immediately.
 --We have added a function called "clear_memory" but it is not able to do it's job. Fix it. 
