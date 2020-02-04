# seniorproject_web_scraper
This web scraper was coded using the framework "Scrapy"

In order to be able to run the web scraper, a few dependencies must be intsalled.

Requirements
=======

* Python 3.5+
* Works on Linux, Windows, Mac OSX, BSD

Install
=======

The quick way::

    pip install scrapy

See the install section in the documentation at
https://docs.scrapy.org/en/latest/intro/install.html for more details.

Documentation
=============

Documentation is available online at https://docs.scrapy.org/ and in the ``docs``
directory.

How to run the scraper
=============

1. Open the terminal
2. Navigate to the folder "ws_seniorproject"
3. Run the scraper (spider we are working with is called "project1")::
       
       scrapy crawl project1
       
Alternatively, store the results in a json file::

       scrapy crawl project1 -o results.json
