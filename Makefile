PY=/usr/bin/python
NOSE=/usr/bin/nosetests1.1 -s -v --with-xunit --with-coverage --cover-erase --cover-package baip_munger_ui
NOSE_ENV=.env/bin/nosetests -s -v --with-xunit --with-coverage --cover-erase --cover-package baip_munger_ui
GIT=/usr/bin/git
COVERAGE=/usr/bin/coverage
COVERAGE_ENV=.env/bin/coverage
PYTHONPATH=.:../logga:../baip-munger

# The TEST variable can be set to allow you to control which tests
# to run.  For example, if the current project has a test set defined at
# "tests/test_<name>.py", to run the "Test<class_name>" class:
#
# $ make test TEST=tests:Test<class_name>
#
# To run individual test cases within each test class:
#
# $ make test TEST=tests:Test<class_name>.test_<test_name>
#
# Note: for this to work you will need to import the test class into
# the current namespace via "tests/__init__.py"
TEST=baip_munger_ui.tests:TestUtils

sdist:
	$(PY) setup.py sdist

rpm:
	$(PY) setup.py bdist_rpm --fix-python

docs:
	PYTHONPATH=$(PYTHONPATH) sphinx-1.0-build -b html doc/source doc/build

build: docs rpm

test:
	 PYTHONPATH=$(PYTHONPATH) $(NOSE) $(TEST)

test_env:
	 $(NOSE_ENV) $(TEST)

coverage: test
	$(COVERAGE) xml -i

coverage_env: test_env
	$(COVERAGE_ENV) xml -i

uninstall:
	$(RPM) -e python-baip-munger-ui

install:
	$(RPM) -ivh dist/python-baip-munger-ui-?.?.?-?.noarch.rpm

upgrade:
	$(RPM) -Uvh dist/python-baip-munger-ui-?.?.?-?.noarch.rpm

clean:
	$(GIT) clean -xdf

.PHONY: docs rpm test
