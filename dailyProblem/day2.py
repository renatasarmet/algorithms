class Solution: 
	def longestPalindrome(self, s):
		print(f"Original word: {s}")
		dic = {}
		# Pré-processamento
		# Primeiro, armazenar a posicao de cada letra. Obs: já está ordenado por natureza
		for i in range(len(s)):
			if s[i] in dic:
				dic[s[i]].append(i)
			else:
				dic[s[i]] = [i]

		maxLen = 0
		maxPalin = ""

		# Esse loop for controla qual vai ser a primeira letra da substring que vou tentar formar palindromo
		for i in range(len(s)):
			#Primeira letra é s[i]
			currentLen = 1

			# Se tem mais outra letra igual a essa, quero tentar formar palindromo
			# Portanto, i não pode ser o último da lista dessa letra 
			# (obs: se i for o único, ele também é o último)
			if (i != dic[s[i]][-1]): 

				# Quando tem mais de 1 ocorrência, pode ter 2 ou até mais....
				# A primeira abordagem é tentar usar a última ocorrência para tentar formar o maior palíndromo com esse i
				# Mas se não der certo, temos que continuar tentando utilizando as outras ocorrências, de trás para frente

				foundPalindrome = False
				qtyTry = 1 # quantidade de vezes que ja tentamos com i como letra inicial

				# Começa pegando a última ocorrencia dessa letra para formar o palíndromo
				lastIndex = dic[s[i]][-qtyTry] 

				# Enquanto ainda nao encontrou um palindromo aqui e tem mais ocorrencias
				while(not foundPalindrome):
					# Sempre que tiver um palindromo, existiriam subpalindromos, mas não queremos eles pq são menores que o outro
					# Também não queremos nem ver os que já aparentam ser menor que algum já encontrado

					# Portanto, se o tamanho que vou tentar ver é maior do que eu ja encontrei ate agora, vamos la ver
					if((lastIndex - i + 1) > maxLen):

						# Vamos tentar construir um palindromo terminando com a ultima ocorrencia dessa letra
						currentLen = 2 
						leftIndex = i+1
						rightIndex = lastIndex - 1
						foundPalindrome = True # começa considerando que vai dar certo, até provar que não da

						while ((leftIndex <= rightIndex) and foundPalindrome):

							# Se era impar e chegamos no meio, é palindromo!
							if leftIndex == rightIndex:
								currentLen += 1
								leftIndex += 1

							# se as letras sao iguais, continua procurando
							elif s[leftIndex] == s[rightIndex]:
								currentLen += 2
								leftIndex += 1
								rightIndex -= 1

							# se nao sao iguais, para.. nao era palindromo
							else:
								currentLen = 0
								foundPalindrome = False

						# Se foi palindromo
						if foundPalindrome:
							if currentLen > maxLen:
								maxLen = currentLen
								maxPalin = s[i:currentLen+i]

						# Se não achei um palíndromo, vamos tentar com a ocorrencia anterior da letra
						else:
							qtyTry += 1

							# Se ainda tem onde procurar
							if qtyTry < len(dic[s[i]]):
								# Pega a próxima última ocorrencia dessa letra para formar o palíndromo
								lastIndex = dic[s[i]][-qtyTry] 
							else:
								foundPalindrome = True # marca essa tag só para parar o loop externo, pq não tem mais ocorrencia

					# Se não, nem adianta tentar ver as ocorrencias anteriores dessa letra pq só seria menor
					else:
						foundPalindrome = True # indica aqui para acabar a busca

			
		# Se não encontrou palindromo mesmo, então o tamanho máximo desse 'palindromo' é 1
		if (maxLen == 0) and (len(s) > 0):
			maxLen = 1 # pelo menos tem 1 letra
			maxPalin = s[0]

		return maxPalin
		

# Test program
s = "tracecars"
# s = "abaora"
print(f"Max palindrome: {str(Solution().longestPalindrome(s))}")

