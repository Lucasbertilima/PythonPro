aviao = []
fortwo= []
terminal = ['comissaria1','comissaria2', 'piloto', 'oficial1', 'oficial2', 'chefe de serviço','policial', 'presidiario']

print('piloto entra no veiculo')
fortwo.append('piloto')
terminal.remove('piloto')
print('oficial 1 entra no veiculo')
fortwo.append('oficial1')
terminal.remove('oficial1')
print(f'Pessoas que ainda estão no terminal {terminal}')

print('fortwo viaja até o avião')
print('oficial 1 desembarca do fortwo')
fortwo.remove('oficial1')
aviao.append('oficial1')
print(f'Pessoas que  estão no aviao {aviao}')

print('fortwo viaja até o terminal')
print('oficial 2 entra no veiculo')
fortwo.append('oficial2')
terminal.remove('oficial2')
print(f'Pessoas que ainda estão no terminal {terminal}')

print('fortwo viaja até o avião')
print('oficial 2 desembarca do fortwo')
fortwo.remove('oficial2')
aviao.append('oficial2')
print(f'Pessoas que  estão no aviao {aviao}')

print('fortwo viaja até o terminal')
print('chefe de serviço entra no veiculo')
fortwo.append('chefe de serviço')
terminal.remove('chefe de serviço')