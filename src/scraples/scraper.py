import os
import pandas as pd

def FetchingData(path, title, col_name):
    data = pd.read_csv(path)
    colm_list = data[col_name].unique().tolist()

    output_dir = "/home/mtech/rishav/Asana_DataBuilder/data/fined_list_data"
    os.makedirs(output_dir, exist_ok=True)  # 🔑 create directory if missing

    output_path = os.path.join(output_dir, f"{title}.csv")

    pd.DataFrame({"title": colm_list}).to_csv(output_path, index=False)

    print(f"Saved file at: {output_path}")


#getting list of different roles in a company
#FetchingData(
 #   "/home/mtech/rishav/Asana_DataBuilder/data/clean_jobs.csv",
  #  "role",
  #  "title"
#)
#import kagglehub

# Download latest version
#path = kagglehub.dataset_download("tedlozzo/apaches-jira-issues")

#print("Path to dataset files:", path)
data=pd.read_csv("/home/mtech/.cache/kagglehub/datasets/tedlozzo/apaches-jira-issues/versions/2")
data.head()


