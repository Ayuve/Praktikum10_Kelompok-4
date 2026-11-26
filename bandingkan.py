import pandas as pd

A = pd.read_csv("hasil_dengan_aug/hasil_5fold.csv", index_col=0)
B = pd.read_csv("hasil_tanpa_aug/hasil_5fold.csv", index_col=0)

kolom = ["accuracy", "precision", "recall", "f1", "roc_auc"]
nama = {"accuracy": "Accuracy", "precision": "Precision", "recall": "Recall",
        "f1": "F1-score", "roc_auc": "ROC-AUC"}

rata = pd.DataFrame({
    "Dengan augmentasi": A.loc["rata-rata", kolom],
    "Tanpa augmentasi": B.loc["rata-rata", kolom],
})
rata["Selisih (dengan - tanpa)"] = rata["Dengan augmentasi"] - rata["Tanpa augmentasi"]
rata.index = [nama[i] for i in rata.index]
rata.round(3).to_csv("perbandingan_aug.csv")

print(rata.round(3))
print("\n--- Tabel Markdown untuk README.md ---\n")
print("| Metrik | Dengan augmentasi | Tanpa augmentasi | Selisih |")
print("|---|---|---|---|")
for m, r in rata.iterrows():
    print(f"| {m} | {r.iloc[0]:.3f} | {r.iloc[1]:.3f} | {r.iloc[2]:+.3f} |")

print("\nJumlah fold yang lebih baik dengan augmentasi (per metrik):")
for c in kolom:
    n = int((A.loc[[str(k) for k in range(1, 6)], c].values > B.loc[[str(k) for k in range(1, 6)], c].values).sum())
    print(f"  {nama[c]:<10}: {n} dari 5 fold")