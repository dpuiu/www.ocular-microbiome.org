import pandas as pd
from itables import show
from IPython.display import HTML, display
from html import escape

from functools import cache

@cache
def show_individuals(center):
    df = pd.read_csv("Individuals.csv")

    # Make the complete table searchable by Pagefind
    display(HTML(
        '<div data-pagefind-body style="display:none">'
        + df.to_html(index=False, escape=True)
        + '</div>'
    ))

    # Add row numbers
    df.insert(0, "#", range(1, len(df) + 1))

    # convert ids to hrefs
    df["individual_id"] = df["individual_id"].apply(
       lambda x: (
           f'<a id="{escape(str(x), quote=True)}">'
           f'{escape(str(x))}</a>'
       )
    )

    show(
    df,
    #paging=True,
    #pageLength=10,
    paging=False,
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