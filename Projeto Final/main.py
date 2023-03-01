from flask import Flask, render_template, request
import psycopg2 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('pokemons.html')

@app.route("/Pokemons")
def verPokemons():
    try:

        con = psycopg2.connect(database = "Pokemon", user = "postgres", password = "postgres", host = "localhost", port = 5432)
        cursor = con.cursor()
        cursor.execute('''SELECT * FROM "Pokemons" ORDER BY "Id" ASC''')
        pokemon = cursor.fetchall()

        return render_template('pokemons.html', pokemons=pokemon)
    
    except(Exception, psycopg2.Error) as error:
        return f"Ocorreu um erro {error}"

@app.route("/Pokemons/Inserir", methods=("GET", "POST"))
def inserirPokemons():
    if request.method == "POST":
        idPokemon = request.form['id']
        nomePokemon = request.form['nome']
        pesoPokemon = request.form['peso']
        alturaPokemon = request.form['altura']
        tipoPokemon = request.form['tipo']

        try:

            con = psycopg2.connect(database = "Pokemon", user = "postgres", password = "postgres", host = "localhost", port = 5432)
            cursor = con.cursor()
            
            cursor.execute(f'''INSERT INTO "Pokemons" VALUES('{idPokemon}', '{nomePokemon}', '{pesoPokemon}', '{alturaPokemon}', '{tipoPokemon}')''')
            con.commit()
            cursor.close()
            con.close()


            return render_template('pokemons.html')
    
        except(Exception, psycopg2.Error) as error:
            return f"Ocorreu um erro {error}"

    else:
        return render_template("inserirPokemon.html")

if __name__ == "__main__":
    app.run(debug=True)