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

.. |codacy| image:: https://img.shields.io/codacy/6b179ec130c545f7a4ed7f782eaf16da.svg
    :target: https://www.codacy.com/app/chanjunweimy/diary-bot
    :alt: Codacy Code Quality Status

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


.. image:: https://api.codacy.com/project/badge/Grade/56e5a1aa787a455db865de920c68f224
   :alt: Codacy Badge
   :target: https://app.codacy.com/app/chanjunweimy/diary-bot?utm_source=github.com&utm_medium=referral&utm_content=chanjunweimy/diary-bot&utm_campaign=Badge_Grade_Dashboard