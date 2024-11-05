# bgc_add_vol_pack.py

The unlimited volume from Belgacom/Proximus is, in fact, limited. And when this limit is reached, your connection is nearly useless because its very low speed.

This script help you to easily add extra volume packs, with a headless mode to use it in a monthly cron by example.

## Parameters

```shell
usage: bgc_add_vol_pack.py [-h] [--repeat REPEAT] [--packSize PACKSIZE]
                           [--headless HEADLESS]
                           login password

Add extra data volume pack to Belgacom Internet

positional arguments:
  login                Belgacom login email
  password             Belgacom password

optional arguments:
  -h, --help           show this help message and exit
  --repeat REPEAT      Number of volume packs to add (1 pack by default)
  --packSize PACKSIZE  Volume size of the pack to add (150 GB by default)
  --headless HEADLESS  Headless mode (enabled by default ; using xvfb)
```

## Requirements

This script is using the following Python 3 modules :

- `argparse`
- `selenium`
- `pyvirtualdisplay`

And the following cmdline tool (headless mode) :

- xvfb (Ubuntu and derivatives) : `sudo apt-get install xvfb`

## Examples of use

Add 1 pack of 150 GB (which are default values)

```shell
./bgc_add_vol_pack.py my_login my_password
```

Add 3 packs of 150 GB in headless mode

```shell
./bgc_add_vol_pack.py my_login my_password --repeat 3 --packSize 150
```

Add 10 packs of 20 GB in headless mode disable (FireFox will be opened)

```shell
./bgc_add_vol_pack.py my_login my_password --repeat 10 --packSize 20 --headless 0
```

## Credits

These scripts have been modified and improved by Francois B. (Makoto) based on the initial script written by Tuxicoman (see Initial Credits And Licence below)

- Website : [Makoto no Blog](https://makotonoblog.be/)

## Initial Credits and Licence

Copyright (C) 2016 Tuxicoman

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later $
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more detail$
You should have received a copy of the GNU Affero General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.

Link to the post on Tuxicoman website : <https://tuxicoman.jesuislibre.net/2016/05/internet-vraiment-illimite-chez-belgacomproximus.html>

## Improvements - Changelog

- Updated for Python3
- Any volume pack sizes
- WebDriverWait increased up to 20 to _try_ to avoid login failures
- Headless mode added as optional parameter
- repeat and packSize parameters are optional with default value to 1 pack of 150 GB
