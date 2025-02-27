# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface     FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O     10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route.replace('O, 'OSPF')
str1 = ospf_route.strip().split()
str1.remove('via')
 names = (
    ...: 'Protocol',
    ...: 'Prefix'
    ...: 'AD/Metric',
    ...: 'Next-Hop',
    ...: 'Last-Update',
    ...: 'Outbound Interface')

                   

                   
fields = tuple(i + ':' for i in names)

str1 = re.sub(r',|via| [\[\]]', '', text).split()
lst = zip(fields, str1)
width = max(map(len,fields))

format = '{:%d}{:10}' % (width + 5)

result = '\n'.join(format.format(*i) for i in lst)

print result

                   
                 
