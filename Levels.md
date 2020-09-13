
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

## AWM_Level2

The constructor for a webserver at level2 of the *Agent Web Model* requires:
- **A**: a numpy boolen matrix representing the adjacency matrix of the public links of the files on the webserver
- **B**: a numpy boolen matrix representing the adjacency matrix of the implicit links of the files on the webserver
- **n_pnames**: an integer number denoting the number of possible parameter names
- **n_pvalues**: an integer number denoting the number of possible parameter values
- **flag**: an tuple made up of three integer: the file, the parameter name, and the parameter value beyond which the flag is hidden

Actions are specified by a dictionary with the following keys:
- **command**: a constant denoting one of the possible actions (CMD_NONE, CMD_READ, CMD_DEEPREAD, CMD_SEARCH)
- **targetfile**: an integer number denoting the file on which to apply the action
- **targetfile**: an integer number denoting the file on which to apply the action
