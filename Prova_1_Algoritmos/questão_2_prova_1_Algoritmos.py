op_c = input() # opção de carne

if op_c != 'C' and op_c != 'BF' and op_c != 'BS':
    print('Opção inválida.')
   
else:
   
    pa = input().upper() # Se quer pão de alho
    ba = input().upper() # Se quer bebidas para adultos
    bc = input().upper() # Se quer bebidas para crianças
    qc = int(input()) # Quantidade de crianças
    qa = int(input()) # Quantidade de adultos


    if op_c == 'C':
        if pa == 'N':
            # 200 bovino   100 frango   100 su�no
            v = (0.2*32 + 0.1*18 + 0.1*15)*qa + (0.2*32)*qc
           
            if ba == 'S' and bc == 'N':
                print(f'R$: {((v + 2*8*qa)*0.98):.2f}')
            elif ba == 'N' and bc == 'S':
                print(f'R$: {((v + 0.5*6*qc)*0.98):.2f}')
            elif ba == 'S' and bc == 'S':
                print(f'R$: {((v + 2*8*qa + 0.5*6*qc)*0.98):.2f}')
            elif ba == 'N' and bc == 'N':
                print(f'R$: {(v*0.98):.2f}')
       
        elif pa == 'S':
            # 200 bovino   100 frango   100 su�no
            v = (0.2*32 + 0.1*18 + 0.1*15)*qa + (0.2*32)*qc
           
            if ba == 'S' and bc == 'N':
                print(f'R$: {(v + 2*8*qa):.2f}')
            elif ba == 'N' and bc == 'S':
                print(f'R$: {(v + 0.5*6*qc):.2f}')
            elif ba == 'S' and bc == 'S':
                print(f'R$: {(v + 2*8*qa + 0.5*6*qc):.2f}')
            elif ba == 'N' and bc == 'N':
                print(f'R$: {v:.2f}')
       
    elif op_c == 'BF':
        if pa == 'N':
            v = (0.25*32*qa + 0.15*18*qa) + (0.2*32)*qc
           
            if ba == 'S' and bc == 'N':
                print(f'R$: {((v + 2*8*qa)*0.98):.2f}')
            elif ba == 'N' and bc == 'S':
                print(f'R$: {((v + 0.5*6*qc)*0.98):.2f}')
            elif ba == 'S' and bc == 'S':
                print(f'R$: {((v + 2*8*qa + 0.5*6*qc)*0.98):.2f}')
            elif ba == 'N' and bc == 'N':
                print(f'R$: {(v*0.98):.2f}')
       
        elif pa == 'S':
            v = (0.25*32*qa + 0.15*18*qa) + (0.2*32)*qc
           
            if ba == 'S' and bc == 'N':
                print(f'R$: {(v + 2*8*qa):.2f}')
            elif ba == 'N' and bc == 'S':
                print(f'R$: {(v + 0.5*6*qc):.2f}')
            elif ba == 'S' and bc == 'S':
                print(f'R$: {(v + 2*8*qa + 0.5*6*qc):.2f}')
            elif ba == 'N' and bc == 'N':
                print(f'R$: {v:.2f}')

    elif op_c == 'BS':
        if pa == 'N':
            v = (0.25*32 + 0.15*15)*qa + (0.2*32)*qc
           
            if ba == 'S' and bc == 'N':
                print(f'R$: {((v + 2*8*qa)*0.98):.2f}')
            elif ba == 'N' and bc == 'S':
                print(f'R$: {((v + 0.5*6*qc)*0.98):.2f}')
            elif ba == 'S' and bc == 'S':
                print(f'R$: {((v + 2*8*qa + 0.5*6*qc)*0.98):.2f}')
            elif ba == 'N' and bc == 'N':
                print(f'R$: {(v*0.98):.2f}')
       
        elif pa == 'S':
            v = (0.25*32 + 0.15*15)*qa + (0.2*32)*qc
           
            if ba == 'S' and bc == 'N':
                print(f'R$: {(v + 2*8*qa):.2f}')
            elif ba == 'N' and bc == 'S':
                print(f'R$: {(v + 0.5*6*qc):.2f}')
            elif ba == 'S' and bc == 'S':
                print(f'R$: {(v + 2*8*qa + 0.5*6*qc):.2f}')
            elif ba == 'N' and bc == 'N':
                print(f'R$: {v:.2f}')
