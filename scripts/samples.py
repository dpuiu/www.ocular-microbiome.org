import pandas as pd
from itables import show
from IPython.display import HTML, display

def show_samples(center, format="fastq", biosample_type=None, biosample_site=None):
    df = pd.read_csv("Samples.csv")

    # Filter
    if biosample_type is not None:
        df = df[df["biosample_type"].isin(biosample_type)].reset_index(drop=True)

    if biosample_site is not None:
        df = df[df["biosample_site"].isin(biosample_site)].reset_index(drop=True)

    # Make the complete table searchable by Pagefind
    display(HTML(
        '<div data-pagefind-body style="display:none">'
        + df.to_html(index=False, escape=True)
        + '</div>'
    ))

    # Add row numbers
    df.insert(0, "#", range(1, len(df) + 1))

    #convert to "," number
    #df["non_human_reads"] = df["non_human_reads"].map(lambda x: f"{x:,}" if pd.notna(x) else x)
    df = df.map(lambda x: f"{x:,}" if isinstance(x, int) else x)

    # Link non-human reads
    df["non_human_reads"] = (
        '<a href="https://data.idies.jhu.edu/'
        'OcularMicrobiome/Consortium_data/'
        + center
        + '/'
        + df["sample_name"].astype(str)
        + '.unmapped.' + format + '.gz">'
        + df["non_human_reads"].astype(str)
        + "</a>"
    )

    show(
    df,
    paging=True,
    pageLength=10,
    scrollX=True,
    classes="display compact",
    layout={
        "topStart": ["buttons"],
        "topEnd": ["search"],
        "bottomStart": ["pageLength","paging"],
        "bottomEnd": [],
    },
    buttons=["copy", "csv", "excel", "colvis"],
    columnDefs=[{"targets": list(range(11, len(df.columns))), "visible": False} ],
    allow_html=True,
    maxBytes=0,
    )
