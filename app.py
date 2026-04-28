import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

st.set_page_config(page_title="VitalSign", page_icon="", layout="centered")

if "patients" not in st.session_state:
    st.session_state.patients = []

if "page" not in st.session_state:
    st.session_state.page = "accueil"

if st.session_state.page == "accueil":

    st.markdown(
        """
        <div style="background: linear-gradient(to right, #4A90D9, #5FBFB0);padding:25px;border-radius:20px;text-align:center;margin-bottom:25px">
            <h1 style="color:white;font-size:42px;font-weight:bold">BIENVENUE DANS VITAL SIGN</h1>
            <p style="color:white;font-size:18px">Votre allie sante au quotidien !</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            """
            <div style="background-color:#E8F4FD;padding:20px;border-radius:15px;text-align:center;height:200px;border: 2px solid #4A90D9">
                <p style="font-size:45px;margin:0">❤️</p>
                <p style="color:#4A90D9;font-size:18px;font-weight:bold">SANTE</p>
                <p style="color:#333333;font-size:14px">Surveillez votre coeur</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            """
            <div style="background-color:#E8F4FD;padding:20px;border-radius:15px;text-align:center;height:200px;border: 2px solid #5FBFB0">
                <p style="font-size:45px;margin:0">🥗</p>
                <p style="color:#5FBFB0;font-size:18px;font-weight:bold">NUTRITION</p>
                <p style="color:#333333;font-size:14px">Mangez equilibre</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown(
            """
            <div style="background-color:#E8F4FD;padding:20px;border-radius:15px;text-align:center;height:200px;border: 2px solid #4A90D9">
                <p style="font-size:45px;margin:0">🚶</p>
                <p style="color:#4A90D9;font-size:18px;font-weight:bold">ACTIVITE</p>
                <p style="color:#333333;font-size:14px">Bougez chaque jour</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")
    
    st.markdown(
        """
        <div style="background-color:#E8F4FD;padding:20px;border-radius:15px;text-align:center;margin-bottom:20px">
            <p style="color:#4A90D9;font-size:20px;font-weight:bold">POURQUOI VITAL SIGN ?</p>
            <p style="color:#333333;font-size:16px">
            Surveillez votre sante cardiovasculaire facilement depuis chez vous
            </p>
            <p style="color:#333333;font-size:16px">
            Obtenez des conseils personnalises en fonction de vos resultats
            </p>
            <p style="color:#333333;font-size:16px">
            Simple - Rapide - Gratuit
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div style="background-color:#E8F4FD;padding:20px;border-radius:15px;text-align:center;margin-bottom:20px">
            <p style="color:#5FBFB0;font-size:20px;font-weight:bold">CE QUE NOUS ANALYSONS</p>
            <p style="color:#333333;font-size:16px">
            Tension arterielle - Glycemie a jeun - Glycemie apres repas
            </p>
            <p style="color:#4A90D9;font-size:16px;font-weight:bold">
            Regression - Clustering - PCA - Classification
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            """
            <style>
            div.stButton > button {
                background: linear-gradient(to right, #4A90D9, #5FBFB0);
                color: white;
                font-size: 22px;
                font-weight: bold;
                padding: 18px 40px;
                border-radius: 50px;
                border: none;
                width: 100%;
            }
            div.stButton > button:hover {
                background: linear-gradient(to right, #5FBFB0, #4A90D9);
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        if st.button("COMMENCER MON BILAN"):
            st.session_state.page = "formulaire"
            st.rerun()

    st.write("")
    st.write("")
    
    st.markdown(
        """
        <div style="background-color:#4A90D9;padding:15px;border-radius:10px;text-align:center">
            <p style="color:white;font-size:14px;margin:0">Application realisee dans le cadre du TP INF 232</p>
        </div>
        """,
        unsafe_allow_html=True
    )

elif st.session_state.page == "formulaire":

    st.markdown(
        """
        <div style="background: linear-gradient(to right, #4A90D9, #5FBFB0);padding:20px;border-radius:15px;text-align:center;margin-bottom:25px">
            <h2 style="color:white;font-weight:bold">MON BILAN DE SANTE</h2>
            <p style="color:white;font-size:16px">Ajoutez plusieurs patients puis lancez l'analyse</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="background-color:#E8F4FD;padding:15px;border-radius:10px;margin-bottom:20px;border-left: 5px solid #4A90D9">
            <p style="color:#4A90D9;font-size:18px;font-weight:bold;margin:0">AJOUTER UN PATIENT</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        nom = st.text_input("Nom du patient", key="nom_input")
    with col2:
        age = st.number_input("Age", min_value=0, max_value=120, value=50, key="age_input")
    with col3:
        poids = st.number_input("Poids (kg)", min_value=30, max_value=200, value=70, key="poids_input")

    col4, col5, col6 = st.columns(3)
    with col4:
        tension = st.number_input("Tension (mmHg)", min_value=80, max_value=250, value=130, key="tension_input")
    with col5:
        glycemie_jeun = st.number_input("Glycemie a jeun (g/L)", min_value=0.0, max_value=5.0, value=1.0, key="jeun_input")
    with col6:
        glycemie_repas = st.number_input("Glycemie apres repas (g/L)", min_value=0.0, max_value=5.0, value=1.4, key="repas_input")

    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("AJOUTER CE PATIENT"):
            if nom != "":
                st.session_state.patients.append({
                    "Nom": nom,
                    "Age": age,
                    "Poids": poids,
                    "Tension": tension,
                    "Glycemie_jeun": glycemie_jeun,
                    "Glycemie_repas": glycemie_repas
                })
                st.success(nom + " ajoute avec succes !")
            else:
                st.warning("Veuillez entrer un nom.")

    if len(st.session_state.patients) > 0:
        st.write("")
        st.markdown(
            """
            <div style="background-color:#E8F4FD;padding:15px;border-radius:10px;margin-bottom:20px">
                <p style="color:#4A90D9;font-size:18px;font-weight:bold;margin:0">PATIENTS ENREGISTRES : """ + str(len(st.session_state.patients)) + """</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        df_temp = pd.DataFrame(st.session_state.patients)
        st.dataframe(df_temp)

    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            """
            <style>
            div.stButton > button {
                background: linear-gradient(to right, #4A90D9, #5FBFB0);
                color: white;
                font-size: 18px;
                font-weight: bold;
                padding: 12px 30px;
                border-radius: 30px;
                border: none;
                width: 100%;
            }
            div.stButton > button:hover {
                background: linear-gradient(to right, #5FBFB0, #4A90D9);
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        if st.button("LANCER LES ANALYSES"):
            if len(st.session_state.patients) >= 2:
                st.session_state.page = "analyses"
                st.rerun()
            else:
                st.warning("Ajoutez au moins 2 patients pour lancer les analyses.")

elif st.session_state.page == "analyses":

    st.markdown(
        """
        <div style="background: linear-gradient(to right, #4A90D9, #5FBFB0);padding:20px;border-radius:15px;text-align:center;margin-bottom:25px">
            <h2 style="color:white;font-weight:bold">RESULTATS DES ANALYSES</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    df = pd.DataFrame(st.session_state.patients)
    X = df[["Age", "Poids", "Glycemie_jeun", "Glycemie_repas"]]
    y = df["Tension"]

    st.write("## 1. Analyse descriptive")
    st.write("### Tableau des donnees")
    st.dataframe(df)
    st.write("### Statistiques descriptives")
    st.dataframe(df.describe())

    st.write("## 2. Regression lineaire : Age vs Tension")
    
    model = LinearRegression()
    X_age = df[["Age"]]
    model.fit(X_age, y)
    r2 = model.score(X_age, y)
    
    st.write("Score R2 = ", round(r2, 4))
    st.write("Equation : Tension = ", round(model.intercept_, 2), " + ", round(model.coef_[0], 2), " x Age")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(df["Age"], df["Tension"], color="#4A90D9", s=80)
    ax.plot(df["Age"], model.predict(X_age), color="#5FBFB0", linewidth=2)
    ax.set_xlabel("Age")
    ax.set_ylabel("Tension (mmHg)")
    ax.set_title("Regression : Age vs Tension")
    ax.set_facecolor("#F5F5F5")
    fig.patch.set_facecolor("#F5F5F5")
    st.pyplot(fig)

    st.write("## 3. Regression lineaire multiple")
    
    model_multi = LinearRegression()
    model_multi.fit(X, y)
    r2_multi = model_multi.score(X, y)
    
    st.write("Score R2 = ", round(r2_multi, 4))
    st.write("Coefficients :")
    for i, col in enumerate(X.columns):
        st.write("- ", col, " : ", round(model_multi.coef_[i], 4))
    st.write("Constante : ", round(model_multi.intercept_, 2))

    st.write("## 4. Clustering K-Means")
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    df["Cluster"] = kmeans.fit_predict(X_scaled)
    
    st.write("Patients repartis en 2 groupes :")
    st.dataframe(df[["Nom", "Age", "Poids", "Tension", "Cluster"]])
    
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    colors = ["#4A90D9", "#5FBFB0"]
    for cluster in [0, 1]:
        data = df[df["Cluster"] == cluster]
        ax2.scatter(data["Age"], data["Tension"], color=colors[cluster], s=80, label="Groupe " + str(cluster+1))
    ax2.set_xlabel("Age")
    ax2.set_ylabel("Tension (mmHg)")
    ax2.set_title("Groupes de patients (K-Means)")
    ax2.legend()
    ax2.set_facecolor("#F5F5F5")
    fig2.patch.set_facecolor("#F5F5F5")
    st.pyplot(fig2)

    st.write("## 5. PCA - Analyse en Composantes Principales")
    
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    
    st.write("Variance expliquee par chaque composante :")
    st.write("- Composante 1 : ", round(pca.explained_variance_ratio_[0]*100, 2), "%")
    st.write("- Composante 2 : ", round(pca.explained_variance_ratio_[1]*100, 2), "%")
    
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    ax3.scatter(X_pca[:, 0], X_pca[:, 1], color="#4A90D9", s=80)
    ax3.set_xlabel("Composante 1")
    ax3.set_ylabel("Composante 2")
    ax3.set_title("Projection PCA des patients")
    ax3.set_facecolor("#F5F5F5")
    fig3.patch.set_facecolor("#F5F5F5")
    st.pyplot(fig3)

    st.write("## 6. Classification K-NN")
    
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
    
    knn = KNeighborsClassifier(n_neighbors=2)
    
    y_class = []
    for val in y_train:
        if val < 120:
            y_class.append(0)
        elif val < 140:
            y_class.append(1)
        else:
            y_class.append(2)
    
    y_class_test = []
    for val in y_test:
        if val < 120:
            y_class_test.append(0)
        elif val < 140:
            y_class_test.append(1)
        else:
            y_class_test.append(2)
    
    knn.fit(X_train, y_class)
    score = knn.score(X_test, y_class_test)
    
    st.write("Score de classification K-NN = ", round(score*100, 2), "%")
    st.write("Le modele predit le niveau de tension (Normal / Eleve / Tres eleve)")

    st.write("## 7. Conseils par patient")
    
    for index, row in df.iterrows():
        st.write("### Patient : ", row["Nom"])
        st.write("Tension : ", row["Tension"], "mmHg")
        
        if row["Tension"] < 90:
            st.warning("Tension basse - Buvez plus d'eau")
        elif row["Tension"] < 120:
            st.success("Tension normale - Continuez !")
        elif row["Tension"] < 140:
            st.warning("Tension un peu elevee - Reduisez le sel")
        else:
            st.error("Tension elevee - Consultez un medecin")
        
        st.write("Glycemie a jeun : ", row["Glycemie_jeun"], "g/L")
        if row["Glycemie_jeun"] < 1.1:
            st.success("Glycemie a jeun normale")
        else:
            st.warning("Glycemie a jeun elevee - Evitez les sucres rapides")
        
        st.write("---")

    st.write("")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("REFAIRE UN BILAN"):
            st.session_state.patients = []
            st.session_state.page = "formulaire"
            st.rerun() 