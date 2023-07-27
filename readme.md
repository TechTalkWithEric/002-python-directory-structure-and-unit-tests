# readme

## setup
I'm not using any additional packages in this example but it's still a good practice to
set up a virtual environment

```sh
python3 -m venv .dev
source .dev/bin/activate
```

## tests/_init_tests
This directory contains a template test file that you can use as the "starter".
Use the `__init__.py` in this directory to control any additional `paths` needed by the unit tests.

I named with an underscore (_init_tests) just so that it's at the top of the directory.  The underscore doesn't server any other purpose than that.

[Python Unittest](https://docs.python.org/3/library/unittest.html)

## basic project structure
```
+ src
    |-- common
    |-- models
    |-- services
+ tests
    |-- common_tests
    |-- models_tests
    |-- services_tests

```

## Watch how this works on 🎥 YouTube
[🐍 Python Project Directory Structures & Unit Test 🧪 - YouTube](https://youtu.be/w8t3CeHHGp4)
