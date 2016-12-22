import os
import time


# create or change hosted network
def hosted_network_create(ssid, key):
    command = "netsh wlan set hostednetwork mode=allow ssid=\"" + ssid + "\" key=\"" + key + "\""
    print(command)
    os.system(command)
    # time.sleep(0.25)


# start hosted network
def hosted_network_start():
    command = "netsh wlan start hostednetwork"
    os.system(command)
    # time.sleep(0.25)


# stop hosted network
def hosted_network_stop():
    command = "netsh wlan stop hostednetwork"
    os.system(command)
    # time.sleep(0.25)


# checks if the machine supports hosted network
def check_drivers():
    f = open('temp.drivers', 'w')
    command = 'netsh wlan show drivers'
    out = os.popen(command).read()
    f.write(out)
    f.close()
    f = open('temp.drivers', 'r')
    data = f.readlines()
    data = data[13].replace('\n', '').split(':')
    return data[1].replace(' ', '')


# returns hostwd network status(Started/Not)
def check_status():
    f = open('temp.txt', 'w')
    command = "netsh wlan show hostednetwork"
    out = os.popen(command).read()
    f.write(out)
    f.close()
    f = open('temp.txt', 'r')
    data = f.readlines()
    data = data[11]
    data = data.replace(' ', '').replace('\n', '').split(':')
    return data[1]
initialization_of_temp_txt = check_status()


# returns hosted network name
def get_name():
    f = open('temp.txt', 'r')
    data = f.readlines()
    data = data[4]
    data = data.replace('  ', '').replace('\n', '').split(':')
    data = data[1]
    if data.startswith(' "'):
        data = data[2:len(data)-1]
    elif data.startswith(' '):
        data = data[1:]
    return data


def get_password():
    f = open('temp.pass', 'w')
    command = 'netsh wlan show hostednetwork setting=security'
    out = os.popen(command).read()
    f.write(out)
    f.close()
    f = open('temp.pass', 'r')
    data = f.readlines()
    passwd = data[6].replace(' ', '').split(':')[1]
    return passwd.replace('\n', '').replace(' ', '')


# returns number of connected clients
def get_no_connected_client():
    f = open('temp.txt', 'w')
    command = "netsh wlan show hostednetwork"
    out = os.popen(command).read()
    f.write(out)
    f.close()
    f = open('temp.txt', 'r')
    data = f.readlines()
    if len(data) > 15:
        data = data[15]
        data = data.replace('  ', '').replace('\n', '').split(':')
        # print(data)
        return data[1].replace(' ', '')
    else:
        return 'None'


# returns mac addresses from netsh wlan show hostednetwork
def get_clients_mac(num):
    mac_list = []
    f = open('temp.txt', 'w')
    command = "netsh wlan show hostednetwork"
    out = os.popen(command).read()
    f.write(out)
    f.close()
    f = open('temp.txt', 'r')
    data = f.readlines()
    end = 15 + int(num) + 1
    # print(data[15])
    for i in range(16, end):
        datax = data[i]
        datax = datax.replace('\n', '').split()
        mac_list.append(datax[0])

    return mac_list


# returns a list of ip and corresponding mac of every client from 'arp -a'
def get_ip_mac():
    f = open('temp.mac.ip', 'w')
    command = "arp -a | findstr /r \"192\.168\.[0-9]*\.[2-9][^0-9] 192\.168\.[0-9]*\.[0-9][0-9][^0-9] " \
              "192\.168\.[0-9]*\.[0-1][0-9][0-9]\""
    out = os.popen(command).read()
    f.write(out)
    f.close()
    f = open('temp.mac.ip', 'r')
    data = f.readlines()
    clients = []
    for line in data:
        this_user = []
        each_line = line.split()
        this_user.append(each_line[0])
        this_user.append(each_line[1])
        clients.append(this_user)
    return clients
