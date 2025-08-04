from flask import Flask, request

app = Flask(__name__)

@app.route('/api/callbacks', methods=['POST'])
def callbacks():
    event_data = request.json
    print("Event empfangen:", event_data)  # Für Logs
    # Hier Verarbeitung der Events einbauen
    return '', 200

if __name__ == "__main__":
    app.run()
