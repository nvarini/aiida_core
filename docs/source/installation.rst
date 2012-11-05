==============================================
Installation and Deployment of AIDA
==============================================

1. Download the Community python edition of ActiveState Python from
ActiveState_. Choose the appropiate distribution corresponding to your 
architecture.

.. _ActiveState: http://www.activestate.com/activepython/downloads


2. After untaring the distribution, cd to the untared directory,
install ActiveState using :program:`install.sh`.

3. Using pypm install django::

     sudo pypm -g install django

4. Install apache::

     sudo yum install httpd httpd-devel

5. Download and install mod_wsgi by hand from GoogleCode_.

.. _GoogleCode: http://code.google.com/p/modwsgi/

6. Download the AIDA distribution to /usr/local/www/aida using svn.

7. Copy the following files::

      $ cp /usr/local/www/aida/aidadb/apache/mod_wsgi.conf  /etc/httpd/conf.d/
      $ cp /usr/local/www/aida/aidadb/apache/z_aida_wsgi.conf  /etc/httpd/conf.d/

   and edit them as you see fit.

8. Restart httpd::

      /etc/init.d/httpd restart
