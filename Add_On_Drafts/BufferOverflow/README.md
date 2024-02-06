# Week 4 BufferOverflow drafts

## NORMAN
I am using the Scope class in the cppcheck import to determine whether or not strcpy is being properly guarded. The description I've been working with is here: [Scope CPPCheck](file:///C:/Users/normanc/Desktop/Capstone/html_elwakil/html/classaddons_1_1cppcheckdata_1_1Scope.html)

I found some uses of `scope.type` in the misra.py addon and tried to implement a similar strategy in my addon, but it basically killed the entire addon so I switched tracks and started trying to just find the if statement using Scopes.
