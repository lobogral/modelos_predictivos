from sklearn.metrics import recall_score

# Ejemplo 1
y_true = [0, 1, 1, 0, 1, 0]
y_pred = [0, 1, 1, 0, 0, 1]
print(recall_score(y_true, y_pred))  # => resultado 0.66

# Ejemplo 2
y_true = [0, 1, 1, 0, 1, 0]
y_pred = [1, 1, 1, 1, 0, 1]
print(recall_score(y_true, y_pred))  # => 0.66

# Ejemplo 3
y_true = [0, 1, 1, 0, 1, 0]
y_pred = [0, 0, 1, 0, 0, 1]
print(recall_score(y_true, y_pred))  # => resultado 0.33
