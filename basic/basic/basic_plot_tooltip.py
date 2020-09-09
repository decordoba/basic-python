import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mpld3
from mpld3 import plugins


def plot_df_with_tooltip(df, y_column, x_column=None, tooltip_columns=None, tooltip_title_column=None,
                         tooltip_style=None, title=None, style="o", color="", show=True):
    """Plot scatterplot with tooltips.

    Requires style with markers to show tooltips (for example, style "-" will not work, but ".-" will).

    :param df: pandas data frame to plot
    :param y_column: column to plot in y axis
    :param x_column: column to plot in x axis, if None will use Row Number
    :param tooltip_columns: list of columns to show in tooltip, if None all will be shown
    :param tooltip_title_column: Column to put on the title, if None don't add a title
    :param tooltip_style: css style for table, as well as any other css attributes desired in the graph
    :param style: plot style (i.e. [o], [.], [.-], [O])
    :param color: plot color (i.e. r, g, b, y c, m, k, w)

    @use plot_df_with_tooltip(df, "y", "x", title="Test graph", tooltip_columns=["x", "y", "z"], tooltip_title_column=None, style=".-")
    """
    if tooltip_style is None:
        tooltip_style = """
table { border-collapse: collapse; border: 1px solid #bbb;}
th { border-bottom: 1px solid #bbb; }
td { border-bottom: 1px solid #bbb; }
table, th, td { font-family: sans-serif; padding: 4; opacity: 0.9; background-color: #fff; }
"""
    tooltip_labels = None
    if tooltip_columns is not None:
        tooltip_labels = []
        for i in range(len(df)):
            label = df.iloc[[i], :].T
            if tooltip_title_column is None:
                label.columns = ["Row: {}".format(i)]
            else:
                label.columns = ["{}: {}".format(tooltip_title_column, label.loc[tooltip_title_column].values[0])]
            if tooltip_columns is not None:
                label = label.loc[tooltip_columns]
            tooltip_labels.append(str(label.to_html(header=(tooltip_title_column is not None))))

    if x_column is None:
        df["Row"] = np.arange(len(df))
        x_column = "Row"

    fig, ax = plt.subplots()
    full_style = (color if color is not None else "") + (style if style is not None else "")
    points = plt.plot(df[x_column], df[y_column], full_style)

    plt.xlabel(x_column)
    plt.ylabel(y_column)
    if title is not None:
        plt.title(title, size=20)

    if tooltip_labels is not None:
        points = plt.gca().lines
        fig = plt.gcf()
        tooltip = plugins.PointHTMLTooltip(points[0], tooltip_labels, voffset=10, hoffset=10, css=tooltip_style)
        plugins.connect(fig, tooltip)

    if show:
        mpld3.show()


def html_table_from_lists(list_left=None, list_right=None, left_attribute="th", right_attribute="td", title=None):
    """Create html table, where 2 columns: list_left and list_right."""
    # make sure both lists have the same length (add None for every mismatched position)
    list_left = list_left if list_left is not None else []
    list_right = list_right if list_right is not None else []
    diff = len(list_left) - len(list_right)
    list_left = list_left if diff >= 0 else list_left + [None] * -diff
    list_right = list_right if diff <= 0 else list_right + [None] * diff
    # create html table
    r = "<table>\n<tbody>\n"
    if title:
        r += '<tr>\n<th colspan="{col_span}">' + str(title) + "</th>\n</tr>\n"
    two_columns = False
    for i, (left, right) in enumerate(zip(list_left, list_right)):
        r += "<tr>\n"
        if i == 0 and left is not None and right is not None:
            two_columns = True
        if left is not None or two_columns:
            r += "  <{1}>{0}</{1}>\n".format(left if left is not None else "", left_attribute)
        if right is not None or two_columns:
            r += "  <{1}>{0}</{1}>\n".format(right if right is not None else "", right_attribute)
        r += "</tr>\n"
    r += "</tbody>\n</table>\n"
    r = r.replace("{col_span}", "2" if two_columns else "1")
    return r


def add_tooltip_to_plt(tooltip_values=None, tooltip_names=None, tooltip_title=None, tooltip_style=None, show=True):
    """Add tooltip to plt.

    :param tooltip_values: list of lists, where every sub-list represents the values that we want to show as tooltip
    :param tooltip_names: list, where every ith element if the label name of the ith value in every sub-list in tooltip_values
    :param tooltip_title: string to put on top of every tooltip as the title
    :param tooltip_style: style for html, including but not limited to table css: table, th, td

    Requires style with markers to show tooltips (for example, style "-" will not work, but ".-" will).

    @use add_tooltip_to_plt([[0,0], [1,1], [0,1], [1,0]], tooltip_names=["y", "x"], tooltip_title="Legend")
    """
    if tooltip_style is None:
        tooltip_style = """
table { border-collapse: collapse; border: 1px solid #bbb;}
th { border-bottom: 1px solid #bbb; }
td { border-bottom: 1px solid #bbb; }
table, th, td { font-family: sans-serif; padding: 4; opacity: 0.9; background-color: #fff; }
"""

    tooltip_labels = None
    if tooltip_values is not None:
        tooltip_labels = []
        for values in tooltip_values:
            tooltip_labels.append(html_table_from_lists(list_left=tooltip_names, list_right=values, title=tooltip_title))

    if tooltip_labels is not None:
        points = plt.gca().lines
        fig = plt.gcf()
        tooltip = plugins.PointHTMLTooltip(points[0], tooltip_labels, voffset=10, hoffset=10, css=tooltip_style)
        plugins.connect(fig, tooltip)

    if show:
        mpld3.show()


if __name__ == "__main__":
    input("1. Press ENTER to see next example")

    N = 10
    df = pd.DataFrame(index=range(N))
    df["x"] = np.arange(10, N + 10)
    df["y"] = np.random.randn(N)
    df["height"] = np.random.randn(N)

    plot_df_with_tooltip(df, "y", "x",title="Test plot",
                         tooltip_columns=["x", "y", "height"], tooltip_title_column=None,
                         style="o-")

    input("2. Press ENTER to see next example")

    try:
        from basic.basic_plot import plotLine1D  # requires basic_plot library, see my basic repo
    except Exception:
        from basic_plot import plotLine1D  # requires basic_plot library, see my basic repo

    y = [1, 2, 1, 3, 5, 2, 9, 10]
    x = range(len(y))
    legend = list(zip(y, x))

    plt.subplots()  # this needs to run before plotting, or the legend may not work
    points = plotLine1D(y, y_label="Price", x_label="Time", title="Daniel's Portfolio", label="TSLA", style=".-", show=False)
    add_tooltip_to_plt(legend, tooltip_names=["y", "x"])
