def selic(q):
    valor=0
    selic=10410
    din=0
    if q<0.01:
        print('Não ')
    else:
        valor=selic*q
        din=valor+(valor*0.0504)*5
    return din
