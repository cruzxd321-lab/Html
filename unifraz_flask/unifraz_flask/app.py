from flask import Flask, render_template, request, make_response
import re

app = Flask(__name__)

PASSWORDS = {
    0: "g4Nw8Xp2mKv5Rz9hYq3cT7bL",
    1: "m8Tz2Xw5pK9nRv4hYq7cL3bJ",
    2: "p3Nw7Xm2vK8qRz5hYt9cL4bG",
    3: "q7Kx3Nm9wP2vRz6hYt8cT4bM",
    4: "r9Lp4Xw7mK3nRv2hYq5cZ8bT",
    5: "s5Vx2Nw8kM4pRz7hYq3cT9bL",
    6: "t4Qw6Xm3vN8pRz2hYq9cL7bK",
    7: "v8Jx5Nm2wK7pRz4hYq6cT3bW",
    8: "w2Px8Nm6kK4vRz9hYq3cT7bF",
    9: "x6Rw3Nk8mP5vQz2hYq7cT4bJ",
}
DICCIONARIO = ['apple','banana','cherry','mango','orange','password','network','secure','firewall']

@app.route('/')
@app.route('/nivel/0')
def nivel0():
    return render_template('nivel0.html')

@app.route('/nivel/1')
def nivel1():
    return render_template('nivel1.html')

@app.route('/nivel/2')
def nivel2():
    return render_template('nivel2.html')

@app.route('/nivel/2/files/')
def nivel2_files():
    return '''<html><body>
    <h2>Index of /files</h2><hr>
    <a href="/nivel/2/files/pixel.png">pixel.png</a><br>
    <a href="/nivel/2/files/usuarios.txt">usuarios.txt</a><br>
    <hr><small>unifraz Server Port 80</small>
    </body></html>'''

@app.route('/nivel/2/files/usuarios.txt')
def nivel2_users():
    content = f"""# username:password
alice:BYNdCesZqW
bob:jw2ueICLvT
charlie:G5vCxkVV3m
unifraz3:{PASSWORDS[2]}
eve:zo4mJWyNj2
mallory:9urtcpzBmH
"""
    return content, 200, {'Content-Type': 'text/plain'}

@app.route('/nivel/2/files/pixel.png')
def nivel2_pixel():
    # 1x1 pixel PNG transparente
    import base64
    px = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==')
    return px, 200, {'Content-Type': 'image/png'}

@app.route('/nivel/3')
def nivel3():
    return render_template('nivel3.html')

@app.route('/nivel/3/robots.txt')
def nivel3_robots():
    return 'User-agent: *\nDisallow: /s3cr3t/\n', 200, {'Content-Type': 'text/plain'}

@app.route('/nivel/3/s3cr3t/')
def nivel3_secret():
    return f'<html><body><pre>unifraz4:{PASSWORDS[3]}</pre></body></html>'

@app.route('/nivel/4')
def nivel4():
    referer = request.headers.get('Referer', '')
    if 'unifraz5' in referer:
        return f'<html><body><p>Acceso concedido.<br>Contrasena para unifraz5: <strong>{PASSWORDS[4]}</strong></p></body></html>'
    return render_template('nivel4.html')
@app.route('/nivel/5')
def nivel5():
    loggedin = request.cookies.get('loggedin', '0')
    if loggedin == '1':
        resp = make_response(f'<html><body><p>Acceso concedido.<br>Contrasena para unifraz6: <strong>{PASSWORDS[5]}</strong></p></body></html>')
        return resp
    return render_template('nivel5.html')
SECRET_6 = "UNIFRAZSECRETO2024"

@app.route('/nivel/6', methods=['GET', 'POST'])
def nivel6():
    result = ''
    if request.method == 'POST':
        secret = request.form.get('secret', '')
        if secret == SECRET_6:
            result = f'Acceso concedido. Contrasena para unifraz7: {PASSWORDS[6]}'
        else:
            result = 'Secreto incorrecto'
    return render_template('nivel6.html', result=result)

@app.route('/nivel/6/includes/secret.inc')
def nivel6_inc():
    return '<pre>&lt;?\n$secret = "UNIFRAZSECRETO2024";\n?&gt;</pre>'
PAGES_7 = {
    'home': 'esta es la pagina principal',
    'about': 'pagina de informacion del juego unifraz',
    '/etc/unifraz_webpass/unifraz8': PASSWORDS[7],
}

@app.route('/nivel/7')
def nivel7():
    page = request.args.get('page', '')
    content = PAGES_7.get(page, '')
    return render_template('nivel7.html', content=content)
@app.route('/nivel/8', methods=['GET', 'POST'])
def nivel8():
    result = ''
    if request.method == 'POST':
        secret = request.form.get('secret', '')
        if secret == 'uFr4z2024':
            result = f'Acceso concedido. Contrasena para unifraz9: {PASSWORDS[8]}'
        else:
            result = 'Secreto incorrecto'
    return render_template('nivel8.html', result=result)

@app.route('/nivel/8/sourcecode')
def nivel8_src():
    return '''<pre style="background:#1e1e1e;color:#ccc;padding:20px;">
$encodedSecret = "7546723432303234";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
        print "Acceso concedido. La contrasena para unifraz9 es &lt;censored&gt;";
    } else {
        print "Secreto incorrecto";
    }
}
</pre>'''

@app.route('/nivel/9')
def nivel9():
    needle = request.args.get('needle', '')
    output = ''
    if needle:
        if ';' in needle or '#' in needle:
            output = f'unifraz10: {PASSWORDS[9]}'
        else:
            results = [w for w in DICCIONARIO if needle.lower() in w.lower()]
            output = '\n'.join(results) if results else '(sin resultados)'
    return render_template('nivel9.html', output=output)

@app.route('/nivel/9/sourcecode')
def nivel9_src():
    return '''<pre style="background:#1e1e1e;color:#ccc;padding:20px;">
$key = "";
if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}
if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
</pre>'''

@app.route('/nivel/10')
def nivel10():
    needle = request.args.get('needle', '')
    output = ''
    if needle:
        if re.search(r'[;|&]', needle):
            output = 'Caracter ilegal en la entrada!'
        elif '.*' in needle:
            output = 'unifraz11: x6Rw3Nk8mP5vQz2hYq7cT4bJ'
        else:
            results = [w for w in DICCIONARIO if needle.lower() in w.lower()]
            output = '\n'.join(results) if results else '(sin resultados)'
    return render_template('nivel10.html', output=output)

@app.route('/nivel/10/sourcecode')
def nivel10_src():
    return '''<pre style="background:#1e1e1e;color:#ccc;padding:20px;">
$key = "";
if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}
if($key != "") {
    if(preg_match('/[;|&]/', $key)) {
        print "Caracter ilegal en la entrada!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
</pre>'''

if __name__ == '__main__':
    app.run(debug=True, port=5000)
