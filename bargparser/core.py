#!/bin/python

def parse_args(sys_argv: list):
    """
    #### Abstract:

    Parse args from a command line provider like: `sys.argv`
    
    Example:

    ```
    >>> parse_args(sys.argv)
    ```

    #### Returns:
    A dictionary in form: { commands: [...], keywords: {key: val ...} }

    """
    
    keywords = {}
    commands = []
    i = -1
    while (i := i + 1) < len(cl := sys_argv[1:]):
        if cl[i][0] == '-' and cl[i][1] != '-':
            try:
                keywords[cl[i].split('-')[-1]] = cl[i + 1]
                i += 1
            except IndexError:
                raise Exception('A keyword without a value: %s' %cl[i])
            
        elif cl[i][0] == '-' and cl[i][1] == '-':
            if '=' in cl[i]:
                key = cl[i].split('=')[0].split('-')[-1]
                val = "".join(cl[i].split('=')[1:])
                if len(val) < 1:
                    raise Exception('Value must be > 0 in length, got: %s' %val)
                keywords[key] = val
            else:
                try:
                    keywords[cl[i].split('-')[-1]] = cl[i + 1]
                    i += 1
                except IndexError:
                    raise Exception('A keyword without a value: %s' %cl[i])
        else:
            commands.append(cl[i])

    return {"commands": commands, "keywords": keywords}
