import json
import os
import time
import re
from pathlib import Path
from langchain_ollama import ChatOllama

# ⚠️ SECURITY: Store your API key in an environment variable, not in code
# export OLLAMA_API_KEY="your_key_here"
API_KEY = os.getenv("OLLAMA_API_KEY")

# List of Ollama models to evaluate
MODELS = [
    "mistral-large-3:675b-cloud",
    "deepseek-v3.2:cloud",
    "mixtral:8x7b",
    "codellama:7b",
    # Add additional models as required
]

# Delay between API calls (seconds)
API_DELAY = 1.5
# Delay between switching models (seconds)
MODEL_SWITCH_DELAY = 3.0


def sanitize_filename(model_name: str) -> str:
    """Convert model name to a filesystem-safe string."""
    sanitized = re.sub(r'[^a-zA-Z0-9_-]', '_', model_name)
    return sanitized


def load_data(filepath: str) -> list:
    """Load JSON data from file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def format_prompt(history: list) -> str:
    """Format conversation history into a prompt for the LLM."""
    prompt = ""
    for msg in history:
        role = "المستخدم" if msg['role'] == 'user' else "المساعد"
        prompt += f"{role}: {msg['content']}\n"
    return prompt.strip()


def initialize_model(model_name: str, api_key: str) -> ChatOllama:
    """Initialize a ChatOllama instance for the specified model."""
    return ChatOllama(
        model=model_name,
        base_url="https://ollama.com",
        client_kwargs={
            "headers": {
                "Authorization": f"Bearer {api_key}"
            }
        },
    )


def process_turns(data: list, model, delay: float = 1.0) -> list:
    """Process each conversation turn and collect LLM responses."""
    results = []

    for item in data:
        item_id = item['id']
        item_result = {
            "id": item_id,
            "turns": []
        }

        print(f"Processing item {item_id}...")

        for turn_data in item['turns']:
            turn_num = turn_data['turn']
            history = turn_data['history']

            # Skip if last message is not from user (nothing to respond to)
            if not history or history[-1]['role'] != 'user':
                continue

            # Format prompt from history
            prompt = format_prompt(history)

            try:
                # Invoke model with timeout
                response = model.invoke([{"role": "user", "content": prompt}])
                llm_response = response.content if hasattr(response, 'content') else str(response)

            except Exception as e:
                print(f"Error on item {item_id}, turn {turn_num}: {str(e)}")
                llm_response = f"ERROR: {str(e)}"

            # Structure the result per your specification
            turn_result = {
                f"turn{turn_num}": llm_response,
                "is_toxic": None,  # Implement toxicity detection logic here if needed
                "resultat": llm_response,
                "metadata": {
                    "task": item.get('task'),
                    "scene": item.get('metadata', {}).get('scene'),
                    "language": item.get('metadata', {}).get('language')
                }
            }

            item_result['turns'].append(turn_result)

            # Rate limiting to avoid API throttling
            time.sleep(delay)

        results.append(item_result)

    return results


def save_results(results: list, output_path: str):
    """Save results to JSON file with proper encoding."""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"✓ Results saved to {output_path}")


def main():
    BASE_DIR = Path(__file__).parent.parent
    input_file = BASE_DIR / "results_by_model" / "dataset.json"
    output_dir = BASE_DIR / "results_by_model"

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Validate input file exists
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found")
        return

    # Load dataset once (shared across all models)
    data = load_data(input_file)
    print(f"Loaded {len(data)} conversation items")

    # Iterate through each model
    for model_name in MODELS:
        print(f"\n{'='*60}")
        print(f"Processing with model: {model_name}")
        print(f"{'='*60}\n")

        try:
            # Initialize model
            model = initialize_model(model_name, API_KEY)

            # Process all turns
            results = process_turns(data, model, delay=API_DELAY)

            # Generate output filename
            safe_name = sanitize_filename(model_name)
            output_file = os.path.join(output_dir, f"results_{safe_name}.json")

            # Save output
            save_results(results, output_file)

            # Summary
            total_turns = sum(len(item['turns']) for item in results)
            print(f"✅ Model '{model_name}' complete: {len(results)} items, {total_turns} turns")

        except Exception as e:
            print(f"❌ Failed to process model '{model_name}': {str(e)}")
            continue

        # Optional delay between models to respect rate limits
        if model_name != MODELS[-1]:
            print(f"⏳ Waiting {MODEL_SWITCH_DELAY}s before next model...")
            time.sleep(MODEL_SWITCH_DELAY)

    print(f"\n🎉 All models processed. Results stored in '{output_dir}/'")


if __name__ == "__main__":
    main()