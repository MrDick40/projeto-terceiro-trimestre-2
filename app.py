```python
import string
import gradio as gr

# ============================================================
# TABELAS DE SUBSTITUICAO
# ============================================================

MAPA_LETRAS = "qwertyuiopasdfghjklzxcvbnm"
LETRAS_ORIGINAIS = "abcdefghijklmnopqrstuvwxyz"

MAPA_CAPITAIS = "QWERTYUIOPASDFGHJKLZXCVBNM"
CAPITAIS_ORIGINAIS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

MAPA_DIGITOS = "9876543210"
DIGITOS_ORIGINAIS = "0123456789"


# ============================================================
# CODIFICACAO E DECODIFICACAO
# ============================================================

def criptografar(texto):
    """Transforma letras e numeros usando substituicao."""
    resultado = ""

    for caractere in texto:
        if caractere in LETRAS_ORIGINAIS:
            indice = LETRAS_ORIGINAIS.index(caractere)
            resultado += MAPA_LETRAS[indice]

        elif caractere in CAPITAIS_ORIGINAIS:
            indice = CAPITAIS_ORIGINAIS.index(caractere)
            resultado += MAPA_CAPITAIS[indice]

        elif caractere in DIGITOS_ORIGINAIS:
            indice = DIGITOS_ORIGINAIS.index(caractere)
            resultado += MAPA_DIGITOS[indice]

        else:
            resultado += caractere

    return resultado


def descriptografar(texto):
    """Recupera o texto anterior a codificacao."""
    resultado = ""

    for caractere in texto:
        if caractere in MAPA_LETRAS:
            indice = MAPA_LETRAS.index(caractere)
            resultado += LETRAS_ORIGINAIS[indice]

        elif caractere in MAPA_CAPITAIS:
            indice = MAPA_CAPITAIS.index(caractere)
            resultado += CAPITAIS_ORIGINAIS[indice]

        elif caractere in MAPA_DIGITOS:
            indice = MAPA_DIGITOS.index(caractere)
            resultado += DIGITOS_ORIGINAIS[indice]

        else:
            resultado += caractere

    return resultado


# ============================================================
# CALCULO DE HASH
# ============================================================

def gerar_hash(texto):
    """Soma os valores Unicode dos caracteres recebidos."""
    if not texto:
        return "0"

    total = sum(ord(caractere) for caractere in texto)
    return f"Valor calculado: {total} (nao reversivel de forma unica)"


# ============================================================
# ANALISE DA SENHA
# ============================================================

def verificar_senha(senha):
    """Classifica a senha conforme tamanho e variedade."""
    if not senha:
        return "Digite uma senha para iniciar a analise."

    minusculas = any(letra.islower() for letra in senha)
    maiusculas = any(letra.isupper() for letra in senha)
    numeros = any(letra.isdigit() for letra in senha)
    especiais = any(letra in string.punctuation for letra in senha)

    tamanho = len(senha)
    variedade = sum([minusculas, maiusculas, numeros, especiais])

    if tamanho >= 8 and variedade >= 3:
        return "FORTE: bom tamanho e variedade de caracteres."

    if tamanho >= 6 and variedade >= 2:
        return "MEDIA: tente aumentar o tamanho e a variedade."

    return "FRACA: utilize mais caracteres e diferentes tipos."


# ============================================================
# INTERFACE DO SISTEMA
# ============================================================

with gr.Blocks(title="Ferramenta de Criptografia") as app:
    gr.Markdown("# Sistema de Seguranca e Criptografia")
    gr.Markdown(
        "Utilize as ferramentas abaixo para codificar textos, "
        "recuperar o conteudo original, calcular um hash simples "
        "ou verificar a complexidade de uma senha."
    )

    with gr.Tab("Codificar"):
        entrada_codificacao = gr.Textbox(
            label="Texto original",
            placeholder="Digite o texto..."
        )
        saida_codificacao = gr.Textbox(
            label="Texto codificado"
        )
        botao_codificar = gr.Button("Codificar texto")

        botao_codificar.click(
            fn=criptografar,
            inputs=entrada_codificacao,
            outputs=saida_codificacao
        )

    with gr.Tab("Decodificar"):
        entrada_decodificacao = gr.Textbox(
            label="Texto codificado",
            placeholder="Digite o texto codificado..."
        )
        saida_decodificacao = gr.Textbox(
            label="Texto recuperado"
        )
        botao_decodificar = gr.Button("Decodificar texto")

        botao_decodificar.click(
            fn=descriptografar,
            inputs=entrada_decodificacao,
            outputs=saida_decodificacao
        )

    with gr.Tab("Hash"):
        entrada_hash = gr.Textbox(
            label="Texto para calculo",
            placeholder="Digite um texto..."
        )
        saida_hash = gr.Textbox(
            label="Resultado"
        )
        botao_hash = gr.Button("Calcular hash")

        botao_hash.click(
            fn=gerar_hash,
            inputs=entrada_hash,
            outputs=saida_hash
        )

    with gr.Tab("Forca da senha"):
        entrada_senha = gr.Textbox(
            label="Senha para avaliar",
            placeholder="Digite uma senha...",
            type="password"
        )
        saida_senha = gr.Textbox(
            label="Resultado da analise"
        )
        botao_analisar = gr.Button("Avaliar senha")

        botao_analisar.click(
            fn=verificar_senha,
            inputs=entrada_senha,
            outputs=saida_senha
        )


if __name__ == "__main__":
    app.launch()
```
