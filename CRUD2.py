x=0
while x==0:
    op1=input("Pressione Enter para começar: ")
    if op1=="":
    	a=0
    	nome=[]
    	email=[]
    	data=[]
    	cpf=[]
    	tell=[]
    	print("-----------------------------------------------------------------------\n")
    	print("                         Programa CRUD por")
    	print("                David Saboia e Silva Filho  N.º13     ")
    	print("                Gabriel Lima Soares de Oliveira  N.º23  ")
    	print("                Ykaro Ribeiro Rosa N.º46    ")
    	print("\n-----------------------------------------------------------------------")
    	qtc=0
    	while a==0:
    		print("\n","="*27," MENU INICIAL ","="*27)
    		print("1-Cadastrar")
    		print("2-Ler")
    		print("3-Deletar")
    		print("4-Atualizar")
    		print("5-Sair")
    		esc=input("Escolha a opção que deseja:\n")
    		if esc=="1":
    			c=0
    			if qtc==0:
        			while c==0:
        				print("__"*35)
        				qtc=int(input('Quantos cadastros você quer fazer?\n '))
        				if qtc>0:
        				    print("__" *35)
        				    print("Preencha os espaços abaixo para fazer o seu cadastro:")
        				    print("__"*35)
        				    qt=1
        				    registro=0
        				    while  registro<qtc:
        				        print("__"*5,"Cadastro %s"%qt,"__"*5)
        				        no=input("Digite seu nome completo: ")
        				        e=input("Digite seu e-mail: ")
        				        d=input("Digite sua data de nascimento: ")
        				        cpf1=input("Digite seu CPF: ")
        				        t=input("Digite seu Telefone: ")
        				        print("__" *35)
        				        print("Deseja continuar o cadastro com essas informações ou deseja refazer? ")
        				        l=0
        				        while l==0:
        				            print("1-Salvar")
        				            print("2-Refazer")
        				            i=int(input("Digite sua escolha: "))
        				            print("__"*35)
        				            if i==1:
        				                if no=="" or e=="" or d=="" or cpf1=="" or t=="":
        				                    print("!!Há campos vazios!!")
        				                    print("Por favor preencha os campos corretamente")
        				                    print("__" *35)
        				                    l=1
        				                else:
        				                    print("  "*13 ,"Dados salvos")
        				                    nome.append(no)
        				                    email.append(e)
        				                    data.append(d)
        				                    cpf.append(cpf1)
        				                    tell.append(t)
        				                    if qt==qtc:
        				                        l=1
        				                        c=1
        				                        registro+=1
        				                    else:
        				                        l=1
        				                        qt+=1
        				                        registro+=1
        				            elif i==2:
        				                    print("Refazer cadastro")
        				                    l=1
        				                    registro=registro
        				            else:
        				                print("  "*13 ,"Sem função")
        				else:
        					print("Número de cadastros invalido")
        					c=0
    			elif qtc!=0:
    			    print("__" *35)
    			    print("Você já tem cadastros feitos!!")
    			    print("__" *35)
    			    k=0
    			    while k==0:
    			        print("Você deseja: ")
    			        print("1-Adicionar cadastros")
    			        print("2-Valtar ao menu inicial")
    			        i=int(input("Escolha sua opção: "))
    			        print("__" *35)
    			        if i==1:
    			            while c==0:
                				print("__"*35)
                				qtc2=int(input('Digite:\n "0" se quiser voltar ao menu\n ou\n Quantos cadastros você quer fazer:\n '))
                				if qtc2>0:
                						print("__" *35)
                						print("Preencha os espaços abaixo para fazer o seu cadastro:")
                						print("__"*35)
                						qtc3=qtc2+qtc
                						qt2=qtc+1
                						registro=0
                						while  registro<qtc2:
                							print("__"*5,"Cadastro %s"%qt2,"__"*5)
                							no=input("Digite seu nome completo: ")
                							e=input("Digite seu e-mail: ")
                							d=input("Digite sua data de nascimento: ")
                							cpf1=input("Digite seu CPF: ")
                							t=input("Digite seu Telefone: ")
                							print("__" *35)
                							print("Deseja continuar o cadastro com essas informações ou deseja refazer? ")
                							l=0
                							while l==0:
                							    print("1-Salvar")
                							    print("2-Refazer")
                							    d=input("Digite sua escolha: ")
                							    print("__"*35)
                							    if d=="1":
                							        if i==1:
                							            if no=="" or e=="" or d=="" or cpf1=="" or t=="":
                							                print("!!Há campos vazios!!")
                							                print("Por favor preencha os campos corretamente")
                							                print("__" *35)
                							                l=1
                							            else:
                							            	print("  "*13 ,"Dados salvos")
                							            	nome.append(no)
                							            	email.append(e)
                							            	data.append(d)
                							            	cpf.append(cpf1)
                							            	tell.append(t)
                							            	qtc+=1
                							            	qt2+=1
                							            	if qt2==qtc3+1:
                							            	    registro+=1
                							            	    l=1
                							            	    c=1
                							            	    k=1
                							            	else:
                							            	    registro+=1
                							            	    l=1
                							    elif d=="2":
                							        print("Refazer cadastro")
                							        registro=registro
                							        l=1
                							    else:
                							        print("  "*13 ,"Sem função")
                				elif qtc2==0:
                				    c=1
                				    k=1
                				else:
                				    print("Número de cadastros invalido")
                				    c=0
    			        elif i==2:
    			            k=1
    			        else:
    			            print("  "*13 ,"Sem função")
    		elif esc=="2":
    			if qtc!=0:
    				registro=0
    				qr=1
    				print("=="*12,"Cadastros Registrados","=="*12)
    				while registro<qtc:
    					print("__"*5,"Cadastro %s"%qr,"__"*5)
    					print("Nome: ",nome[registro])
    					print("E-mail: ",email[registro])
    					print("Data de nascimento: ",data[registro])
    					print("CPF: ",cpf[registro])
    					print("Telefone: ",tell[registro])
    					print("--"*35)
    					registro+=1
    					qr+=1
    				e=0
    				while e==0:
    					enter=input("Pressione 'Enter' para voltar ao menu:\n")
    					if enter=="":
    						e=1
    					else:
    						print("__"*35)
    						print("!!Erro na tecla digitada tente novamente!!")
    						print("--"*35)
    			elif qtc==0:
    				print("__"*35)
    				print("  "*13 ,"Sem cadastro")
    				print("__"*35)
    		elif esc=="3":
    			print("__" *35)
    			if qtc!=0:
    				u=0
    				while u==0:
    					registro=0
    					print("=="*12,"Cadastros Registrados","=="*12)
    					while registro<qtc:
    						print("-="*5,"Cadastro ",registro+1,"-="*5)
    						print("Nome: ",nome[registro])
    						print("E-mail: ",email[registro])
    						print("Data de nascimento: ",data[registro])
    						print("CPF: ",cpf[registro])
    						print("Telefone: ",tell[registro])
    						print("--"*35)
    						registro+=1
    					qcd=int(input('Digite:\n"-1" para deletar todos\nou\n"0" para voltar ao menu inicial\nou\nQual cadastro você quer deletar\n'))
    					if qcd<=qtc and qcd>0:
    					    print("Cadastro deletado")
    					    qcd-=1
    					    del nome[qcd]
    					    del email[qcd]
    					    del data[qcd]
    					    del cpf[qcd]
    					    del tell[qcd]
    					    qtc=qtc-1
    					    if qtc==0:
    					        u=1
    					elif qcd==0:
    						u=1
    					elif qcd==-1:
    					    print("-"*35)
    					    print("                           Todos os cadastros foram deletados")
    					    print("-"*35)
    					    nome=[]
    					    emai=[]
    					    data=[]
    					    cpf=[]
    					    tell=[]
    					    qtc=0
    					    u=1
    					else:
    						print("__"*35)
    						print("Não há esse cadastro/Função")
    						print("__"*35)
    			else:
    				print("__"*35)
    				print("  "*13 ,"Sem cadastro")
    				print("__"*35)
    		elif esc=="4":
    			print("__" *35)
    			if qtc!=0:
    				u=0
    				while u==0:
    					registro=0
    					print("=="*12,"Cadastros Registrados","=="*12)
    					while registro<qtc:
    						print("__"*5,"Cadastro ",registro+1,"__"*5)
    						print("Nome: ",nome[registro])
    						print("E-mail: ",email[registro])
    						print("Data de nascimento: ",data[registro])
    						print("CPF: ",cpf[registro])
    						print("Telefone: ",tell[registro])
    						print("--"*35)
    						registro+=1
    					qcd=int(input('Digite "-1" para atualizar todos\nou\nDigite "0" para voltar ao menu inicial\nou\nDigite qual cadastro você quer atualizar\n'))
    					if qcd<=qtc and qcd>0:
    						t=0
    						while t==0:
    						    h=0
    						    print("-"*5,"Você está atualizado o cadastro ",qcd,"-"*5)
    						    inp=input("Digite seu novo nome: ")
    						    inp2=input("Digite seu novo e-mail: ")
    						    inp3=input("Digite sua nova data de nascimento: ")
    						    inp4=input("Digite seu novo CPF: ")
    						    inp5=input("Digite seu novo telefone: ")
    						    while h==0:
    						        vcd=int(input("Você deseja:\n1-Salvar\n2-Refazer\n3-Voltar sem salvar\n"))
    						        if vcd==1:
    						            if inp=="" or inp2=="" or inp3=="" or inp4=="" or inp5=="":
    						                print("Há campos vazios!")
    						                print("Por favor preencha os campos")
    						                print("--"*35)
    						            else:
    						                qcd-=1
    						                nome[qcd]=inp
    						                email[qcd]=inp2
    						                data[qcd]=inp3
    						                cpf[qcd]=inp4
    						                tell[qcd]=inp5
    						                print("!!Todas as informações foram atualizadas!!")
    						                print("__"*35)
    						                h=1
    						                t=1
    						                u=0
    						        elif vcd==2:
    						            h=1
    						            t=1
    						            u=0
    						        elif vcd==3:
    						            h=1
    						            t=1
    						        else:
    						            print("  "*13 ,"Sem função")
    					elif qcd==0:
    					    u=1
    					elif qcd==-1 and qtc!=0:
    					    qt3=0
    					    while qt3<qtc:
    					        print("-"*5,"Você está atualizado o cadastro ",qt3+1,"-"*5)
    					        inp=input("Digite seu novo nome: ")
    					        inp2=input("Digite seu novo e-mail: ")
    					        inp3=input("Digite sua nova data de nascimento: ")
    					        inp4=input("Digite seu novo CPF: ")
    					        inp5=input("Digite seu novo telefone: ")
    					        h=0
    					        while h==0:
    					            vcd=int(input("Você deseja:\n1-Salvar\n2-Refazer\n"))
    					            if vcd==1:
    					                if inp=="" or inp2=="" or inp3=="" or inp4=="" or inp5=="":
    						                print("!!Há campos vazios!!")
    						                print("Por favor preencha os campos")
    						                h=1
    						                print("--"*35)
    					                else:
    						                nome[qt3]=inp
    						                email[qt3]=inp2
    						                data[qt3]=inp3
    						                cpf[qt3]=inp4
    						                tell[qt3]=inp5
    						                print("As informações foram atualizadas")
    						                print("__"*35)
    						                h=1
    						                qt3+=1
    					            elif vcd==2:
    					                h=1
    					            else:
    						            print("  "*13 ,"Sem função")
    					else:
    						print("_"*35)
    						print("Não á esse cadastro")
    						print("_"*35)
    			else:
    				print("__"*35)
    				print( "  "*13 ,"Sem cadastro")
    				print("__"*35)
    		elif esc=="5":
    		    ss=0
    		    while ss==0:
    			    ops=int(input("Deseja sair do programa?\n 1-Sim\n 2-Não\n "))
    			    if ops==1:
    				    print("Fechando sistema...")
    				    print("Fim do programa")
    				    a=1
    				    x=1
    				    ss=1
    			    elif ops==2:
    			        a=0
    			        ss=1
    			    else:
    			        print("Opção Inválida")
    			        ss=0
    		else:
    			print("Essa opção não existe\n==Por favor digite uma opção do menu==\n")
    else:
    	print("===Enter não pressionado===\nVocê digitou '%s'! "%op1)