import os,json,azure.functions as func
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def main(req: func.HttpRequest)->func.HttpResponse:
    body=req.get_json()
    text=body.get("text","")
    endpoint=os.getenv("LANGUAGE_ENDPOINT")
    key=os.getenv("LANGUAGE_KEY")
    client=TextAnalyticsClient(endpoint=endpoint,credential=AzureKeyCredential(key))

    lang=client.detect_language(documents=[text])[0].primary_language.name
    pii=client.recognize_pii_entities(documents=[text])[0]
    redacted=pii.redacted_text

    try:
        poller=client.begin_abstract_summary([redacted])
        result=poller.result()
        summary=""
        for doc in result:
            if not doc.is_error:
                summary=" ".join(s.text for s in doc.summaries)
    except Exception:
        summary="Abstractive summarization requires a supported Azure AI Language resource."

    return func.HttpResponse(
        json.dumps({"language":lang,"redacted":redacted,"summary":summary}),
        mimetype="application/json"
    )
