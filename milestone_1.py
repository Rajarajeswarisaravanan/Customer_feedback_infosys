import pandas as pd
import re # text clening 
import string

STOPWORDS={
    "is","the","and","to","a","an","of","in","for","on","with","as","by","at","from","that","this","it","be","are","was","from","or","but"
}

def clean_text(text):
    text=str(text).lower()
    text=re.sub(r"http\S+","",text) # remove urls
    text=re.sub(r"\d+","",text) # remove numbers
    text=text.translate(str.maketrans("","",string.punctuation)) # remove punctuation
    text=re.sub(r"\s+","",text).strip() # remove extra whitespace
    words=[W for W in text.split() if W not in STOPWORDS]
    return " ".join(words)

def main():
    file_path_excel="ReviewSense_Customer_Feedback_5000.xlsx"
    file_path_csv="Milestone1_cleaned_feedback.csv"

    try:
        df=pd.read_excel(file_path_excel)
        print("Reading from Excel file")
    except FileNotFoundError:
        print("Excel file not found. Attempting to read from existing CSV.")
        try:
            df=pd.read_csv(file_path_csv)
            if "clean_feedback" in df.columns:
                print("CSV already has cleaned feedback. Skipping cleaning.")
                return 
            elif "feedback"in df.columns:
                print("Re-cleaning feedback from CSV.")
            else:
                raise ValueError("'feedback' column not found in CSV file.")
        except FileNotFoundError:
            raise ValueError("Neither Excel nor CSV file found. Please Provide the Input File")
    if "feedback" not in df.columns:
            raise ValueError(" 'feedback' column not found in the file")

    df["clean_feedback"] = df["feedback"].apply(clean_text)
    df.to_csv("Milestone1_cleaned_feedback.csv", index=False)
    print("Milestone 1 Completed Successfully")
    print(df[["feedback","clean_feedback"]].head())
if __name__=="__main__":
    main()
    
