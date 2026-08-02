from flask import Flask, render_template, jsonify, request, redirect, url_for, session
import random

app = Flask(__name__)
# Necesario para usar 'session' en Flask
app.secret_key = 'una_clave_muy_secreta_y_segura_para_alisson' 

# La lista completa de frases, incluyendo las nuevas
frases = [
    "Eres mi melodía favorita.",
    "Cada día te quiero más.",
    "Haces que mi mundo sea mucho mejor.",
    "Eu te amo muito.",
    "Eres la mejor parte de mi día.",
    "Gracias por ser como eres.",
    "Te quiero mucho, hoy y siempre.",
    "Eres la luz que ilumina mi camino y el sueño que nunca quiero despertar.",
    "En cada latido de mi corazón, solo puedo sentir tu nombre.",
    "Contigo, cada día es una aventura maravillosa llena de amor y risas.",
    "Tú eres mi refugio en medio de la tormenta, mi paz en la locura del mundo.",
    "Cada momento contigo es una razón para sonreír y agradecer al universo por ponerte en mi camino.",
    "Tú llenas mi vida de colores y pintas mis días con la paleta del amor más hermosa.",
    "Eres mi sueño hecho realidad, mi realidad que supera cualquier sueño.",
    "Con cada beso tuyo, siento que el tiempo se detiene y el mundo desaparece a nuestro alrededor.",
    "No hay distancia ni obstáculo que pueda separarnos, porque nuestro amor es más fuerte que cualquier adversidad.",
    "Cada momento lejos de ti es una eternidad, pero cada momento contigo es un suspiro de felicidad.",
    "En tu sonrisa encuentro la paz que buscaba y en tus ojos el reflejo de un amor puro y sincero.",
    "Tú eres el latido de mi corazón, la melodía de mi alma y el amor de mi vida.",
    "A tu lado descubro el verdadero significado del amor, un sentimiento que trasciende palabras y abraza el alma.",
    "Contigo aprendí que el amor no se trata de encontrar a alguien perfecto, sino de amar a alguien de manera perfecta.",
    "En cada abrazo tuyo encuentro el hogar que siempre anhelé, el lugar donde pertenezco.",
    "Eres mi inspiración, mi motivación y mi razón para levantarme cada mañana con una sonrisa en el rostro.",
    "Contigo, cada momento se convierte en un recuerdo invaluable que atesoro en lo más profundo de mi corazón.",
    "Tus besos son la medicina para todas mis heridas y tus abrazos el bálsamo para todas mis penas.",
    "En cada mirada tuya encuentro la paz que tanto buscaba y el amor que siempre necesitaré.",
    "Te amo más de lo que las palabras pueden expresar, más de lo que mi corazón puede contener.",
    "Eres mi mejor amiga, mi confidente y mi compañera de vida, y por eso te amaré por siempre.",
    "Contigo, el amor se convierte en un poema eterno que nunca deja de escribirse.",
    "En tus brazos encuentro el refugio perfecto, el lugar donde puedo ser completamente yo mismo.",
    "Tú haces que cada día valga la pena vivirlo, cada momento digno de ser recordado.",
    "YO TE AMO MA Y PUNTO ",
    "Te amo no solo por lo que eres, sino por lo que soy cuando estoy contigo, porque a tu lado soy la mejor versión de mí mismo."
]

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        usuario = request.form.get('username')
        password = request.form.get('password')
        
        # Validación
        if usuario == 'ALISSON' and password == '20052026':
            session['autorizado'] = True
            return redirect(url_for('sorpresa'))
        else:
            error = 'Datos incorrectos, mi amor. ¡Intenta de nuevo!'
            
    return render_template('login.html', error=error)

@app.route('/sorpresa')
def sorpresa():
    if not session.get('autorizado'):
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/obtener_frase')
def obtener_frase():
    if not session.get('autorizado'):
        return jsonify({"error": "No autorizado"}), 401
    
    frase_elegida = random.choice(frases)
    return jsonify({"frase": frase_elegida})

if __name__ == '__main__':
    app.run(debug=True)