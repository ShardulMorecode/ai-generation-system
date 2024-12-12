from diffusers import StableDiffusionPipeline, LMSDiscreteScheduler
import torch
import os

# Directories for saving images and videos
STATIC_DIR = 'static'
IMAGES_DIR = os.path.join(STATIC_DIR, 'images')
VIDEOS_DIR = os.path.join(STATIC_DIR, 'videos')

# Make sure directories exist
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(VIDEOS_DIR, exist_ok=True)

# Initialize the Stable Diffusion model
def load_model():
    # Use LMSDiscreteScheduler as an alternative scheduler
    scheduler = LMSDiscreteScheduler.from_pretrained("CompVis/stable-diffusion-v1-4", subfolder="scheduler")
    model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", scheduler=scheduler)
    return model

model = load_model()

# Use GPU if available, otherwise use CPU
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Image generation logic
def generate_images(prompt, num_images=1):
    images = []
    for idx in range(num_images):
        result = model(prompt)
        image = result.images[0]
        image_filename = f"{prompt.replace(' ', '_')}_{idx+1}.png"
        image_path = os.path.join(IMAGES_DIR, image_filename)
        image.save(image_path)
        images.append(image_filename)  # Only store the filename, not the full path
    return images

# Video generation logic
def generate_videos(prompt, num_videos=1):
    images = generate_images(prompt, num_images=10)  # Generate frames for the video
    video_paths = []
    for idx in range(num_videos):
        video_filename = f"{prompt.replace(' ', '_')}_{idx+1}.mp4"
        video_path = os.path.join(VIDEOS_DIR, video_filename)
        # Generate video from images using ffmpeg
        os.system(f"ffmpeg -framerate 1 -i {IMAGES_DIR}/%d.png -c:v libx264 -r 30 -pix_fmt yuv420p {video_path}")
        video_paths.append(video_filename)  # Store only the video filename
    return video_paths
