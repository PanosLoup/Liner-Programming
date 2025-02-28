from scipy.optimize import linprog

# Συντελεστές της συνάρτησης στόχου (κέρδος ανά μονάδα)
c = [-18, -15, -22, -10]  # Αρνητικές τιμές για τη μεγιστοποίηση

# Συντελεστές των περιορισμών (χρόνος παραγωγής σε λεπτά)
A = [
    [14, 12, 16, 9],    # Χρόνος στη μηχανή Χ
    [21, 28, 36, 26],   # Χρόνος στη μηχανή Υ
    [17, 15, 24, 14],   # Χρόνος στη μηχανή Ζ
    [0.18, 0.12, 0.55, 0.06],  # Χωρητικότητα αποθήκευσης σε τ.μ.
    [0, 0, -1, 2],      # Σχέση παραγωγής Γ και Δ (2xD - xC <= 0.05 * xC)
    [0, 0, 1, -2]       # Σχέση παραγωγής Γ και Δ (xC <= 2xD + 0.05 * xC)
]

# Δεξιές πλευρές των περιορισμών
b = [
    (40 * 60 * (1 - 0.07)),  # Διαθέσιμος χρόνος στη μηχανή Χ
    (40 * 60 * (1 - 0.03)),  # Διαθέσιμος χρόνος στη μηχανή Υ
    (40 * 60 * (1 - 0.04)),  # Διαθέσιμος χρόνος στη μηχανή Ζ
    45,                      # Χωρητικότητα αποθήκευσης
    0,                       # Σχέση παραγωγής (2xD - xC <= 0.05 * xC)
    0                        # Σχέση παραγωγής (xC <= 2xD + 0.05 * xC)
]

# Περιορισμοί των μη αρνητικών τιμών
x_bounds = (0, None)

# Επίλυση του γραμμικού προγράμματος
res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds]*4, method='highs')

# Εκτύπωση των αποτελεσμάτων
print("Αριθμός μονάδων που πρέπει να παραχθούν από κάθε προϊόν:")
print(f"Προϊόν Α: {res.x[0]:.2f}")
print(f"Προϊόν Β: {res.x[1]:.2f}")
print(f"Προϊόν Γ: {res.x[2]:.2f}")
print(f"Προϊόν Δ: {res.x[3]:.2f}")
print(f"Μέγιστο κέρδος: {-res.fun:.2f} ευρώ")
.github/workflows/main.yml
