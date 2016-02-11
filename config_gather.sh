nmap -sP 192.168.1.0/24
# You wait - time passes

echo "[General]" > Wake-On-Lan-Python/.wol_config.ini
echo "broadcast=192.168.1.255" >> Wake-On-Lan-Python/.wol_config.ini
echo >> Wake-On-Lan-Python/.wol_config.ini

arp | grep ".home" | awk '{print $1,$3}' | sed 's/.home//g' | \
while read -r a ; do echo "[" `echo $a | awk '{print $1}'` "]" | tr -d ' ' >> Wake-On-Lan-Python/.wol_config.ini; \
    echo "mac="`echo $a | awk '{print $2}'` >> Wake-On-Lan-Python/.wol_config.ini; echo >> Wake-On-Lan-Python/.wol_config.ini; done

