import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from imblearn.pipeline import make_pipeline
from imblearn.over_sampling import SMOTE
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score
from sklearn.compose import make_column_transformer
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score,f1_score,confusion_matrix
from sklearn.model_selection import cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.conf import settings
import os



def value_predict(X_train, y_train, X_val, y_val, steps):
    pipeline = make_pipeline(*steps)
    pipeline.fit(X_train, y_train)
    y_val_pred = pipeline.predict(X_val)

    return y_val_pred



def Knn_view(request):
    # Assuming you have your training and validation data (X_train, y_train, X_val, y_val)
    # Replace this with your actual data

    # Define your preprocessing steps
    #column_transformer = ColumnTransformer()  # Define your ColumnTransformer
    #scaler = StandardScaler()  # Example: Use StandardScaler for scaling

    # Define the hyperparameter grid for KNN

    data_dir = os.path.join(settings.BASE_DIR,'myapp', 'views', 'ML_model', 'data','processed')

    #train_file_path = os.path.join(data_dir, 'train.csv')
    #val_file_path = os.path.join(data_dir, 'val.csv')
    #test_file_path = os.path.join(data_dir, 'test.csv')
    train_file_path = request.FILES['knn_train']
    val_file_path = request.FILES['knn_val']
    #print(request.FILES['knn_val'])
    test_file_path = request.FILES['knn_test']

    df_train = pd.read_csv(train_file_path)
    df_val = pd.read_csv(val_file_path )
    df_test = pd.read_csv(test_file_path)


    X_train = df_train.drop(columns=["claim_number", "fraud"])
    y_train = df_train["fraud"]
    X_val = df_val.drop(columns=["fraud"])
    y_val = df_val["fraud"]
    X_test = df_test.drop(columns=["claim_number"])




    categorical_features = X_train.columns[X_train.dtypes == object].tolist()
    column_transformer = make_column_transformer(
        (OneHotEncoder(drop="first"), categorical_features),
        remainder="passthrough",
    )
    scaler = MinMaxScaler()


    def modeling(X_train, y_train, X_val, y_val, steps):
        pipeline = make_pipeline(*steps)
        pipeline.fit(X_train, y_train)
        y_val_pred_proba = pipeline.predict_proba(X_val)[:, 1]
        y_val_pred = pipeline.predict(X_val)
        #accuracy = accuracy_score(y_val,y_val_pred)
        metric = roc_auc_score(y_val, y_val_pred_proba)
        metric_f1 = f1_score(y_val,y_val_pred)
    
        if isinstance(pipeline._final_estimator, RandomizedSearchCV) or isinstance(pipeline._final_estimator, GridSearchCV):
            print(f"Best params: {pipeline._final_estimator.best_params_}")
        #print(f"Accuracy:{accuracy}")    
        print(f"AUC score: {metric}")
        print(f"f1 score:{metric_f1}")
        
        
        return pipeline




    param_grid = {
        "n_neighbors": [5, 10, 25, 50],
        "weights": ["uniform", "distance"],
    }

    # Create a KNN classifier with grid search
    knn_clf = GridSearchCV(
        KNeighborsClassifier(),
        param_grid=param_grid,
        n_jobs=-1,
        cv=5,
        scoring="roc_auc",
    )

    # Call the modeling function to train the model and print evaluation metrics
    knn_pipeline = modeling(X_train, y_train, X_val, y_val, [column_transformer, scaler, knn_clf])

    # Call the value_predict function to get predicted values
    predicted_value = value_predict(X_train, y_train, X_val, y_val, [column_transformer, scaler, knn_clf])

    # You can customize the response based on your requirements
    response = f"Model trained. Predicted values: {predicted_value}"
    knn_accuracy = accuracy_score(y_val, knn_pipeline.predict(X_val))

    context={
        'knn_accuracy':knn_accuracy,
        'logistic_accuracy':'',
        'XGboost_accuracy':''
    }
    request.session['knn_accuracy'] = knn_accuracy
    #return render(request,'ML_ui.html',context)
    return redirect('ml_ui')




def logistic_view(request):
    data_dir = os.path.join(settings.BASE_DIR,'myapp', 'views', 'ML_model', 'data','processed')

    #train_file_path = os.path.join(data_dir, 'train.csv')
    #val_file_path = os.path.join(data_dir, 'val.csv')
    #test_file_path = os.path.join(data_dir, 'test.csv')
    train_file_path = request.FILES['logistic_train']
    val_file_path = request.FILES['logistic_val']
    #print(request.FILES['knn_val'])
    test_file_path = request.FILES['logistic_test']

    df_train = pd.read_csv(train_file_path)
    df_val = pd.read_csv(val_file_path )
    df_test = pd.read_csv(test_file_path)


    X_train = df_train.drop(columns=["claim_number", "fraud"])
    y_train = df_train["fraud"]
    X_val = df_val.drop(columns=["fraud"])
    y_val = df_val["fraud"]
    X_test = df_test.drop(columns=["claim_number"])




    categorical_features = X_train.columns[X_train.dtypes == object].tolist()
    column_transformer = make_column_transformer(
        (OneHotEncoder(drop="first"), categorical_features),
        remainder="passthrough",
    )
    scaler = MinMaxScaler()


    def modeling(X_train, y_train, X_val, y_val, steps):
        pipeline = make_pipeline(*steps)
        pipeline.fit(X_train, y_train)
        y_val_pred_proba = pipeline.predict_proba(X_val)[:, 1]
        y_val_pred = pipeline.predict(X_val)
        #accuracy = accuracy_score(y_val,y_val_pred)
        metric = roc_auc_score(y_val, y_val_pred_proba)
        metric_f1 = f1_score(y_val,y_val_pred)
    
        if isinstance(pipeline._final_estimator, RandomizedSearchCV) or isinstance(pipeline._final_estimator, GridSearchCV):
            print(f"Best params: {pipeline._final_estimator.best_params_}")
        #print(f"Accuracy:{accuracy}")    
        print(f"AUC score: {metric}")
        print(f"f1 score:{metric_f1}")

        
        
        
        return pipeline
    
    lr_clf = LogisticRegression()
    lr_pipeline = modeling(X_train, y_train, X_val, y_val, [column_transformer, scaler, lr_clf])
    predicted_value = value_predict(X_train, y_train, X_val, y_val, [column_transformer, scaler, lr_clf])
    logistic_accuracy = accuracy_score(y_val, lr_pipeline.predict(X_val))*100
    print(logistic_accuracy)

    
    request.session['logistic_accuracy'] = logistic_accuracy
    #return render(request,'ML_ui.html',context)
    return redirect('ml_ui')


def xgboost_view(request):

    data_dir = os.path.join(settings.BASE_DIR,'myapp', 'views', 'ML_model', 'data','processed')

    #train_file_path = os.path.join(data_dir, 'train.csv')
    #val_file_path = os.path.join(data_dir, 'val.csv')
    #test_file_path = os.path.join(data_dir, 'test.csv')
    train_file_path = request.FILES['xgb_train']
    val_file_path = request.FILES['xgb_val']
    #print(request.FILES['knn_val'])
    test_file_path = request.FILES['xgb_test']

    df_train = pd.read_csv(train_file_path)
    df_val = pd.read_csv(val_file_path )
    df_test = pd.read_csv(test_file_path)


    X_train = df_train.drop(columns=["claim_number", "fraud"])
    y_train = df_train["fraud"]
    X_val = df_val.drop(columns=["fraud"])
    y_val = df_val["fraud"]
    X_test = df_test.drop(columns=["claim_number"])




    categorical_features = X_train.columns[X_train.dtypes == object].tolist()
    column_transformer = make_column_transformer(
        (OneHotEncoder(drop="first"), categorical_features),
        remainder="passthrough",
    )
    scaler = MinMaxScaler()


    def modeling(X_train, y_train, X_val, y_val, steps):
        pipeline = make_pipeline(*steps)
        pipeline.fit(X_train, y_train)
        y_val_pred_proba = pipeline.predict_proba(X_val)[:, 1]
        y_val_pred = pipeline.predict(X_val)
        #accuracy = accuracy_score(y_val,y_val_pred)
        metric = roc_auc_score(y_val, y_val_pred_proba)
        metric_f1 = f1_score(y_val,y_val_pred)

        if isinstance(pipeline._final_estimator, RandomizedSearchCV) or isinstance(pipeline._final_estimator, GridSearchCV):
            print(f"Best params: {pipeline._final_estimator.best_params_}")
        #print(f"Accuracy:{accuracy}")    
        print(f"AUC score: {metric}")
        print(f"f1 score:{metric_f1}")

        
        
        
        return pipeline
    
    param_grid = {
    "max_depth": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "learning_rate": [0.001, 0.01, 0.1, 0.2, 0.3],
    "subsample": [0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    "colsample_bytree": [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    "colsample_bylevel": [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    "min_child_weight": [0.5, 1.0, 3.0, 5.0, 7.0, 10.0],
    "gamma": [0, 0.25, 0.5, 1.0],
    "n_estimators": [10, 20, 40, 60, 80, 100, 150, 200]
    }

    xgb_clf = RandomizedSearchCV(
        XGBClassifier(),
        param_distributions=param_grid,
        n_iter=50,
        n_jobs=-1,
        cv=5,
        random_state=23,
        scoring="roc_auc",
    )

    xgb_pipeline = modeling(X_train, y_train, X_val, y_val, [column_transformer, scaler, xgb_clf])
    xgb_accuracy = accuracy_score(y_val, xgb_pipeline.predict(X_val))*100
    request.session['xgb_accuracy'] = xgb_accuracy
    print(xgb_accuracy)
    return redirect('ml_ui')



def randomforest_view(request):
    #train_file_path = os.path.join(data_dir, 'train.csv')
    #val_file_path = os.path.join(data_dir, 'val.csv')
    #test_file_path = os.path.join(data_dir, 'test.csv')
    train_file_path = request.FILES['rdmf_train']
    val_file_path = request.FILES['rdmf_val']
    #print(request.FILES['knn_val'])
    test_file_path = request.FILES['rdmf_test']

    df_train = pd.read_csv(train_file_path)
    df_val = pd.read_csv(val_file_path )
    df_test = pd.read_csv(test_file_path)


    X_train = df_train.drop(columns=["claim_number", "fraud"])
    y_train = df_train["fraud"]
    X_val = df_val.drop(columns=["fraud"])
    y_val = df_val["fraud"]
    X_test = df_test.drop(columns=["claim_number"])




    categorical_features = X_train.columns[X_train.dtypes == object].tolist()
    column_transformer = make_column_transformer(
        (OneHotEncoder(drop="first"), categorical_features),
        remainder="passthrough",
    )
    scaler = MinMaxScaler()


    def modeling(X_train, y_train, X_val, y_val, steps):
        pipeline = make_pipeline(*steps)
        pipeline.fit(X_train, y_train)
        y_val_pred_proba = pipeline.predict_proba(X_val)[:, 1]
        y_val_pred = pipeline.predict(X_val)
        #accuracy = accuracy_score(y_val,y_val_pred)
        metric = roc_auc_score(y_val, y_val_pred_proba)
        metric_f1 = f1_score(y_val,y_val_pred)

        if isinstance(pipeline._final_estimator, RandomizedSearchCV) or isinstance(pipeline._final_estimator, GridSearchCV):
            print(f"Best params: {pipeline._final_estimator.best_params_}")
        #print(f"Accuracy:{accuracy}")    
        print(f"AUC score: {metric}")
        print(f"f1 score:{metric_f1}")

        
        
        
        return pipeline
    
    rfclf = RandomForestClassifier(n_estimators=25,random_state=42)
    rfclf_pipeline = modeling(X_train, y_train, X_val, y_val, [column_transformer, scaler, rfclf])
    predicted_value = value_predict(X_train, y_train, X_val, y_val, [column_transformer, scaler, rfclf])
    rfclf_accuracy = accuracy_score(y_val, predicted_value) * 100

    request.session['rfclf_accuracy'] = rfclf_accuracy
    return redirect('ml_ui')

def ml_ui(request):
    context = {
        'knn_accuracy':request.session.get('knn_accuracy'),
        'logistic_accuracy':request.session.get('logistic_accuracy'),
        'xgb_accuracy':request.session.get('xgb_accuracy'),
        'rfclf_accuracy':request.session.get('rfclf_accuracy')
    }
    return render(request,'ML_ui(2).html',context)

def delete_sessions(request, session_keys):
    for key in session_keys:
        if key in request.session:
            del request.session[key]


def reset_accuracy(request):
    session_keys_to_delete = ['knn_accuracy','logistic_accuracy','xgb_accuracy','rfclf_accuracy']

    delete_sessions(request,session_keys_to_delete)
    return redirect('ml_ui')    

def testing(request):
    return render(request,'ML_ui(2).html')


def reset_knn(request):
    if 'knn_accuracy' in request.session:
        del request.session['knn_accuracy']
        return redirect('ml_ui')

def reset_logistic(request):
    if 'logistic_accuracy' in request.session:
        del request.session['logistic_accuracy']
        return redirect('ml_ui')

def reset_xgboost(request):
    if 'xgb_accuracy' in request.session:
        del request.session['xgb_accuracy']
        return redirect('ml_ui')

    
def reset_rdmf(request):
    if 'rfclf_accuracy' in request.session:
        del request.session['rfclf_accuracy']
        return redirect('ml_ui')
