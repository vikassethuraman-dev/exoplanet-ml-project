import pandas as pd

def main():
    stars = pd.read_csv("data/star_list.csv")
    print (stars)

if __name__ == "__main__":
    main()