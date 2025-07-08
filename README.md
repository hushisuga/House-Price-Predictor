#  House Price Prediction – ML Project

A machine learning web app that predicts house prices based on key features like location, area, number of bedrooms, and more. Built with Python, scikit-learn, and Flask. The UI is implemented using HTML. The project includes a Jupyter notebook showcasing data preprocessing, model training, and evaluation.


##  Demo

 Click Watch Demo to watch the demo video (hosted Google Drive):
[[Watch Demo]](https://drive.google.com/file/d/1e2Z2ydFXxERD9LWyNPlzQNDiNAUGjUqG/view?usp=sharing)

> 💡 _Not deployed live — this video demonstrates how the web app works locally._


##  Features Used

- Location (One-Hot Encoded)
- Area (in square feet)
- Number of Bedrooms
- Number of Bathrooms
- Furnishing Type
- BHK/1RK indicator



##  Model Info

- **Algorithm:** Ridge Regression  
- **Performance Metric:** R² Score  
- **Model Saved As:** `RidgeModel.pkl`  
- **Model Development:** See `house_prediction.ipynb` for full preprocessing, EDA, and training pipeline.



##  How to Run the Project

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/house-price-predictor.git
   cd house-price-predictor
2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
3. **Install dependencies**
   ```bash
     pip install -r requirements.txt
4. **Run the Flask app**
   ```bash
     python main.py
5. **Open your browser** and go to http://127.0.0.1:5000

##  Deployment
Not deployed online. Please watch the demo video above to see how it works locally.






