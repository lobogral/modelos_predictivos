from sklearn.metrics import accuracy_score
y_pred = [0, 1, 2, 3]
y_true = [0, 1, 2, 3]

print(accuracy_score(y_true, y_pred))
print(accuracy_score(y_true, y_pred, normalize=False))
