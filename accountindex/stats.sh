res=""
for table in Weibo_User_Profile Weibo_User_Relationship;do
    declare -i n=0
    for i in $(seq 0 9);do 
        n+=$(mysql -N -e "select count(1) from ${table}_$i" -u root -pcicdata WeiboPanel)
    done
    res+=" "$n
done
echo "$(date "+%Y-%m-%d %H:%M:%S")" $res>>/root/src/stats.txt
