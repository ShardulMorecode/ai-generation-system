import os
from models import UserContent, Session
import logging

def update_database(user_id, prompt, image_paths, video_paths, status):
    session = Session()
    content = UserContent(
        user_id=user_id,
        prompt=prompt,
        video_paths=video_paths,
        image_paths=image_paths,
        status=status
    )
    session.add(content)
    session.commit()
    session.close()

def save_content(user_id, images, videos):
    base_dir = f"generated_content/{user_id}"
    os.makedirs(base_dir, exist_ok=True)

    image_paths, video_paths = [], []
    for i, img_path in enumerate(images):
        img_save_path = os.path.join(base_dir, f"image_{i+1}.png")
        os.rename(img_path, img_save_path)
        image_paths.append(img_save_path)

    for i, vid_path in enumerate(videos):
        vid_save_path = os.path.join(base_dir, f"video_{i+1}.mp4")
        os.rename(vid_path, vid_save_path)
        video_paths.append(vid_save_path)

    return image_paths, video_paths

logging.basicConfig(filename='user_activity.log', level=logging.INFO)

def log_activity(user_id, action):
    logging.info(f"{datetime.datetime.utcnow()}: User {user_id} performed action: {action}")
    