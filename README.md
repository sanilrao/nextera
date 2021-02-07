
The application name is FLASK CSV File Upload.
Folder Structure:
nextera:
- static
  - files
- templates
  - index.html
  - result.html
- Dockerfile
- main.py
- README.md
- requirements.txt

The main.py is a Flask application that enables the user to upload any file. The uploaded file is stored in the static/files/ folder.
The csvParser() function checks whether the file is .CSV type using a try except block. If it is a .CSV file, it then counts the rows and columns and checks if there are 10 rows and 3 columns.
Then it checks if every cell has data to declare whether it is complete or incomplete.

 
The HTML files for rendering on the browser are stroed in the templates/ folder. The index.html is the first page that is loaded. Once submit is clicked, the page is redirected to result.html.
The result.html page displays the following:
1. Whether the file is a .CSV file.
2. If it is a .CSV file, then the row and column count is displayed.
3. If every cell contains data, then it displays "Complete", else it displays "Incomplete".

The requirements.txt defines the dependencies and versions to be installed.


The code base was pushed to GitHub as a private repository. This code was then cloned to the Cloud Shell as described below.

***************************************************************************************************************************

Reference link: https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app

On Google Cloud Shell:
git clone https://github.com/sanilrao/nextera.git
git checkout -b master
git pull origin master --allow-unrelated-histories

docker build -t gcr.io/${PROJECT_ID}/nextera:v2 .
docker run --rm -p 5000:5000 gcr.io/${PROJECT_ID}/nextera:v2
gcloud auth configure-docker
docker push gcr.io/${PROJECT_ID}/nextera:v2
gcloud config set project $PROJECT_ID
gcloud config set compute/zone us-east1-b
gcloud container clusters create nextera-cluster
kubectl create deployment nextera --image=gcr.io/${PROJECT_ID}/nextera:v2
kubectl scale deployment nextera --replicas=3
kubectl autoscale deployment nextera --cpu-percent=80 --min=1 --max=5
kubectl get pods
kubectl expose deployment nextera --name=nextera-service --type=LoadBalancer --port 80 --target-port 5000
kubectl get service
External IP: 35.190.133.229