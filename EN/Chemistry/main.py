import numpy as np
import torch
import torch.nn as nn
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt

# [EN] Dummy molecular feature matrix representing 5 chemical compounds with 10 features each
# [PL] Sztuczna macierz cech cząsteczkowych reprezentujące 5 związków chemicznych po 10 cech każdy
molecular_features = np.random.rand(5, 10)

# [EN] Calculating pairwise Euclidean distance between molecular descriptors using SciPy
# [PL] Obliczanie odległości euklidesowej między deskryptorami cząsteczkowymi za pomocą SciPy
distance_matrix = squareform(pdist(molecular_features, metric='euclidean'))
print("Molecular Distance Matrix (SciPy):\n", distance_matrix)

# [EN] Converting features array to PyTorch Tensor for Deep Learning modeling
# [PL] Konwertowanie tablicy cech do PyTorch Tensor na potrzebowy modelowania głębokiego uczenia
X_tensor = torch.tensor(molecular_features, dtype=torch.float32)

# [EN] Defining mock target property values (e.g., aqueous solubility) for training
# [PL] Definiowanie przykładowych docelowych wartości właściwości np. rozpuszczalności w wodzie do treningu
y_tensor = torch.tensor([[2.5], [1.1], [3.8], [0.4], [1.9]], dtype=torch.float32)

# [EN] Defining a simple PyTorch Neutral Network for molecular property prediction
# [PL] Definiowanie  prostej sieci neuronowej PyTorch do predykcji właściwości chemicznych
class MolecularPropertyPredictor(nn.Module):
    def __init__(self, input_dim):
        super(MolecularPropertyPredictor, self).__init__()
        # [EN] Fully connected layer mapping input features to hidden layer
        # [PL] (Warstwa w pełni połączona odwzorowująca cechy wejściowe na warstwę ukrytą)
        self.fc1 = nn.Linear(input_dim, 16)
        self.relu = nn.ReLU()
        # [EN] Output layer predicting a continuous chemical property (e.g., solubility)
        # [PL] (Warstwa wyjściowa przewidująca ciągłą właściwość chemiczną np. rozpuszczalność)
        self.fc2 = nn.Linear(16, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# [EN] Initializing model with feature dimension equal to 10
# [PL] Inicjalizowanie modelu z rozmiarem cech równym 10
model = MolecularPropertyPredictor(input_dim=10)

# [EN] Defining loss function and optimizer for training the neutral network
# [PL] Definiowanie funkcji starty i optymalizator do treningu sieci neuronowej
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# [EN] Training loop to update model weights based on chemical data
# [PL] Pętla treningowa aktualizująca wagi modelu na podstawie danych chemicznych
print("\n--- Training Neural Network Model ---")
for epoch in range(101):
    # [EN] Forward pass: computing predictions from features
    # [PL] Przebieg w przód: obliczanie predykcji z cech
    predictions = model(X_tensor)

    # [EN] Calculating the Mean Squared Error loss between predicitons and true targets
    # [PL] Obliczanie błąd średniokwadratowy między predykcjami a prawdziwymi celami
    loss = criterion(predictions, y_tensor)

    # [EN] Backward pass and optimization step to update weights
    # [PL] Przebieg wsteczny i krok optymalizacji w celu aktualizacji wag
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
# [EN] Setting model to evaluation mode and extracting predictions for plotting
# [PL] Ustawianie modelu w tryb ewaluacji i wyciąganie przewidywań do wykresu
model.eval()
with torch.no_grad():
    final_preds = model(X_tensor).numpy()
true_values = y_tensor.numpy()

# [EN] Plotting predictions vs true values using Matplotlib
# [PL] Wizualizacja przewidywań względem prawdziwych wartości za pomocą Matplotlib
plt.figure(figsize=(6, 6))
plt.scatter(true_values, final_preds, color='blue', label='Compounds ([PL] Związki chemiczne)')

# [EN] Plot reference diagonal line (ideal predictions where Predicted = True)
# [PL] Wizualizacja linii przekątnej odniesienia (idealne przewidywania, gdzie Przewidywane = Prawdziwe)
min_val = min(true_values.min(), final_preds.min())
max_val = max(true_values.max(), final_preds.max())
plt.plot([min_val, max_val], [min_val, max_val], 'k--', label='Ideal Fit ([PL] Idealne dopasowanie)')

plt.xlabel('True Solubility ([PL] Prawdziwa rozpuszczalność)')
plt.ylabel('Predicted Solubility ([PL] Przewidywana rozpuszczalność)')
plt.title('PyTorch Molecular Property Prediction ([PL] Predykcja właściwości cząsteczek)')
plt.legend()
plt.grid(True)
plt.show()
