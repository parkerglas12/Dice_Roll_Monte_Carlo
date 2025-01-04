import numpy as np
from numpy.random import PCG64 as pcg
from numpy.random import Generator as gen
import matplotlib.pyplot as plt
import seaborn as sns

def get_user_input() -> int:
    while True:
        try:
            sims: int = int(input("How many dice rolls would you like to perform: "))
            if sims <= 1 or sims >= 100000001:
                raise ValueError("Enter an integer between 2 and 100,000,000.")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            return sims    

def get_results(rng, sims: int) -> dict[int, int]:
    results = rng.integers(1, 7, sims)
    unique, counts = np.unique(results, return_counts=True)
    return dict(zip(unique, counts))

def print_results(results: dict[int, int], sims: int) -> None:
    results_string: str = ", ".join(f"{outcome}: {count:,}" for outcome, count in sorted(results.items()))
    print(f"Results of the {sims:,} rolls -> {results_string}")

def create_bar_chart(results: dict[int, int], sims: int) -> None:
    sns.set()
    sns.set_style("white")
    plt.figure(figsize=(10, 6))

    outcomes: list[int] = sorted(results.keys())
    counts: list[int] = [results[outcome] for outcome in outcomes]

    bars = plt.bar(outcomes, counts, color="#0081cf")
    plt.xlabel("Outcome", fontsize=14, weight="bold", labelpad=10)
    plt.xticks(range(1, 7), fontsize=12, weight="bold")
    plt.ylabel("Count",  fontsize=14, weight="bold", labelpad=15)
    plt.title(f"Monte Carlo Simulation of {sims:,} Dice Rolls",  fontsize=14, weight="bold", pad=15)
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f"{yval:,}", ha="center", va="bottom", fontsize=12, weight="bold")

    sns.despine()
    plt.tight_layout(pad=1)
    plt.show()

def main() -> None:
    rng = gen(pcg()) # Random number generator
    sims: int = get_user_input()
    results: dict[int, int] = get_results(rng, sims)
    print_results(results , sims)
    create_bar_chart(results, sims)

if __name__ == "__main__":
    main()