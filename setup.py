from distutils.core import setup

setup(name = 'simplesms',
      version = '0.1.0',
      author = 'Emmanuel Okyere',
      author_email = 'chief@hutspace.net',
      url = 'http://github.com/eokyere/simplesms',
      description = 'Build SMS apps on top of a simple SMS/USSD gateway',
      packages = ['simplesms', 'simplesms.contrib'],
      keywords = ['gsm', 'sms', 'communication'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Other Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Communications :: SMS',
          'Topic :: Office/Business'],
      long_description= """
      
      """,
          )