# hello_world_py : Python Source code for tests

## Objectives

Test the sonarQube environment :

* creata a simple .py file and unit test
* run basic python quality tools
* obtain a SonarQube (here sonarQube 7.4)


## Tools used (with their versions)

- CentOS 7.3
- python (3.6.2)
- sonarQube (7.4)
- sonar-scanner (3.2.0.1227)
- pylint 1.6.5
- py.test 3.0.7
- coverage 4.3.3
- doxygen (1.8.5)

## Installation

Download the project:

`$ git clone https://github.com/ExemplesDev/HelloWorld_cpp.git`

## Build the main code:

`doxygen Doxyfile #other configuration:Doxyfile2)`

## Run the binary:

```
$ python3 message.py
Hello World !
```

# Execute pylint

```
$ pylint --rcfile=pylintrc --py3k --reports=n message.py

This option 'ignore-iface-methods' will be removed in Pylint 2.0This option 'required-attributes' will be removed in Pylint 2.0
```

## Execute the unit tests

```
$ py.test -v --junitxml=test_results.xml
============================================================================================================ test session starts ============================================================================================================
platform linux -- Python 3.6.2, pytest-3.0.7, py-1.4.33, pluggy-0.4.0 -- /cvmfs/euclid-dev.in2p3.fr/CentOS7/EDEN-2.0/usr/bin/python3
cachedir: .cache
rootdir: /home/user/Work/Projects/hello_world_py, inifile:
collected 2 items 

message_test.py::TestMessage::test_init PASSED
message_test.py::TestMessage::test_exists PASSED

------------------------------------------------------------------------------- generated xml file: /home/user/Work/Projects/hello_world_py/test_results.xml --------------------------------------------------------------------------------
========================================================================================================= 2 passed in 0.07 seconds ==========================================================================================================
user[euclid-dev.in2p3.fr]:~/Work/Projects/hello_world_py
```

## Execute the coverage (with unit tests)

```

$ coverage3 run --source=. -m py.test -v --junitxml=test_results.xml
============================================================================================================ test session starts ============================================================================================================
platform linux -- Python 3.6.2, pytest-3.0.7, py-1.4.33, pluggy-0.4.0 -- /cvmfs/euclid-dev.in2p3.fr/CentOS7/EDEN-2.0/usr/bin/python3
cachedir: .cache
rootdir: /home/user/Work/Projects/hello_world_py, inifile:
collected 2 items 

message_test.py::TestMessage::test_init PASSED
message_test.py::TestMessage::test_exists PASSED

------------------------------------------------------------------------------- generated xml file: /home/user/Work/Projects/hello_world_py/test_results.xml --------------------------------------------------------------------------------
========================================================================================================= 2 passed in 0.12 seconds ==========================================================================================================

$ coverage3 report
Name              Stmts   Miss  Cover
-------------------------------------
message.py           15      6    60%
message_test.py      13      0   100%
-------------------------------------
TOTAL                28      6    79%


```
Xml output:

```
coverage3 xml

$ tree -L 1
.
|-- coverage.xml
|-- docs
|-- Doxyfile
|-- Doxyfile2
|-- Doxyfile_default
|-- html
|-- latex
|-- message.py
|-- message_test.py
|-- __pycache__
|-- pylintrc
|-- pylintrc_default
`-- test_results.xml

```

## sonarQube usage

* configuration file:

```

# required metadata
sonar.projectKey=Message 
sonar.projectName=Message Project
sonar.projectVersion=0.1

# path to source directories (required)
sonar.projectDescription=First usage of sonar with static and dynamic analysis
sonar.sources=.

# paths to the reports
sonar.python.xunit.reportPath=test_results.xml
sonar.python.coverage.reportPath=coverage.xml 

```

Run sonarQube :

`$ sonar-scanner` 


