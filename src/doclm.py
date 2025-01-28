# Use a pipeline as a high-level helper
from transformers import pipeline
# Load model directly
from transformers import AutoTokenizer, AutoModelForDocumentQuestionAnswering

pipe = pipeline("document-question-answering", model="impira/layoutlm-document-qa")
tokenizer = AutoTokenizer.from_pretrained("impira/layoutlm-document-qa")
model = AutoModelForDocumentQuestionAnswering.from_pretrained("impira/layoutlm-document-qa")