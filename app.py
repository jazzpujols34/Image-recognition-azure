from flask import Flask, render_template, request, redirect, url_for
import requests
import json
import os
import uuid

app = Flask(__name__)

prediction_key = "XXXXXXXXXXXXXXXXXXXXXXXXXX"
prediction_endpoint = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


@app.route("/", methods=["GET", "POST"])    
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        # Save the uploaded image with a unique name
        image_filename = f"{uuid.uuid4().hex}.jpg"
        file.save(os.path.join("static", image_filename))

        # Reset the file pointer
        file.seek(0)

        headers = {
            "Prediction-Key": prediction_key,
            "Content-Type": "application/octet-stream",
        }

        response = requests.post(prediction_endpoint, headers=headers, data=file.read())
        result = json.loads(response.content)
        predictions = result["predictions"]

        # Store the prediction history
        # Find the most probable prediction
        most_probable_prediction = max(predictions, key=lambda x: x["probability"])

        # Save the most probable prediction and the image filename to a text file
        with open("history.txt", "a") as f:
            f.write(f"{image_filename}\t{most_probable_prediction['tagName']}\t{most_probable_prediction['probability'] * 100:.2f}\n")

        return render_template("index.html", predictions=predictions, uploaded_image=image_filename)

    return render_template("index.html")



@app.route("/submit_feedback", methods=["POST"])
def submit_feedback():
    tag = request.form["tag"]
    confidence = request.form["confidence"]
    correct = request.form["correct"]

    # Store the feedback in your preferred storage/database
    # For example, store it in a text file
    with open("feedback.txt", "a") as f:
        f.write(f"{tag}\t{confidence}\t{correct}\n")

    return redirect(url_for("index"))

@app.route("/history", methods=["GET"])
def history():
    page = request.args.get("page", 1, type=int)
    per_page = 5  # Set the number of items per page

    # Load the prediction history from storage (for example, a text file)
    with open("history.txt", "r") as f:
        lines = f.readlines()

    total_pages = (len(lines) + per_page - 1) // per_page
    start = (page - 1) * per_page
    end = start + per_page

    predictions = []
    for line in lines[start:end]:
        image, tag, confidence = line.strip().split("\t")
        predictions.append({"image": image, "tag": tag, "confidence": confidence})

    return render_template("history.html", predictions=predictions, total_pages=total_pages, current_page=page)

@app.route("/tagging", methods=["GET", "POST"])
def tagging():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        # Save the uploaded image with a unique name
        image_filename = f"{uuid.uuid4().hex}.jpg"
        file.save(os.path.join("static", image_filename))

        return render_template("tagging.html", uploaded_image=image_filename)

    return render_template("tagging.html")

@app.route("/submit_tagging", methods=["POST"])
def submit_tagging():
    tag = request.form["tag"]
    image = request.form["image"]

    # Save the tagged image information in your preferred storage/database
    # For example, store it in a text file
    with open("tagged_images.txt", "a") as f:
        f.write(f"{image}\t{tag}\n")

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
