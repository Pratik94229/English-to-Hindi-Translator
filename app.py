from flask import Flask, request, render_template
from src.translator.pipeline.prediction import PredictionPipeline

app = Flask(__name__)
model_predict = PredictionPipeline()  # Create an instance of PredictionPipeline

@app.route('/', methods=['GET', 'POST'])
def translate_text():
    if request.method == 'POST':
        user_input = request.form['user_input']
        translated_text = model_predict.predict(user_input)
        return render_template('index.html', user_input=user_input, translated_text=translated_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
