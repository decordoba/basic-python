import matplotlib.pyplot as plt


def transformCurvesToPlot(y_pts, x_pts):
    """Get a list of curves y_pts and x_pts and return a tuple formatted for pyplot.
    
    pyplot can print more than one curve at the same time, but it doesn't do it in an intuitive way.
    This method gets a list of curves y_pts
        [[curveA_y], [curveB_y], [curveC_y]]
    and x_pts
        [[curveA_x], [curveB_x], [curveC_x]]
    and returns a tuple
        ([[curveA_y0, curveB_y0, curveC_y0], [curveA_y1, curveB_y1, curveC_y1]...],
         [[curveA_x0, curveB_x0, curveC_x0], [curveA_x1, curveB_x1, curveC_x1]...])
    
    It accepts curves of different lengths too. The returned y_pts and x_pts will plot all curves fine.
    
    @use transformCurvesToPlot([[-2,2],[-2,-1,0,1,2],[0,0]], [[0,0],[-2,-1,0,1,2],[-2,2]])
    @ret ([[-2, -2, 0], [2, -1, 0], [2, 0, 0], [2, 1, 0], [2, 2, 0], [2, 2, 0]],
          [[0, -2, -2], [0, -1, 2], [0, 0, 2], [0, 1, 2], [0, 2, 2], [0, 2, 2]])
    """
    new_y_pts = []
    new_x_pts = []
    last_row = max([len(row) for row in y_pts])
    for i, row in enumerate(y_pts):
        for j, y in enumerate(row):
            try:
                new_y_pts[j].append(y)
                new_x_pts[j].append(x_pts[i][j])
            except IndexError:
                new_y_pts.append([y])
                new_x_pts.append([x_pts[i][j]])
        x = x_pts[i][j]
        while j < last_row:
            j += 1
            try:
                new_y_pts[j].append(y)
                new_x_pts[j].append(x)
            except IndexError:
                new_y_pts.append([y])
                new_x_pts.append([x])
    return new_y_pts, new_x_pts


def plotLine(y_pts, x_pts=None, y_label=None, x_label=None, title=None, axis=None, style="-",
             color="", y_scale="linear", x_scale="linear", label=None, show=True):
    """Plot a line or point cloud.
    
    It accepts several lines at the same time, if you set y_pts and x_pts as lists of lists.

    @use plotLine([1,2,3,2,1], [0,1,2,3,4])

    :param y_pts: y coordinates. A list of list can represent several lines
    :param x_pts: x coordinates. A list of list can represent several lines
    :param y_label: label for y axis
    :param x_label: label for x axis
    :param title: the title of the figure
    :param axis: len4 list [xmin, xmax, ymin, ymax] to pick range we will see
    :param style: ('-': line), ('x': cross), ('o': circle), ('s': squre), ('--': dotted line)...
    :param color: 'r','g','b','c','m','y','k'... If left blank, every curve will take a new color
    :param label: text that will be displayed if we show a legend
    :param show: whether to show result or not. Show is blocking (pauses the execution) until the
                 plot window is closed
    """
    full_style = (color if color is not None else "") + (style if style is not None else "")
    if x_pts is None:
        ret = plt.plot(y_pts, full_style, label=label)
    else:
        if isinstance(y_pts, list) and isinstance(y_pts[0], list):
            (y_pts, x_pts) = transformCurvesToPlot(y_pts, x_pts)
        ret = plt.plot(x_pts, y_pts, full_style, label=label)
    if y_label is not None:
        plt.ylabel(y_label)
    if x_label is not None:
        plt.xlabel(x_label)
    if title is not None:
        plt.title(title)
    if axis is not None:
        plt.axis(axis)
    plt.yscale(y_scale)
    plt.xscale(x_scale)
    plt.draw()
    if show:
        plt.show()
    return ret


def plotLine1D(y_pts, y_label=None, x_label=None, title=None, y_scale="linear", style=None, label=None,
               show=True):
    """Print line between points in a list.
    
    Every point will be separated a constant space in the x coordinates,
    and the y coordinate of every point will be the values in the list.
    """
    return plotLine(y_pts, y_label=y_label, x_label=x_label, title=title, y_scale=y_scale, label=label,
                    show=show, style=style)


def plotLine2D(y_pts, x_pts, y_label=None, x_label=None, title=None, style=None, y_scale="linear",
               x_scale="linear", label=None, show=True):
    """Print line between points in a list. Every point is caracterized by an x and y coordinate."""
    return plotLine(y_pts, x_pts=x_pts, y_label=y_label, x_label=x_label, title=title, y_scale=y_scale,
                    x_scale=x_scale, label=label, show=show, style=style)


def plotCloud2D(y_pts, x_pts, y_label=None, x_label=None, title=None, style="x", y_scale="linear",
                x_scale="linear", label=None, show=True):
    """Print point cloud of coordinates (x_pts, y_pts)."""
    return plotLine(y_pts, x_pts=x_pts, y_label=y_label, x_label=x_label, title=title, style=style,
                    y_scale=y_scale, x_scale=x_scale, label=label, show=show)


def plotLegend(labels=None, location="best", boxed=None):
    """Display legend (labels can be set beforehand using other functions like plotLine) in location.

    :param labels: labels shown. If None, all labels introduced in other functions will be displayed
    :param location: "best", "upper right", "upper left", "lower left", "lower right", "right",
                     "center left", "center right", "lower center", "upper center", "center" (numbers 0 to 10)
    :param boxed: whether to show a semi-transparent box around the legend or not. None means default
    Find more (accurate location...) here: https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.legend
    """
    if labels is None:
        return plt.legend(loc=location, frameon=boxed)
    else:
        if isinstance(labels, int):
            return plt.legend(loc=labels, frameon=boxed)
        elif isinstance(labels, str):
            return plt.legend([labels], loc=location, frameon=boxed)
        else:
            return plt.legend(labels, loc=location, frameon=boxed)


def plotText(y, x, text, style="normal", color="k", fontsize=None, fontweight=None,
             verticalalignment="center", horizontalalignment="center", show=True):
    """Print text in the plot.

    @use plotText(0.5, 0.5, "Middle") --> print text in the middle of screen
    @use plotText(0.0, 0.0, "Bottom-Left") --> print text in the bottom left of screen
    @use plotText(1.0, 1.0, "Top-Right") --> print text in the top right of screen

    :param y: y coordinate for text (one int/float).
    :param x: x coordinates for text (one int/float).
    :param style: "normal", "italic" or "oblique"
    :param color: 'r','g','b','c','m','y','k'...
    :param fontsize: number of pixels or 'large', 'medium', 'smaller', 'small', 'x-large',
                     "xx-small", "larger", "x-small", "xx-large"
    :param fontweight: "normal", "bold", "heavy", "light", "ultrabold", "ultralight"
    :param verticalalignment: "center", "top", "bottom", "baseline"
    :param horizontalalignment: "center", "right", "left"
    :param show: whether to show result or not. Show is blocking (pauses the execution) until the
                 plot window is closed
    Find more (rotation, alpha, fontname, box...) here: https://matplotlib.org/users/text_props.html
    """
    ret = plt.text(x, y, text, style=style, color=color, fontsize=fontsize, fontweight=fontweight,
                   verticalalignment=verticalalignment, horizontalalignment=horizontalalignment)
    plt.draw()
    if show:
        plt.show()
    return ret
