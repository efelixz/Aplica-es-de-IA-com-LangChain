from openai import OpenAI;

cliente = OpenAI(api_key="")

numero_de_dias = 7 
numero_de_crianca = 3
gostam = ""

prompt = f"Crie um roteiro de viagem de {numero_de_dias} dias para uma familia de {numero_de_crianca} que gostam de {gostam}."

cliente.chat.completion.create