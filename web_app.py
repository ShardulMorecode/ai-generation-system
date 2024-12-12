from flask import Flask, render_template, request, redirect, url_for, session, flash
import logging
from generation import generate_images, generate_videos  # Import the generation functions

# Initialize Flask app
app = Flask(__name__)

# Secret key for session management
app.secret_key = 'Mysecretkey'

# Home Route (Login Page)
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_id = request.form.get("user_id")
        if user_id:
            session["user_id"] = user_id
            flash("Login successful!", "success")
            return redirect(url_for("gallery"))
        else:
            flash("Please enter a valid User ID.", "error")
    return render_template("login.html")

# Gallery Route (Displays generated content)
@app.route("/gallery", methods=["GET"])
def gallery():
    # Check if the user is logged in
    if "user_id" not in session:
        flash("You need to log in first.", "error")
        return redirect(url_for("login"))
    
    # Example prompt for image and video generation
    prompt = "A futuristic city at sunset"
    
    # Generate images and videos based on the prompt
    image_paths = generate_images(prompt, num_images=1) 
    video_paths = generate_videos(prompt, num_videos=1)  

    # Pass generated content (image and video paths) to the gallery template
    return render_template("gallery.html", content={"image_paths": image_paths, "video_paths": video_paths})

if __name__ == "__main__":
    app.run(debug=True)
