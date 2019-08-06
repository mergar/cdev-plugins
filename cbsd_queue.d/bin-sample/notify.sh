#!/bin/sh
LOG="/tmp/notify.log"

date >> ${LOG}
echo $* >> ${LOG}

for i in $*; do
	export "${i}"
done

SQL="${workdir}/jails-system/${id}/local.sqlite"
[ ! -r ${SQL} ] && exit 0
sqlite3 ${SQL} "SELECT * FROM settings" >> ${LOG}
