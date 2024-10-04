from tempfile import NamedTemporaryFile
import pandas as pd
from pathlib import Path
import adtl
from InsightBoard.parsers import parse_adtl

SPECIFICATION_FILE = Path("adtl") / "source1.toml"
TABLE_NAME = "linelist"


def parse(df: pd.DataFrame) -> list[dict]:
    spec_file = Path(__file__).parent / SPECIFICATION_FILE
    return parse_adtl(df, spec_file, [TABLE_NAME])


def parse_full(df: pd.DataFrame) -> list[dict]:
    # ADTL parser
    parser = adtl.Parser(SPECIFICATION_FILE.resolve())

    # Write the dataframe to a temporary file and load it into ADTL
    with NamedTemporaryFile(suffix=".csv") as source_temp_file:
        df.to_csv(source_temp_file.name)
        parsed = parser.parse(source_temp_file.name)

    # Write the parsed data to a temporary file and load it into a pandas dataframe
    with NamedTemporaryFile(suffix=".parquet") as parsed_temp_file:
        parsed.write_parquet(TABLE_NAME, parsed_temp_file.name)
        df = pd.read_parquet(parsed_temp_file.name)

    # Drop ADTL-specific columns
    df.drop(columns=["adtl_valid", "adtl_error"], inplace=True)

    # Dataset specific cleaning:
    # - Convert Symptoms to a list
    df["Symptoms"] = df["Symptoms"].str.split(",")

    # Return a list of dictionaries with the table name and the dataframe
    return [
        {
            "database": TABLE_NAME,
            "data": df,
        },
    ]


def test_parse():
    print("Test: Parse")
    data_file = Path(__file__).parent.parent / "data" / "sample_data_source1.csv"
    orig_df = pd.read_csv(data_file)
    rtn = parse(orig_df)
    df = rtn[0]["data"]
    assert isinstance(df, pd.DataFrame)
    print("Test: Parse - Passed")


if __name__ == "__main__":
    test_parse()
