cat /sys/class/fc_host/*/port_name


cat /sys/class/fc_remote_ports/*/port_name | grep -i "63af"
cat /sys/class/fc_remote_ports/*/port_name | grep -i "85a5"

iscsiadm -m session
cat /etc/multipath.conf

perl -pe 's/[a-f0-9]+(?:-[a-f0-9]+){3}-[a-f0-9]+/<hidden token>/g' /etc/cinder/cinder.conf
grep -n "\(multip\|d_backe\)" /etc/cin*/cin*.conf
grep -n multipath /etc/nova/nova*.conf

watch -n 1 multipath -ll
sg_inq /dev/sdc

watch -n 1 ./multipath.sh
