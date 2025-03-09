import streamlit as st
import pandas as pd
import pickle


st.title("Aplikasi Prediksi Penyakit Stroke")
st.subheader("Menggunakan Streamlit")
with st.expander('Data Training'):
  st.write('Berikut adalah data yang digunakan untuk membuat Model Training')
  df = pd.read_csv('stroke_dataset.csv')
  df = df.drop('id', axis=1)
  df
  
#  st.write('**Atribut**')
#  X_raw = df.drop('stroke', axis=1)
#  X_raw

#  st.write('**label**')
#  y_raw = df.stroke
#  y_raw
  
  
  
# sidebar:
# with st.sidebar:
#     st.header('Input Data Testing')
#     gender = st.radio('gender (Jenis Kelamin)',("Male", "Female"))
#     age = st.slider('Age (Usia)',0.0, 100.0, 60.0)
#     hypertension = st.radio('hypertension (Hipertensi/Darah Tinggi)',("Ya", "Tidak")) 
#     heart_disease = st.radio('heart_disease (Penyakit Jantung)',("Ya", "Tidak")) 
#     ever_married = st.radio('ever_married (Menikah/Tidak)',("Ya", "Tidak")) 
#     work_type = st.radio('work_type (Pekerjaan)',("Private","Self-employed","Govt_job"))
#     Residence_type = st.radio('Residence_type (Tipe tempat tinggal)',("Rural","Urban"))
#     avg_glucose_level = st.slider('avg_glucose_level (Rata-rata Gula Darah)', 55.0, 275.0, 100.0)
#     bmi = st.slider('bmi (Body Mass Index/Indeks Massa Tubuh)', 10.0, 100.0, 36.0)
#     smoking_status = st.radio('smoking_status (Status Merokok)',("formerly smoked","never smoked","smokes","unknown"))
   # left_column, right_column = st.columns(2)
   # left_column.button('Prediksi !!')

st.header('Input Data Testing')
gender = st.radio('Pilih Jenis Kelamin (Male=Pria ; Female=Wanita)',("Male", "Female"))
age = st.slider('Berapa Usia dalam Tahun',0.0, 100.0, 60.0)
hypertension = st.radio('Apakah anda mempunyai Hipertensi/Darah Tinggi ?',("Ya", "Tidak")) 
heart_disease = st.radio('Apakah anda mempunyai Penyakit Jantung ?',("Ya", "Tidak")) 
ever_married = st.radio('Apakah anda sudah/pernah Menikah ?',("Ya", "Tidak")) 
work_type = st.radio('Apakah Tipe Pekerjaan anda ?',("Private","Self-employed","Govt_job"))
Residence_type = st.radio('Apakah Tipe tempat tinggal anda ? (Rural : Desa ; Urban : Kota)',("Rural","Urban"))
avg_glucose_level = st.slider('Berapa Rata-rata Gula Darah anda ?', 55.0, 275.0, 100.0)
bmi = st.slider('Berapa Indeks Massa Tubuh anda ?', 10.0, 100.0, 36.0)
smoking_status = st.radio('Apakah Status Merokok anda ? (formerly : Pernah ; never : Tidak Pernah ; smoked : Merokok; unknown:Tidak Tahu)',("formerly smoked","never smoked","smokes","unknown"))



#convert
if gender=="Male":
    gender=1
else:
    gender=0

if hypertension=="Ya":
    hypertension=1
else:
    hypertension=0
        
if heart_disease=="Ya":
    heart_disease=1
else:
    heart_disease=0
    
if ever_married=="Ya":
    ever_married=1
else:
    ever_married=0

if work_type=="Private":
    work_type=2
elif work_type=="Self-employed":
    work_type=3
else:
    work_type=1

if Residence_type=="Rural":
    Residence_type=0
else:
    Residence_type=1
    
if smoking_status=="formerly smoked":
    smoking_status=1
elif smoking_status=="never smoked":
    smoking_status=2
elif smoking_status=="smokes":
    smoking_status=3
else:
    smoking_status=0



data_testing={
      'gender':[gender],
      'age':[age],
      'hypertension':[hypertension],
      'heart_disease':[heart_disease],
      'ever_married':[ever_married],
      'work_type':[work_type],
      'Residence_type':[Residence_type],
      'avg_glucose_level':[avg_glucose_level],
      'bmi':[bmi],
      'smoking_status':[smoking_status]
      }

input_data=pd.DataFrame(data_testing);
print(input_data)
coba=input_data.to_numpy()
print(coba)
model=pickle.load(open('rfwp.pkl','rb'))

if st.button('Prediksi'):
    prediksi=model.predict(input_data)
    if prediksi==0:
        st.write("Prediksi : Tidak Menderita Penyakit Stroke")
    else:
        st.write("Prediksi : Menderita Penyakit Stroke")
#'Starting a long computation...'

# Add a placeholder
#latest_iteration = st.empty()
#bar = st.progress(0)

#for i in range(100):
  # Update the progress bar with each iteration.
  #latest_iteration.text(f'Iteration {i+1}')
  #bar.progress(i + 1)
  #time.sleep(0.1)
#'...and now we\'re done!'