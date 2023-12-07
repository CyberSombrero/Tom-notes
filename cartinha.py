closed_book = '''    
    _______
   /      /,
  /      //
 /______//
(______(/
'''

opened_book = '''
     ______ ______
    _/      Y      \_
   // ~~ ~~ | ~~ ~  \\
  // ~ ~ ~~ | ~~~ ~~ \\      
 //________.|.________\\    
`----------`-'----------'''

pagina1 = '''
_____________________
|                   |
|      Meu amor     |
|   eu preferiria   |
|  dar-te uma carta |  
|    de papel real  |
|     tão real      |  
| quanto o que sinto|
|                   |  
|                   |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾'''
pagina2 = '''
_____________________
|                   |
|mas papel não tenho|
|minha letra entorta|
|  eu fico confuso  |  
|      eu caio      |
|   por isso peço   |  
| essa carta digital|
|que mesmo sem papel|  
| tem o meu coração |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾'''

pagina3 = '''
_____________________
|                   |
|     eu te amo     |
|   como o mar ama  |
|       a lua       |
|    você me move   |
|     me balança    |  
|   mexe meu corpo  |
|    minha alma     |  
|                   |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾'''

pagina3 = '''
_____________________
|                   |
|  dentre as cartas |
|      de amor      |
|essa é desengonçada|
|      como eu      |
|  como o meu amor  |  
|ambos desengonçados|
|mas quero que aceite|  
|esse desengonçado  |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾'''

pagina4 = "Eu te amo muito. S2"

foi_embora = False
teimoso = False

while not foi_embora:
    livro_aberto = False 

    print(closed_book)

    

    abrir = '-1'
    while not ((abrir == '1') or (abrir == '2')): 
        abrir = input("Olha, um livro!!! Deseja abrí-lo para ver o que tem dentro? 1-Sim///2-Não ")
        if not ((abrir == '1') or (abrir == '2')):
            print("se decida, por favor. To com pressa por aqui")

        elif abrir == '1':
            livro_aberto = True
        
        elif abrir == '2': 
            deseja_sair = input("Você deseja sair? 1-sim")
            if deseja_sair == '1':
                foi_embora = True
                print('uma pena te ver indo embora :(')
            else:
                input("Então você so vai ficar olhando o livro aí parada mesmo?")
                input("Olha, vamos tentar denovo. Dessa vez abra o livro e se decida se que ler ou sair >:(")
                abrir = '-1'
            
    if livro_aberto and not foi_embora:
        print(opened_book)

        livro_lido = False
        ler = '-1'
        while not ler == '1' or ler == '2':
            ler = input("Abrindo o livro, parece ter uma mensagem escrita. Desejas lê-la? 1 - sim")

            if ler == '1':
                livro_lido = True
            else:
                print('Aí você me coloca em uma situação complicada... vamos tentar denovo e vê se você segue a história certinho dessa vez')
                input('a gente vai tenar mais uma vez, tudo certo? ')
                input('Não me importa qual foi a sua resposta, a gente vai tentar sim. Aperte qualquer coisa aí')
                ler = '-2'
                teimoso = True
    
        print(f'abrindo o livro {"e deixando de ser teimosa"*teimoso} e vendo os seus conteúdos, você começa a ler')


                
        input()
        print(pagina1)
        input()
        print(pagina2)
        input()
        print(pagina3)
        input()
        print(pagina4)

        input()
        foi_embora = True

