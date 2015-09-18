# sananmuunnos
Transforming Finnish spoonerisms made easy (and systematic).
## Usage
    import sananmuunnos as sm
    
    print(sm.transform("sanan muunnos"))

Or as a stand-alone script:

$sananmuunnos.py sanan muunnos
## background
A sananmuunnos ("word transformation") is a Finnish wordplay similar to spoonerisms in English. The basic idea is to swap the beginnings of two words to form new expressions. You can read more about the phenomenom on [Wikipedia](https://en.wikipedia.org/wiki/Sananmuunnos). A huge list of sananmuunnoses can be found [here](http://users.spa.aalto.fi/slemmett/sananm.html).

AS with all language-related things, there is not a completely systematic logic behind sananmuunnoses. However, there are a small number of rules to which most sananmuunnoses conform. This program attempts to solve sananmuunnoses by relying on these rules. It also attempts to make the newly-created words to comply with Finnish vowel harmony.
## Requirements
Sananmuunnos requires python 3.x to run. Python 2.7 works to some extent but there may be encoding-related issues; these might be fixed later.
## Copyright
Copyright 2015 Tuukka Ojala <tuukka.ojala@gmail.com>
## License
Sananmuunnos is distributed under the MIT license. See the file LICENSE for more information.