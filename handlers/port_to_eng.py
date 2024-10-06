import google.generativeai as genai

def corrigir_texto(texto):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f'Apenas faça o que eu pedir, não fale mais nada desnecessário como comentarios. Corrija o seguinte texto: {texto}')
    return response.text

def traducao_para_ingles(texto):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f'Apenas faça o que eu pedir, não fale mais nada desnecessário como comentarios. Traduza o seguinte texto para o inglês: {texto}')
    return response.text

genai.configure(api_key="coloque_sua_api_key_aqui")