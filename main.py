import numpy as np
import pandas as pd

def main():
    print("✅ Python is running")
    print("NumPy version:", np.__version__)
    print("Pandas version:", pd.__version__)
    print("-" * 40)

    # NumPy test
    arr = np.array([5, 10, 15, 20, 25])
    print("NumPy Array:", arr)
    print("Mean:", arr.mean())
    print("Squared:", arr ** 2)
    print("-" * 40)

    # Pandas test
    data = {
        "Name": ["Sayan", "Amit", "Riya", "Neha"],
        "Age": [20, 22, 21, 23],
        "Score": [95, 90, 78, 88]
    }

    df = pd.DataFrame(data)
    print("Pandas DataFrame:")
    print(df)
    print("-" * 40)

    print("Average Score:", df["Score"].mean())
    print("Top Scorers:")
    print(df[df["Score"] >= 85])

if __name__ == "__main__":
    main()
