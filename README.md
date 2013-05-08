CodeDateScanner
===============

CodeDateScanner:

You can use my gennerated dep.list file wich containts the list of php deprecated functions as of May 8th 2013.


However, if you would like a more updated file.

Run getDep:

	$- python getDep.py

>Recommend:
    Compile getDep.py for better preformance. 
            
>  	$- python -m py_compile getDep.py

and then run
    
    $- python getDep.pyc


Run depFind:

	$- python depFind.py

The program will ask you for two sets of inputs.

The first one is where you have moved dep.list. Leave empty if its the same folder as getDep.py


The second input is the full path to the sources you want to scan.
  
	e.g: /var/www/someSite
