#!/bin/sh
rm -f x.json
for i in settings bhyve_dskcontroller bhyvenic pcibus bhyvedsk; do
	./sql2json.py --dbfile /home/oginzburg/oginzburg/vm/jenkinslin1/local.sqlite --sqlquery="SELECT * FROM ${i}" | python3.6 -mjson.tool >> x.json
done