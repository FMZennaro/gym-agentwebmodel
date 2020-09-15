
## AWM_Level1

The constructor for a webserver at level1 of the *Agent Web Model* requires:
- **A**: a numpy boolen matrix representing the adjacency matrix of the files on the webserver
- **flag**: an integer number denoting the file in which the flag is hidden

Actions are specified by a dictionary with the following keys:
- **command**: a constant denoting one of the possible actions (CMD_NONE, CMD_READ, CMD_SEARCH)
- **targetfile**: an integer number denoting the file on which to apply the action


## AWM_Level2

The constructor for a webserver at level2 of the *Agent Web Model* requires:
- **A**: a numpy boolen matrix representing the adjacency matrix of the public links of the files on the webserver
- **B**: a numpy boolen matrix representing the adjacency matrix of the implicit links of the files on the webserver
- **flag**: an integer number denoting the file in which the flag is hidden

Actions are specified by a dictionary with the following keys:
- **command**: a constant denoting one of the possible actions (CMD_NONE, CMD_READ, CMD_DEEPREAD, CMD_SEARCH)
- **targetfile**: an integer number denoting the file on which to apply the action

## AWM_Level3

The constructor for a webserver at level3 of the *Agent Web Model* requires:
- **n_files**: an integer number denoting the number of files on the server
- **n_pnames**: an integer number denoting the number of parameter names that can be sent
- **n_values**: an integer number denoting the number of parameter values that can be sent
- **webserver()**: a function that receives an *action* as a dictionary, and returns a tuple (*observation*, *reward*, *done*, *additional_info*). Instead of using simple adjacency matrices, using a function allows for the definition of complex dynamics depending on parameters.  

Actions are specified by a dictionary with the following keys:
- **command**: a constant denoting one of the possible actions (CMD_NONE, CMD_READ, CMD_DEEPREAD, CMD_SEARCH)
- **targetfile**: an integer number denoting the file on which to apply the action
- **pname**: an integer number denoting the parameter name to send to the server
- **pvalue**: an integer number denoting the parameter value to send to the server
