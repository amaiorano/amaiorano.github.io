---
layout: post
title:  "Virtual Functions in C"
categories: Programming
comments: true
---
NOTE: I first wrote this post on [Blogspot](http://vgcoding.blogspot.com/2014/03/virtual-functions-in-c.html) before moving it here.

## A Motivating Discussion

A good friend of mine, Ken, has been giving interviews at his work, and expressed how many candidates struggled with basic questions about object-oriented programming in C++. He said they would be able to explain concepts like inheritance and polymorphism, but would choke when asked, for instance, "Why is the virtual keyword necessary? Why aren't all functions automatically virtual?".

There are a couple of valid answers to this question. One of them is related to software design: if a function is non-virtual in a base class, it cannot and should not be overridden in child classes. The other answer is related to performance: virtual functions are more costly to invoke than non-virtuals (via a base class pointer or reference). This second answer is one that interests me more because I believe many programmers don't really understand what makes virtual functions more costly.

When I first learned about virtual functions in C++, I remember being really impressed with this feature, because accomplishing something similar in C wasn't easy. A fairly simple form of polymorphism is possible in C by using structs of function pointers that would be set at runtime; good examples of these can be seen in [Quake 2's source code](https://github.com/id-Software/Quake-2) (see [client/ref.h](https://github.com/id-Software/Quake-2/blob/master/client/ref.h)) where they are used to polymorphically invoke rendering functions via OpenGL or the software renderer. However, to mimic C++ inheritance and virtual functions in C is another story.

I eventually read about how C++ compilers generate virtual function tables to implement virtual functions; and with that mystery solved, I happily coded in C++ for years. But since this recent discussion with Ken, I thought it might be fun, and perhaps instructive, to try and implement basic inheritance and virtual functions in C. Bjarne Stroustrup's first version of C++ was actually called ["C with Classes"](http://www.cplusplus.com/info/history/) because he would first transform C++ code to C, then compile it with a regular C compiler. So I figured I could whip up a simple program in C that would show how virtual dispatch and inheritance could be implemented. I think understanding and being able to step through such code can give some insight into what the cost of virtual functions are.

## Implementation

The code is available on github: [https://github.com/amaiorano/VFuncsInC](https://github.com/amaiorano/VFuncsInC)

There are two files: [main.cpp](https://github.com/amaiorano/VFuncsInC/blob/master/main.cpp) which contains a simple test case in C++, and [main.c](https://github.com/amaiorano/VFuncsInC/blob/master/main.c) which contains the equivalent implementation in C. Each can be compiled and run separately (tested: Visual Studio, GCC).


## The base C++ sample (main.cpp)

The code in main.cpp is simple, declaring 3 classes Base, ChildOne, and ChildTwo:

```cpp
class Base
{
public:
    Base();
    virtual ~Base();
    virtual void Func1();
    virtual float Func2(int arg1);

    int a;
    float b;
};
```

```cpp
class ChildOne : public Base
{
public:
    ChildOne();
    virtual ~ChildOne();
    virtual void Func1();

    char c;
};
```

```cpp
class ChildTwo : public ChildOne
{
public:
    ChildTwo();
    virtual ~ChildTwo();
    virtual float Func2(int arg1);

    short c;
    short d;
};
```

ChildOne derives from Base, and ChildTwo derives from ChildOne. There are 3 virtual functions declared and implemented in Base: the destructor, Func1, and Func2\. ChildOne overrides Func1, while ChildTwo overrides Func2\. Both child classes implement a destructor as well.

All the functions are implemented the same way: they are simply stubs that output the name of the function. For example:

```cpp
void Base::Func1()
{
    printf("Base::Func1\n");
}
```

In main, we declare a Base* pointer pBase, then proceed to instantiate each of the three classes, invoke the 2 virtual functions, and delete the instance:

```cpp
int main()
{
    Base* pBase;

    pBase = new Base();
    pBase->Func1();
    pBase->Func2(11);
    delete pBase;

    printf("\n");

    pBase = new ChildOne();
    pBase->Func1();
    pBase->Func2(12);
    delete pBase;

    printf("\n");

    pBase = new ChildTwo();
    pBase->Func1();
    pBase->Func2(13);
    delete pBase;
}
```

The output from this sample is pretty straightforward:

```
Base::Construct
Base::Func1
Base::Func2 arg1=11
Base::Destruct

Base::Construct
ChildOne::Construct
ChildOne::Func1
Base::Func2 arg1=12
ChildOne::Destruct
Base::Destruct

Base::Construct
ChildOne::Construct
ChildTwo::Construct
ChildOne::Func1
ChildTwo::Func2 arg1=13
ChildTwo::Destruct
ChildOne::Destruct
Base::Destruct
```

The main C++ features that this sample demonstrates are:

*   **Inheritance:** ChildTwo inherits from ChildOne, which inherits from Base, which means that ChildTwo's data members include those of its two bases.

*   **Constructor Chaining:** when constructing, say, a ChildTwo instance, we see that Base's constructor gets invoked, followed by ChildOne's, and then ChildTwo's.

*   **(Virtual) Destructor chaining:** destructors get automatically invoked in the opposite order of the constructors.

*   **Virtual Functions (Polymorphism):** the most derived implementation of a virtual function gets called depending on the type of the instance pBase points to. For example, on an instance of ChildTwo, we see that calling Func1 invokes ChildOne's version, while calling Func2 invokes ChildTwo's version.

## Doing it in C (main.c)

Now for the interesting part: the implementation of the same C++ code, but now in C, which can be seen in main.c. First, let's take a look at the output from running an executable built from main.c to see that it is practically the same as that of main.cpp:

```
Base_Construct
Base_Func1
Base_Func2 arg1=11
Base_Destruct

Base_Construct
ChildOne_Construct
ChildOne_Func1
Base_Func2 arg1=12
ChildOne_Destruct
Base_Destruct

Base_Construct
ChildOne_Construct
ChildTwo_Construct
ChildOne_Func1
ChildTwo_Func2 arg1=13
ChildTwo_Destruct
ChildOne_Destruct
Base_Destruct
```

Let's go through each of the C++ features I listed above and see how they are implemented in C:

### Inheritance

In C, there are no classes, only structs; and structs can only contain data, and cannot inherit from another type. So the three "classes" are implemented as structs:

```cpp
typedef struct
{
    void** vtable;
    int a;
    float b;
} Base;
```

```cpp
typedef struct
{
    Base base; // This is how we "inherit" from Base in C to have the same memory layout
    char c;
} ChildOne;
```

```cpp
typedef struct
{
    ChildOne base; // This is how we "inherit" from Base in C to have the same memory layout
    short c;
    short d;
} ChildTwo;
```

The important part is how ChildOne "derives" from Base by declaring a member of type Base as its _first_ member, and ChildTwo "derives" from ChildOne in a similar fashion. This mimics how data gets laid out in memory for inherited types in C++, namely that data is laid out in the order its declared, starting from the most-base to the most-derived class. What this boils down to is pointers and address manipulation.

In C++, we can write the following:

```cpp
ChildTwo* pChildTwo = new ChildTwo();
Base* pBase = pChildTwo;
```

We don't need to cast pChildTwo to Base* because semantically in C++, a derived type _is-a_ base type. The fact that memory is laid out from base-most to child-most also means that the address of pChildTwo and that of pBase will be exactly the same. The compiler doesn't need to manipulate the address at all when assigning from child pointer to base pointer.

In C, by laying out the data to mimic C++, we can also assign from child to base, but must explicitly cast since the types are not actually related, like so:

```cpp
ChildTwo* pChildTwo = NewChildTwo();
Base* pBase = (Base*)pChildTwo;
```

This type of explicit up-casting is done in many places in main.c.



### Constructor Chaining


Constructors are special functions in C++ in that the compiler makes sure that parent constructors are invoked before child constructors up the chain. In fact, you can explicitly specify which parent constructor should be invoked via the initialization list of a child constructor:

```cpp
Child::Child() : Base()
{
}
```

In C, there is no way to specify implicit function chains, so to mimic this behavior we must explicitly invoke the parent constructor from the child constructor before initializing any data:

```cpp
void Base_Construct(Base* pThis)
{
    pThis->vtable = g_allVTables[CLASS_BASE];
    printf("Base_Construct\n");
    pThis->a = 0;
    pThis->b = 0.f;
}
```

```cpp
void ChildOne_Construct(ChildOne* pThis)
{
    Base_Construct((Base*)pThis);
    ((Base*)pThis)->vtable = g_allVTables[CLASS_CHILDONE];

    printf("ChildOne_Construct\n");
    pThis->c = 0;
}
```

```cpp
void ChildTwo_Construct(ChildTwo* pThis)
{
    ChildOne_Construct((ChildOne*)pThis);
    ((Base*)pThis)->vtable = g_allVTables[CLASS_CHILDTWO];

    printf("ChildTwo_Construct\n");
    pThis->c = 0;
    pThis->d = 0;
}
```

As can be seen, the two child classes, ChildOne and ChildTwo, invoke their parent constructor first. You may be wondering about the setting of the 'vtable' member; ignore it for now as I cover this later on.

Another important difference from their C++ counterparts that you may have noticed is how these constructors take a member named 'pThis'. In C++, all non-static member functions, including the constructor, can access other members of the class explicitly using a pointer named 'this' (or implicitly by omitting the 'this' altogether). The way it works is that the compiler adds a hidden 'this' parameter to all member functions of a class that is a pointer to the type of that class; when a member function gets invoked, the compiler passes in the instance of the class to the function via this parameter. In C, we must expose this parameter in our member functions, and pass in the instance explicitly.

### Virtual Functions

As far as I know, all C++ compilers implement virtual functions by using the virtual function table, or vtable, mechanism. If a class declares or inherits at least one virtual function, the compiler adds a hidden member that is a pointer to a vtable. The vtable is simply an array of pointers to virtual functions. The compiler generates a vtable per class, where each entry points to the most derived implementation of a virtual function for that class. To mimic all this in C, I do pretty much the same thing a C++ compiler does, except I do it at runtime.

First some useful type declarations:

```cpp
enum
{
    CLASS_BASE,
    CLASS_CHILDONE,
    CLASS_CHILDTWO,

    NUM_CLASSES
};

enum
{
    VFUNC_DESTRUCTOR,
    VFUNC_FUNC1,
    VFUNC_FUNC2,

    NUM_VFUNCS
};

typedef void (*Destructor)(void*);
typedef void (*Func1)();
typedef float (*Func2)(int arg1);
```

The two enums are used to index the vtable by class and function respectively. The typedefs are used to cast the generic void* pointer that contains the address of a function to the specific function type (more on this below).

I then declare a pointer that will point to a table of all vtables, one per class:

```cpp
void*** g_allVTables = NULL;
```

I think this is the first time I've written a triple pointer myself ;) The reason we have a triple pointer here is simple: we use a ```void*``` to point to a single virtual function; a vtable is an array of these ```void*``` entries per class, so a ```void**```; and finally, g_allVTables is a table of vtables, so ```void***```.

Now to build our vtables, the very first function called in main is InitVTables():

First we allocate a table of 3 vtable pointers and store that in the global variable g_allVTables:

```cpp
void InitVTables()
{
    int i;
 
    // We need a pointer to a vtable per class
    g_allVTables = (void***)malloc( sizeof(void**) * NUM_CLASSES );
```

Then we allocate each vtable - that is, 3 entries per table since we have 3 virtual functions:

```cpp
    // For each class, we allocate vtable - in our case, it's simple as we have a fixed number
    // of virtual functions for each class.
    for (i = 0; i < NUM_CLASSES; ++i)
    {
        g_allVTables[i] = (void**)malloc(sizeof(void*) * NUM_VFUNCS);
    }
```

Finally, we populate the vtables by setting the most-derived version of the virtual function per class:

```cpp
    // Populate Base vtable entries
    g_allVTables[CLASS_BASE][VFUNC_DESTRUCTOR] = (void*)&Base_Destruct;
    g_allVTables[CLASS_BASE][VFUNC_FUNC1] = (void*)&Base_Func1;
    g_allVTables[CLASS_BASE][VFUNC_FUNC2] = (void*)&Base_Func2;
 
    // Populate ChildOne vtable entries
    g_allVTables[CLASS_CHILDONE][VFUNC_DESTRUCTOR] = (void*)&ChildOne_Destruct;
    g_allVTables[CLASS_CHILDONE][VFUNC_FUNC1] = (void*)&ChildOne_Func1;
    g_allVTables[CLASS_CHILDONE][VFUNC_FUNC2] = (void*)&Base_Func2;
 
    // Populate ChildTwo vtable entries
    g_allVTables[CLASS_CHILDTWO][VFUNC_DESTRUCTOR] = (void*)&ChildTwo_Destruct;
    g_allVTables[CLASS_CHILDTWO][VFUNC_FUNC1] = (void*)&ChildOne_Func1;
    g_allVTables[CLASS_CHILDTWO][VFUNC_FUNC2] = (void*)&ChildTwo_Func2;
}
```

Now that we have our vtables built, we need to make sure instances of each class use them. Let's take a look again at how the Base "class" was declared:

```cpp
typedef struct
{
    void** vtable;
    int a;
    float b;
} Base;
```

Notice there is a data member named vtable. Each instance of a Base, ChildOne, or ChildTwo will contain this member, and it must be set to point to the correct vtable for that class when the instance gets created. In C++, this happens when you invoke operator new like so:

```cpp
pBase = new ChildTwo();
```

Operator new allocates memory for the object and invokes the constructor chain, which in turn sets up the vtable if necessary. To do this in C, we first write a function to instantiate, or "new", each type. Here's the one for instantiating ChildTwo:

```cpp
ChildTwo* NewChildTwo()
{
    ChildTwo* pInstance = (ChildTwo*)malloc(sizeof(ChildTwo));
    ChildTwo_Construct(pInstance);
    return pInstance;
}
```

After allocating the memory for the instance, we invoke the class-specific constructor for ChildTwo. Let's take a look at that constructor again:

```cpp
void ChildTwo_Construct(ChildTwo* pThis)
{
    ChildOne_Construct((ChildOne*)pThis);
    ((Base*)pThis)->vtable = g_allVTables[CLASS_CHILDTWO];
 
    printf("ChildTwo_Construct\n");
    pThis->c = 0;
    pThis->d = 0;
}
```

Notice how after it invokes its parent constructor, ChildOne_Construct, it then initializes its vtable member by setting it to the corresponding class entry from the master table. ChildOne_Construct and Base_Construct are implemented in the same way, each one initializing the vtable member to its class-specific vtable after invoking its parent constructor (if one exists). This may seem a bit strange: why would the constructors each set the _same_ vtable data member one after another? As it turns out, this mimics how things really work in C++; that is, within a constructor, if you try to invoke a virtual function, it will invoke the one for that class, and _not_ the most derived implementation. This is because within a class Foo's constructor, the vtable is Foo's vtable for the _duration of that constructor_. [This is why it's not recommended to call virtual functions from constructors](http://www.artima.com/cppsource/nevercall.html).

If the previous paragraph on why the vtable member gets set in each constructor is a little confusing, don't worry too much. The most important thing to understand is that by the time all constructors have been invoked, the vtable member will correctly point to the most-derived class's vtable. In our example, the instance of ChildTwo that gets returned by NewChildTwo() will have it's vtable set to g_allVTables[CLASS_CHILDTWO].

We now have everything we need to be able to invoke these virtual functions polymorphically via a base class pointer. For instance, in main, we 'new' a ChildTwo and invoke the 2 virtual functions on it like so:

```cpp
pBase = (Base*)NewChildTwo();               // pBase = new ChildTwo();
((Func1)pBase->vtable[VFUNC_FUNC1])();      // pBase->Func1();
((Func2)pBase->vtable[VFUNC_FUNC2])(13);    // pBase->Func2(13);
DeleteBase(pBase);                          // delete pBase;
```

To invoke Func1, we first look up the address of the function in the instance's vtable, pBase->vtable[VFUNC_FUNC1]. This evaluates to a void*, a pointer to the function we setup in InitVTables. We cast this pointer to a Func1 function pointer type so that we can invoke the function using the call operator (). You may recall that in InitVTables we set ChildTwo's VFUNC_FUNC1 entry in its vtable to point to ChildOne_Func1, which is the most-derived implementation of Func1 for ChildTwo; so that's the function that gets invoked. For similar reasons, the second call will invoke ChildTwo_Func2.

### Virtual Destructor Chaining

In C++, the destructor for a type gets invoked when the instance gets destroyed via operator delete. If the type has a vtable, the destructor should be declared virtual so that the most derived destructor gets invoked. Similar to constructors, the destructors are automatically chained, except destruction happens in the opposite order: children before parents.
In my C code, the destructor is just another virtual function added to the vtables in InitVTables, for instance:

```cpp
g_allVTables[CLASS_CHILDTWO][VFUNC_DESTRUCTOR] = (void*)&ChildTwo_Destruct;
```

The analog to operator delete is a single function used to delete all 3 class types:

```cpp
void DeleteBase(Base* pThis)
{
    if (pThis != 0)
    {
        ((Destructor)pThis->vtable[VFUNC_DESTRUCTOR])(pThis);
        free(pThis);
    }
}
```

The invocation of the most-derived destructor is handled exactly the same way as for any virtual function. As for chaining destructors, we must do it manually within the destructor functions as we did for the constructors:

```cpp
void ChildTwo_Destruct(ChildTwo* pThis)
{
    printf("ChildTwo_Destruct\n");
 
    ChildOne_Destruct((ChildOne*)pThis);    
}
```

Notice how the parent destructor, ChildOne_Destruct, is invoked last to mimic the C++-style chaining. ChildOne_Destruct, in turn, invokes Base_Destruct in a similar fashion.

## Summary

With this very basic implementation of C++ in C, we can now see more clearly what the _extra_ cost of invoking a virtual function is. With a regular function call, the compiler (or linker) already knows which function to call, so it simply outputs instructions to jump to the specific function address. On the other hand, invoking a virtual function requires 2 extra pointer dereferences, or lookups: first we dereference the vtable pointer to access the class-specific vtable, and then we dereference the function pointer for the function being invoked to get its address. So the compiler must output code to perform these two lookups, followed by the jump to the dynamically resolved function address.

On its own, two extra memory lookups may not seem very expensive, but they can be when they involve instruction cache misses. I'm not a computer architecture expert, but I do know that on certain platforms, instructions that cause a cache miss can cost orders of magnitude more cycles than an instruction which does not. So hopefully, this helps answer the question  "Why is the virtual keyword necessary? Why aren't all functions automatically virtual?".

Thanks for reading!

## Special Thanks

Thanks to Fred, Ken, and Adamo for their helpful critiques and corrections. I would also like to thank everyone who posted on this blog and on [reddit/r/programming](http://www.reddit.com/r/programming/comments/21dv5s/virtual_functions_in_c/) for your many insightful comments! I've done my best to update and improve this post based on them.
