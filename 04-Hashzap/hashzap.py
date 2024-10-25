# Tela Inicial:
    # Título: Hashzap
    # Botão: Iniciar Chat
        # Quando clicar:
            #abrir popup
                # Título: bem vindo ao Hashzap
                # TextBox: insira seu nome
                # Botão: entrar no chat
                    # Quando clicar
                        # Sumir titulo e sumir botão
                            # carregar chat e caixa de enviar mensagem
                                # Botão enviar: envia mensagem

# importar flet
import flet as ft

# criar uma função principal para rodar o app
def main(pagina):
    titulo = ft.Text("Haszap")

    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(mensagem)
        pagina.update()

    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = (f"{nome_usuario}: {texto_campo_mensagem}")
        pagina.pubsub.send_all(mensagem)
        campo_enviar_mensagem.value = ''
        pagina.update()

    campo_enviar_mensagem = ft.TextField(label="Digite sua mensagem",on_submit=enviar_mensagem )
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    chat = ft.Column()
    

    def entrar_chat(evento):
        popup.open = False
        pagina.remove(titulo)
        pagina.remove(botao)
        pagina.add(chat)
        pagina.add(linha_enviar)

        nome_usuario = caixa_nome.value
        mensagem = f'{nome_usuario} entrou no chat!'
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    # Criar um popup
    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    caixa_nome = ft.TextField(label="Digite seu nome")
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome,actions=[botao_popup])

    # Botão inicial
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        print("Clicou no botão")

    # Botão para abrir o popup
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    # Adicionando elementos
    pagina.add(titulo)
    pagina.add(botao)

# executar essa função com o flet
ft.app(main)