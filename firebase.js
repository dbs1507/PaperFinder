// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getDatabase, ref, push } from "firebase/database";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyClG_cwwy7DAbp4zfoW9SFr8wQ5oldrM4g",
  authDomain: "papersfinder.firebaseapp.com",
  databaseURL: "https://papersfinder-default-rtdb.firebaseio.com",
  projectId: "papersfinder",
  storageBucket: "papersfinder.appspot.com",
  messagingSenderId: "274191884289",
  appId: "1:274191884289:web:7cf8a7a1ae4f2749d76000",
  measurementId: "G-0B5EJPVL0S",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

// Referência ao banco de dados
const database = getDatabase();
const searchHistoryRef = ref(database, "search_history");

// Função para inserir a palavra-chave no banco de dados
function insertKeyword(keyword) {
  push(searchHistoryRef, {
    keyword: keyword,
    timestamp: firebase.database.ServerValue.TIMESTAMP,
  });
}
window.insertKeyword = insertKeyword;
