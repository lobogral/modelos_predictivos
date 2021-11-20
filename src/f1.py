from sklearn.metrics import f1_score
y_true = [0, 1, 0, 0, 1, 1]
y_pred = [0, 0, 1, 0, 0, 1]
print(f1_score(y_true, y_pred))
