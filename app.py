import gradio as gr
from model import score_headline
from analysis import find_risky_phrases

def run(headline):
    result = score_headline(headline)
    risky = find_risky_phrases(headline)
    return (
        f"Credibility: {result['credibility']}%",
        str(result["scores"]),
        ", ".join(risky) if risky else "None"
    )

with gr.Blocks() as demo:
    gr.Textbox(label="Headline", lines=1, placeholder="Enter news headline")
    out1 = gr.Textbox(label="Credibility")
    out2 = gr.Textbox(label="Raw scores")
    out3 = gr.Textbox(label="Risk phrases")

    demo.launch()
