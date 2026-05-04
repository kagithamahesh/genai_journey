# Templates use {{variable}} placeholders
templates = {
    "classify": """
You are a {{role}} classifier.
Classify the following text into one of these categories: {{categories}}.
Text: {{input_text}}
Respond with only the category name.
""",
    "summarise": """
Summarise the following {{document_type}} in {{num_sentences}} sentences.
Audience: {{audience}}
Document: {{input_text}}
""",
}