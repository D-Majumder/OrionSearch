import os
from sentence_transformers import SentenceTransformer
from PIL import Image
import chromadb

# --- 1. Setup ---
model = SentenceTransformer('clip-ViT-B-32')
IMAGE_FOLDER = "test_images"

# --- 2. Initialize Database ---
db_client = chromadb.PersistentClient(path="./orion_db")
collection = db_client.get_or_create_collection(name="photos")

# --- 3. Scan and Index Images ---
print("Starting image scan...")
indexed_count = 0

existing_ids = set(collection.get(include=[])['ids'])
print(f"Found {len(existing_ids)} existing images in database.")

for filename in os.listdir(IMAGE_FOLDER):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        
        file_path = os.path.join(IMAGE_FOLDER, filename)
        image_id = file_path
        
        if image_id in existing_ids:
            continue
            
        try:
            img = Image.open(file_path).convert('RGB')
            embedding = model.encode(img).tolist()
            
            collection.add(
                ids=[image_id],
                embeddings=[embedding],
                metadatas=[{"filename": filename, "path": file_path}]
            )
            indexed_count += 1
            print(f"Added: {image_id}")
            
        except Exception as e:
            print(f"Error adding {image_id}: {e}")

print("--- Indexing Complete ---")
print(f"Total new images added: {indexed_count}")
print(f"Total images in database: {collection.count()}")