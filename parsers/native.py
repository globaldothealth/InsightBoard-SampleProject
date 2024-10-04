import pandas as pd


def parse(linelist: pd.DataFrame) -> pd.DataFrame:
    return [
        {
            "database": "linelist",
            "data": linelist,
        }
    ]
