# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)


Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ipaddr = input("Введите адрес: ")

network10 = '''
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}'''

network2 = '''{0}  {1}  {2}  {3}'''

maskSlash = '''
Mask:
/{0}'''
mask10 =  '''{0:<8}  {1:<8}  {2:<8}  {3:<8}'''
mask2 = '''{0}  {1}  {2}  {3}'''

ip = ipaddr.split('/')

ip1 = ip[0].split(".")
int0 = int(ip1[0])
int1 = int(ip1[1])
int2 = int(ip1[2])
int3 = int(ip1[3])

mask = int(ip[1])
m2 = "1" * mask + "0" * (32 - mask)
zeros = 32 - mask

m2Int0 = m2[0:8]
m2Int1 = m2[8:16]
m2Int2 = m2[16:24]
m2Int3 = m2[24:32]

bin0 = bin(int0).lstrip("0").lstrip("b").zfill(8)
bin1 = bin(int1).lstrip("0").lstrip("b").zfill(8)
bin2 = bin(int2).lstrip("0").lstrip("b").zfill(8)
bin3 = bin(int3).lstrip("0").lstrip("b").zfill(8)

binFull = bin0 + bin1 + bin2 + bin3
binNetworkWithoutZeros = binFull[0:mask]
binNetworkPlusZeros = binNetworkWithoutZeros + "0" * (32 - mask)

binNetwork0 = binNetworkPlusZeros[0:8]
binNetwork1 = binNetworkPlusZeros[8:16]
binNetwork2 = binNetworkPlusZeros[16:24]
binNetwork3 = binNetworkPlusZeros[24:32]


#print(binNetworkWithoutZeros)
#print(binNetworkPlusZeros)

print(network10.format(int(binNetwork0, 2), int(binNetwork1, 2),int(binNetwork2, 2),int(binNetwork3, 2)))
print(network2.format(binNetwork0, binNetwork1, binNetwork2, binNetwork3))

print(maskSlash.format(mask))
print(mask10.format(int(m2Int0, 2), int(m2Int1, 2),int(m2Int2, 2),int(m2Int3, 2)))
print(mask2.format(m2Int0, m2Int1, m2Int2, m2Int3))
