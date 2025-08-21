# Importa a classe principal do Kivy que controla o ciclo de vida da aplicação.
from kivy.app import App

# Importa o widget Label, usado para exibir texto na tela.
from kivy.uix.label import Label


# Cria a classe principal do aplicativo.
# Ela herda de App, o que significa que ganha todas as funcionalidades do Kivy para rodar uma aplicação.
class HelloWorldApp(App):

    # O método build() é chamado automaticamente quando o aplicativo inicia.
    # Ele define o "conteúdo" da janela, ou seja, o que vai aparecer na tela.
    def build(self):
        # Retorna um widget do tipo Label.
        # Esse Label exibirá o texto "hello, word" na janela.
        # halign="center" → alinha o texto horizontalmente ao centro.
        # valign="middle" → alinha o texto verticalmente ao centro.
        return Label(
            text="hello, word",
            halign="center",
            valign="middle",
        )  


# Verifica se o arquivo está sendo executado diretamente (não importado por outro módulo).
# Se for executado, inicia o aplicativo chamando o método run().
if __name__ == "__main__":
    HelloWorldApp().run()
