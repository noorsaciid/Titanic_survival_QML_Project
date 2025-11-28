# Raw Data Directory

## Files

### `toy_titanic.csv`

**Source:** Schuld & Petruccione (2018), *Supervised Learning with Quantum Computers*, Chapter 1.2

This is the **exact 3-passenger toy dataset** from the book used to demonstrate the quantum squared-distance classifier.

#### Format:
```csv
passenger,ticket_price,cabin_number,survival
passenger1,8500,910,1
passenger2,1200,2105,0
passenger3,7800,1121,
```

#### Columns:
- **passenger**: Passenger identifier (passenger1, passenger2, passenger3)
- **ticket_price**: Ticket price in dollars (integer)
- **cabin_number**: Cabin number (integer)
- **survival**: Survival outcome
  - `1` = Survived
  - `0` = Died
  - Empty = Unknown (to be predicted)

#### Dataset Details:

| Passenger | Ticket Price | Cabin Number | Survival | Role |
|-----------|-------------|--------------|----------|------|
| passenger1 | $8,500 | 910 | 1 (Survived) | Training |
| passenger2 | $1,200 | 2,105 | 0 (Died) | Training |
| passenger3 | $7,800 | 1,121 | ? (Unknown) | Test |

#### Book Reference:

This toy dataset is deliberately minimal to demonstrate the quantum algorithm without distracting engineering details. The book notes:

> "We use a tiny illustrative subset inspired by the Titanic dataset: two labeled training examples and one unlabeled test example."

The features (ticket price and cabin number) are rescaled using:
- **Ticket price range:** [0, 10,000]
- **Cabin number range:** [0, 2,500]

#### Validation:

After preprocessing (STEP 0: min-max scaling, STEP A: L2 normalization), these values should produce:

**Normalized vectors:**
- Passenger 1: [0.921, 0.390]
- Passenger 2: [0.141, 0.990]
- Passenger 3: [0.866, 0.500]

**Classification (book's expected output):**
- p(survive | passenger3) ≈ 0.552
- p(die | passenger3) ≈ 0.448
- **Prediction:** SURVIVED

#### Usage:

```python
import pandas as pd

# Load data
df = pd.read_csv('Data/Raw/toy_titanic.csv')

# Extract passengers (book's naming: P1, P2, P3)
P1_raw = df.iloc[0][['ticket_price', 'cabin_number']].values  # Passenger 1 (survived)
P1_label = int(df.iloc[0]['survival'])

P2_raw = df.iloc[1][['ticket_price', 'cabin_number']].values  # Passenger 2 (died)
P2_label = int(df.iloc[1]['survival'])

P3_raw = df.iloc[2][['ticket_price', 'cabin_number']].values  # Passenger 3 (unknown)
```

#### Notes:

- This is NOT the full Titanic dataset
- Values are exactly as specified in the example toy dataset in the book
- Do not modify this file (it's the ground truth)
- For processed data, see `Data/Processed/`

---

*Last updated: November 27, 2025 by Saciid*
