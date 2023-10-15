# Voting System
# Implement a simple voting system using dictionaries. Allow users to vote for candidates, count the votes, and determine the winner.

voting_system = {
    'la_libertad_avanza':{
        'candidato': 'Milei',
        'numero_lista': '135A',
        'votos': 0
    },

    'union_por_la_patria':{
        'candidato': 'maza',
        'numero_lista': '502B',
        'votos': 0
    }

}

def vote_users(numero_lista):
    if numero_lista in voting_system:
        voting_system[numero_lista]['votos'] += 1


vote_users("135A")
vote_users("135A")
vote_users("135A")
vote_users("135A")
vote_users("135A")
vote_users("135A")
vote_users("135A")
vote_users("502B")

print(voting_system)