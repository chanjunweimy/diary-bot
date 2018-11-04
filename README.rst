========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
        | |codacy|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/diary-bot/badge/?style=flat
    :target: https://readthedocs.org/projects/diary-bot
    :alt: Documentation Status


.. |travis| image:: https://travis-ci.org/chanjunweimy/diary-bot.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/chanjunweimy/diary-bot

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/chanjunweimy/diary-bot?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/chanjunweimy/diary-bot

.. |requires| image:: https://requires.io/github/chanjunweimy/diary-bot/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/chanjunweimy/diary-bot/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/chanjunweimy/diary-bot/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/chanjunweimy/diary-bot

.. |codacy| image:: https://img.shields.io/codacy/REPLACE_WITH_PROJECT_ID.svg
    :target: https://www.codacy.com/app/chanjunweimy/diary-bot
    :alt: Codacy Code Quality Status

.. |version| image:: https://img.shields.io/pypi/v/diary-bot.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/diary-bot

.. |commits-since| image:: https://img.shields.io/github/commits-since/chanjunweimy/diary-bot/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/chanjunweimy/diary-bot/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/diary-bot.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/diary-bot

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/diary-bot.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/diary-bot

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/diary-bot.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/diary-bot


.. end-badges

Telegram bot that is used for recording diary implemented in python

* Free software: MIT license

Installation
============

::

    pip install diary-bot

Documentation
=============


https://diary-bot.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
