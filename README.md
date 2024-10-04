# InsightBoard-SampleProject

Sample project for use with [InsightBoard](https://github.com/globaldothealth/InsightBoard) ([documentation](https://insightboard.readthedocs.io/en/latest/)).

The project contains a single target schema, sample datasets (one in the target format, the other that requires parsing), parsers to ingest the data into the target schema, and a sample report.
```bash
├─ data/
│  ├─ sample_data_native.csv     # Sample data in the target format
│  └─ sample_data_source1.csv    # Sample data in another (non-target) format
├─ parsers/
│  ├─ native.py                  # Basic parser to read data in the target format
│  ├─ adtl-source1.py            # Sample parser using ADTL to ingest source1 data
│  └─ adtl/
│     └─ source1.toml            # Configuration file for the source1 parser
├─ reports/
│  └─ summary.py                 # Sample report to generate a summary of the data
└─ schemas/
   └─ linelist.schema.json       # JSON schema for the target data format
```

To load the project, install [InsightBoard](https://github.com/globaldothealth/InsightBoard) following the instructions on that repository. Then, clone this repository into the `InsightBoard/projects` (which will appear in your home folder by default).

For more information on how to use InsightBoard, see the [InsightBoard documentation](https://insightboard.readthedocs.io/en/latest/).
