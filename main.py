import yfinance as yf
import pandas as pd  
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


btc_data = yf.download('BTC-USD',start="2020-01-01",end=pd.Timestamp.today().strftime('%Y-%m-%d'))

btc_data = btc_data[['Close']]

btc_data.loc[:, 'Future_Price']= btc_data['Close'].shift(-1)
btc_data.dropna(inplace=True)

X = btc_data[['Close']]
y = btc_data['Future_Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 42)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print(f'Mean Squared Error: {mse:.2f}')
print(f'R² Score: {r2:.2f}')

preco_atual = pd.DataFrame([[btc_data.iloc[-1]['Close']]], columns=["Close"])  
previsao_futura = model.predict(preco_atual)

print(f'Preço previsto do Bitcoin para o próximo dia: {previsao_futura[0]:.2f}$')

plt.figure(figsize=(10,6))
plt.plot(btc_data.index, btc_data["Close"],label="Preço de Fechamento Histórico",color="blue")
plt.scatter(pd.Timestamp.today(),previsao_futura[0],color="red",label="Previsão do Proximo dia")

plt.title("Previsão do preço do Bitcoin")
plt.xlabel("Data")
plt.ylabel("Preço em USD")
plt.legend()

plt.show()