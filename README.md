# << SOFTWARE NAME >>
**Author:** Aivars Umbrasko <umbrasko.aivars@gmail.com>
> << SHORT DESCRIPTION >>

## Development

-   **Requirements**
    -   Python 3
	-	LaTex

### Branch structure

**master**

Latest working state of application, in here go merge request and no direct commits.

**New Features and major changes**

New Features and major changes need to be commited in to a separate branch which originated from
master.

## Tests

**General**

To run the unit test do the following

1. Activate the virtual environment

    ```
    source venv/bin/activate
    ```

2. Invoke the unit tests with python

    ```
    python setup.py test
    ```

    Please make sure all tests pass before commiting.

    Individual tests may also be run from within the
    directory and sub-directories there-in.

    ```
    /tests
    ```

    or adding by file name,
    file name can be testFile or module(for doctests) name

    ```
    python setup.py test --module=<filename>
    ```

    Manage test output verbosity, default is setted to '1':
      * 0 (quiet): you just get the total numbers of tests executed and the global result
      * 1 (default): you get the same plus a dot for every successful test or a F for every failure
      * 2 (verbose): you get the help string of every test and the result
    ```
    python setup.py test --verbosity=<number>
    ```

    If you add new tests please make sure that:
      * they are executable
      * the test file and the classes match the naming conventions
      * the tests are found by pythons `unittest` discover mechanism
      * tests are deterministic (should either always fail or always pass)
        If needed set the random generator seed in the test
      * for test input and/or output use input_test_dir and output_test_dir variables (this is absolute path to directories)
      ```
      Example:
      >>> from tests import input_test_dir
      >>> from tests import output_test_dir
      ```

NOTE:
All test should be checked to pass before committing but MUST pass
before pushing to ```origin:master```.

Code Style
----------
The package is written in the python `pep8` standard
https://www.python.org/dev/peps/pep-0008/ .
The code style is checked as a step in the unit testing and can
be run explicitly by invoking

  ```
  python setup.py codestyle
  ```

Empty output means that all source files respect `pep8`. All style
warnings errors shall be corrected before commiting changes.

## Installation

1.  **Clone the repository**
    -   First of all clone the repository.

2.  **Create python virtual environment**
    -   From the root folder, run `virtualenv -p python3 venv`.

3. **Setup aplication**
    -   activate virtual environment, run `source venv/bin/activate` and run setup script `pip install -e .`.

## Development Rules

**General**

-   Always write DOCBlocks for all public methods
-   For all new public methods, add DOCtests or unittest.


## Documentation

**General**

-   Dokumentation will be ganareted from Docstrings.

**Example for Generating pdf dokumentation**

From the root folder activate virtual environment `source venv/bin/activate`,
Change directory `cd docs`,
run MAKE `make latexpdf`,
output will be generated in `\build` directory.

**Note**: There is more options for generating documentation run `make` from `\docs` directory to see they.
