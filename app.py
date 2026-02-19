

from flask import Flask, render_template_string

app = Flask(__name__)

# --- TEMPLATE HTML/CSS MINIMALISTA ---
# Injetamos o CSS diretamente no HTML para manter a simplicidade em um único arquivo.
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PontoAPonto Delivery</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📦</text></svg>" />
    <style>
        body {
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f8f8f8;
            color: #333;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            text-align: center;
        }
        .container {
            background-color: #fff;
            padding: 40px 30px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            max-width: 500px;
            width: 90%;
            animation: fadeIn 0.8s ease-out;
        }
        h1 {
            color: #2c3e50;
            font-size: 2.5em;
            margin-bottom: 15px;
            letter-spacing: -0.5px;
        }
        p {
            font-size: 1.1em;
            line-height: 1.6;
            color: #555;
            margin-bottom: 25px;
        }
        .btn {
            display: inline-block;
            background-color: #007bff; /* Azul vibrante */
            color: white;
            padding: 12px 25px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            transition: background-color 0.3s ease, transform 0.2s ease;
            box-shadow: 0 2px 10px rgba(0, 123, 255, 0.2);
        }
        .btn:hover {
            background-color: #0056b3; /* Azul mais escuro no hover */
            transform: translateY(-2px);
        }
        footer {
            margin-top: 40px;
            font-size: 0.9em;
            color: #888;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📦 PontoAPonto Delivery</h1>
        <p>A sua entrega rápida e eficiente, de qualquer ponto para qualquer ponto. <br>Conectando você ao que importa, sem complicação.</p>
        <a href="#" class="btn">Saiba Mais</a>
    </div>
    <footer>
        <p>&copy; 2026 PontoAPonto. Todos os direitos reservados.</p>
    </footer>
</body>
</html>
"""

# Rota principal para a aplicação de delivery
@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

# Se quiser adicionar mais rotas, por exemplo, para pedidos:
@app.route('/pedido')
def pedido():
    return "<h1>Faça seu pedido com PontoAPonto!</h1><p>Em breve, mais funcionalidades aqui.</p>"

if __name__ == '__main__':
    app.run(debug=True) # debug=True para desenvolvimento local
