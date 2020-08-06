import sys

file_path = sys.argv[1]

with open(file_path,'r') as file:
    texto_completo = file.read()

    a = texto_completo.split('Use your Operating System')
    final = ''
    for i in a[1:46]:
        indice_menor = i.find('update package')+len('update package')
        indice_maior = i.find('. For more')
        goal = i[indice_menor:indice_maior]
        final += goal

        identified_cve_lower_index = i.find('<div class="details_h1">')+len('<div class="details_h1">')
        identified_cve_upper_index = i.find('</div><div class="details_h2">Severity')
        goal_cve = i[identified_cve_lower_index:identified_cve_upper_index]
        print(goal + ':' + goal_cve)
