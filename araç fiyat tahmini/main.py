import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score

# Veriyi yükleme
data = pd.read_csv('data.csv')


# Kategorik sütunları seçip sayısallaştırma (One-hot encoding)
categorical_columns = data.select_dtypes(include=['object']).columns
data_encoded = pd.get_dummies(data, columns=categorical_columns, drop_first=True)

# Hedef değişken ve bağımsız değişkenlerin ayrılması
X = data_encoded.drop(columns=['price', 'car_ID'])  # 'price' hedef değişken, 'car_ID' benzersiz bir tanımlayıcı
y = data_encoded['price']

# Eğitim ve test setlerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ridge regresyonu modeli
ridge_model = Ridge(alpha=1.0)  # Ceza parametresi
ridge_model.fit(X_train, y_train)

# Model tahminleri ve değerlendirme
y_pred = ridge_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R^2 Score:", r2)
