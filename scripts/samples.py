import pandas as pd
from itables import show
from IPython.display import HTML, display


def show_samples(consortium):
    df = pd.read_csv("Samples.csv")

    # Make the complete table searchable by Pagefind
    display(HTML(
        '<div data-pagefind-body style="display:none">'
        + df.to_html(index=False, escape=True)
        + '</div>'
    ))

    # Add row numbers
    df.insert(0, "#", range(1, len(df) + 1))

    # Link non-human reads
    df["non_human_reads"] = (
        '<a href="https://data.idies.jhu.edu/'
        'OcularMicrobiome/Consortium_data/'
        + consortium
        + '/'
        + df["sample_id"].astype(str)
        + '.unmapped.fastq.gz">'
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
            "bottomStart": ["pageLength"],
            "bottomEnd": ["paging"],
        },
        buttons=["colvis"],
        allow_html=True,
    )
