from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath

app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

# Result List
result_list = []

# Root URL
@app.route('/')
def index():
     # Set The upload HTML template '\templates\index.html'
    return render_template('index.html')


# Get the uploaded files
@app.route("/", methods=['POST'])
def uploadFiles():
      # get the uploaded file
      uploaded_file = request.files['file']
      result_list = []
      if uploaded_file.filename != '':
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
          # set the file path
           uploaded_file.save(file_path)
           csvParser(file_path)
          # save the file
      return redirect(url_for('result'))

#Result page
@app.route("/result")
def result():
     # Set The upload HTML template '\templates\index.html'
    return render_template('result.html',data=result_list)
      
    
# importing pandas 
import pandas as pd   

def csvParser(filepath):
    try:
        # importing csv file 
        df = pd.read_csv(filepath, header=None) 
        
        result_list.append("Uploaded file is in .CSV format.")

        print(df.head()) 

        # obtaining the shape 
        print("shape of dataframe", df.shape) 

        # obtaining the number of rows
        rows = df.shape[0]
        print("number of rows : ", rows) 

        # obtaining the number of columns 
        columns = df.shape[1]
        print("number of columns : ", columns) 

        if rows == 10 and columns == 3:
            result_list.append("Uploaded .CSV file has exactly 10 rows and 3 columns")
            print("Uploaded .CSV file has exactly 10 rows and 3 columns")
        else:
            result_list.append("Uploaded .CSV file does not have exactly 10 rows and 3 columns")
            print("Uploaded .CSV file does not have exactly 10 rows and 3 columns")
            
        for i in range(0, rows):
            for j in range(0, columns):
                if df.loc[i,j] == None:
                   result_list.append("Uploaded .CSV file is not Complete")
                   return
        result_list.append("Uploaded .CSV file is Complete")
    except:
        result_list.append("Uploaded file is not in .CSV format.")
        
    
    

if (__name__ == "__main__"):
     app.run(port = 5000)
   

















