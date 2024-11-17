#AULA RESUMO - PRINT, SEP (SEPARADOR) E END (FINAL DA LINHA), USO IDENTICO COM JAVA DO \N

# \r\n -> CRLF quebra de linha
# \n -> LF quebra de linha UNIX
print(12, 34, 1011, 10, 11, sep='-', end='##\n') # quebra de linha em python por padrão é sensítivel pela escrita na IDE não sendo necessário quebrar a linha
print(56, 78, sep="---", end='\n')
print(9, 10, sep='*') #argumento não nomeados, prevejo que sejam dados que não sejam armazenados em memória devido não ter sido alocado em mémoria por uma variável

# Python também é case sensitive (Caps != non-capital), ex.: comando print x Print
# sep = separador, pode utilizar tanto "" (aspas duplas) quanto '' (aspas simples)
# end = final da linha