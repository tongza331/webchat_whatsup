## Step run
1. install channels, channels_redis
2. install redis_server (for ubuntu if windows can use Memurai: https://www.memurai.com/)
3. Run venv_channels

(for ubuntu extends terminal)
1. Run $ redis-server
If port already use pls type : sudo service redis-server stop


## Keep ideas
for i in range(len(c)):
    if "gamer2" == c[i].room_name:
        print(True)

## for add room_joined
c = RoomCreate.objects.get(creater=2)
p2=RoomList.objects.all()
p2[1].room_joined.count()
p2[1].room_joined.add(c)
p2[1].room_joined.count()