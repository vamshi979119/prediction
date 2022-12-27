from flask import Flask, request, jsonify
import helpers

app = Flask(__name__)
@app.route('/get-prediction')
def predict():
    filePath = request.args.get('image_path')
    res=helpers.getCloudPrediction(filePath=filePath)
    return jsonify(results=res.tolist())

if __name__=='__main__':
    app.run(debug=True)
