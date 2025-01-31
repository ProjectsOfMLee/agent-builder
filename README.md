# agent-builder

## Use Case 1: Build a Conversational Agent for tech documentation

### Prerequisites

- python 3.12
- data
    - format
        - [recommended] txt
        - PDF
        - json
        - HTML 

    - size
        - [recommended] each document should be under 3MB (by o1 token limit)
        - if broken into chunks, each chunk should be under 8KB (~6000 words)
- metadata: for the above data
    - content
        - name/doc title
        - summary: 2,3 sentences crucial for agent to understand if this doc is relevant to the user's query
        - tags: for the agent to NOT output giberrish 
            - contains image or not
            - contains table or not
            - contains code or not
            - wiki source article url
- compute
    - GPU (not required, but recommended)
    - over 8GB of RAM

### Steps
1. Install dependencies
```bash
pip install -r requirements.txt
```
2. Run the main.py
```bash
python main.py
```