RESPONSE=$(curl -s -X POST -H "Authorization: Token $REPLICATE_API_TOKEN" https://dreambooth-api-experimental.replicate.com/v1/upload/mini-summarization-training-ds-forllama-text.jsonl)

curl -X PUT -H "Content-Type: application/jsonl" --upload-file mini-summarization-training-ds-forllama-text.jsonl "$(jq -r ".upload_url" <<< "$RESPONSE")"

SERVING_URL=$(jq -r ".serving_url" <<< $RESPONSE)
echo $SERVING_URL
