# cmdChart

Utility to build charts inside a terminal or assci document.

## Getting Started

Streamline the way vulnerability management programs are created and run. This project is made to be modular so automation can be put into place at any program level.

## Installation TBA

This package is available on [PyPi](https://pypi.org) and can be installed with the following command:

```
$ TBA
```

## Running the tests

```
TBA
```

## How to use
``` 
from cmdchart import cmdchart

# Break down value for chart
value_slice = 100

# Chart data to display
data = {
   "Jan": 100,
   "Feb": 200,
   "Mar": 100,
   "Apr": 500,
   "May": 400,
   "Jun": 300,
   "Jul": 200,
   "Aug": 100,
   "Sep": 100,
   "Oct": 100,
   "Nov": 900,
   "Dec": 800
}

chart = chart.loader(data, value_slice, chart_type='bar')

print(chart)
```

```
900 |                                                   XXX      
800 |                                                   XXX  XXX 
700 |                                                   XXX  XXX 
600 |                                                   XXX  XXX 
500 |                XXX                                XXX  XXX 
400 |                XXX  XXX                           XXX  XXX 
300 |                XXX  XXX  XXX                      XXX  XXX 
200 |      XXX       XXX  XXX  XXX  XXX                 XXX  XXX 
100 | XXX  XXX  XXX  XXX  XXX  XXX  XXX  XXX  XXX  XXX  XXX  XXX 
     ------------------------------------------------------------
      Jan  Feb  Mar  Apr  May  Jun  Jul  Aug  Sep  Oct  Nov  Dec
```

## TO-DO
* Integrate with PyPi
* Document code
* Add other chart types

## Authors

* **Matt Ferreira** - *Developer* - [RackReaver](https://github.com/RackReaver)

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details