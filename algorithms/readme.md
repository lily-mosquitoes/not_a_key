## About

The algorithms module collects algorithms available to the user for couplet selection. These algorithms aim to return the 'best' next couplet for each chosen state, at each step of the key-out.

What ultimately will be the best next couplet at each step is a difficult problem to solve and may depend on the goal of the user, thus this section is prone to constant changes.

Adding, removing and modifying algorithms is made easy by the use of the `__init__.py` file, there human readable names can be coupled with the function names imported from the module files; this coupling is done in the `available_algorithms` variable of the class "Algorithms", which will be imported by the main program. Additionally, you can specify if the algorithm uses the additional parameter "percent" in the `use_percent` variable of the class "Algorithms".
