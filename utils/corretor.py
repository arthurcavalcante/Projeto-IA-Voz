import language_tool_python

# ler o conteúdo de um arquivo .txt
with open('arquivo.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# escolher a língua para correção
tool = language_tool_python.LanguageTool('pt-BR') 

# corrigir o texto
matches = tool.check(text)
corrected_text = language_tool_python.utils.correct(text, matches)

# gravar o texto corrigido em um novo arquivo .txt
with open('texto_corrigido.txt', 'w', encoding='utf-8') as file:
    file.write(corrected_text)

# biblioteca: pip install language-tool-python