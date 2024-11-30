from flask import Flask
import json
app = Flask(__name__)

def is_prime(number):
    if number < 2:
        return False
    elif number > 2:
        for i in range(2, number):
            if (number % i) == 0:
                return False
            return True

@app.route("/prime_number/<int:number>")
def prime_number(number):
    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return json.dumps(result)
if __name__ == '__main__':
    app.run(debug=True)
