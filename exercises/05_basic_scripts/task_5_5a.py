# -*- coding: utf-8 -*-
"""
Завдання 5.5a

Доповнити скрипт із завдання 5.5 таким чином, щоб, залежно від вибраного
режиму, задавалися різні запитання у запиті про номер VLAN або список VLANів:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter the allowed VLANs:'

Плюсом буде вирішити завдання без використання умови if та циклу for, але
перший варіант рішення краще зробити так, як виходитиме.
"""

access_template = """switchport mode access
switchport access vlan {}
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
"""

trunk_template = """switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan {}
"""
int_mode = input('Enter interface mode (access/trunk): ')
int_type = input('Enter interface type and number: ')
if int_mode == 'access':
    vlan = input('Enter VLAN number: ')
elif int_mode == 'trunk':
    vlan = input('Enter the allowed VLANs:')

print('interface', int_type)
if int_mode == 'access':
    print(access_template.format(vlan))
elif int_mode == 'trunk':
    print(trunk_template.format(vlan))