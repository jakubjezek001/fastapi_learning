
@REM docker build -t poll-app .

@REM docker run -it -p 80:80 -v %CD%/app:/app poll-app

docker-compose up