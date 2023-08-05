from string import digits
from pprint import pprint

data = " FastEthernet0/1  switchport trunk encapsulation dot1q  switchport trunk allowed vlan 100,200  switchport mode trunk"


# 'FastEthernet0/0  switchport mode access  switchport access vlan 10', ' FastEthernet0/1  switchport trunk encapsulation dot1q  switchport trunk allowed vlan 100,200  switchport mode trunk ', ' FastEthernet0/2  switchport mode access  switchport access vlan 20 ', ' FastEthernet0/3  switchport trunk encapsulation dot1q  switchport trunk allowed vlan 100,300,400,500,600  switchport mode trunk ', ' FastEthernet1/0  switchport mode access  switchport access vlan 20 ', ' FastEthernet1/1  switchport mode access  switchport access vlan 30 ', ' FastEthernet1/2  switchport trunk encapsulation dot1q  switchport trunk allowed vlan 400,500,600  switchport mode trunk ', ' Vlan100']

# def make_tunk_dict(data):
#     res_data = {}
#     check_str = digits + ','
#     for i in data.split():
#         if 'FastEthernet' in i:
#             res_data[i] = []
#             k = i
#         if all(map(lambda x: x in check_str, i)):
#             v = i
#             res_data[k] = [int(x) for x in v.split(',')]
#     return res_data

def add_vlan_1(data_dict):
  for i in data_dict:
    if bool(data_dict[i]) == False:
      data_dict[i] = 1
  return data_dict

# pprint(make_tunk_dict(data))
# check_str = digits + ','
# i = '10'
# res = any(map(lambda x: x in i, check_str))
# print(res)

m_dict = {'FastEthernet0/0': 10,
  'FastEthernet0/2': 20,
  'FastEthernet1/0': 20,
  'FastEthernet1/1': 30,
  'FastEthernet1/3': [],
  'FastEthernet2/0': [],
  'FastEthernet2/1': []}

pprint(add_vlan_1(m_dict))