*LOCAL*
uvicorn app.main:app --reload

*DOCKER*
docker build -t word-embed-api .
docker run --rm -p 8000:8000 word-embed-api
