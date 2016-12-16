import plotly.graph_objs as go
import numpy as np



def create_scatter_trace(data, name, mode = 'lines+markers',
                         lineshape = 'hv', marker_shp='circle',
                         width=2, show=True, benefit_col='Eliminated'):
    """
    create a Plotly scatter trace object with benefit data.

    data = Pandas dataframe holding the following columns:
        Option_ID = id of the SFR scenario
        Cost = cost of implementation
        Improved = count of parcels with flood risk reduced
        incr_benefit_cost = incremental ratio of benefit/cost

    """
    #calculate dot size
    marker_size = np.sqrt(data.incr_benefit_cost)

    #create a Plotly scatter graph object
    scatter = go.Scatter(
                x = data.Cost.tolist(),
                y = data[benefit_col].tolist(),
                name = name,
                mode = mode,
                text= data.Option_ID.tolist(),
                line = {'shape':lineshape, 'width':width},
                marker=dict(
                    size=marker_size,
                    symbol=marker_shp,
                ),
                visible = show,
            )
    return scatter
