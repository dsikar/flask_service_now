Notes

1. Every update to flaskapp.py must be immediately followed by a server restart

sudo /etc/init.d/apache2 restart

2. .csv files must be owned by www-data user e.g.

sudo chown www-data www-data *.csv

3. Absolute paths may not be necessary TBT

4. On AWS ubuntu flaskapp VM we have python 3.6.9. We want to update that to 3.8.10 so
it is inline with dev environment (AN, DS).


