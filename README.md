# granturismo-stats
Statistics for Gran Turismo online events

![GitHub](https://img.shields.io/github/license/dudenr33/granturismo-stats) 
![PyPI](https://img.shields.io/pypi/v/granturismo-stats)
![Travis (.com) branch](https://img.shields.io/travis/com/dudenr33/granturismo-stats/main)
![Coveralls github branch](https://img.shields.io/coveralls/github/DudeNr33/granturismo-stats/main)
![PyPI - Downloads](https://img.shields.io/pypi/dm/granturismo-stats)
![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/DudeNr33/granturismo-stats)

## Purpose
I started this project because I wanted to see how my qualifying times for the 
Gran Turismo Sport daily races compare to other drivers with similar driver and sportsmanship rating.

This is a work in progress. Currently, it is possible to do exactly what my original
goal included: get the complete qualifying leaderboard and compute some basic statistics.  
If you have suggestions what information to add feel free to open an issue and I will
see if it is a) possible and b) I find it interesting as well. ;) 

## Examples
If you would like to see example code, look at the *examples* directory on github.

## Limitations

### Performance
The performance is not the best. While there are probably a few things that can be done
on my side of the code, the main limiting factor when retrieving the qualification 
leaderboards is the Gran Turismo Sport API itself which limits the number of entries that 
can be obtained in a single request and takes quite some time to respond.
With several ten thousand qualification entries for each race it can easily take 10 seconds or 
longer to obtain them all. Just be patient! :) 

### Region
There is currently no option to change the region for which you want to retrieve the results.
The code uses the API URL for Germany and thus the results are all for the EMEA region.
However, this is something I'd like to change in the future (see issue #1).

## Further remarks
Bear in mind that in order to retrieve a full leaderboard somewhat in the region of
50 requests will be sent concurrently to the GT Sport API. 
Use this library responsibly. Querying the leaderboard every now and then should be
totally fine, but doing so over and over again without a pause in an endless loop will 
generate a lot of traffic on the server side.  
I intend to implement a caching mechanism so that executing a script multiple times will 
become faster on the one hand and produce less traffic on the other.
Until then, check out the *get_leaderboard* function of *gtsport_test_drive.py* in the
*examples* directory how to do it yourself.
