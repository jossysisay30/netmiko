from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint
password = getpass()
vlan_list = []
vlan_list2 = []
dev = []
print('-'*20 ,'welcome to vlan checker input the vlan nu','-'*20)
for x in range(2,5):
            dev2='192.168.{}.2'.format(x)
            dev.append(dev2)
#devices = ['192.168.2.2','192.168.3.2','192.168.4.2']
for device in dev:
  cisco_sw = {
            'device_type': 'cisco_ios_telnet',
            'host': device,
            'username': 'cisco',
            'password': password,
            }
  def telnetconnection():
         global telnet
         telnet = ConnectHandler(**cisco_sw)
  def vlanconf():
       for i in range(16,20):
          commands = ['vlan ' + str(i),'name vlan' + str(i)]
          telnet.send_config_set(commands)
  def vlanlist():
          result = telnet.send_command('show vlan brief')
          for line in result.splitlines():

              if 'VLAN' in line or '-----' in line or line.startswith('  '):
                  continue
              fields = line.split()

          result = telnet.send_command('show vlan brief')
          for line in result.splitlines():

              if 'VLAN' in line or '-----' in line or line.startswith('  '):
                  continue
              fields = line.split()
              global vlan_id
              vlan_id = fields[0]
              vlan_name = fields[1]
              vlan_list.append((vlan_id, vlan_name))
              vlan_list2.append(vlan_id)
          print()
          #pprint(vlan_list)
          #pprint(vlan_list2)
          print()
  def vlanchecker():
          print('vlan check for {}'.format(device))
          print('-'*60)
          vlnauser= input('enter the vlan nu you want to check:')
          print('-'*60)
          if vlnauser in vlan_list2:
              pprint('-'*60)
              print('vlan ',vlnauser , 'is under the vlan list ',device,' no need to add into vlan database')
              pprint('-'*60)
              #pprint(vlan_list)
          else:
                         pprint('-'*60)
                         ans=input('you wana to add the vlan at {}:'.format(device) +cisco_sw['host']+ '<y/n>' )
                         if ans == 'y':
                           commands = ['vlan ' + str(vlnauser),'name vlan' + str(vlnauser)]
                           telnet.send_config_set(commands)
                           print('-'*60)
                           print('vlan {} add to database'.format(vlnauser))
                           pprint('-'*60)
                          # pprint(vlan_list)
                         else:
                              print('you choose the not to add the database:')
                              pprint('-'*60)
                              pprint(vlan_list)  
  def main():
        telnetconnection()
        vlanconf()
        vlanlist()
        vlanchecker()

  if __name__ == '__main__':
        main()
