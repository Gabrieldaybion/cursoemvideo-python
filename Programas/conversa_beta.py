try:
    a=int(input('Digite o prmeiro valor'))
    b=int(input('Digite o segundo valor :'))
    r= a/b
except (ValueError,TypeError):
    print('Deu erro meu filho, o dado inserido nao pode  ser usado')
except ZeroDivisionError:
    print('O numero nao pode ser dividido')

except KeyboardInterrupt:
    print('o usuario degistiu aquele viado')

else:
    print(f'O valor é {r}')
finally:
    print('Obriado por ter usado :)')
    