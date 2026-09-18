from flask import Flask, render_template, request, redirect, url_for 
from datetime import datetime

app = Flask(__name__)
# nome do módulo
print(__name__)
# def é função, cria uma função, route é a rota, com a / é  para abrir o site
@app.route('/')
def inicio():
    return '<h1>Olá, mundo!</h1>'

@app.route('/sobre')
def sobre():
    return '''
    <h1 style='color:red'>Meu nome é: </h1>
    <p> Amanda Menezes <b> de Jesus</p>

    <--- Tudo que eu pensar em html pode vir aqui --->
'''
#  Exercício 1
@app.route('/curso')
def curso():
    return '''
    <h1> Este curso é chamado de: <h1>
    <h2 style='color:pink'> Gestão da Tecnologia da Informação!! </h2>
    <p style='color:deeppink'> Quarto semestre - Programação para Internet </p>
    '''
# f diz que o texto vai ser formatado para que receba variáveis. F = FORMATAR
@app.route('/var')
def variavel():
    palavra = 'Mariana Roma Corteze'
    return f'<h1> Adicionando texto de var: {palavra}'
# as variaveis devem ter o mesmo nome, ex o ano. Sinal de <> significa que é uma variável

@app.route('/idade/<int:ano>') 
def idade(ano):
    calculoIdade = 2026 - ano
    return f'Você tem {calculoIdade} anos!'

@app.route('/salvar/<nome>/produtos') 
def salvar(nome):
    return f'Você salvou o produto [ {nome} ] com sucesso!'

@app.route('/html') 
def pagina_html():
    return render_template('index.html')

# Exercício 2
@app.route('/gatinho') 
def gatinho():
   return '''
       <h1> Esta página é dedicada a um gatinho<h1>
       <h2 style='color:purple'> Amo meu Floquinho! </h2>
       <nav>
       <ul> 
       <li> 
       <a href="/html">Voltar</a> 
       </li> 
       <li> 
              <a href="/branco">Mais gatinhos</a> 
              </li> 
       </ul> 
       </nav> 

       '''

# CAIRÁ NA PROVA IF E ELSE
@app.route('/calcular/<nome>/<int:ano>') 
def calcular(nome, ano):
   ano_atual = datetime.now().year
   idade = ano_atual - ano

   if idade > 18:
          status = 'Maior de Idade'
   else:
          status = 'Menor de idade - ACESSO NEGADO'

   return render_template('variaveis.html', nome_usuario = nome, ano_atual = ano_atual, 
                           nascimento = ano, idade = idade, status = status) 
   
# AULA 04 - continuação da aula anterior!

@app.route('/dicio')
def dicionario():
    dados = {
        'chave' : 'valor',
        'curso' : 'GTI',
        'local' : 'Fatec Jahu',
        'semestre' : 4, 
    }
    return render_template('dicio.html', **dados)
# os dois asteriscos avisam pro codigo desempacotar toda a chave com as variavéis para o outro lado
 
# Atividade 1

@app.route('/condicao/<int:numero>')
def condicao(numero):
    return render_template('condicao.html', numero = numero)

#Aula 17/09
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():

    if request.method == 'POST':
        nome = request.form.get('nome', 'Nada enviado')
        num1 = int(request.form['numero1'])
        num2 = float(request.form['numero2'])

        soma = num1 + num2
        sub = num1 - num2
        mult = num1 * num2
        div = num1 / num2

        # redireciona para outra rota
        # url_for chama a função, não a rota
        return redirect(url_for('exibir_resultado',nome=nome, soma=soma, sub=sub, mult=mult, div=div))

    return render_template('formulario.html')

@app.route('/exibir')    
def exibir_resultado():
    nome =request.args.get('nome')
    soma = request.args.get('soma') 
    sub = request.args.get('sub')
    mult = request.args.get('mult')
    div = request.args.get('div')

    return render_template('exibir.html', nome=nome, soma=soma, sub=sub, mult=mult, div=div)

#Exibir é a rota
#Exibir_resultado é a função
#O url_for chama a função, não a rota


# O pedaço de código a seguir tem que ser sempre a ultima coisa do código!

if __name__ == '__main__':
    app.run(debug=True)



    





















#   --- ULTIMA COISA DO ARQUIVO --- 
if __name__ == '__main__':
    app.run(debug=True)