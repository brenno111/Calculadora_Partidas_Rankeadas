def rank(vitoria = int, derrota = int):
    saldo_vitorias = vitoria - derrota

    if saldo_vitorias <= 10:
        nivel = "Ferro"
    
    elif saldo_vitorias <=20:
        nivel = "Bronze"

    elif saldo_vitorias <=50:
        nivel = "Prata"
    
    elif saldo_vitorias <=80:
        nivel = "Ouro"
    
    elif saldo_vitorias <=90:
        nivel = "Diamante"

    elif saldo_vitorias <=100:
        nivel = "Lendário"

    elif saldo_vitorias >= 101:
        nivel = "Imortal"

    print(f"O Herói tem de saldo de {saldo_vitorias} e está no nível de {nivel}")


rank(60,10)