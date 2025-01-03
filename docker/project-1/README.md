1. Build the docker image by: `docker build -t webapp .`

2. After successful image creation run: `docker run -d --name webapp-test -p 8000:8000 webapp`

3. Open the browser and navigate: `http://localhost:8000/`
