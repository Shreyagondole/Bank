from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bank():
    balance = 10000  # Initial balance
    output = ""      # To store messages for display

    if request.method == 'POST':
        try:
            # Get inputs from the form
            operation = request.form['operation']
            amount = int(request.form['amount'])

            # Perform the operation
            if operation == '1':  # Debit
                balance -= amount
                output = f"Debit successful! New balance: {balance}"
            elif operation == '2':  # Credit
                balance += amount
                output = f"Credit successful! New balance: {balance}"
            else:
                output = "Invalid operation selected."
        except ValueError:
            output = "Invalid amount entered."

    # HTML with CSS for background image
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>ABC Bank</title>
        <style>
            body {{
                background-image: url('/static/background.jpg.jpg'); /* Link to the static folder */
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
                font-family: Arial, sans-serif;
                color: white;
                text-align: center;
                margin: 0;
                padding: 0;
            }}
            .container {{
                margin-top: 50px;
                background: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
                padding: 20px;
                border-radius: 10px;
                display: inline-block;
            }}
            input, button {{
                margin: 10px;
                padding: 10px;
                border-radius: 5px;
                border: none;
                font-size: 16px;
            }}
        </style>
    </head>
    <body>
        <h1>Welcome to ABC Bank</h1>
        <div class="container">
            <form method="POST">
                <label for="operation">Choose operation:</label><br>
                <input type="radio" name="operation" value="1"> Debit<br>
                <input type="radio" name="operation" value="2"> Credit<br><br>
                <label for="amount">Enter amount:</label><br>
                <input type="number" name="amount" required><br><br>
                <button type="submit">Submit</button>
            </form>
            <p>{output}</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
