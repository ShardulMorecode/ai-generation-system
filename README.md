# AI Image and Video Generation System

## Project Overview
This project is a web-based AI system that generates images and videos based on user-provided text prompts. It utilizes Stable Diffusion for image generation and FFmpeg for video generation, offering an intuitive interface for users to generate and view their content.

---

## Features
- **User Authentication**: Simple login page using a unique User ID.
- **Image Generation**: Generate high-quality images from text prompts.
- **Video Generation**: Create videos by combining a series of AI-generated images.
- **Gallery**: View generated images and videos in a grid layout.
- **Notifications**: Alert users when their content is ready.

---

## Technologies Used
- **Backend**: Python, Flask
- **AI Models**: Stable Diffusion (via the `diffusers` library)
- **Video Processing**: FFmpeg
- **Frontend**: HTML, CSS
- **Database**: SQLite (for managing content)

---

## Installation and Setup

### Prerequisites
- Python 3.8 or above
- FFmpeg installed ([Download FFmpeg](https://ffmpeg.org/download.html))
- Git

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/ai-image-video-gen.git
   cd ai-image-video-gen
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the root directory with the following content:
   ```plaintext
   FLASK_APP=web_app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   ```

5. **Run the Application**:
   ```bash
   flask run
   ```

6. **Access the Web App**:
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## Directory Structure
```
.
├── static/
│   ├── images/             # Generated images
│   ├── videos/             # Generated videos
├── templates/
│   ├── login.html          # Login page
│   ├── gallery.html        # Gallery page
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
├── web_app.py              # Main Flask app
├── generation.py           # Image and video generation logic
├── models.py               # Database models
├── notifications.py        # Notification handling
└── README.md               # Project documentation
```

---

## Usage
1. **Login**: Enter your unique User ID to access the system.
2. **Generate Content**: Prompts like `A futuristic city at sunset` will generate corresponding images and videos.
3. **View Gallery**: Check the generated content in the gallery.

---

## Contributing
Feel free to fork this repository and create pull requests for new features or fixes. Contributions are welcome!

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contact
For any queries, please contact:
- **Name**: Shardul More
- **Email**: morepatilshardul@gmail.com

