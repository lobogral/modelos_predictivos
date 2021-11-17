# Matriz de Confusión
from sklearn.metrics import confusion_matrix
y_true = ["gato", "lobo", "gato", "gato", "lobo", "perro"]  # i => Renglones
y_pred = ["lobo", "lobo", "gato", "gato", "lobo", "gato"]  # j => Columnas
print(confusion_matrix(y_true, y_pred, labels=["lobo", "perro", "gato"]))
