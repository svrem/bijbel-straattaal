from distutils.core import setup

setup(
  name = 'straattaal_bijbel',         # How you named your package folder (MyLib)
  packages = ['straattaal_bijbel'],   # Chose the same as "name"
  version = '3490582904859234859023490238490823905829058029384092384098234098234.0',      # Start with a small number and increase it with every change you make
  license='Apache 2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'TYPE YOUR DESCRIPTION HERE',   # Give a short description about your library
  author = 'God',                   # Type in your name
  author_email = 'god@prutsor.nl',      # Type in your E-Mail
  url = 'https://github.com/Prutsor/bijbel-straattaal',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Prutsor/bijbel-straattaal/archive/refs/tags/bijbel4life.tar.gz',    # I explain this later on
  keywords = ['bijbel', 'god', 'patta'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.9',
  ],
)