import os
import boto3
from dotenv import load_dotenv

load_dotenv()

profile = os.getenv("AWS_PROFILE", "default")
region = os.getenv("AWS_REGION", "us-east-1")

session = boto3.Session(profile_name=profile, region_name=region)

# Bedrock "control plane" (listar modelos, etc.)
bedrock = session.client("bedrock")

# Bedrock Runtime (invocar modelos)
bedrock_runtime = session.client("bedrock-runtime")


def list_models():
    resp = bedrock.list_foundation_models()
    models = resp.get("modelSummaries", [])
    print(f"Found {len(models)} models in {region}")
    for m in models[:20]:
        print(f"- {m.get('modelId')} | {m.get('providerName')} | {m.get('modelName')}")


def invoke_example():
    """
    Exemplo genérico.
    O body muda de acordo com o provider/modelo (Anthropic, Amazon Titan, Meta, etc).
    """
    model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"  # exemplo comum (pode variar na sua conta)

    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 300,
        "messages": [
            {"role": "user", "content": "Write a short Python function that validates an email address."}
        ]
    }

    resp = bedrock_runtime.invoke_model(
        modelId=model_id,
        contentType="application/json",
        accept="application/json",
        body=bytes(__import__("json").dumps(body), "utf-8"),
    )

    raw = resp["body"].read().decode("utf-8")
    print(raw)


if __name__ == "__main__":
    list_models()
    # invoke_example()